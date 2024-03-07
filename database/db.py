import psycopg
from database.keys import db_config

def connect():
    conn = psycopg.connect(
        dbname=db_config["dbname"],
        user=db_config["user"],
        password=db_config["password"],
        host=db_config["host"]
    )
    return conn
