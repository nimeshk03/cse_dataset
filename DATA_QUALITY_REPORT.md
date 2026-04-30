# CSE Dataset — Data Quality Report

Generated: 2026-04-30 21:16

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,235,110 |
| Symbols | 290 |
| Date range | 2010-01-01 to 2026-04-29 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,235,110 (100.0%) |
| OHLC-invalid rows | 59,626 (4.83%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 176,030 (14.3%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,235,110 | 100.0% |
| `finbert_label` | 1,235,110 | 100.0% |
| `vader_score_max` | 1,235,110 | 100.0% |
| `vader_score_mean` | 1,235,110 | 100.0% |
| `market_vader_mean` | 1,059,080 | 85.75% |
| `market_news_count` | 1,059,080 | 85.75% |
| `usd_lkr` | 100,630 | 8.15% |
| `close_to_ma200` | 28,710 | 2.32% |
| `inflation_pct` | 24,650 | 2.0% |
| `gdp_growth_pct` | 24,650 | 2.0% |
| `close_to_ma50` | 6,960 | 0.56% |
| `return_20d` | 5,800 | 0.47% |
| `volatility_20d` | 2,900 | 0.23% |
| `return_5d` | 1,450 | 0.12% |
| `return_1d` | 290 | 0.02% |
| `pct_change_1d` | 290 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4259 |
| Median trading days per symbol | 4259 |
| Min trading days | 4259 |
| Max trading days | 4259 |
| Symbols with full 10+ year coverage | 290 |
| Symbols with OHLC violations | 14 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
