from database.db import connect


# function to execute the query to insert a new member into the database
def insert_new_member(user_type, username, password, weight_lbs=0, heart_rate=0, sleep_hours=0):
    conn = connect()
    cur = conn.cursor()
    # execute the query to insert a new member into the database using the passed in parameters
    cur.execute(f"INSERT INTO {user_type} (username, password, fitness_goal, achievements) VALUES (%s, %s, %s, %s) RETURNING id", (username, password, '', '',))
    user_id = cur.fetchone()[0]
    # execute the query to insert the health stats of the new member into the database using the passed in parameters (or defaults)
    cur.execute("INSERT INTO HealthStats (member_id, weight_lbs, heart_rate, sleep_hours) VALUES (%s, %s, %s, %s)", (user_id, weight_lbs, heart_rate, sleep_hours,))
    conn.commit()
    conn.close()


# function to execute the query to update a member in the database
def update_member(member_id, username, password, fitness_goal):
    conn = connect()
    cur = conn.cursor()
    # select the member from the database using the passed in username
    cur.execute("SELECT * FROM Members WHERE username = %s", (username,))
    user = cur.fetchone()
    # if the username is already taken, append "_1" to the username
    if user and user[0] != member_id:
        username += "_1"
    # execute the query to update the member in the database using the passed in parameters
    cur.execute(
        "UPDATE Members SET username = %s, password = %s, fitness_goal = %s WHERE id = %s",
        (username, password, fitness_goal, member_id,)
    )
    conn.commit()
    conn.close()


# function to update the health stats of a member in the database
def update_member_health_stats(member_id, weight_lbs, heart_rate, sleep_hours):
    conn = connect()
    cur = conn.cursor()
    # execute the query to update the health stats of the member in the database using the passed in parameters
    cur.execute("UPDATE HealthStats SET weight_lbs = %s, heart_rate = %s, sleep_hours = %s WHERE member_id = %s", (weight_lbs, heart_rate, sleep_hours, member_id,))
    conn.commit()
    conn.close()


# function to update the exercises of a member in the database
def update_member_exercises(member_id, exercises):
    conn = connect()
    cur = conn.cursor()
    # first, delete all exercises of the member from the database
    cur.execute("DELETE FROM Exercises WHERE member_id = %s", (member_id,))
    # then, insert the new exercises of the member into the database
    for exercise in exercises:
        cur.execute("INSERT INTO Exercises (member_id, exercise_name) VALUES (%s, %s)", (member_id, exercise,))
    conn.commit()
    conn.close()


# function to update the profile of a member in the database
def update_member_profile(user_type, username, password, fitness_goal, achievements):
    conn = connect()
    cur = conn.cursor()
    # execute the query to update the profile of the member in the database using the passed in parameters
    cur.execute(f"UPDATE {user_type} SET fitness_goal = %s, achievements = %s, password = %s WHERE username = %s", (fitness_goal, achievements, password, username,))
    cur.execute(f"SELECT id FROM {user_type} WHERE username = %s", (username,))
    conn.commit()
    cur.close()
    conn.close()


# function to get the username of a member from the database
def get_member_username(member_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the username of the member from the database using the passed in member_id
    cur.execute("SELECT username FROM Members WHERE id = %s", (member_id,))
    # fetch the username from the query result
    username = cur.fetchone()[0]
    conn.close()
    # return the username
    return username


# function to get the member from the database using the passed in username
def get_member_by_username(user_type, username):
    conn = connect()
    cur = conn.cursor()
    # execute the query to select the member from a specific table using the passed in username by joining the HealthStats table
    cur.execute(f"SELECT * FROM {user_type} LEFT JOIN HealthStats ON {user_type}.id = HealthStats.member_id WHERE {user_type}.username = %s", (username,))
    # fetch the member from the query result
    user = cur.fetchone()
    conn.close()
    # return the member
    return user


# function to get the member from the database using the passed in member_id
def get_member_by_id(member_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the member from the database using the passed in member_id
    cur.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
    # fetch the member from the query result
    member = cur.fetchone()
    conn.close()
    # return the member
    return member


# function to get the health stats of a member from the database
def get_member_exercises(member_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the exercises of the member from the database using the passed in member_id
    cur.execute("SELECT * FROM Exercises WHERE member_id = %s", (member_id,))
    # fetch the exercises from the query result
    exercises = cur.fetchall()
    conn.close()
    # return the exercises
    return exercises


# function to get the achievements of a member from the database
def get_member_achievements(member_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the achievements of the member from the database using the passed in member_id
    cur.execute("SELECT achievements FROM members WHERE id = %s", (member_id,))
    # fetch the achievements from the query result
    achievements = cur.fetchall()
    conn.close()
    # return the achievements
    return achievements


# function to get the health stats of a member from the database
def get_member_health_stats(member_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the health stats of the member from the database using the passed in member_id
    cur.execute("SELECT * FROM HealthStats WHERE id = %s", (member_id,))
    # fetch the health stats from the query result
    health_stats = cur.fetchall()
    conn.close()
    # return the health stats
    return health_stats


# function to get the sessions of a member from the database
def get_member_sessions(member_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the sessions of the member, the username of the trainer, and the name of the room from the database 
    # run an inner join on the Sessions, Trainers, and Rooms tables and return where the member_id is equal to the passed in member_id
    cur.execute("""
        SELECT Sessions.*, Trainers.username, Rooms.name 
        FROM Sessions 
        INNER JOIN Trainers ON Sessions.trainer_id = Trainers.id 
        INNER JOIN Rooms ON Sessions.room_id = Rooms.id
        WHERE Sessions.member_id = %s
    """, (member_id,))
    # fetch the sessions from the query result
    sessions = cur.fetchall()
    conn.close()
    # return the sessions
    return sessions
