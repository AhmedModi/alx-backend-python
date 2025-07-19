#!/usr/bin/env python3
"""Unit test for access_nested_map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json  # Make sure this path is correct

class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map"""

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Test KeyError is raised for missing keys in nested map"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{expected_key}'")

class TestGetJson(unittest.TestCase):
    """Test get_json function with mocked requests"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns correct payload and calls requests.get with URL"""

        # Patch 'requests.get' in the utils module where it's used
        with patch("utils.requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the actual function
            result = get_json(test_url)

            # Assertions
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
