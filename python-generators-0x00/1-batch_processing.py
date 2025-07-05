import mysql.connector
from mysql.connector import Error

def stream_users_in_batches(batch_size=1000):
    """Generator that yields batches of users from the database"""
    connection = None
    cursor = None
    
    try:
        # Establish database connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ALX_prodev'
        )
        
        # Create server-side cursor
        cursor = connection.cursor(dictionary=True)
        
        # Execute query
        cursor.execute("SELECT * FROM user_data")
        
        # Fetch and yield batches
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
            
    except Error as e:
        print(f"Database error: {e}")
    finally:
        # Clean up resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def batch_processing(batch_size=1000):
    """Process batches of users, filtering those over 25 years old"""
    # First loop: iterate through batches
    for batch in stream_users_in_batches(batch_size):
        # Second loop: filter users in batch
        filtered_users = [
            user for user in batch  # List comprehension counts as one "loop"
            if user['age'] > 25
        ]
        
        # Third loop: yield filtered users one by one
        for user in filtered_users:
            yield user
