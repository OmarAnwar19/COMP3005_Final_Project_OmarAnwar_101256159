from database.db import connect


# function to update the trainer availability in the database using the passed in trainer_id, available_from, and available_to
def update_trainer_availability(trainer_id, available_from, available_to):
    conn = connect()
    cur = conn.cursor()
    # execute the query to update the available_from and available_to of the trainer in the database using the passed in trainer_id, available_from, and available_to
    cur.execute("UPDATE Trainers SET available_from = %s, available_to = %s WHERE id = %s", (available_from, available_to, trainer_id))
    conn.commit()
    conn.close()


# function to get all available trainers from the database
def get_available_trainers():
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the available trainers from the database
    cur.execute("SELECT * FROM Trainers",)
    trainers = cur.fetchall()
    conn.close()
    return trainers


# function to get the trainer username from the database
def get_trainer_username(trainer_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the username of the trainer from the database using the passed in trainer_id
    cur.execute("SELECT username FROM Trainers WHERE id = %s", (trainer_id,))
    # fetch the username from the query result
    username = cur.fetchone()[0]
    conn.close()
    # return the username
    return username


# function to get the trainer availability from the database using the passed in trainer_id
def get_trainer_availability(trainer_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the available_from and available_to of the trainer from the database using the passed in trainer_id
    cur.execute("SELECT available_from, available_to FROM Trainers WHERE id = %s", (trainer_id,))
    sessions = cur.fetchall()
    conn.close()
    return sessions


# function to get the sessions of a trainer from the database
def get_trainer_sessions(trainer_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the sessions, the username of the member, and the name of the room from the database using the passed in trainer_id
    # by running an inner join on the Sessions, Members, and Rooms tables where the trainer_id is equal to the passed in trainer_id
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


# function to search members from the database using the passed in search_query
def search_members(search_query):
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the members from the database using the passed in search_query
    # by running a like query on the username column
    cur.execute("""
        SELECT * FROM Members
        WHERE username LIKE %s
    """, ("%" + search_query + "%",))
    # fetch the members from the query result
    members = cur.fetchall()
    conn.close()
    # return the members
    return members