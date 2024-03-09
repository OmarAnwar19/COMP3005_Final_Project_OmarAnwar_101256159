from datetime import date, timedelta
from database.db import connect


def add_room(room_name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO Rooms (name) VALUES (%s)", (room_name,))
    conn.commit()
    conn.close()


def fix_equipment(equipment_id):
    conn = connect()
    cur = conn.cursor()
    one_year_from_now = date.today() + timedelta(days=365)
    cur.execute("UPDATE Equipment SET broken = FALSE, maintenance_date = %s WHERE id = %s", (one_year_from_now, equipment_id))
    conn.commit()
    conn.close()


def _delete_from_sessions_payments(cur, room_id):
    cur.execute("SELECT id FROM Sessions WHERE room_id = %s", (room_id,))
    session_ids = cur.fetchall()
    for session_id_tuple in session_ids:
        session_id = session_id_tuple[0]
        cur.execute("DELETE FROM Payments WHERE session_id = %s", (session_id,))
    cur.execute("DELETE FROM Sessions WHERE room_id = %s", (room_id,))


def delete_room(room_id):  
    conn = connect()
    cur = conn.cursor()
    _delete_from_sessions_payments(cur, room_id)
    cur.execute("DELETE FROM Rooms WHERE id = %s", (room_id,))
    conn.commit()
    conn.close()


def unbook_room(room_id):
    conn = connect()
    cur = conn.cursor()
    _delete_from_sessions_payments(cur, room_id)
    cur.execute("UPDATE Rooms SET booked = FALSE WHERE id = %s", (room_id,))
    conn.commit()
    conn.close()


def update_equipment_maintenance_date(equipment_id, new_date):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE Equipment SET maintenance_date = %s WHERE id = %s", (new_date, equipment_id))
    conn.commit()
    conn.close()


def get_available_rooms():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Rooms WHERE booked = FALSE",)
    rooms = cur.fetchall()
    conn.close()
    return rooms


def get_all_users():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT username, 'Member' as role FROM Members
        UNION
        SELECT username, 'Trainer' as role FROM Trainers
    """)
    users = cur.fetchall()
    conn.close()
    return users


def get_all_equipment():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Equipment")
    equipment = cur.fetchall()
    conn.close()
    return equipment


def get_admin_sessions():
    conn = connect()
    cur = conn.cursor()
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


def get_room_bookings():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT Rooms.*, Sessions.session_time, Sessions.session_type, Members.username AS member_name, Trainers.username AS trainer_name
        FROM Rooms
        LEFT JOIN Sessions ON Rooms.id = Sessions.room_id
        LEFT JOIN Members ON Sessions.member_id = Members.id
        LEFT JOIN Trainers ON Sessions.trainer_id = Trainers.id
    """)
    bookings = cur.fetchall()
    conn.close()
    return bookings