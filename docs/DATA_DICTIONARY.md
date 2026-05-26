# Data Dictionary

Full column definitions for all dataset files.

---

## `data/processed/company_metadata.csv`

| Column | Type | Description |
|---|---|---|
| `symbol` | string | CSE ticker symbol (e.g., `COMB.N0000`) |
| `company_name` | string | Full registered company name |
| `sector` | string | CSE sector classification |
| `gics_sector` | string | Mapped GICS sector equivalent |
| `board` | string | Listing board: `Main`, `Diri Savi`, or `Empower` |
| `listing_date` | date | Date first listed on the CSE |
| `isin` | string | International Securities Identification Number |
| `delisted` | bool | `True` if company has been delisted |
| `delisting_date` | date | Date of delisting, or null if still active |
| `yahoo_ticker` | string | Yahoo Finance ticker format (e.g., `COMB.CM`) |
| `yf_available` | bool | Whether yfinance returns data for this ticker |

---

## `data/processed/all_stocks_merged.parquet`

One row per stock per trading day.

| Column | Type | Description |
|---|---|---|
| `symbol` | string | CSE ticker symbol |
| `date` | date | Trading date (`YYYY-MM-DD`) |
| `open` | float64 | Opening price (LKR) |
| `high` | float64 | Daily high price (LKR) |
| `low` | float64 | Daily low price (LKR) |
| `close` | float64 | Closing price (LKR) |
| `volume` | int64 | Number of shares traded |
| `turnover` | float64 | Total traded value in LKR |
| `trade_count` | int64 | Number of individual trades |
| `pct_change` | float64 | Daily percentage change in close price |
| `source_open` | float64 | Original open value from the CSE payload before any repair |
| `source_high` | float64 | Original high value from the CSE payload before any repair |
| `source_low` | float64 | Original low value from the CSE payload before any repair |
| `source_close` | float64 | Original close value from the CSE payload before any repair |
| `source_ohlc_invalid` | bool | Whether original high/low failed to bound open/close |
| `ohlc_repaired` | bool | Whether published high/low were repaired deterministically |
| `ohlc_invalid` | bool | Whether published high/low still fail OHLC validation after repair |

---

## `data/processed/fundamentals/dividends.csv`

| Column | Type | Description |
|---|---|---|
| `symbol` | string | CSE ticker symbol |
| `company` | string | Company name as returned by the API |
| `xd_date` | date | Ex-dividend date |
| `payment_date` | date | Dividend payment date |
| `type` | string | Announcement category (e.g., `Cash Dividend`) |
| `remarks` | string | Free-text description of the corporate action |

---

## `data/processed/fundamentals/splits.csv`

| Column | Type | Description |
|---|---|---|
| `symbol` | string | CSE ticker symbol |
| `company` | string | Company name |
| `xd_date` | date | Ex-date of the split/bonus issue |
| `payment_date` | date | Effective payment date |
| `type` | string | Action type (e.g., `Share Split`, `Bonus Issue`) |
| `remarks` | string | Free-text description |

---

## `data/processed/fundamentals/annual_reports_index.csv`

| Column | Type | Description |
|---|---|---|
| `symbol` | string | CSE ticker symbol |
| `year` | int | Financial year of the report |
| `report_type` | string | `Annual` or `Quarterly` |
| `file_text` | string | Display label for the report |
| `url` | string | Direct URL to the PDF on `cse.lk` |

---

## `data/processed/news/lbo_articles_clean.csv`

| Column | Type | Description |
|---|---|---|
| `id` | int | WordPress post ID |
| `date` | datetime | Publication date and time |
| `source` | string | Always `LBO` |
| `title` | string | Article headline (HTML stripped) |
| `excerpt` | string | Short summary (HTML stripped) |
| `url` | string | Canonical article URL |
| `text` | string | Combined `title + " " + excerpt` used for sentiment |

---

## `data/processed/news/cse_news_clean.csv`

| Column | Type | Description |
|---|---|---|
| `symbol` | string | CSE ticker symbol the announcement relates to |
| `date` | datetime | Announcement date |
| `date_missing_reason` | string | Reason date is absent when the API payload does not provide one |
| `source` | string | Always `CSE` |
| `title` | string | Announcement subject |
| `text` | string | Full announcement body text (HTML stripped) |
| `url` | string | Link to announcement PDF or detail page |

---

## `data/processed/news/unified_sentiment.csv`

All news from both sources with sentiment scores appended.

| Column | Type | Description |
|---|---|---|
| `symbol` | string | Ticker (where available; null for LBO general news) |
| `date` | datetime | Publication or announcement date |
| `source` | string | `LBO` or `CSE` |
| `title` | string | Headline or announcement subject |
| `text` | string | Input text used for sentiment scoring |
| `url` | string | Source URL |
| `vader_score` | float64 | VADER compound score, range [-1.0, +1.0] |
| `vader_label` | string | Mapped VADER label: `positive`, `neutral`, or `negative` |
| `finbert_label` | string | Reserved for true FinBERT inference; currently null |

> `vader_label` is derived from `vader_score` thresholds (>=0.05 positive, <=-0.05 negative). `finbert_label` is reserved for future model inference.

---

## `data/processed/macro/usd_lkr_daily.csv`

| Column | Type | Description |
|---|---|---|
| `date` | date | Year-end date (annual World Bank data) |
| `usd_lkr` | float64 | Official exchange rate: LKR per 1 USD |

---

## `data/processed/macro/global_indices.csv`

| Column | Type | Description |
|---|---|---|
| `date` | date | Trading date |
| `sp500` | float64 | S&P 500 closing level |
| `nikkei225` | float64 | Nikkei 225 closing level |
| `hangseng` | float64 | Hang Seng Index closing level |

---

## `data/processed/macro/cbsl_indicators.csv`

Annual macroeconomic indicators for Sri Lanka from the World Bank.

| Column | Type | Description |
|---|---|---|
| `year` | string | Year (e.g., `2023`) |
| `date` | date | Year-end date |
| `gdp_growth_pct` | float64 | Annual GDP growth rate (%) — World Bank `NY.GDP.MKTP.KD.ZG` |
| `inflation_pct` | float64 | Annual CPI inflation (%) — World Bank `FP.CPI.TOTL.ZG` |
| `deposit_rate_pct` | float64 | Bank deposit interest rate (%) — World Bank `FR.INR.DPST` |

---

## `data/processed/macro/interest_rates.csv`

| Column | Type | Description |
|---|---|---|
| `date` | date | Date of rate observation |
| `tbill_3m` | float64 | 3-month Treasury bill rate (%) |
| `tbill_12m` | float64 | 12-month Treasury bill rate (%) |

> Currently a placeholder. Populate with data from the [CBSL website](https://www.cbsl.gov.lk/en/statistics/statistical-tables/financial-sector/interest-rates).
