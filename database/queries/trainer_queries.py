from database.db import connect


def get_available_trainers():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Trainers",)
    trainers = cur.fetchall()
    conn.close()
    return trainers


def get_trainer_availability(trainer_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT available_from, available_to FROM Trainers WHERE id = %s", (trainer_id,))
    sessions = cur.fetchall()
    conn.close()
    return sessions