# Clarifying Prompts for Robust English-Arabic Question-Type Classification

Professional research repository for a Prompt Engineering course project at the Mediterranean Institute of Technology (MedTech).

## Project overview

This controlled empirical study evaluates prompt design for bilingual English-Arabic question-type classification. Each question is classified into one of six answer-type labels: `NUMBER`, `LOCATION`, `PERSON`, `DESCRIPTION`, `ENTITY`, or `ABBREVIATION`.

The research story is: Falcon3-7B-Instruct was used for prompt progression; the prompt evolved from simple label-only prompts to definitions, few-shot examples, and a targeted `DESCRIPTION`/`ENTITY` disambiguation rule; the final prompt was frozen and tested on an unseen balanced validation dataset; cross-model validation used Falcon3, ALLaM, AceGPT, and Gemini 2.5 Flash.

## Research questions

1. How does prompt design affect bilingual question-type classification accuracy in English and Arabic?
2. Do explicit definitions, few-shot examples, and a targeted `DESCRIPTION`/`ENTITY` rule reduce prompt sensitivity and improve consistency?
3. Does the frozen final prompt generalize across open and closed instruction-tuned models on an unseen balanced validation set?

## Models

| Model | Type | Role |
|---|---|---|
| `tiiuae/Falcon3-7B-Instruct` | Open general baseline | Prompt progression + cross-model validation |
| `humain-ai/ALLaM-7B-Instruct-preview` | Open Arabic-focused | Cross-model validation |
| `FreedomIntelligence/AceGPT-v2-8B-Chat` | Open Arabic-focused | Cross-model validation |
| `gemini-2.5-flash` | Closed proprietary | Closed-model validation with 8 compact prompt variants |

## Dataset

The final validation dataset contains 120 questions: 60 English and 60 Arabic, with 10 examples per label per language. See `data/unseen_validation_dataset_pilot07.csv` and `data/label_schema.json`.

## Final prompt strategy

The final prompt uses explicit definitions, few-shot examples, a targeted `DESCRIPTION`/`ENTITY` disambiguation rule, and an exact-label-only output constraint. Prompt files are in `prompts/`. Gemini was evaluated with eight compact variants of the frozen final strategy using `temperature=0.0`, `max_output_tokens=64`, and `thinking_budget=0`.

## Results summary

| Model | English Acc. | Arabic Acc. | English F1 | Arabic F1 | English Sens. | Arabic Sens. | English Cons. | Arabic Cons. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Falcon3-7B-Instruct | 1.0000 | 0.9833 | 1.0000 | 0.9833 | 0.0048 | 0.0105 | 0.9917 | 0.9542 |
| ALLaM-7B-Instruct-preview | 0.9833 | 1.0000 | 0.9833 | 1.0000 | 0.0059 | 0.0059 | 0.9833 | 0.9833 |
| AceGPT-v2-8B-Chat | 0.9167 | 0.8833 | 0.9087 | 0.8618 | 0.0385 | 0.0313 | 0.8787 | 0.8824 |
| Gemini-2.5-Flash | 0.9833 | 0.8333 | 0.9833 | 0.7778 | 0.0253 | 0.0225 | 0.9662 | 0.9704 |

Main Gemini finding: the closed model remained strong in English, but in Arabic it consistently mapped all 10 ABBREVIATION questions to DESCRIPTION under the compact variants. This made Arabic ABBREVIATION the dominant closed-model failure mode.

## Repository structure

```text
bilingual-prompt-classification/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── data/
├── prompts/
├── notebooks/
├── scripts/
├── results/
├── figures/
├── paper/
└── logs/
```

## Reproduction steps

Offline verification from the checked-in CSV files:

```bash
pip install -r requirements.txt
python scripts/build_summary_tables.py
python scripts/generate_figures.py
```

The notebook defaults to `RUN_MODE = "local_results_only"`, which verifies the local datasets, prompts, metrics, and existing result CSVs without external model/API calls. To rerun Gemini, change `RUN_MODE` to `gemini_only` and provide `GEMINI_API_KEY` through an environment variable or Colab Secret.

Compile `paper/main.tex` with XeLaTeX or LuaLaTeX. For Gemini-only reruns on Windows, use:

```powershell
python scripts/run_gemini.py --root . --out-dir results --model gemini-2.5-flash --max-output-tokens 64 --thinking-budget 0 --sleep-seconds 0.6 --retries 3 --seed 42
```

Add API keys only through environment variables or Colab Secrets. Do not commit secrets.

## Limitations

This is a small balanced validation dataset, not a broad natural benchmark. The dataset was manually created and does not cover all Arabic varieties. The prompts were not validated through a native-speaker questionnaire. The prompt was developed through prior error analysis. Hugging Face runs used 4-bit quantization. Closed API behavior can change over time.

## Course note

Prepared for the Prompt Engineering course research project at MedTech.
