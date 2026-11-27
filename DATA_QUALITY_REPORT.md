# CSE Dataset - Data Quality Report

Generated: 2026-11-27T02:48:13Z

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,278,263 |
| Symbols | 303 |
| Date range | 2010-01-01 to 2026-11-27 |
| Columns | 46 |
| Duplicate `(symbol, date)` rows | 0 |
| OHLC-invalid rows | 0 (0.00%) |
| Source OHLC-invalid rows | 41,677 |
| OHLC-repaired rows | 41,677 |
| `volume_zscore` null rate | 0.00% |
| Adjusted-close rows | 0 |
| Adjusted-close symbols | 0 |
| Dividend rows with amount | 0 / 1,779 |
| Interest-rate source rows | 0 / 0 |
| Interest-rate max date | n/a |
| Interest-rate staleness | n/a days |
| Rows with T-bill 3M | 0 |
| Rows with policy rate | 0 |
| Rows with symbol sentiment | 0 |
| Symbols with sentiment | 0 |
| Rows with macro data (sp500 non-null) | 1,224,398 |
| Rows with market sentiment | 176,327 |
| Max-date staleness | 0 days |

## Validation Gates

- PASS: all configured quality gates passed

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `policy_rate` | 1,278,263 | 100.0% |
| `vader_score_mean` | 1,278,263 | 100.0% |
| `vader_score_max` | 1,278,263 | 100.0% |
| `vader_label` | 1,278,263 | 100.0% |
| `finbert_label` | 1,278,263 | 100.0% |
| `tbill_6m` | 1,278,263 | 100.0% |
| `tbill_3m` | 1,278,263 | 100.0% |
| `tbill_12m` | 1,278,263 | 100.0% |
| `market_vader_mean` | 1,101,936 | 86.21% |
| `market_news_count` | 1,101,936 | 86.21% |
| `gdp_growth_pct` | 53,865 | 4.21% |
| `sp500` | 53,865 | 4.21% |
| `usd_lkr` | 53,865 | 4.21% |
| `nikkei225` | 53,865 | 4.21% |
| `inflation_pct` | 53,865 | 4.21% |
| `hangseng` | 53,865 | 4.21% |
| `close_to_ma200` | 29,338 | 2.3% |
| `close_to_ma50` | 7,148 | 0.56% |
| `return_20d` | 5,964 | 0.47% |
| `volatility_20d` | 3,004 | 0.24% |
| `return_5d` | 1,515 | 0.12% |
| `pct_change_1d` | 460 | 0.04% |
| `return_1d` | 460 | 0.04% |

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|
| AAF.R0000 | 2026-08-14 | 2026-08-21 | 6 |
| CHL.N0000 | 2026-03-02 | 2026-11-27 | 195 |
| CHL.X0000 | 2026-03-02 | 2026-11-27 | 189 |
| CINS.N0000 | 2026-03-02 | 2026-11-27 | 158 |
| CPRT.R0000 | 2026-10-19 | 2026-10-26 | 6 |
| HNBF.R0000 | 2026-06-10 | 2026-06-18 | 7 |
| HNBF.R0001 | 2026-06-10 | 2026-06-18 | 7 |
| JXG.N0000 | 2026-03-02 | 2026-11-27 | 195 |
| MBSL.R0001 | 2026-07-21 | 2026-07-29 | 7 |
| NAMU.N0000 | 2026-03-02 | 2026-11-27 | 193 |
| SFIN.R0000 | 2026-10-30 | 2026-11-06 | 6 |
| SING.N0000 | 2026-07-23 | 2026-11-27 | 89 |
| TAJ.R0000 | 2026-11-16 | 2026-11-20 | 5 |

## Known Limitations

- `usd_lkr` is annual World Bank data forward-filled to daily rows.
- `interest_rates.csv` is populated from a manual CBSL CSV/XLSX import under `data/raw/macro/`.
- `adj_close` applies only dividend rows with parsed `amount_per_share`; missing amounts are reported.
- `vader_label` is derived from VADER thresholds; true `finbert_label` is reserved for model inference.
- Symbol-level sentiment is partial and depends on dated CSE announcement records.
- `source_*` OHLC columns preserve original CSE values where high/low repairs were needed.
