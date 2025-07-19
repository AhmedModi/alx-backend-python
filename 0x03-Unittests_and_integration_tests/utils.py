#!/usr/bin/env python3
"""Utils module"""

def access_nested_map(nested_map, path):
    """Access a nested map with a given path"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map
