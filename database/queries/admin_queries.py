from database.db import connect


def get_available_rooms():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Rooms WHERE booked = FALSE",)
    rooms = cur.fetchall()
    conn.close()
    return rooms