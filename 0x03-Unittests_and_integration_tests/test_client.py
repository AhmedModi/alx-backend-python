#!/usr/bin/env python3
"""Test client.GithubOrgClient.public_repos."""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient.public_repos."""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repos."""
        # Define the test payload for get_json
        test_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
        ]
        mock_get_json.return_value = test_repos_payload

        # Define the test URL for _public_repos_url
        test_url = "https://api.github.com/orgs/google/repos"

        # Patch _public_repos_url to return the test URL
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock,
            return_value=test_url
        ) as mock_public_repos_url:
            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")
            # Call public_repos
            repos = client.public_repos()

            # Assert _public_repos_url was called once
            mock_public_repos_url.assert_called_once()
            # Assert get_json was called once with the test URL
            mock_get_json.assert_called_once_with(test_url)
            # Assert the result matches the expected list of repo names
            self.assertEqual(repos, ["repo1", "repo2"])
