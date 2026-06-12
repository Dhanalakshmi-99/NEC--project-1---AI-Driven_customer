import sqlite3

DB_NAME = "database/customer.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        city TEXT,
        income REAL,
        tenure INTEGER
    )
    """)

    conn.commit()
    conn.close()