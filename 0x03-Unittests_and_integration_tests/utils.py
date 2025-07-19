#!/usr/bin/env python3
"""utils module with access_nested_map function"""


def access_nested_map(nested_map, path):
    """Access a nested map with a sequence of keys"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map
