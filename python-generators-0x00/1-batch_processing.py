#!/usr/bin/env python3
import json

def stream_users_in_batches(batch_size):
    """Generator that yields users in batches from the database file."""
    with open("user_data.json", "r") as f:
        users = json.load(f)

    total_users = len(users)
    for i in range(0, total_users, batch_size):
        yield users[i:i + batch_size]

def batch_processing(batch_size):
    """Processes each batch to print users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user.get('age', 0) > 25:
                print(user)
