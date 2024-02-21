from models import connect


def get_user_by_username(user_type, username):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {user_type} WHERE username = %s", (username,))
    user = cur.fetchone()
    conn.close()
    return user


def insert_user(user_type, username, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {user_type} (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    conn.close()


def update_member(member_id, username, password, fitness_goal, health_metrics):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Members WHERE username = %s", (username,))
    user = cur.fetchone()
    if user and user[0] != member_id:
        username += "_1"
    cur.execute(
        "UPDATE Members SET username = %s, password = %s, fitness_goal = %s, health_metrics = %s WHERE id = %s",
        (username, password, fitness_goal, health_metrics, member_id)
    )
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
    cur.execute("SELECT * FROM Achievements WHERE member_id = %s", (member_id,))
    achievements = cur.fetchall()
    conn.close()
    return achievements


def get_member_health_stats(member_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM HealthStats WHERE member_id = %s", (member_id,))
    health_stats = cur.fetchall()
    conn.close()
    return health_stats


def get_available_trainers():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Trainers WHERE available = TRUE")
    trainers = cur.fetchall()
    conn.close()
    return trainers


def book_session(member_id, trainer_id, session_time):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Sessions (member_id, trainer_id, session_time) VALUES (%s, %s, %s)",
        (member_id, trainer_id, session_time)
    )
    conn.commit()
    conn.close()


def update_user_profile(user_type, username, fitness_goal, health_metrics, exercises, statistics, achievements):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE {user_type} SET fitness_goal = %s, health_metrics = %s, exercises = %s, statistics = %s, achievements = %s WHERE username = %s", 
        (fitness_goal, health_metrics, exercises, statistics, achievements, username)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_available_trainers():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Trainers WHERE available = TRUE")
    trainers = cur.fetchall()
    conn.close()
    return trainers


def get_available_trainers():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Trainers WHERE available = TRUE")
    trainers = cur.fetchall()
    cur.close()
    conn.close()
    return trainers


def book_session(member_id, trainer_id, session_time):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Sessions (member_id, trainer_id, session_time) VALUES (%s, %s, %s)",
        (member_id, trainer_id, session_time)
    )
    conn.commit()
    cur.close()
    conn.close()