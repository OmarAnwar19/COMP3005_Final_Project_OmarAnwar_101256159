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