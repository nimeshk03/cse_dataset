# CSE Dataset - Data Quality Report

Generated: 2026-09-04T22:19:55Z

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,261,263 |
| Symbols | 300 |
| Date range | 2010-01-01 to 2026-09-04 |
| Columns | 46 |
| Duplicate `(symbol, date)` rows | 0 |
| OHLC-invalid rows | 0 (0.00%) |
| Source OHLC-invalid rows | 40,554 |
| OHLC-repaired rows | 40,554 |
| `volume_zscore` null rate | 0.00% |
| Adjusted-close rows | 0 |
| Adjusted-close symbols | 0 |
| Dividend rows with amount | 0 / 1,734 |
| Interest-rate source rows | 0 / 0 |
| Interest-rate max date | n/a |
| Interest-rate staleness | n/a days |
| Rows with T-bill 3M | 0 |
| Rows with policy rate | 0 |
| Rows with symbol sentiment | 0 |
| Symbols with sentiment | 0 |
| Rows with macro data (sp500 non-null) | 1,224,398 |
| Rows with market sentiment | 177,869 |
| Max-date staleness | 0 days |

## Validation Gates

- PASS: all configured quality gates passed

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `policy_rate` | 1,261,263 | 100.0% |
| `vader_score_mean` | 1,261,263 | 100.0% |
| `vader_score_max` | 1,261,263 | 100.0% |
| `vader_label` | 1,261,263 | 100.0% |
| `finbert_label` | 1,261,263 | 100.0% |
| `tbill_6m` | 1,261,263 | 100.0% |
| `tbill_3m` | 1,261,263 | 100.0% |
| `tbill_12m` | 1,261,263 | 100.0% |
| `market_vader_mean` | 1,083,394 | 85.9% |
| `market_news_count` | 1,083,394 | 85.9% |
| `usd_lkr` | 126,783 | 10.05% |
| `sp500` | 36,865 | 2.92% |
| `inflation_pct` | 36,865 | 2.92% |
| `nikkei225` | 36,865 | 2.92% |
| `gdp_growth_pct` | 36,865 | 2.92% |
| `hangseng` | 36,865 | 2.92% |
| `close_to_ma200` | 29,262 | 2.32% |
| `close_to_ma50` | 7,131 | 0.57% |
| `return_20d` | 5,947 | 0.47% |
| `volatility_20d` | 2,987 | 0.24% |
| `return_5d` | 1,500 | 0.12% |
| `pct_change_1d` | 457 | 0.04% |
| `return_1d` | 457 | 0.04% |

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|
| AAF.R0000 | 2026-08-14 | 2026-08-21 | 6 |
| CHL.N0000 | 2026-03-02 | 2026-09-04 | 135 |
| CHL.X0000 | 2026-03-02 | 2026-09-04 | 132 |
| CINS.N0000 | 2026-03-02 | 2026-09-04 | 113 |
| HNBF.R0000 | 2026-06-10 | 2026-06-18 | 7 |
| HNBF.R0001 | 2026-06-10 | 2026-06-18 | 7 |
| JXG.N0000 | 2026-03-02 | 2026-09-04 | 135 |
| MBSL.R0001 | 2026-07-21 | 2026-07-29 | 7 |
| NAMU.N0000 | 2026-03-02 | 2026-09-04 | 133 |
| SING.N0000 | 2026-07-23 | 2026-09-04 | 30 |

## Known Limitations

- `usd_lkr` is annual World Bank data forward-filled to daily rows.
- `interest_rates.csv` is populated from a manual CBSL CSV/XLSX import under `data/raw/macro/`.
- `adj_close` applies only dividend rows with parsed `amount_per_share`; missing amounts are reported.
- `vader_label` is derived from VADER thresholds; true `finbert_label` is reserved for model inference.
- Symbol-level sentiment is partial and depends on dated CSE announcement records.
- `source_*` OHLC columns preserve original CSE values where high/low repairs were needed.
