import sqlite3

DB_PATH = "notebooks/cricbuzz.db"   # correct relative path

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn
