# CSE ML Dataset

Automated data pipeline for a machine-learning-ready Colombo Stock Exchange
(CSE) dataset.

**Status:** daily automation hardening  
**Current generated coverage:** 295 symbols, 1,240,806 price rows,
2010-01-01 to 2026-05-26  
**Primary source:** undocumented CSE `tradeSummary` daily market API

---

## Overview

This project collects CSE equity market data, corporate actions, annual report
links, financial news, sentiment scores, and macro context into a unified
Parquet dataset. The core discovery is that one CSE internal API call per
trading day returns OHLCV rows for all listed securities, which makes historical
collection practical without paid finance APIs.

The current priority is reliable unattended daily updates through GitHub
Actions. Raw source caches stay ignored under `data/raw/`; processed and
published outputs are intended to be committed after validation passes.

---

## Dataset Contents

| Domain | File | Current Rows | Notes |
|---|---:|---:|---|
| Company metadata | `data/processed/company_metadata.csv` | 305 | 302 active, 3 delisted in the current local artifact |
| Daily OHLCV | `data/processed/all_stocks_merged.parquet` | 1,240,806 | Built from CSE `tradeSummary` |
| Cleaned/features | `data/processed/all_stocks_features.parquet` | 1,240,806 | Returns, volatility, MA ratios, volume z-score |
| Published unified dataset | `data/published/cse_unified.parquet` | 1,240,806 | Prices + features + macro + sentiment |
| Dividends | `data/processed/fundamentals/dividends.csv` | 1,654 | Ex/payment dates preserved; parsed amount fields included |
| Splits | `data/processed/fundamentals/splits.csv` | 0 | No split rows in current artifact |
| Annual report index | `data/processed/fundamentals/annual_reports_index.csv` | 4,128 | Official CSE PDF links |
| LBO news | `data/processed/news/lbo_articles_clean.csv` | 2,000 | WordPress API archive sample |
| CSE news | `data/processed/news/cse_news_clean.csv` | 495 | Symbol news; dates depend on API payload availability |
| Unified sentiment | `data/processed/news/unified_sentiment.csv` | 2,495 | VADER score and `vader_label` |
| Macro | `data/processed/macro/*.csv` | varies | World Bank, stooq, placeholder interest rates |

See [docs/DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md) for schema details.

---

## Setup

Use `uv` as the single supported local and CI environment path:

```bash
uv sync
uv run python scripts/smoke_check.py
```

Run an offline rebuild from existing cached/committed artifacts:

```bash
uv run python scripts/daily_update.py --offline --allow-stale
```

Run the normal incremental daily pipeline:

```bash
uv run python scripts/daily_update.py
```

Validate the published dataset:

```bash
uv run python scripts/validate_dataset.py
```

---

## Pipeline

```text
scripts/01_collect_metadata.py
scripts/02_collect_prices.py --mode incremental
scripts/02b_merge_data.py
scripts/06_clean_prices.py
scripts/07_engineer_features.py
scripts/05_collect_macro.py
scripts/04a_scrape_lbo.py
scripts/04b_scrape_cse_news.py
scripts/04c_sentiment_analysis.py
scripts/08_build_unified.py
scripts/validate_dataset.py
```

For automation, use the orchestrator:

```bash
uv run python scripts/daily_update.py
```

The GitHub Actions workflow runs the orchestrator, validates quality gates,
optionally publishes to Hugging Face/Kaggle when credentials are present, and
commits generated processed/published outputs only when files changed.

---

## Quality Gates

`scripts/validate_dataset.py` writes:

- `DATA_QUALITY_REPORT.md`
- `data/published/quality_summary.json`

Current gates check that:

- `data/published/cse_unified.parquet` exists and loads
- row count does not drop by more than 1% from the previous summary
- symbol count does not drop by more than 1
- max dataset date is within 7 calendar days for real daily runs
- OHLC-invalid rows stay under the current baseline of 3.11%
- `volume_zscore` null rate is under 20%
- no duplicate `(symbol, date)` rows exist

Use `--allow-stale` only for local/offline rebuilds against old artifacts.

---

## Known Limitations

- `adj_close` uses parsed dividend amounts where available; events without
  amounts are preserved and reported but not applied.
- `interest_rates.csv` is populated from a manual CBSL CSV/XLSX import placed
  under `data/raw/macro/`.
- USD/LKR is annual World Bank data forward-filled to daily rows unless a daily
  source is available.
- `vader_label` is a VADER-threshold label. `finbert_label` is reserved for true
  FinBERT inference and is currently null.
- Symbol-level sentiment is partial because some CSE news API payloads still do
  not expose recoverable announcement dates.
- The current quality baseline still has OHLC-invalid rows; these are flagged
  in `source_ohlc_invalid`. Published `high`/`low` values are repaired when the
  fix is deterministic, and `source_*` columns preserve the original values.

---

## Optional Publishing

Publishing scripts are no-ops unless credentials are configured:

```bash
uv run python scripts/publish_huggingface.py
uv run python scripts/publish_kaggle.py
```

Required environment:

- Hugging Face: `HF_TOKEN`, `HF_DATASET_REPO`
- Kaggle: `KAGGLE_USERNAME`, `KAGGLE_KEY`, `KAGGLE_DATASET_SLUG`

---

## License

MIT License. Data is sourced from public websites/APIs. This project is not
affiliated with the Colombo Stock Exchange.
