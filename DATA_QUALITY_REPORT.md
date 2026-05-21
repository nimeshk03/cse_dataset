# CSE Dataset — Data Quality Report

Generated: 2026-05-21 21:49

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,243,734 |
| Symbols | 291 |
| Date range | 2010-01-01 to 2026-05-20 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,243,734 (100.0%) |
| OHLC-invalid rows | 47,014 (3.78%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 178,383 (14.3%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,243,734 | 100.0% |
| `finbert_label` | 1,243,734 | 100.0% |
| `vader_score_max` | 1,243,734 | 100.0% |
| `vader_score_mean` | 1,243,734 | 100.0% |
| `market_vader_mean` | 1,065,351 | 85.66% |
| `market_news_count` | 1,065,351 | 85.66% |
| `usd_lkr` | 105,342 | 8.47% |
| `inflation_pct` | 29,100 | 2.34% |
| `gdp_growth_pct` | 29,100 | 2.34% |
| `close_to_ma200` | 28,809 | 2.32% |
| `close_to_ma50` | 6,984 | 0.56% |
| `return_20d` | 5,820 | 0.47% |
| `volatility_20d` | 2,910 | 0.23% |
| `return_5d` | 1,455 | 0.12% |
| `return_1d` | 291 | 0.02% |
| `pct_change_1d` | 291 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4274 |
| Median trading days per symbol | 4274 |
| Min trading days | 4274 |
| Max trading days | 4274 |
| Symbols with full 10+ year coverage | 291 |
| Symbols with OHLC violations | 11 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
