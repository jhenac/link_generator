from datetime import datetime, timedelta
from link_generator import LinkGenerator

start_date = datetime(2025, 8, 13) # Year, Month, Day
end_date = datetime(2025, 9, 13) # Year, Month, Day

link_generator1 = LinkGenerator(
    start_date=start_date,
    end_date=end_date,
    base_url_csv='input/base_urls1.csv',
    output_csv='output/rfc_links1.csv'

)

link_generator2 = LinkGenerator(
    start_date=start_date,
    end_date=end_date,
    base_url_csv='input/base_urls2.csv',
    output_csv='output/rfc_links2.csv'

)

link_generator3 = LinkGenerator(
    start_date=start_date,
    end_date=end_date,
    base_url_csv='input/base_urls3.csv',
    output_csv='output/rfc_links3.csv'

)

link_generator1.generate_links()
link_generator2.generate_links()
link_generator3.generate_links()