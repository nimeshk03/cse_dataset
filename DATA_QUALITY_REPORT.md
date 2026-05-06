# CSE Dataset — Data Quality Report

Generated: 2026-05-06 21:23

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 637,686 |
| Symbols | 294 |
| Date range | 2010-01-04 to 2026-05-01 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 637,686 (100.0%) |
| OHLC-invalid rows | 32,535 (5.10%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 87,024 (13.6%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 637,686 | 100.0% |
| `finbert_label` | 637,686 | 100.0% |
| `vader_score_max` | 637,686 | 100.0% |
| `vader_score_mean` | 637,686 | 100.0% |
| `market_vader_mean` | 550,662 | 86.35% |
| `market_news_count` | 550,662 | 86.35% |
| `usd_lkr` | 48,216 | 7.56% |
| `close_to_ma200` | 29,106 | 4.56% |
| `inflation_pct` | 11,760 | 1.84% |
| `gdp_growth_pct` | 11,760 | 1.84% |
| `close_to_ma50` | 7,056 | 1.11% |
| `return_20d` | 5,880 | 0.92% |
| `volatility_20d` | 2,940 | 0.46% |
| `return_5d` | 1,470 | 0.23% |
| `return_1d` | 294 | 0.05% |
| `pct_change_1d` | 294 | 0.05% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 2169 |
| Median trading days per symbol | 2169 |
| Min trading days | 2169 |
| Max trading days | 2169 |
| Symbols with full 10+ year coverage | 294 |
| Symbols with OHLC violations | 15 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
