import sqlite3
import pandas as pd


def migrate_cyber_incdt_to_db(conn):
    data = pd.read_csv("DATA/cyber_incidents.csv")
    data.to_sql("cyber_incidents", conn)

def get_all_cyber_incdt(conn):
    conn = sqlite3.connect("DATA/int_platform.db")
    sql = '''SELECT * FROM cyber_incidents'''
    data = pd.read_sql(sql, conn)
    conn.close()
    return (data)
