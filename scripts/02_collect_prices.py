import argparse
import requests
import pandas as pd
import time
import logging
import os
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

RAW_CSV = 'data/raw/ohlcv/all_raw_2010_to_present.csv'


def get_incremental_start() -> pd.Timestamp:
    """Return the day after the latest date already in the raw CSV."""
    if os.path.exists(RAW_CSV):
        try:
            existing = pd.read_csv(RAW_CSV, usecols=['date'])
            last_date = pd.to_datetime(existing['date']).max()
            start = last_date + pd.Timedelta(days=1)
            logging.info("Incremental mode: last fetched date = %s, starting from %s",
                         last_date.date(), start.date())
            return start
        except Exception as e:
            logging.warning("Could not read existing raw CSV (%s) — falling back to full fetch", e)
    return pd.to_datetime('2010-01-01')

def fetch_trade_summary_for_date(date_str):
    url = 'https://www.cse.lk/api/tradeSummary'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.post(url, files={'date': (None, date_str)}, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            if 'reqTradeSummery' in data:
                return date_str, data['reqTradeSummery']
    except Exception as e:
        pass
    return date_str, None

def collect_historical_prices(mode: str = 'full'):
    os.makedirs('data/raw/ohlcv', exist_ok=True)
    os.makedirs('data/processed/daily_ohlcv', exist_ok=True)

    # 1. Determine dates to fetch
    start_date = get_incremental_start() if mode == 'incremental' else pd.to_datetime('2010-01-01')
    end_date = pd.to_datetime(datetime.today().strftime('%Y-%m-%d')) - pd.Timedelta(days=1)
    
    # Generate business days
    trading_dates = pd.date_range(start=start_date, end=end_date, freq='B')
    date_strings = [d.strftime('%Y-%m-%d') for d in trading_dates]
    
    logging.info(f"Generated {len(date_strings)} potential trading dates from 2010 to present.")
    
    # To avoid overwhelming the server, we'll process in chunks and sleep
    all_data = []
    
    # Let's do a fast concurrent fetch, but limit workers to 5 to be polite to cse.lk
    CHUNK_SIZE = 500 # Adjust for demonstration, let's fetch first 500 for proof of concept
    
    # For a full run, we would do all date_strings. 
    # Because we are in an automated step, let's fetch the first year (2010) as a test, 
    # then explain that the full run takes ~10-15 mins.
    dates_to_fetch = date_strings # doing full
    
    fetched_count = 0
    empty_count = 0
    error_count = 0
    
    # We will accumulate records in memory, then group by symbol
    # This takes roughly 5-10 minutes for 3800 days at 5 req/sec
    batch_size = 100
    
    # Instead of doing all 3800 right now, let's collect the most recent 1 year (2025-2026), 
    # plus the gap year we had issues with (2021) to prove the pipeline.
    # Actually, we should just run the whole thing concurrently if it's fast enough.
    # Let's just collect 2021-2022 to show it works, then we can run the rest offline.
    
    target_dates = date_strings
    if not target_dates:
        logging.info("No new dates to fetch — dataset is already up to date.")
        return
    logging.info(f"Fetching {len(target_dates)} dates concurrently...")
    
    records = []
    
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(fetch_trade_summary_for_date, d): d for d in target_dates}
        
        for i, future in enumerate(as_completed(futures)):
            date_str, data = future.result()
            
            if data is not None:
                if len(data) > 0:
                    fetched_count += 1
                    for row in data:
                        # Append date to the row
                        row['date'] = date_str
                        records.append(row)
                else:
                    empty_count += 1 # market likely closed
            else:
                error_count += 1
                
            if (i+1) % 100 == 0:
                logging.info(f"Processed {i+1}/{len(target_dates)} dates... (Success: {fetched_count}, Empty: {empty_count}, Error: {error_count})")
                
    logging.info(f"Finished fetching. Total records: {len(records)}")
    
    if len(records) == 0:
        logging.error("No records fetched!")
        return
        
    # Convert to DataFrame
    df = pd.DataFrame(records)
    
    # Append to existing raw CSV in incremental mode, otherwise overwrite
    if mode == 'incremental' and os.path.exists(RAW_CSV):
        existing = pd.read_csv(RAW_CSV)
        df = pd.concat([existing, df], ignore_index=True).drop_duplicates(subset=['date', 'symbol'])
        logging.info("Appended to existing raw CSV — total rows: %d", len(df))
    df.to_csv(RAW_CSV, index=False)
    
    # Group by symbol and save individual files
    symbols = df['symbol'].unique()
    logging.info(f"Found {len(symbols)} unique symbols. Saving individual CSVs...")
    
    # Load metadata to track failure rates
    try:
        meta = pd.read_csv('data/processed/company_metadata.csv')
        known_symbols = set(meta['symbol'])
    except:
        known_symbols = set(symbols)
        
    collection_log = []
    
    for sym in symbols:
        sym_df = df[df['symbol'] == sym].copy()
        
        # Sort and clean
        sym_df = sym_df.sort_values('date')
        
        # Rename columns to standard format
        rename_map = {
            'date': 'Date',
            'open': 'Open',
            'high': 'High',
            'low': 'Low',
            'closingPrice': 'Close',
            'sharevolume': 'Volume',
            'turnover': 'Turnover',
            'tradevolume': 'Trades'
        }
        
        # Keep only existing columns
        cols_to_keep = [c for c in rename_map.keys() if c in sym_df.columns]
        sym_df = sym_df[cols_to_keep]
        sym_df = sym_df.rename(columns={k: rename_map[k] for k in cols_to_keep})
        
        # Drop rows with zero volume or NaN close
        sym_df = sym_df.dropna(subset=['Close'])
        sym_df = sym_df[sym_df['Volume'] > 0]
        
        if len(sym_df) > 0:
            sym_df.to_csv(f'data/raw/ohlcv/{sym}.csv', index=False)
            
            collection_log.append({
                'symbol': sym,
                'date_min': sym_df['Date'].min(),
                'date_max': sym_df['Date'].max(),
                'row_count': len(sym_df),
                'status': 'success'
            })
        else:
            collection_log.append({
                'symbol': sym,
                'date_min': None,
                'date_max': None,
                'row_count': 0,
                'status': 'failed'
            })
            
    # Mark known symbols that didn't appear at all as failed
    for sym in known_symbols:
        if sym not in symbols:
            collection_log.append({
                'symbol': sym,
                'date_min': None,
                'date_max': None,
                'row_count': 0,
                'status': 'failed'
            })
            
    log_df = pd.DataFrame(collection_log)
    log_df.to_csv('data/raw/ohlcv/collection_log.csv', index=False)
    
    success_rate = len(log_df[log_df['status'] == 'success']) / len(log_df)
    logging.info(f"Collection complete. Success rate: {success_rate:.1%}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Collect CSE OHLCV price data')
    parser.add_argument('--mode', choices=['full', 'incremental'], default='full',
                        help='full = fetch 2010-present; incremental = fetch from last date only')
    args = parser.parse_args()
    collect_historical_prices(mode=args.mode)
