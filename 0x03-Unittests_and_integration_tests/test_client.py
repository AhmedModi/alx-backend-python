#!/usr/bin/env python3
"""Integration tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class
from client import GithubOrgClient


@parameterized_class([
    {
        'org_payload': {"repos_url": "https://api.github.com/orgs/testorg/repos"},
        'repos_payload': [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}}
        ],
        'expected_repos': ["repo1", "repo2", "repo3"],
        'apache2_repos': ["repo2"]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test with @parameterized_class"""

    @classmethod
    def setUpClass(cls):
        """Patch requests.get before tests"""
        cls.get_patcher = patch('client.requests.get')

        # Start patching
        cls.mock_get = cls.get_patcher.start()

        # Mocking org and repos responses
        cls.mock_get.side_effect = [
            MagicMock(json=lambda: cls.org_payload),   # First call: org()
            MagicMock(json=lambda: cls.repos_payload)  # Second call: public_repos()
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop patching requests.get"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns the expected repo names"""
        client = GithubOrgClient("testorg")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test filtering repos by license key"""
        client = GithubOrgClient("testorg")
        repos = client.public_repos()
        filtered = [r for r in repos if any(
            r == repo["name"] and repo.get("license", {}).get("key") == "apache-2.0"
            for repo in self.repos_payload)]
        self.assertEqual(filtered, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
