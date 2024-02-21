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
    def __init__(self, id, username, password, fitness_goal, health_metrics):
        self.id = id
        self.username = username
        self.password = password
        self.fitness_goal = fitness_goal
        self.health_metrics = health_metrics

    @staticmethod
    def register(username, password, fitness_goal=None, health_metrics=None):
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO members (username, password, fitness_goal, health_metrics) VALUES (%s, %s, %s, %s)", 
                    (username, password, fitness_goal, health_metrics))
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