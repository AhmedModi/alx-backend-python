#!/usr/bin/env python3
"""Integration test for GithubOrgClient"""

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class
from client import GithubOrgClient


@parameterized_class([
    {
        "org_payload": {"repos_url": "https://api.github.com/orgs/testorg/repos"},
        "repos_payload": [
            {"name": "repo1"},
            {"name": "repo2"}
        ],
        "expected_repos": ["repo1", "repo2"],
        "org": "testorg"
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up mock for requests.get"""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Mock response instances
        org_response = MagicMock()
        org_response.json.return_value = cls.org_payload

        repos_response = MagicMock()
        repos_response.json.return_value = cls.repos_payload

        # Side effects: first call returns org_payload, second call returns repos_payload
        cls.mock_get.side_effect = [org_response, repos_response]

    @classmethod
    def tearDownClass(cls):
        """Tear down patcher"""
        cls.get_patcher.stop()

    def test_public_repos_integration(self):
        """Test that public_repos returns the expected list of repo names"""
        client = GithubOrgClient(self.org)
        self.assertEqual(client.public_repos(), self.expected_repos)


if __name__ == "__main__":
    unittest.main()
