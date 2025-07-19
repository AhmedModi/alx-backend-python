#!/usr/bin/env python3
"""Test client.GithubOrgClient."""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient.org method."""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """Test that GithubOrgClient.org returns the correct payload."""
        # Set up the mock return value
        mock_get_json.return_value = expected_payload

        # Call the method
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert the mock was called correctly
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        # Assert the result matches the expected payload
        self.assertEqual(result, expected_payload)
