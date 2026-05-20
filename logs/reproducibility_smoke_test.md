# Reproducibility smoke test

Date: 2026-05-20

Checks performed before packaging this cleaned repository:

- Validated that the notebook JSON is executable in an offline smoke-test copy with `RUN_MODE = "local_results_only"` and the pip-install cell skipped for this environment.
- Executed the notebook smoke test successfully through `jupyter nbconvert --execute`.
- Regenerated figures from checked-in CSV summary tables with `python scripts/generate_figures.py`.
- Verified `python scripts/make_figures.py` compatibility wrapper.
- Verified `python scripts/evaluate_predictions.py` on the Gemini compact-variant sample-level CSV.
- Recompiled `paper/main.tex` with XeLaTeX and regenerated `paper/main.pdf`.
- Rendered the final PDF pages to PNG to check that the previous GitHub placeholder and Arabic rendering issue were removed.

Scope note:

The offline smoke test verifies local data, prompt, metric, summary-table, figure, and paper reproducibility. It does not rerun Hugging Face model inference or Gemini API inference because those require GPU/model downloads and/or a `GEMINI_API_KEY`.
