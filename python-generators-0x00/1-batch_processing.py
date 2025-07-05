import mysql.connector
from mysql.connector import Error

def stream_users_in_batches(batch_size=1000):
    """Generator that yields batches of users from the database"""
    connection = None
    cursor = None
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ALX_prodev'
        )
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
            
    except Error as e:
        print(f"Database error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def batch_processing(batch_size=1000):
    """Process batches of users, filtering those over 25 years old"""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                yield user
