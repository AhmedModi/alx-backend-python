#!/usr/bin/env python3
"""utils module with utility functions for accessing nested maps and memoization"""


def access_nested_map(nested_map, path):
    """Access a nested map with a sequence of keys"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url):
    """Get JSON from a given URL"""
    import requests
    res = requests.get(url)
    return res.json()


class Memoize:
    """Simple memoization class"""

    def __init__(self, func):
        self.func = func
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.func(*args)
        return self.memo[args]
