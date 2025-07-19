#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class
from client import GithubOrgClient


@parameterized_class([
    {"org_payload": {"repos_url": "https://api.github.com/orgs/testorg/repos"},
     "repos_payload": [{"name": "repo1"}, {"name": "repo2"}],
     "expected_repos": ["repo1", "repo2"],
     "org": "testorg"}
])
class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Start patcher for requests.get"""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Mock org response
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload,       # For org
            cls.repos_payload      # For repos
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop patcher for requests.get"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient(self.org)
        self.assertEqual(client.public_repos(), self.expected_repos)
