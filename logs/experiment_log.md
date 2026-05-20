# Experiment Log - Bilingual Prompt Classification

## Project
Clarifying Prompts for Robust English-Arabic Question-Type Classification

## Objective
The objective was to test how prompt design affects bilingual question-type classification for English and Arabic questions. The task uses six labels: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, and ABBREVIATION.

## Prompt progression summary
- Pilot_03 used simple label-only prompts and reached 0.8667 English accuracy and 0.6667 Arabic accuracy.
- Pilot_04 added label definitions and improved to 0.9500 English accuracy and 0.8000 Arabic accuracy.
- Pilot_05 added one example per label and improved to 0.9667 English accuracy and 0.8667 Arabic accuracy.
- Pilot_06 added a targeted DESCRIPTION vs ENTITY disambiguation rule and improved to 0.9833 English accuracy and 0.9500 Arabic accuracy.
- Pilot_07 reused the frozen best prompt on unseen validation data and reached 1.0000 English accuracy and 0.9833 Arabic accuracy with Falcon3.

## Final cross-model validation
The frozen final prompt strategy was evaluated on Falcon3-7B-Instruct, ALLaM-7B-Instruct-preview, AceGPT-v2-8B-Chat, and Gemini-2.5-Flash. Each question was tested with eight prompt-level outputs and majority voting.

| Model | English Acc. | Arabic Acc. | English F1 | Arabic F1 | English Sens. | Arabic Sens. | English Cons. | Arabic Cons. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Falcon3-7B-Instruct | 1.0000 | 0.9833 | 1.0000 | 0.9833 | 0.0048 | 0.0105 | 0.9917 | 0.9542 |
| ALLaM-7B-Instruct-preview | 0.9833 | 1.0000 | 0.9833 | 1.0000 | 0.0059 | 0.0059 | 0.9833 | 0.9833 |
| AceGPT-v2-8B-Chat | 0.9167 | 0.8833 | 0.9087 | 0.8618 | 0.0385 | 0.0313 | 0.8787 | 0.8824 |
| Gemini-2.5-Flash | 0.9833 | 0.8333 | 0.9833 | 0.7778 | 0.0253 | 0.0225 | 0.9662 | 0.9704 |

## Gemini compact-variant experiment
The Gemini 2.5 Flash closed-model experiment used eight compact variants of the frozen final strategy. The run used temperature 0.0, max output tokens 64, seed 42 where supported, and thinking budget 0. The resulting CSV files are included under results/ using the suffix `compact_variants`.

Main result: Gemini was very strong in English, with only one majority-vote error: the question "What does HTTP stand for?" tied between ABBREVIATION and DESCRIPTION and was resolved as DESCRIPTION. In Arabic, Gemini correctly handled NUMBER, LOCATION, PERSON, DESCRIPTION, and ENTITY, but all ten Arabic ABBREVIATION questions were classified as DESCRIPTION. This lowered Arabic accuracy to 0.8333 and macro-F1 to 0.7778.

## Interpretation
The prompt progression confirms that explicit label definitions, few-shot examples, and a targeted DESCRIPTION/ENTITY rule reduce label-boundary confusion. Cross-model validation shows that the final prompt generalizes strongly across open models. Gemini's Arabic error pattern shows that a model can be stable across compact prompt variants while still being systematically wrong for a language-specific class.

## Generated files
- `results/raw_predictions/raw_predictions_crossmodel_gemini_2_5_flash_compact_variants.csv`
- `results/sample_level/sample_level_results_crossmodel_gemini_2_5_flash_compact_variants.csv`
- `results/metrics/metrics_crossmodel_gemini_2_5_flash_compact_variants.csv`
- `results/class_level/class_level_results_crossmodel_gemini_2_5_flash_compact_variants.csv`
- `results/error_analysis/error_analysis_crossmodel_gemini_2_5_flash_compact_variants.csv`
- `results/prompt_level_errors/prompt_level_errors_crossmodel_gemini_2_5_flash_compact_variants.csv`
- `results/summary_tables/bootstrap_ci_gemini_compact_variants.csv`

## Current conclusion
The final prompt design is effective for the open models and remains strong for Gemini in English. The main unresolved issue is Arabic ABBREVIATION under the compact Gemini prompt variants. Future work should add more explicit Arabic acronym-expansion examples or a separate Arabic abbreviation rule.
