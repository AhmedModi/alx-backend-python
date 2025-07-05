import mysql.connector
from mysql.connector import Error

def stream_user_ages():
    """Generator that yields user ages one by one"""
    connection = None
    cursor = None
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ALX_prodev'
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")
        
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row[0]  # Yield just the age
            
    except Error as e:
        print(f"Database error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def calculate_average_age():
    """Calculate average age using the generator"""
    total = 0
    count = 0
    
    # First loop: iterate through ages from generator
    for age in stream_user_ages():
        total += age
        count += 1
    
    # Calculate and return average
    return total / count if count > 0 else 0

if __name__ == "__main__":
    average = calculate_average_age()
    print(f"Average age of users: {average:.2f}")
