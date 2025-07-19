#!/usr/bin/env python3
"""Unit tests for client.py"""

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


@parameterized_class([
    {
        "org_payload": {"repos_url": "https://api.github.com/orgs/testorg/repos"},
        "repos_payload": [{"name": "repo1"}, {"name": "repo2"}],
        "expected_repos": ["repo1", "repo2"]
    }
])
class TestGithubOrgClient(unittest.TestCase):
    """Tests GithubOrgClient class with patching"""

    @classmethod
    def setUpClass(cls):
        """Patch requests.get"""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Mock responses for org and public_repos
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload,
            cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop patching"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns the expected list"""
        client = GithubOrgClient("testorg")
        self.assertEqual(client.public_repos(), self.expected_repos)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method"""
        client = GithubOrgClient("testorg")
        self.assertEqual(client.has_license(repo, license_key), expected)
