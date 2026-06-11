import sqlite3

def init_db():

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        job TEXT,

        skill TEXT,

        question TEXT,

        answer TEXT,

        score INTEGER,

        create_time DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        create_time DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mistakes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        question TEXT,

        answer TEXT,

        score INTEGER
    )
    """)

    conn.commit()

    conn.close()

def save_record(data):

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO interviews
    (
        job,
        skill,
        question,
        answer,
        score
    )

    VALUES

    (
        ?,
        ?,
        ?,
        ?,
        ?
    )
    """,

    (
        data["job"],
        data["skill"],
        data["question"],
        data["answer"],
        data["score"]
    )
    )

    conn.commit()

    conn.close()

def get_all_records():

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM interviews
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_scores():

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT score
    FROM interviews
    """)

    rows = cursor.fetchall()

    conn.close()

    return [
        row[0]
        for row in rows
    ]