#!/usr/bin/env python3
"""Unit tests for client.py"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @patch('client.get_json')
    def test_org(self, mock_get_json):
        """Test that org returns correct data"""
        expected_payload = {"login": "google"}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient("google")
        self.assertEqual(client.org(), expected_payload)
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google")

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct URL"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns expected list"""
        payload = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = payload

        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/google/repos"

            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            self.assertEqual(client.public_repos(license="apache-2.0"), ["repo1"])

            mock_url.assert_called_once()
            self.assertEqual(mock_get_json.call_count, 2)
