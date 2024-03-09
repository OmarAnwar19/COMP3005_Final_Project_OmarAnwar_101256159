from database.db import connect


def update_trainer_availability(trainer_id, available_from, available_to):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE Trainers SET available_from = %s, available_to = %s WHERE id = %s", (available_from, available_to, trainer_id))
    conn.commit()
    conn.close()


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


def get_trainer_sessions(trainer_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT Sessions.*, Members.username, Rooms.name 
        FROM Sessions 
        INNER JOIN Members ON Sessions.member_id = Members.id 
        INNER JOIN Rooms ON Sessions.room_id = Rooms.id
        WHERE Sessions.trainer_id = %s
    """, (trainer_id,))
    sessions = cur.fetchall()
    conn.close()
    return sessions


def search_members(search_query):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Members
        WHERE username LIKE %s
    """, ("%" + search_query + "%",))
    members = cur.fetchall()
    conn.close()
    return members