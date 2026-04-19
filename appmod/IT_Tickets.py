import pandas as pd
import sqlite3
conn = sqlite3.connect("DATA/int_platform.db")


def migrate_tickets_to_db(conn):
    data = pd.read_csv("DATA/it_tickets.csv")
    data.to_sql("it_tickets", conn)


def get_all_tickets(conn):
    sql = '''
        SELECT * FROM it_tickets'''
    data = pd.read_sql(sql, conn)
    conn.close()
    return (data)