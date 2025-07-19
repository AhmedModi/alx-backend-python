#!/usr/bin/env python3
"""Test client.GithubOrgClient._public_repos_url."""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient._public_repos_url."""

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct URL."""
        # Define the test payload
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        # Patch GithubOrgClient.org to return the test payload
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock,
            return_value=test_payload
        ) as mock_org:
            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")
            # Call _public_repos_url
            result = client._public_repos_url

            # Assert that org was accessed (since it's a property)
            mock_org.assert_called_once()
            # Assert that the result matches the expected URL
            self.assertEqual(result, test_payload["repos_url"])
