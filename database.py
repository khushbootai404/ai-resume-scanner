import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), "database.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        score REAL
    )
    """)

    conn.commit()
    conn.close()

def insert_resume(filename, score):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO resumes (filename, score) VALUES (?, ?)", (filename, score))

    conn.commit()
    conn.close()

def get_resumes():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT filename, score FROM resumes ORDER BY score DESC")
    data = cursor.fetchall()

    conn.close()
    return data