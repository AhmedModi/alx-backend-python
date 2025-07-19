#!/usr/bin/env python3
"""Unit tests for client.py module"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @patch('client.get_json')
    def test_org(self, mock_get_json):
        """Test GithubOrgClient.org returns correct value"""
        test_payload = {"login": "test-org"}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient("test-org")
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test-org"
        )

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns expected URL
        from org payload
        """
        with patch.object(
            GithubOrgClient, 'org', new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': 'https://api.github.com/orgs/test-org/repos'
            }

            client = GithubOrgClient("test-org")
            self.assertEqual(
                client._public_repos_url,
                'https://api.github.com/orgs/test-org/repos'
            )
            mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns expected list of repository names"""
        test_payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        mock_get_json.return_value = test_payload

        with patch.object(
            GithubOrgClient, '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = 'https://fakeurl.com/org/repos'

            client = GithubOrgClient("test-org")
            result = client.public_repos()

            self.assertEqual(result, ['repo1', 'repo2', 'repo3'])
            mock_get_json.assert_called_once_with(
                'https://fakeurl.com/org/repos'
            )
            mock_url.assert_called_once()


if __name__ == '__main__':
    unittest.main()
