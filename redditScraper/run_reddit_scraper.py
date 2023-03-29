import constants.settings
import db_handler
from post_scraper import scrape_subreddit as scrape
from data_cleaner import clean_dataset as clean_set
from db_handler import store_in_database as store
# dict to store raw data before entering to the database
raw_dataset = dict()


# run_scrape calls the post scraper for all the subreddits in the list,
# and adds them all to the raw dataset and returns it
def run_scrape():
    for sub in constants.settings.SUBREDDITS:
        raw_dataset[sub] = scrape(sub)
        # the raw dataset is basically a dictionary of dictionaries labeled by subreddit
    # need to clean raw_dataset, and then add cleaned info to cleaned_dataset and pass it to the storage handler
    return raw_dataset


for entry in clean_set(run_scrape()):
    # store the cleaned dataset in the database
    store(entry)
