import dataset
from constants import private, settings

# connect to the database
db = dataset.connect(private.DB_CONNECTION_STRING)
# connect to the table, or create a new one if it doesn't exist
table = db[settings.TABLE_NAME]


def store_in_database(self):
    # store data passed as an argument to the database,
    table.insert(self)
