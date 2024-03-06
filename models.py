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


class Member:
    def __init__(self, id, username, password, fitness_goal):
        self.id = id
        self.username = username
        self.password = password
        self.fitness_goal = fitness_goal

    @staticmethod
    def register(username, password, fitness_goal=None):
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO members (username, password, fitness_goal) VALUES (%s, %s, %s)", 
                    (username, password, fitness_goal))
        conn.commit()
        conn.close()


class Trainer:
    def __init__(self, id, username, password, availability):
        self.id = id
        self.username = username
        self.password = password
        self.availability = availability


class Admin:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password