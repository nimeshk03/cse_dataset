# Changelog

## 0.1.0 - Daily Automation Hardening

- Added a `uv` managed runtime with Python 3.11.
- Added daily orchestration through `scripts/daily_update.py`.
- Added dataset validation gates and machine-readable quality summary output.
- Split VADER-derived labels into `vader_label` and reserved `finbert_label` for true model inference.
- Added optional Hugging Face and Kaggle publishing scripts that skip when credentials are absent.
- Updated documentation to reflect current generated artifact quality and known limitations.
