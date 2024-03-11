from datetime import date, timedelta
from database.db import connect


# function to add the room to the database using the passed in room_name
def add_room(room_name):
    conn = connect()
    cur = conn.cursor()
    # execute the query to add the room to the database using the passed in room_name
    cur.execute("INSERT INTO Rooms (name) VALUES (%s)", (room_name,))
    conn.commit()
    conn.close()


# function to fix the equipment in the database using the passed in equipment_id
def fix_equipment(equipment_id):
    conn = connect()
    cur = conn.cursor()
    # create a date object that is one year from now
    one_year_from_now = date.today() + timedelta(days=365)
    # execute the query to fix the equipment in the database using the passed in equipment_id, and set the maintenance_date to one year from now
    cur.execute("UPDATE Equipment SET broken = FALSE, maintenance_date = %s WHERE id = %s", (one_year_from_now, equipment_id))
    conn.commit()
    conn.close()


# function to delete the equipment from the database using the passed in equipment_id
# this function is basically a helper function for the delete_room function and unbook_room function
def _delete_from_sessions_payments(cur, room_id):
    # execute the query to get the session ids from the database using the passed in room_id
    cur.execute("SELECT id FROM Sessions WHERE room_id = %s", (room_id,))
    session_ids = cur.fetchall()
    # loop through the session ids
    for session_id_tuple in session_ids:
        session_id = session_id_tuple[0]
        # execute the query to delete the payments from the database using the passed in session_id
        cur.execute("DELETE FROM Payments WHERE session_id = %s", (session_id,))
    # execute the query to delete the sessions from the database using the passed in room_id
    cur.execute("DELETE FROM Sessions WHERE room_id = %s", (room_id,))


# function to delete the room from the database using the passed in room_id
def delete_room(room_id):  
    conn = connect()
    cur = conn.cursor()
    # call the _delete_from_sessions_payments function to delete the sessions and payments from the database using the passed in room_id
    _delete_from_sessions_payments(cur, room_id)
    # then, execute the query to delete the room from the database using the passed in room_id
    cur.execute("DELETE FROM Rooms WHERE id = %s", (room_id,))
    conn.commit()
    conn.close()


# function to unbook the room from the database using the passed in room_id
def unbook_room(room_id):
    conn = connect()
    cur = conn.cursor()
    # call the _delete_from_sessions_payments function to delete the sessions and payments from the database using the passed in room_id
    _delete_from_sessions_payments(cur, room_id)
    # then, execute the query to unbook the room in the database using the passed in room_id
    cur.execute("UPDATE Rooms SET booked = FALSE WHERE id = %s", (room_id,))
    conn.commit()
    conn.close()


# function to update the equipment maintenance date in the database using the passed in equipment_id
def update_equipment_maintenance_date(equipment_id, new_date):
    conn = connect()
    cur = conn.cursor()
    # execute the query to update the maintenance_date of the equipment in the database using the passed in equipment_id and new_date
    cur.execute("UPDATE Equipment SET maintenance_date = %s WHERE id = %s", (new_date, equipment_id))
    conn.commit()
    conn.close()


# function to update the session time in the database using the passed in session_id
def update_session_time(session_id, new_time):
    conn = connect()
    cur = conn.cursor()
    # execute the query to update the session_time of the session in the database using the passed in session_id and new_time
    cur.execute("UPDATE Sessions SET session_time = %s WHERE id = %s", (new_time, session_id))
    conn.commit()
    conn.close()


# function to get the room from the database using the passed in room_id
def approve_payment(payment_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to update the processed and approved columns of the payment in the database using the passed in payment_id
    cur.execute("UPDATE Payments SET processed = TRUE, approved = TRUE WHERE id = %s", (payment_id,))
    conn.commit()
    conn.close()


# function to reject the payment from the database using the passed in payment_id
def reject_payment(payment_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to update the processed and approved columns of the payment in the database using the passed in payment_id
    cur.execute("UPDATE Payments SET processed = TRUE, approved = FALSE WHERE id = %s", (payment_id,))
    conn.commit()
    conn.close()


# function to get all available rooms from the database
def get_available_rooms():
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the available rooms from the database
    cur.execute("SELECT * FROM Rooms WHERE booked = FALSE",)
    rooms = cur.fetchall()
    conn.close()
    return rooms


# function to get the room name from the database using the passed in room_id
def get_room_name(room_id):
    conn = connect()
    cur = conn.cursor()
    # execute the query to get the room name from the database using the passed in room_id
    cur.execute("SELECT name FROM Rooms WHERE id = %s", (room_id,))
    # fetch the room name from the query result
    room_name = cur.fetchone()[0]
    conn.close()
    # return the room name
    return room_name


# function to get all users from the database
def get_all_users():
    conn = connect()
    cur = conn.cursor()
    # execute the query to get all users from the database by running a union on the Members and Trainers tables
    cur.execute("""
        SELECT username, 'Member' as role FROM Members
        UNION
        SELECT username, 'Trainer' as role FROM Trainers
    """)
    # fetch the users from the query result
    users = cur.fetchall()
    conn.close()
    # return the users
    return users


# function to get all equipment from the database
def get_all_equipment():
    conn = connect()
    cur = conn.cursor()
    # execute the query to get all equipment from the database
    cur.execute("SELECT * FROM Equipment")
    # fetch the equipment from the query result
    equipment = cur.fetchall()
    conn.close()
    # return the equipment
    return equipment


# function to get all payments from the database
def get_all_payments():
    conn = connect()
    cur = conn.cursor()
    # execute the query to get all payments, and the username of the member, the username of the trainer, and the session type
    # by running an inner join on the Payments, Members, Sessions, and Trainers tables
    cur.execute("""
        SELECT Payments.*, Members.username AS member_name, Trainers.username AS trainer_name, Sessions.session_type 
        FROM Payments 
        INNER JOIN Members ON Payments.member_id = Members.id
        INNER JOIN Sessions ON Payments.session_id = Sessions.id
        INNER JOIN Trainers ON Sessions.trainer_id = Trainers.id;
    """)
    payments = cur.fetchall()
    conn.close()
    return payments


# function to get all sessions from the database
def get_admin_sessions():
    conn = connect()
    cur = conn.cursor()
    # execute the query to get all sessions, and the username of the member, the username of the trainer, and the name of the room
    # by running an inner join on the Trainers, Members, and Rooms tables
    cur.execute("""
        SELECT Sessions.*, Trainers.username AS trainer_name, Members.username AS member_name, Rooms.name 
        FROM Sessions 
        INNER JOIN Trainers ON Sessions.trainer_id = Trainers.id 
        INNER JOIN Members ON Sessions.member_id = Members.id
        INNER JOIN Rooms ON Sessions.room_id = Rooms.id
    """)
    sessions = cur.fetchall()
    conn.close()
    return sessions


# function to get all room bookings from the database
def get_room_bookings():
    conn = connect()
    cur = conn.cursor()
    # execute the query to get all room bookings, and the username of the member, and the username of the trainer
    # by running a left join on Sessions, Members, and Trainers tables
    cur.execute("""
        SELECT Sessions.id, Rooms.*, Sessions.session_time, Sessions.session_type, Members.username AS member_name, Trainers.username AS trainer_name
        FROM Rooms
        LEFT JOIN Sessions ON Rooms.id = Sessions.room_id
        LEFT JOIN Members ON Sessions.member_id = Members.id
        LEFT JOIN Trainers ON Sessions.trainer_id = Trainers.id
    """)
    bookings = cur.fetchall()
    conn.close()
    return bookings