# CSE Dataset - Data Quality Report

Generated: 2026-05-29T22:02:09Z

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,241,666 |
| Symbols | 295 |
| Date range | 2010-01-01 to 2026-05-29 |
| Columns | 46 |
| Duplicate `(symbol, date)` rows | 0 |
| OHLC-invalid rows | 0 (0.00%) |
| Source OHLC-invalid rows | 38,976 |
| OHLC-repaired rows | 38,976 |
| `volume_zscore` null rate | 0.00% |
| Adjusted-close rows | 0 |
| Adjusted-close symbols | 0 |
| Dividend rows with amount | 0 / 1,671 |
| Interest-rate source rows | 0 / 0 |
| Interest-rate max date | n/a |
| Interest-rate staleness | n/a days |
| Rows with T-bill 3M | 0 |
| Rows with policy rate | 0 |
| Rows with symbol sentiment | 0 |
| Symbols with sentiment | 0 |
| Rows with macro data (sp500 non-null) | 1,224,398 |
| Rows with market sentiment | 178,496 |
| Max-date staleness | 0 days |

## Validation Gates

- PASS: all configured quality gates passed

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `policy_rate` | 1,241,666 | 100.0% |
| `vader_score_mean` | 1,241,666 | 100.0% |
| `vader_score_max` | 1,241,666 | 100.0% |
| `vader_label` | 1,241,666 | 100.0% |
| `finbert_label` | 1,241,666 | 100.0% |
| `tbill_6m` | 1,241,666 | 100.0% |
| `tbill_3m` | 1,241,666 | 100.0% |
| `tbill_12m` | 1,241,666 | 100.0% |
| `market_vader_mean` | 1,063,170 | 85.62% |
| `market_news_count` | 1,063,170 | 85.62% |
| `usd_lkr` | 107,186 | 8.63% |
| `gdp_growth_pct` | 31,206 | 2.51% |
| `inflation_pct` | 31,206 | 2.51% |
| `close_to_ma200` | 29,035 | 2.34% |
| `nikkei225` | 17,268 | 1.39% |
| `hangseng` | 17,268 | 1.39% |
| `sp500` | 17,268 | 1.39% |
| `close_to_ma50` | 7,080 | 0.57% |
| `return_20d` | 5,900 | 0.48% |
| `volatility_20d` | 2,950 | 0.24% |
| `return_5d` | 1,475 | 0.12% |
| `pct_change_1d` | 295 | 0.02% |
| `return_1d` | 295 | 0.02% |

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|
| CHL.N0000 | 2026-03-02 | 2026-05-29 | 65 |
| CHL.X0000 | 2026-03-02 | 2026-05-29 | 65 |
| CINS.N0000 | 2026-03-02 | 2026-05-29 | 65 |
| JXG.N0000 | 2026-03-02 | 2026-05-29 | 65 |
| NAMU.N0000 | 2026-03-02 | 2026-05-29 | 65 |

## Known Limitations

- `usd_lkr` is annual World Bank data forward-filled to daily rows.
- `interest_rates.csv` is populated from a manual CBSL CSV/XLSX import under `data/raw/macro/`.
- `adj_close` applies only dividend rows with parsed `amount_per_share`; missing amounts are reported.
- `vader_label` is derived from VADER thresholds; true `finbert_label` is reserved for model inference.
- Symbol-level sentiment is partial and depends on dated CSE announcement records.
- `source_*` OHLC columns preserve original CSE values where high/low repairs were needed.
