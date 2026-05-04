# CSE Dataset — Data Quality Report

Generated: 2026-05-04 21:23

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,252,734 |
| Symbols | 294 |
| Date range | 2010-01-01 to 2026-05-01 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,252,734 (100.0%) |
| OHLC-invalid rows | 59,654 (4.76%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 178,164 (14.2%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,252,734 | 100.0% |
| `finbert_label` | 1,252,734 | 100.0% |
| `vader_score_max` | 1,252,734 | 100.0% |
| `vader_score_mean` | 1,252,734 | 100.0% |
| `market_vader_mean` | 1,074,570 | 85.78% |
| `market_news_count` | 1,074,570 | 85.78% |
| `usd_lkr` | 102,606 | 8.19% |
| `close_to_ma200` | 29,106 | 2.32% |
| `inflation_pct` | 25,578 | 2.04% |
| `gdp_growth_pct` | 25,578 | 2.04% |
| `close_to_ma50` | 7,056 | 0.56% |
| `return_20d` | 5,880 | 0.47% |
| `volatility_20d` | 2,940 | 0.23% |
| `return_5d` | 1,470 | 0.12% |
| `return_1d` | 294 | 0.02% |
| `pct_change_1d` | 294 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4261 |
| Median trading days per symbol | 4261 |
| Min trading days | 4261 |
| Max trading days | 4261 |
| Symbols with full 10+ year coverage | 294 |
| Symbols with OHLC violations | 14 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
