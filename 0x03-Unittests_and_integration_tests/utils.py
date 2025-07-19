#!/usr/bin/env python3
"""Utils module for helper functions."""

import requests


def get_json(url):
    """Makes a GET request to the URL and returns the JSON content."""
    response = requests.get(url)
    return response.json()
