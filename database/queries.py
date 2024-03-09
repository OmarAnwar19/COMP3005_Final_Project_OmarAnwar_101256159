from database.db import connect


def get_user_by_username(user_type, username):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {user_type} LEFT JOIN HealthStats ON {user_type}.id = HealthStats.member_id WHERE {user_type}.username = %s", (username,))
    user = cur.fetchone()
    conn.close()
    return user


def insert_user(user_type, username, password, weight_lbs, heart_rate, sleep_hours):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {user_type} (username, password, fitness_goal, achievements) VALUES (%s, %s, %s, %s) RETURNING id", (username, password, '', '',))
    user_id = cur.fetchone()[0]
    cur.execute("INSERT INTO HealthStats (member_id, weight_lbs, heart_rate, sleep_hours) VALUES (%s, %s, %s, %s)", (user_id, weight_lbs, heart_rate, sleep_hours,))
    conn.commit()
    conn.close()


def update_member(member_id, username, password, fitness_goal):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Members WHERE username = %s", (username,))
    user = cur.fetchone()
    if user and user[0] != member_id:
        username += "_1"
    cur.execute(
        "UPDATE Members SET username = %s, password = %s, fitness_goal = %s WHERE id = %s",
        (username, password, fitness_goal, member_id,)
    )
    conn.commit()
    conn.close()


def update_member_health_stats(member_id, weight_lbs, heart_rate, sleep_hours):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE HealthStats SET weight_lbs = %s, heart_rate = %s, sleep_hours = %s WHERE member_id = %s", (weight_lbs, heart_rate, sleep_hours, member_id,))
    conn.commit()
    conn.close()


def update_member_exercises(member_id, exercises):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM Exercises WHERE member_id = %s", (member_id,))
    for exercise in exercises:
        cur.execute("INSERT INTO Exercises (member_id, exercise_name) VALUES (%s, %s)", (member_id, exercise,))
    conn.commit()
    conn.close()


def get_member_by_id(member_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
    member = cur.fetchone()
    conn.close()
    return member


def get_member_exercises(member_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Exercises WHERE member_id = %s", (member_id,))
    exercises = cur.fetchall()
    conn.close()
    return exercises


def get_member_achievements(member_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT achievements FROM members WHERE id = %s", (member_id,))
    achievements = cur.fetchall()
    conn.close()
    return achievements


def get_member_health_stats(member_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM HealthStats WHERE id = %s", (member_id,))
    health_stats = cur.fetchall()
    conn.close()
    return health_stats


def get_member_sessions(member_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT Sessions.*, Trainers.username, Rooms.name 
        FROM Sessions 
        INNER JOIN Trainers ON Sessions.trainer_id = Trainers.id 
        INNER JOIN Rooms ON Sessions.room_id = Rooms.id
        WHERE Sessions.member_id = %s
    """, (member_id,))
    sessions = cur.fetchall()
    conn.close()
    return sessions


def get_available_trainers():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Trainers",)
    trainers = cur.fetchall()
    conn.close()
    return trainers


def get_aviailable_rooms():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Rooms WHERE booked = FALSE",)
    rooms = cur.fetchall()
    conn.close()
    return rooms


def update_user_profile(user_type, username, password, fitness_goal, achievements):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"UPDATE {user_type} SET fitness_goal = %s, achievements = %s, password = %s WHERE username = %s", (fitness_goal, achievements, password, username,))
    cur.execute(f"SELECT id FROM {user_type} WHERE username = %s", (username,))
    conn.commit()
    cur.close()
    conn.close()


def book_new_session(member_id, trainer_id, room_id, session_time, session_type):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO Sessions (member_id, trainer_id, room_id, session_time, session_type) VALUES (%s, %s, %s, %s, %s) RETURNING id", (member_id, trainer_id, room_id, session_time, session_type,))
    session_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return session_id


def make_session_payment(member_id, session_id, amount):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO Payments (member_id, session_id, amount) VALUES (%s, %s, %s)", (member_id, session_id, amount,))
    conn.commit()
    cur.close()
    conn.close()


def cancel_member_session(session_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT room_id FROM Sessions WHERE id = %s", (session_id,))
    room_id = cur.fetchone()[0]
    cur.execute("DELETE FROM Payments WHERE session_id = %s", (session_id,))
    cur.execute("DELETE FROM Sessions WHERE id = %s", (session_id,))
    cur.execute("UPDATE Rooms SET booked = FALSE WHERE id = %s", (room_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_trainer_availability(trainer_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT available_from, available_to FROM Trainers WHERE id = %s", (trainer_id,))
    sessions = cur.fetchall()
    conn.close()
    return sessions