import pandas as pd
import glob
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def process_and_merge():
    """Merge the recently fetched API data and Kaggle legacy data into a single parquet file."""
    
    logging.info("Starting merge process...")
    os.makedirs('data/processed', exist_ok=True)
    
    # 1. Load Kaggle legacy data
    # The Kaggle dataset only contains ASPI, so we don't merge it into individual stock files!
    # Wait, earlier we checked 'data/raw/legacy/CSE.csv' and it was ONLY ASPI data.
    # So we don't have a 1985-2009 Kaggle dataset for INDIVIDUAL stocks, only for the index.
    # Our individual stock history starts from whenever the CSE API has data (which we found goes back to at least 2012).
    
    # 2. Load API fetched stock data (2022-2026 for now, as fetched)
    csv_files = glob.glob('data/raw/ohlcv/*.csv')
    csv_files = [f for f in csv_files if 'collection_log' not in f and 'all_raw' not in f]
    
    if not csv_files:
        logging.warning("No individual stock CSV files found in data/raw/ohlcv/")
        return
        
    logging.info(f"Found {len(csv_files)} stock CSV files to merge.")
    
    dfs = []
    parquet_path = 'data/processed/all_stocks_merged.parquet'

    if os.path.exists(parquet_path):
        try:
            existing = pd.read_parquet(parquet_path)
            dfs.append(existing)
            logging.info("Loaded existing merged parquet: %d rows", len(existing))
        except Exception as e:
            logging.warning("Could not load existing merged parquet: %s", e)

    for f in csv_files:
        try:
            df = pd.read_csv(f)
            symbol = os.path.basename(f).replace('.csv', '')
            df['symbol'] = symbol
            dfs.append(df)
        except Exception as e:
            logging.error(f"Failed to read {f}: {e}")
            
    if not dfs:
        logging.error("No valid data frames to merge.")
        return
        
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # Standardize columns and types
    merged_df['Date'] = pd.to_datetime(merged_df['Date'])
    for col in ['Open', 'High', 'Low', 'Close', 'Volume', 'Turnover', 'Trades']:
        if col in merged_df.columns:
            merged_df[col] = pd.to_numeric(merged_df[col], errors='coerce')
            
    # Sort and drop duplicates
    merged_df = merged_df.sort_values(['symbol', 'Date']).drop_duplicates(subset=['symbol', 'Date'])
    
    merged_df.to_parquet(parquet_path, engine='pyarrow', index=False)
    
    logging.info(f"Successfully merged data into {parquet_path}")
    logging.info(f"Total rows: {len(merged_df):,}")
    logging.info(f"Unique symbols: {merged_df['symbol'].nunique()}")
    logging.info(f"Date range: {merged_df['Date'].min().date()} to {merged_df['Date'].max().date()}")

if __name__ == '__main__':
    process_and_merge()
