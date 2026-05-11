# CSE Dataset — Data Quality Report

Generated: 2026-05-11 21:31

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,258,470 |
| Symbols | 295 |
| Date range | 2010-01-01 to 2026-05-08 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,258,470 (100.0%) |
| OHLC-invalid rows | 42,660 (3.39%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 179,360 (14.3%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,258,470 | 100.0% |
| `finbert_label` | 1,258,470 | 100.0% |
| `vader_score_max` | 1,258,470 | 100.0% |
| `vader_score_mean` | 1,258,470 | 100.0% |
| `market_vader_mean` | 1,079,110 | 85.75% |
| `market_news_count` | 1,079,110 | 85.75% |
| `usd_lkr` | 104,430 | 8.3% |
| `close_to_ma200` | 29,205 | 2.32% |
| `inflation_pct` | 27,140 | 2.16% |
| `gdp_growth_pct` | 27,140 | 2.16% |
| `close_to_ma50` | 7,080 | 0.56% |
| `return_20d` | 5,900 | 0.47% |
| `volatility_20d` | 2,950 | 0.23% |
| `return_5d` | 1,475 | 0.12% |
| `return_1d` | 295 | 0.02% |
| `pct_change_1d` | 295 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4266 |
| Median trading days per symbol | 4266 |
| Min trading days | 4266 |
| Max trading days | 4266 |
| Symbols with full 10+ year coverage | 295 |
| Symbols with OHLC violations | 10 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
