import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), "database.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # ✅ USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # ✅ RESUMES TABLE (YOU WERE MISSING THIS)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        score REAL
    )
    """)

    conn.commit()
    conn.close()


# ✅ RESUME FUNCTIONS
def insert_resume(filename, score):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO resumes (filename, score) VALUES (?, ?)",
        (filename, score)
    )

    conn.commit()
    conn.close()


def get_resumes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT filename, score FROM resumes ORDER BY score DESC")
    data = cursor.fetchall()

    conn.close()
    return data


# ✅ USER FUNCTIONS
def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )

    conn.commit()
    conn.close()


def get_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    return user