#!/usr/bin/env python3
"""Integration test for GithubOrgClient"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient


@parameterized_class([
    {
        "org_payload": {"repos_url": "https://api.github.com/orgs/testorg/repos"},
        "repos_payload": [{"name": "repo1"}, {"name": "repo2"}],
        "expected_repos": ["repo1", "repo2"],
        "org": "testorg"
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration Test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Start patcher for requests.get"""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Mock org and repos responses
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload,
            cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop patcher for requests.get"""
        cls.get_patcher.stop()

    def test_public_repos_integration(self):
        """Test public_repos method"""
        client = GithubOrgClient(self.org)
        self.assertEqual(client.public_repos(), self.expected_repos)


if __name__ == "__main__":
    unittest.main()
