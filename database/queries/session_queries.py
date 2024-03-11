from database.db import connect


# function to book a new session in the database using the passed in member_id, trainer_id, room_id, session_time, and session_type
def book_new_session(member_id, trainer_id, room_id, session_time, session_type):
    conn = connect()
    cur = conn.cursor()
    # execute the query to insert a new session in the database using the passed in member_id, trainer_id, room_id, session_time, and session_type
    cur.execute("INSERT INTO Sessions (member_id, trainer_id, room_id, session_time, session_type) VALUES (%s, %s, %s, %s, %s) RETURNING id", (member_id, trainer_id, room_id, session_time, session_type,))
    session_id = cur.fetchone()[0]
    # then update the booked status of the room in the database using the passed in room_id
    cur.execute("UPDATE Rooms SET booked = TRUE WHERE id = %s", (room_id,))
    conn.commit()
    cur.close()
    conn.close()
    # return the session_id
    return session_id


# function to make a payment for a session in the database using the passed in member_id, session_id, and amount
def make_session_payment(member_id, session_id, amount):
    conn = connect()
    cur = conn.cursor()
    # execute the query to insert a new payment in the database using the passed in member_id, session_id, and amount
    cur.execute("INSERT INTO Payments (member_id, session_id, amount) VALUES (%s, %s, %s)", (member_id, session_id, amount,))
    conn.commit()
    cur.close()
    conn.close()


# function to cancel a member session in the database using the passed in session_id
def cancel_member_session(session_id):
    conn = connect()
    cur = conn.cursor()
    # first, get the room_id of the session from the database using the passed in session_id
    cur.execute("SELECT room_id FROM Sessions WHERE id = %s", (session_id,))
    # fetch the room_id from the query result
    room_id = cur.fetchone()[0]
    # then delete the payment and session from the database using the passed in session_id
    cur.execute("DELETE FROM Payments WHERE session_id = %s", (session_id,))
    cur.execute("DELETE FROM Sessions WHERE id = %s", (session_id,))
    # then update the booked status of the room in the database using the room_id
    cur.execute("UPDATE Rooms SET booked = FALSE WHERE id = %s", (room_id,))
    conn.commit()
    cur.close()
    conn.close()