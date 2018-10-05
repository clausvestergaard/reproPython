import datetime
from .data import subset_data_GBP
from .data import country_subset

today = datetime.datetime.today().strftime('%Y-%m-%d')

subset_data_GBP.process_data_GBP('./data/raw/winemag-data-130k-v2.csv')
country_subset.get_country(f'./data/interim/{today}-winemag_priceGBP.csv', 'Chile')
