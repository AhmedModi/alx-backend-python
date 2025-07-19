#!/usr/bin/env python3
"""Test client.GithubOrgClient class."""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Set up mock return value
        mock_get_json.return_value = {"login": org_name}

        # Create client instance and call the method
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        # Assert the result matches the mock return value
        self.assertEqual(result, {"login": org_name})
