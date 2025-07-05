#!/usr/bin/env python3
import json


def stream_users_in_batches(batch_size):
    """
    Generator that yields batches of users from the user_data.json file.
    """
    with open("user_data.json", "r") as f:
        users = json.load(f)

    for i in range(0, len(users), batch_size):
        yield users[i:i + batch_size]  # ✅ YIELD used correctly here


def batch_processing(batch_size):
    """
    Filters and prints users older than 25 from each batch.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user.get("age", 0) > 25:
                print(user)
