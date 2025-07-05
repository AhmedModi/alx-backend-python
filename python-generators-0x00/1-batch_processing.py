#!/usr/bin/env python3
import json


def stream_users_in_batches(batch_size):
    """
    Generator that yields user data in batches of size `batch_size`.
    """
    with open("user_data.json", "r") as f:
        users = json.load(f)

    index = 0
    while index < len(users):
        yield users[index: index + batch_size]
        index += batch_size


def batch_processing(batch_size):
    """
    Processes batches of users, filtering and printing users older than 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user.get("age", 0) > 25:
                print(user)
