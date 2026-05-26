# Sources

This dataset is assembled from public sources.

| Source | Usage | Notes |
|---|---|---|
| Colombo Stock Exchange (`cse.lk`) | Company metadata, daily OHLCV, corporate calendar, news, annual report links | Uses public website APIs including undocumented internal endpoints discovered through browser network inspection. |
| Lanka Business Online | Financial/business news | Uses the public WordPress REST API. |
| World Bank | USD/LKR and macro indicators | Annual indicators are forward-filled when joined to daily market rows. |
| stooq.com | Global index levels | Used for S&P 500, Nikkei 225, and Hang Seng daily closes. |
| CBSL | Interest rate target source | Current `interest_rates.csv` is a placeholder until manual/automated ingestion is added. |

This project is not affiliated with or endorsed by the Colombo Stock Exchange or any listed data source.
