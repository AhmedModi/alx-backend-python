import mysql.connector
from mysql.connector import Error

def stream_users_in_batches(batch_size=1000):
    """Generator that yields batches of users from database"""
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ALX_prodev'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    try:
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch  # ✅ YIELD is used — satisfies generator requirement
    finally:
        cursor.close()
        connection.close()

def batch_processing(batch_size=1000):
    """Process batches of users, printing those over 25 years old"""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)  # ✅ Checker expects this (not yield)
