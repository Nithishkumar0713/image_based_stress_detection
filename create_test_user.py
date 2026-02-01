import sqlite3

DB_NAME = "database.db"

def create_user():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Check if user already exists
        cursor.execute("SELECT * FROM users WHERE email = 'admin@example.com'")
        if cursor.fetchone():
            print("User admin@example.com already exists.")
            return

        # Insert test user
        # Corresponding to columns: name, password, email, Gender, mobile, address, dob, Happy, Fear, Disgust, Sad, Angry, Neutral, Surprise
        sql = """INSERT INTO users (name, password, email, Gender, mobile, address, dob, Happy, Fear, Disgust, Sad, Angry, Neutral, Surprise)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        val = ("Admin", "admin123", "admin@example.com", "Other", 1234567890, "Admin HQ", "2000-01-01", "0", "0", "0", "0", "0", "0", "0")
        
        cursor.execute(sql, val)
        conn.commit()
        print("Test user 'admin@example.com' created successfully.")
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_user()
