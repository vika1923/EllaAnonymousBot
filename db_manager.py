import sqlite3

def start_db():     # open a new table IF NOT ALREADY CREATED
    conn = sqlite3.connect("question-user.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions_users
                      (question_id INTEGER PRIMARY KEY, user_id INTEGER)''')
    conn.commit()
    cursor.close()
    conn.close()
    

def add_to_waitlist(user_id):
    conn = sqlite3.connect("question-user.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO questions_users (user_id) VALUES (?)", (user_id,))

    conn.commit()
    cursor.close()
    conn.close()


def get_max_primary_key():
    conn = sqlite3.connect("question-user.db")
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(question_id) FROM questions_users")
    max_primary_key = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return max_primary_key if max_primary_key else 0


def get_user_by_question(question_id):
    conn = sqlite3.connect("question-user.db")
    cursor = conn.cursor()

    cursor.execute("SELECT user_id FROM questions_users WHERE question_id = ?", (question_id,))
    row = cursor.fetchone()

    user_id = row[0] if row else 360554569      # 360554569 = my ID

    cursor.close()
    conn.close()

    return user_id


def clear_table():
    conn = sqlite3.connect("question-user.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM questions_users")

    conn.commit()
    cursor.close()
    conn.close()
    print("Table cleared")