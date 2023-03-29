# redditScraper
A service to webscrape reddit posts and add them to a database for later data analysis

# Pre-Requisites
The service is built with python 3.10, and uses a PostgreSQL database of the latest stable version.
It also requires several python packages as dependencies.
# Install
to install and use the service, first create a directory to clone the repository into
```
mkdir reddit_scraper_directory
```
navigate to the new directory you just created and clone the repo into it with 
```
cd reddit_scraper_directory
git clone https://github.com/SeanRogan/redditScraper
```
navigate to the constants folder with ```cd constants```
create a private.py file with ```touch private.py``` to store sensitive information. 
then use the ```pip install requirements.txt``` command to install required packages.

# Sensitive Information
this scraper requires several sensitive pieces of information to be use in the code. 
Your Client id and secret, username and password, and a database connection string 
with the username and password visible, are all potential vulnerabilities that shouldnt be hardcoded into the program. 
To keep things separate, the application calls these strings from a private.py file. the file should look like this:
```
# the following value are fake placeholders, make sure you replace them with your real API and DB credentials
USER_AGENT = "python:com.yourname.appname:v1.0(by /u/yourRedditUsername)"
CLIENT_ID = "_j2dfnef32h2ZCEMw"
CLIENT_SECRET = "_fddEB-1-YHLHloh3fFVDAVgdsSDV"
DB_CONNECTION_STRING = "postgresql://user:pass@dbprovider.cloudhost.com:5432/postgres"
REDDIT_USER_PASSWORD = "password"
REDDIT_USERNAME = "yourUserName"
```
# Reddit API Credentials
To use the scraper youll need to sign up for a reddit account here https://reddit.com , and create a reddit app here https://www.reddit.com/prefs/apps. Make sure you create a 'script' type application. Then save your credentials into the private.py file.
# Data Storage
The scraper is made to work with a postgresql database. If you have a database simply add your connection string in the private.py file. the database connection string format for postgresql is as follows:  
### postgresql://username:password@hostname:port/dbname 

# Configuration
The webscraper has a settings.py file which holds configuration info. it looks like this 
```
SUBREDDITS = ["wallstreetbets", "python"]
TABLE_NAME = "reddit_posts"
```
In this file you can change the Subreddits you want to be scraped. Use the url element after ```/r/``` in the subreddit url. For example, if you want to scrape ```https://www.reddit.com/r/learnprogramming``` You would add "learnprogramming" to the SUBREDDITS list. You can also change the name of the table your data will be saved under in the database you connect to. 

# How to set up for your first scrape
Once you've installed everything and your database is up and waiting for inserts, ensure there is at least one valid subreddit string in the SUBREDDITS list in settings.py. Once that is confirmed, and you have your reddit api credentials in the private.py file, you should be ready to begin! You can run the program with ```python run_reddit_scraper.py``` and it will cycle through the subbreddits found in the settings.py file, and scrape the top 100 newest posts and its associated comments and deposit the data into the database. 
# Happy Scraping 🎅🏻

