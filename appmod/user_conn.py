import sqlite3



def add_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute('''
            INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)
        ''', (username, password))
    conn.commit()

def migrate_users_to_db(conn):
    with open("DATA/users.txt", "r") as f:
        users = f.readlines()
        for user in users:
            name, password = user.strip().split(',')
            add_user(conn, name, password)



def get_all_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def get_user(conn, name):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, password FROM users WHERE username = ?", (name,))
    user = cursor.fetchone()
    conn.close()
    return user


def update_user(conn, name, new_name):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET username = ? WHERE username = ?", (new_name, name))
    conn.commit()
    conn.close()
    return name + " has been updated." + " New username: " + new_name


def delete_user(conn, name):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username = ?", (name,))
    conn.commit()
    conn.close()
    return name + " has been deleted from the database."