#!/usr/bin/env python3
"""
Gemini compact-variant rerun for bilingual question-type classification.
No pandas / numpy / sklearn / matplotlib are used. This avoids Windows DLL policy blocks.
This v3 version also disables Gemini 2.5 Flash thinking by default to avoid empty MAX_TOKENS responses.

Outputs:
- results/raw_predictions/raw_predictions_crossmodel_gemini_2_5_flash_compact_variants.csv
- results/sample_level/sample_level_results_crossmodel_gemini_2_5_flash_compact_variants.csv
- results/metrics/metrics_crossmodel_gemini_2_5_flash_compact_variants.csv
- results/class_level/class_level_results_crossmodel_gemini_2_5_flash_compact_variants.csv
- results/error_analysis/error_analysis_crossmodel_gemini_2_5_flash_compact_variants.csv
- results/prompt_level_errors/prompt_level_errors_crossmodel_gemini_2_5_flash_compact_variants.csv
- results/summary_tables/bootstrap_ci_gemini_compact_variants.csv
"""

import argparse
import csv
import json
import math
import os
import random
import re
import sys
import time
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except Exception as exc:
    print("ERROR: google-genai is not installed or cannot be imported.")
    print("Run: python -m pip install --upgrade google-genai")
    raise exc

LABELS = ["NUMBER", "LOCATION", "PERSON", "DESCRIPTION", "ENTITY", "ABBREVIATION"]
ALL_CLASSES = LABELS + ["N/A"]
MODEL_SLUG = "gemini_2_5_flash"
RUN_SUFFIX = "compact_variants"

LABEL_DEFINITIONS = """Labels:
NUMBER = asks for a number, date, year, quantity, percentage, calculation, or measurement.
LOCATION = asks for a place, country, city, continent, region, river, lake, ocean, or geographic location.
PERSON = asks for a person, author, inventor, founder, composer, leader, or named human figure.
DESCRIPTION = asks for an explanation, meaning, definition, function, purpose, use, process, or how something works.
ENTITY = asks for a concrete non-person and non-location thing such as an object, animal, planet, language, currency, device, material, gas, app, software, food, sport, tool, vehicle, element, metal, or instrument.
ABBREVIATION = asks what an acronym or abbreviation stands for, such as API, CPU, URL, DNA, or NGO.
Rule: Choose DESCRIPTION for explanation/meaning/function/process questions. Choose ENTITY for the name of a concrete thing. Return exactly one label only.
"""

EN_EXAMPLES = """Examples:
Question: How many days are in a leap year? -> NUMBER
Question: Where is the Eiffel Tower located? -> LOCATION
Question: Who painted the Mona Lisa? -> PERSON
Question: What is photosynthesis? -> DESCRIPTION
Question: What device is used to measure temperature? -> ENTITY
Question: What does CPU stand for? -> ABBREVIATION
"""

AR_EXAMPLES = """أمثلة:
السؤال: كم دقيقة في الساعة الواحدة؟ -> NUMBER
السؤال: أين يقع برج إيفل؟ -> LOCATION
السؤال: من رسم لوحة الموناليزا؟ -> PERSON
السؤال: ما هو التمثيل الضوئي؟ -> DESCRIPTION
السؤال: ما الجهاز المستخدم لقياس درجة الحرارة؟ -> ENTITY
السؤال: ماذا يعني اختصار CPU؟ -> ABBREVIATION
"""

DEFAULT_VARIANTS = {
    "English": [
        "Classify this question into one answer-type label.\n{defs}\n{examples}\nQuestion: {question}\nLabel:",
        "Assign the most appropriate label to the question.\n{defs}\n{examples}\nInput question: {question}\nAnswer with the label only:",
        "You are doing six-way question-type classification.\n{defs}\n{examples}\nQuestion to classify: {question}\nFinal label:",
        "Read the question and decide which answer type it asks for.\n{defs}\n{examples}\nQuestion: {question}\nReturn one label:",
        "Choose exactly one label from NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION.\n{defs}\n{examples}\nQuestion: {question}\nLabel only:",
        "Determine the expected answer category for the question.\n{defs}\n{examples}\nQuestion: {question}\nCategory:",
        "For the following question, output only its answer-type class.\n{defs}\n{examples}\nQuestion: {question}\nClass:",
        "Identify whether the question asks for a number, place, person, explanation, entity, or abbreviation.\n{defs}\n{examples}\nQuestion: {question}\nOutput label:"
    ],
    "Arabic": [
        "صنّف السؤال إلى نوع إجابة واحد. أعد اسم التصنيف بالإنجليزية فقط.\n{defs}\n{examples}\nالسؤال: {question}\nالتصنيف:",
        "اختر التصنيف الأنسب لهذا السؤال من التصنيفات الستة. أجب بتصنيف واحد فقط.\n{defs}\n{examples}\nالسؤال: {question}\nالإجابة:",
        "هذه مهمة تصنيف نوع السؤال. أعد فقط NUMBER أو LOCATION أو PERSON أو DESCRIPTION أو ENTITY أو ABBREVIATION.\n{defs}\n{examples}\nالسؤال: {question}\nالتصنيف النهائي:",
        "اقرأ السؤال وحدد نوع الإجابة المطلوبة.\n{defs}\n{examples}\nالسؤال: {question}\nأعد التصنيف فقط:",
        "صنّف السؤال التالي حسب نوع الجواب المتوقع، مع الانتباه للفرق بين DESCRIPTION و ENTITY.\n{defs}\n{examples}\nالسؤال: {question}\nالتصنيف:",
        "حدد هل السؤال يطلب رقماً، مكاناً، شخصاً، شرحاً، كياناً، أو معنى اختصار.\n{defs}\n{examples}\nالسؤال: {question}\nLabel:",
        "أعطِ تصنيفاً واحداً فقط للسؤال التالي.\n{defs}\n{examples}\nالسؤال: {question}\nالتصنيف فقط:",
        "استعمل التعريفات والأمثلة لتصنيف السؤال. لا تشرح.\n{defs}\n{examples}\nالسؤال: {question}\nOutput label:"
    ]
}


def ensure_dirs(root: Path, out_dir: str):
    base = root / out_dir
    for sub in [
        "raw_predictions", "sample_level", "metrics", "class_level",
        "error_analysis", "prompt_level_errors", "summary_tables"
    ]:
        (base / sub).mkdir(parents=True, exist_ok=True)
    return base


def read_csv_dicts(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def find_validation_file(root: Path):
    candidates = [
        root / "data" / "unseen_validation_dataset_pilot07.csv",
        root / "data" / "pilot07_unseen_validation.csv",
        root / "data" / "validation.csv",
        root / "data" / "unseen_validation.csv",
    ]
    for path in candidates:
        if path.exists():
            return path
    matches = list((root / "data").glob("*validation*.csv")) if (root / "data").exists() else []
    if matches:
        return matches[0]
    raise FileNotFoundError("Could not find validation CSV under data/. Expected data/unseen_validation_dataset_pilot07.csv")


def _coerce_prompt_list(value):
    """Accept a list of strings or dictionaries with prompt/template/text fields."""
    prompts = []
    if isinstance(value, list):
        for item in value:
            if isinstance(item, str):
                prompts.append(item)
            elif isinstance(item, dict):
                for key in ["prompt", "template", "text", "content"]:
                    if key in item:
                        prompts.append(str(item[key]))
                        break
                else:
                    prompts.append(str(item))
    return prompts

def extract_variants_from_json(obj, language):
    if isinstance(obj, list):
        return _coerce_prompt_list(obj)
    if not isinstance(obj, dict):
        return []
    keys = [language, language.lower(), language.upper(), language.capitalize()]
    if language.lower().startswith("arab"):
        keys += ["ar", "arabic", "Arabic", "AR"]
    else:
        keys += ["en", "english", "English", "EN"]
    for key in keys:
        if key in obj:
            value = obj[key]
            if isinstance(value, list):
                return _coerce_prompt_list(value)
            if isinstance(value, dict):
                for inner_key in ["variants", "prompts", "templates"]:
                    if inner_key in value and isinstance(value[inner_key], list):
                        return _coerce_prompt_list(value[inner_key])
    for key in ["variants", "prompts", "templates"]:
        if key in obj and isinstance(obj[key], list):
            return _coerce_prompt_list(obj[key])
    return []


def load_prompt_variants(root: Path):
    path = root / "prompts" / "final_prompt_variants_gemini_compact.json"
    variants = {}
    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            obj = json.load(f)
        variants["English"] = extract_variants_from_json(obj, "English")
        variants["Arabic"] = extract_variants_from_json(obj, "Arabic")
    for lang in ["English", "Arabic"]:
        if not variants.get(lang):
            variants[lang] = DEFAULT_VARIANTS[lang]
        variants[lang] = variants[lang][:8]
        if len(variants[lang]) < 8:
            variants[lang] += DEFAULT_VARIANTS[lang][len(variants[lang]):8]
    return variants


def render_prompt(template: str, question: str, language: str):
    examples = AR_EXAMPLES if language.lower().startswith("arab") else EN_EXAMPLES
    replacements = {
        "question": question,
        "QUESTION": question,
        "input": question,
        "INPUT": question,
        "defs": LABEL_DEFINITIONS,
        "definitions": LABEL_DEFINITIONS,
        "examples": examples,
    }
    out = template
    try:
        out = out.format(**replacements)
    except Exception:
        pass
    for token in ["{question}", "[QUESTION]", "<QUESTION>", "{{question}}"]:
        out = out.replace(token, question)
    if question not in out:
        out = out.rstrip() + "\nQuestion: " + question + "\nLabel:"
    if "NUMBER" not in out or "ABBREVIATION" not in out:
        out = LABEL_DEFINITIONS + "\n" + examples + "\n" + out
    return out


def normalize_label(text):
    if text is None:
        return "N/A"
    clean = str(text).strip().upper()
    clean = clean.replace("`", " ").replace("*", " ")
    for label in LABELS:
        if re.search(r"\b" + re.escape(label) + r"\b", clean):
            return label
    # Common partial fallback
    aliases = {
        "NUM": "NUMBER", "LOC": "LOCATION", "PER": "PERSON", "DESC": "DESCRIPTION",
        "ENT": "ENTITY", "ABBR": "ABBREVIATION", "ABBREV": "ABBREVIATION"
    }
    for alias, label in aliases.items():
        if re.search(r"\b" + re.escape(alias) + r"\b", clean):
            return label
    return "N/A"


def extract_response_text(response):
    """Return visible Gemini text without converting the entire response object to a string."""
    # response.text is the normal SDK shortcut, but it can be empty/raise when MAX_TOKENS fires.
    try:
        text = getattr(response, "text", None)
        if text:
            return str(text).strip()
    except Exception:
        pass

    chunks = []
    try:
        for cand in getattr(response, "candidates", []) or []:
            content = getattr(cand, "content", None)
            for part in getattr(content, "parts", []) or []:
                text = getattr(part, "text", None)
                if text:
                    chunks.append(str(text))
    except Exception:
        pass
    return "".join(chunks).strip()


def response_debug_info(response):
    finish = "UNKNOWN"
    thoughts = ""
    try:
        cands = getattr(response, "candidates", []) or []
        if cands:
            finish = str(getattr(cands[0], "finish_reason", "UNKNOWN"))
    except Exception:
        pass
    try:
        usage = getattr(response, "usage_metadata", None)
        thoughts = str(getattr(usage, "thoughts_token_count", ""))
    except Exception:
        pass
    return finish, thoughts


def make_config(max_output_tokens, thinking_budget):
    kwargs = {
        "temperature": 0.0,
        "top_p": 1.0,
        "max_output_tokens": max_output_tokens,
        "response_mime_type": "text/plain",
    }
    # Gemini 2.5 Flash supports thinking_budget=0 to disable thinking. This prevents
    # hidden thinking tokens from consuming the tiny label-only output budget.
    if thinking_budget is not None:
        try:
            kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=thinking_budget)
        except Exception:
            pass
    return types.GenerateContentConfig(**kwargs)


def call_gemini(client, model, prompt, max_output_tokens, retries, sleep_seconds, thinking_budget=0):
    last_error = None
    current_tokens = max_output_tokens
    for attempt in range(retries + 1):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=make_config(current_tokens, thinking_budget),
            )
            text = extract_response_text(response)
            finish, thoughts = response_debug_info(response)
            if text:
                return text
            # Empty text with MAX_TOKENS is a known Gemini 2.5 failure mode when the
            # token budget is consumed by thinking. Increase visible budget and retry.
            if "MAX_TOKENS" in finish and attempt < retries:
                current_tokens = max(current_tokens * 2, 128)
                print(f"Empty Gemini text with finish_reason={finish}, thoughts={thoughts}. Retrying with max_output_tokens={current_tokens}...")
                time.sleep(sleep_seconds * (attempt + 1))
                continue
            return f"N/A_EMPTY_RESPONSE finish_reason={finish} thoughts_tokens={thoughts}"
        except Exception as exc:
            last_error = exc
            wait = sleep_seconds * (attempt + 1)
            print(f"Gemini call failed on attempt {attempt + 1}/{retries + 1}: {exc}")
            if attempt < retries:
                time.sleep(wait)
    return f"ERROR: {last_error}"

def entropy_sensitivity(preds):
    counts = Counter(preds)
    total = sum(counts.values())
    if total == 0:
        return 0.0
    ent = 0.0
    for cls in ALL_CLASSES:
        p = counts.get(cls, 0) / total
        if p > 0:
            ent -= p * math.log(p)
    return ent / math.log(len(ALL_CLASSES))


def distribution(preds):
    counts = Counter(preds)
    total = sum(counts.values()) or 1
    return {cls: counts.get(cls, 0) / total for cls in ALL_CLASSES}


def tvd(p, q):
    return 0.5 * sum(abs(p.get(cls, 0.0) - q.get(cls, 0.0)) for cls in ALL_CLASSES)


def average_consistency(sample_rows):
    by_gold = defaultdict(list)
    for row in sample_rows:
        by_gold[row["label"]].append(row)
    class_scores = []
    for gold, rows in by_gold.items():
        if len(rows) < 2:
            continue
        pair_scores = []
        for a, b in combinations(rows, 2):
            pair_scores.append(1.0 - tvd(a["dist"], b["dist"]))
        if pair_scores:
            class_scores.append(sum(pair_scores) / len(pair_scores))
    if not class_scores:
        return 1.0
    return sum(class_scores) / len(class_scores)


def majority_vote(preds):
    counts = Counter(preds)
    best_count = max(counts.values())
    tied = [cls for cls, n in counts.items() if n == best_count]
    for cls in ALL_CLASSES:
        if cls in tied:
            return cls
    return tied[0]


def macro_f1(golds, preds):
    scores = []
    for label in LABELS:
        tp = sum(1 for g, p in zip(golds, preds) if g == label and p == label)
        fp = sum(1 for g, p in zip(golds, preds) if g != label and p == label)
        fn = sum(1 for g, p in zip(golds, preds) if g == label and p != label)
        denom = (2 * tp + fp + fn)
        scores.append((2 * tp / denom) if denom else 0.0)
    return sum(scores) / len(scores)


def bootstrap_accuracy_ci(correct_values, n_boot=10000, seed=42):
    if not correct_values:
        return (0.0, 0.0)
    rng = random.Random(seed)
    n = len(correct_values)
    vals = []
    for _ in range(n_boot):
        vals.append(sum(correct_values[rng.randrange(n)] for _ in range(n)) / n)
    vals.sort()
    lo_idx = int(0.025 * (n_boot - 1))
    hi_idx = int(0.975 * (n_boot - 1))
    return vals[lo_idx], vals[hi_idx]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--out-dir", default="results")
    parser.add_argument("--model", default="gemini-2.5-flash")
    parser.add_argument("--max-output-tokens", type=int, default=64)
    parser.add_argument("--thinking-budget", type=int, default=0, help="Gemini 2.5 Flash thinking budget. Use 0 to disable thinking for short label-only outputs.")
    parser.add_argument("--sleep-seconds", type=float, default=0.6)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out_base = ensure_dirs(root, args.out_dir)

    key = os.environ.get("GEMINI_API_KEY")
    if not key or key.strip() in {"PASTE_YOUR_REAL_KEY_HERE", "PASTE_YOUR_GEMINI_KEY_HERE", "YOUR_KEY_HERE"}:
        print("ERROR: GEMINI_API_KEY is missing or still set to a placeholder.")
        print('PowerShell example: $env:GEMINI_API_KEY = "YOUR_REAL_KEY_HERE"')
        sys.exit(1)

    validation_path = find_validation_file(root)
    prompts_by_lang = load_prompt_variants(root)
    rows = read_csv_dicts(validation_path)

    print(f"Loaded validation data: {validation_path}")
    print(f"Rows: {len(rows)}")
    print(f"Prompt variants: English={len(prompts_by_lang['English'])}, Arabic={len(prompts_by_lang['Arabic'])}")
    print(f"Model: {args.model}")

    client = genai.Client(api_key=key)
    raw_rows = []

    for idx, sample in enumerate(rows, 1):
        sample_id = str(sample.get("id", idx))
        gold = str(sample.get("label", "")).strip().upper()
        language = str(sample.get("language", "English")).strip()
        question = str(sample.get("question", "")).strip()
        lang_key = "Arabic" if language.lower().startswith("arab") else "English"
        variants = prompts_by_lang[lang_key]

        print(f"[{idx}/{len(rows)}] {lang_key} id={sample_id} gold={gold}")
        for prompt_idx, template in enumerate(variants, 1):
            prompt = render_prompt(template, question, lang_key)
            raw_output = call_gemini(
                client=client,
                model=args.model,
                prompt=prompt,
                max_output_tokens=args.max_output_tokens,
                retries=args.retries,
                sleep_seconds=args.sleep_seconds,
                thinking_budget=args.thinking_budget,
            )
            pred = normalize_label(raw_output)
            raw_rows.append({
                "model": args.model,
                "model_type": "closed",
                "sample_id": sample_id,
                "id": sample_id,
                "language": lang_key,
                "label": gold,
                "gold_label": gold,
                "question": question,
                "prompt_id": prompt_idx,
                "prompt_variant": prompt_idx,
                "raw_output": raw_output,
                "prediction": pred,
                "predicted_label": pred,
                "is_correct": int(pred == gold),
            })
            time.sleep(args.sleep_seconds)

    # Sample-level majority vote
    grouped = defaultdict(list)
    sample_meta = {}
    for row in raw_rows:
        key_tuple = (row["language"], row["sample_id"])
        grouped[key_tuple].append(row)
        sample_meta[key_tuple] = row

    sample_rows_internal = []
    sample_rows_out = []
    for key_tuple, group in grouped.items():
        meta = sample_meta[key_tuple]
        preds = [g["predicted_label"] for g in group]
        majority = majority_vote(preds)
        vote_counts = dict(Counter(preds))
        dist = distribution(preds)
        correct = int(majority == meta["gold_label"])
        internal = {
            "language": meta["language"],
            "sample_id": meta["sample_id"],
            "label": meta["gold_label"],
            "majority_prediction": majority,
            "is_correct": correct,
            "dist": dist,
        }
        sample_rows_internal.append(internal)
        sample_rows_out.append({
            "model": args.model,
            "model_type": "closed",
            "sample_id": meta["sample_id"],
            "id": meta["sample_id"],
            "language": meta["language"],
            "label": meta["gold_label"],
            "gold_label": meta["gold_label"],
            "question": meta["question"],
            "majority_prediction": majority,
            "predicted_label": majority,
            "is_correct": correct,
            "vote_counts": json.dumps(vote_counts, ensure_ascii=False, sort_keys=True),
            "sensitivity": f"{entropy_sensitivity(preds):.6f}",
        })

    # Metrics
    metrics_rows = []
    ci_rows = []
    for language in ["English", "Arabic"]:
        lang_samples = [r for r in sample_rows_internal if r["language"] == language]
        if not lang_samples:
            continue
        golds = [r["label"] for r in lang_samples]
        preds = [r["majority_prediction"] for r in lang_samples]
        correct_values = [r["is_correct"] for r in lang_samples]
        raw_lang = [r for r in raw_rows if r["language"] == language]
        by_sample_preds = defaultdict(list)
        for r in raw_lang:
            by_sample_preds[r["sample_id"]].append(r["predicted_label"])
        sensitivities = [entropy_sensitivity(v) for v in by_sample_preds.values()]
        acc = sum(correct_values) / len(correct_values)
        f1 = macro_f1(golds, preds)
        sens = sum(sensitivities) / len(sensitivities) if sensitivities else 0.0
        cons = average_consistency(lang_samples)
        lo, hi = bootstrap_accuracy_ci(correct_values, seed=args.seed)
        metrics_rows.append({
            "model": args.model,
            "model_type": "closed",
            "language": language,
            "n_samples": len(lang_samples),
            "n_prompts": 8,
            "total_generations": len(raw_lang),
            "accuracy": f"{acc:.6f}",
            "macro_f1": f"{f1:.6f}",
            "average_sensitivity": f"{sens:.6f}",
            "average_consistency": f"{cons:.6f}",
        })
        ci_rows.append({
            "model": args.model,
            "language": language,
            "n_samples": len(lang_samples),
            "accuracy": f"{acc:.6f}",
            "accuracy_ci_low": f"{lo:.6f}",
            "accuracy_ci_high": f"{hi:.6f}",
            "n_bootstrap": 10000,
            "seed": args.seed,
        })

    # Safety check: if every majority vote is N/A, the run is not scientifically usable.
    total_samples = len(sample_rows_out)
    total_na_majority = sum(1 for r in sample_rows_out if r["majority_prediction"] == "N/A")
    if total_samples and total_na_majority == total_samples:
        print("\nERROR: All majority predictions are N/A.")
        print("This usually means Gemini returned empty MAX_TOKENS responses or the API key/run failed.")
        print("Try again with --thinking-budget 0 and --max-output-tokens 64 or 128.")
        sys.exit(2)

    # Class-level
    class_rows = []
    for language in ["English", "Arabic"]:
        for label in LABELS:
            subset = [r for r in sample_rows_internal if r["language"] == language and r["label"] == label]
            if not subset:
                continue
            correct = sum(r["is_correct"] for r in subset)
            class_rows.append({
                "model": args.model,
                "model_type": "closed",
                "language": language,
                "label": label,
                "n_samples": len(subset),
                "correct": correct,
                "accuracy": f"{correct / len(subset):.6f}",
            })

    error_rows = [r for r in sample_rows_out if int(r["is_correct"]) == 0]
    prompt_error_rows = [r for r in raw_rows if int(r["is_correct"]) == 0]

    raw_fields = ["model", "model_type", "sample_id", "id", "language", "label", "gold_label", "question", "prompt_id", "prompt_variant", "raw_output", "prediction", "predicted_label", "is_correct"]
    sample_fields = ["model", "model_type", "sample_id", "id", "language", "label", "gold_label", "question", "majority_prediction", "predicted_label", "is_correct", "vote_counts", "sensitivity"]
    metric_fields = ["model", "model_type", "language", "n_samples", "n_prompts", "total_generations", "accuracy", "macro_f1", "average_sensitivity", "average_consistency"]
    class_fields = ["model", "model_type", "language", "label", "n_samples", "correct", "accuracy"]
    ci_fields = ["model", "language", "n_samples", "accuracy", "accuracy_ci_low", "accuracy_ci_high", "n_bootstrap", "seed"]

    write_csv(out_base / "raw_predictions" / f"raw_predictions_crossmodel_{MODEL_SLUG}_{RUN_SUFFIX}.csv", raw_rows, raw_fields)
    write_csv(out_base / "sample_level" / f"sample_level_results_crossmodel_{MODEL_SLUG}_{RUN_SUFFIX}.csv", sample_rows_out, sample_fields)
    write_csv(out_base / "metrics" / f"metrics_crossmodel_{MODEL_SLUG}_{RUN_SUFFIX}.csv", metrics_rows, metric_fields)
    write_csv(out_base / "class_level" / f"class_level_results_crossmodel_{MODEL_SLUG}_{RUN_SUFFIX}.csv", class_rows, class_fields)
    write_csv(out_base / "error_analysis" / f"error_analysis_crossmodel_{MODEL_SLUG}_{RUN_SUFFIX}.csv", error_rows, sample_fields)
    write_csv(out_base / "prompt_level_errors" / f"prompt_level_errors_crossmodel_{MODEL_SLUG}_{RUN_SUFFIX}.csv", prompt_error_rows, raw_fields)
    write_csv(out_base / "summary_tables" / "bootstrap_ci_gemini_compact_variants.csv", ci_rows, ci_fields)

    print("\nDone. Generated Gemini compact-variant CSV files under:")
    print(out_base)
    for m in metrics_rows:
        print(f"{m['language']}: accuracy={m['accuracy']} macro_f1={m['macro_f1']} sensitivity={m['average_sensitivity']} consistency={m['average_consistency']}")


if __name__ == "__main__":
    main()
