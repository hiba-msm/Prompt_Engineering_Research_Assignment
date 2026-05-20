#!/usr/bin/env python3
"""Evaluate a sample-level prediction CSV and compute bootstrap accuracy CIs.

Supports both repository sample-level formats:
- gold / majority_prediction
- gold_label or label / predicted_label or majority_prediction
"""
from pathlib import Path
import argparse
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, f1_score

LABELS = ["NUMBER", "LOCATION", "PERSON", "DESCRIPTION", "ENTITY", "ABBREVIATION"]


def bootstrap_accuracy_ci(correct, n_boot=10000, seed=42):
    rng = np.random.default_rng(seed)
    correct = np.asarray(correct, dtype=float)
    n = len(correct)
    idx = rng.integers(0, n, size=(n_boot, n))
    vals = correct[idx].mean(axis=1)
    return np.percentile(vals, [2.5, 97.5])


def first_existing(df: pd.DataFrame, names):
    for name in names:
        if name in df.columns:
            return name
    raise KeyError(f"None of these columns were found: {names}. Available columns: {list(df.columns)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample-file", required=True)
    ap.add_argument("--model-name", required=True)
    ap.add_argument("--out", default="results/summary_tables/bootstrap_from_one_file.csv")
    args = ap.parse_args()

    df = pd.read_csv(args.sample_file)
    gold_col = first_existing(df, ["gold", "gold_label", "label"])
    pred_col = first_existing(df, ["majority_prediction", "predicted_label", "prediction"])
    lang_col = first_existing(df, ["language", "lang"])

    rows = []
    for lang, g in df.groupby(lang_col):
        gold = g[gold_col].astype(str).str.strip().values
        pred = g[pred_col].astype(str).str.strip().values
        correct = gold == pred
        lo, hi = bootstrap_accuracy_ci(correct)
        rows.append({
            "model": args.model_name,
            "language": str(lang).capitalize(),
            "n": len(g),
            "accuracy": accuracy_score(gold, pred),
            "accuracy_ci_low": lo,
            "accuracy_ci_high": hi,
            "macro_f1": f1_score(gold, pred, labels=LABELS, average="macro", zero_division=0),
        })

    out = pd.DataFrame(rows)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False)
    print(out.to_string(index=False))


if __name__ == "__main__":
    main()
