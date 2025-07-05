from seed import connect_to_prodev

def paginate_users(page_size, offset):
    """Fetch a page of users from database"""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """Generator that lazily loads paginated data"""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:  # No more results
            break
        yield page
        offset += page_size
