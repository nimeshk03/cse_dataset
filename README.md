# CSE ML Dataset

> An end-to-end data engineering pipeline for the Colombo Stock Exchange (CSE), producing a comprehensive, ML-ready dataset covering all ~284 listed equities from 2010 to present.

**Status: Active Development** | **Coverage: 284 stocks | 2010–present | 5 data domains**

---

## Overview

This project reverse-engineers undocumented internal REST APIs on the CSE website and combines them with public data sources (World Bank, stooq, WordPress REST APIs) to build the most complete open dataset of Sri Lankan equity market data available.

The pipeline is fully automated, zero-cost, and designed to be extended with daily updates via GitHub Actions.

### What makes this project interesting

- **Discovered and validated hidden CSE internal APIs** (`/api/tradeSummary`, `/api/corporateCalender`, `/api/news/web`) through browser DevTools network interception — these are undocumented and not referenced anywhere publicly
- **Single API call per trading day** returns OHLCV data for all 284 listed equities simultaneously, enabling efficient bulk historical collection back to 2010
- **Concurrent data collection** using `ThreadPoolExecutor` reduces fetch time by ~20x vs sequential requests
- **Survivorship-bias-free** design — includes delisted companies with `delisted` flag
- **Multi-source text corpus** combining official CSE announcements and LBO news with VADER sentiment scores

---

## Dataset Contents

| Domain | File | Rows | Coverage |
|---|---|---|---|
| Company Metadata | `data/processed/company_metadata.csv` | ~284 | All active + delisted CSE companies |
| Daily OHLCV | `data/processed/all_stocks_merged.parquet` | ~2M+ | 284 stocks, 2010–present |
| Dividends | `data/processed/fundamentals/dividends.csv` | ~5,000+ | All declared dividends, 2010–present |
| Annual Reports Index | `data/processed/fundamentals/annual_reports_index.csv` | ~1,000+ | PDF links per company per year |
| News Headlines | `data/processed/news/lbo_articles_clean.csv` | ~1,400+ | LBO archive, 2021–present |
| CSE Announcements | `data/processed/news/cse_news_clean.csv` | varies | Per-company official announcements |
| Unified Sentiment | `data/processed/news/unified_sentiment.csv` | all news | VADER scores + FinBERT labels |
| USD/LKR Rate | `data/processed/macro/usd_lkr_daily.csv` | 64 | World Bank annual, 1960–present |
| Global Indices | `data/processed/macro/global_indices.csv` | ~6,800 | S&P 500, Nikkei 225, Hang Seng, 2000–present |
| CBSL Indicators | `data/processed/macro/cbsl_indicators.csv` | 66 | GDP growth, CPI, deposit rate (World Bank) |

---

## Architecture

```
scripts/
├── 00_recon.py                  # API endpoint discovery + source validation
├── 00b_fill_aspi_gap.py         # ASPI index gap-filling
├── 01_collect_metadata.py       # Active company list + GICS sector mapping
├── 01b_find_delisted.py         # Delisted company enrichment
├── 02_collect_prices.py         # Bulk OHLCV via hidden /api/tradeSummary
├── 02b_merge_data.py            # Per-stock CSVs → merged Parquet
├── 03_collect_fundamentals.py   # Annual report PDF index
├── 03b_collect_corporate_actions.py  # Dividends + splits via /api/corporateCalender
├── 04a_scrape_lbo.py            # Lanka Business Online via WP REST API
├── 04b_scrape_cse_news.py       # CSE per-company announcements
├── 04c_sentiment_analysis.py    # VADER scoring + FinBERT label mapping
└── 05_collect_macro.py          # USD/LKR, global indices, World Bank macro
```

---

## Technical Stack

| Category | Libraries |
|---|---|
| HTTP / Scraping | `requests`, `httpx`, `beautifulsoup4`, `playwright` |
| Data | `pandas`, `polars`, `pyarrow` |
| Finance APIs | `yfinance`, `finnhub-python`, `wbdata` |
| NLP / Sentiment | `vaderSentiment`, `transformers` (FinBERT), `nltk` |
| ML / Validation | `scikit-learn`, `statsmodels` |
| PDF Parsing | `pdfplumber`, `pypdf` |

---

## Key API Discoveries

### `/api/tradeSummary` (undocumented)
Returns full OHLCV data for all listed equities on a given trading day.
```python
import requests
r = requests.post(
    "https://www.cse.lk/api/tradeSummary",
    files={"date": (None, "2024-01-15")},
    headers={"User-Agent": "Mozilla/5.0"},
)
rows = r.json()["reqTradeSummery"]  # list of all equities for that day
```

### `/api/corporateCalender` (undocumented)
Returns all dividend and corporate action announcements for a given month.
```python
r = requests.post(
    "https://www.cse.lk/api/corporateCalender",
    data={"year": "2024", "month": "6"},
    headers={"User-Agent": "Mozilla/5.0"},
)
actions = r.json()["approvedCoopCalAnnouncements"]
```

---

## Setup

```bash
git clone https://github.com/nimeshk03/cse_dataset.git
cd cse_dataset
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add optional API keys (Alpha Vantage, Finnhub — not required for core collection):
```
ALPHA_VANTAGE_KEY=your_key_here
FINNHUB_KEY=your_key_here
```

Run the full pipeline in order:
```bash
python scripts/01_collect_metadata.py
python scripts/02_collect_prices.py      # ~2–4 hours for full 2010–present range
python scripts/02b_merge_data.py
python scripts/03_collect_fundamentals.py
python scripts/03b_collect_corporate_actions.py
python scripts/04a_scrape_lbo.py
python scripts/04b_scrape_cse_news.py
python scripts/04c_sentiment_analysis.py
python scripts/05_collect_macro.py
```

---

## Roadmap

| Phase | Status | Description |
|---|---|---|
| Recon & Setup | Done | API discovery, source validation |
| Stock List & Metadata | Done | 284 companies, GICS sectors, delisted flag |
| Historical OHLCV | Done | 2010–present, all equities, merged Parquet |
| Fundamentals | Done | Dividends, splits, annual report index |
| News & Sentiment | Done | LBO + CSE announcements, VADER scores |
| Macroeconomic Features | Done | USD/LKR, S&P 500/Nikkei/HSI, GDP, CPI |
| Cleaning & Feature Engineering | Planned | Returns, volatility, MA ratios, adj_close |
| Baseline Notebooks | Planned | Price prediction, portfolio optimization, anomaly detection |
| Publishing | Planned | Kaggle + Hugging Face, GitHub Actions daily update |

---

## Data Schema

See [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md) for full column definitions.

---

## Limitations

- `interest_rates.csv` (T-bill rates) requires a manual download from the CBSL website — a placeholder file is included
- USD/LKR rate is annual (World Bank) — daily granularity pending a reliable free source
- LBO news archive only covers 2021–present via their WordPress API
- CSE API rate limits are not published; the pipeline uses conservative delays

---

## License

MIT License. Data sourced from public APIs and websites. Not affiliated with the Colombo Stock Exchange.
