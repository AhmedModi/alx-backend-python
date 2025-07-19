#!/usr/bin/env python3
"""Integration tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class
from client import GithubOrgClient
import fixtures  # Import fixtures as required by ALX

@parameterized_class([
    {
        "org_payload": fixtures.org_payload,
        "repos_payload": fixtures.repos_payload,
        "expected_repos": fixtures.expected_repos,
        "apache2_repos": fixtures.apache2_repos,
        "org": "testorg"
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()
        mock_org = MagicMock(json=lambda: cls.org_payload)
        mock_repos = MagicMock(json=lambda: cls.repos_payload)
        cls.mock_get.side_effect = [mock_org, mock_repos]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        self.get_patcher  # Ensures self.get_patcher exists
        client = GithubOrgClient(self.org)
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient(self.org)
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )

if __name__ == "__main__":
    unittest.main()
