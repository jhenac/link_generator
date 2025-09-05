import pandas as pd
from datetime import datetime, timedelta

class LinkGenerator:

    def __init__(self, start_date, end_date, base_url_csv):
        self.start_date = start_date
        self.end_date = end_date
        self.base_url_csv = base_url_csv

    def generate_links(self):
        urls_df = pd.read_csv(self.base_url_csv)
        base_urls = urls_df['base_url'].to_list()

        url_list = []

        for base_url in base_urls:
            current_date = self.start_date
            while current_date <= self.end_date:
                formatted_date = current_date.strftime("%m/%d/%Y")
                full_url = base_url + formatted_date
                url_list.append(full_url)
                current_date += timedelta(days=1)

        df = pd.DataFrame(url_list, columns=['URL'])
        return df