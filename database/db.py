import psycopg
from database.keys import db_config

# create a function to connect to the database
def connect():
    # connect to the database using the db_config information
    conn = psycopg.connect(
        dbname=db_config["dbname"],
        user=db_config["user"],
        password=db_config["password"],
        host=db_config["host"]
    )
    # return the connection
    return conn
