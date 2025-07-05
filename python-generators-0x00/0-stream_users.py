import mysql.connector
from mysql.connector import Error

def stream_users():
    """Generator that streams rows from user_data table one by one"""
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
        
        # Create server-side cursor (important for memory efficiency)
        cursor = connection.cursor(dictionary=True)
        
        # Execute query
        cursor.execute("SELECT * FROM user_data")
        
        # Stream rows one by one
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row
            
    except Error as e:
        print(f"Database error: {e}")
    finally:
        # Clean up resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()
