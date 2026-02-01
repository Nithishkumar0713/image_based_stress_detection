import sqlite3
import os

DB_NAME = "database.db"

def init_db():
    if os.path.exists(DB_NAME):
        print(f"{DB_NAME} already exists. Removing to recreate...")
        os.remove(DB_NAME)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create table as per db.sql schema
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        Gender TEXT NOT NULL,
        mobile INTEGER NOT NULL,
        address TEXT NOT NULL,
        dob TEXT NOT NULL,
        Happy TEXT NOT NULL,
        Fear TEXT NOT NULL,
        Disgust TEXT NOT NULL,
        Sad TEXT NOT NULL,
        Angry TEXT NOT NULL,
        Neutral TEXT NOT NULL,
        Surprise TEXT NOT NULL
    );
    """
    
    cursor.execute(create_table_sql)
    print("Table 'users' created successfully.")
    
    conn.commit()
    conn.close()
    print(f"Database {DB_NAME} initialized.")

if __name__ == "__main__":
    init_db()
