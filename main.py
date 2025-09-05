from datetime import datetime, timedelta
from link_generator import LinkGenerator
import pandas as pd

start_date = datetime(2025, 9, 10) # Year, Month, Day
end_date = datetime(2025, 10, 10) # Year, Month, Day

base_csvs = [
    'input/base_urls1.csv',
    'input/base_urls2.csv',
    'input/base_urls2.csv'
]

all_dfs = []

for base_csv in base_csvs:
    generator = LinkGenerator(start_date, end_date, base_csv)
    df = generator.generate_links()
    all_dfs.append(df)

combined_df = pd.concat(all_dfs, ignore_index=True)

combined_df.to_csv('rfc_links.csv', index=False)