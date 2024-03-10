from database.db import connect


def book_new_session(member_id, trainer_id, room_id, session_time, session_type):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO Sessions (member_id, trainer_id, room_id, session_time, session_type) VALUES (%s, %s, %s, %s, %s) RETURNING id", (member_id, trainer_id, room_id, session_time, session_type,))
    session_id = cur.fetchone()[0]
    cur.execute("UPDATE Rooms SET booked = TRUE WHERE id = %s", (room_id,))
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