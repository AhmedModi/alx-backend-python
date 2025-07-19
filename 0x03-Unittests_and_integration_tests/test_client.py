#!/usr/bin/env python3
"""Integration test for GithubOrgClient"""

import unittest
from unittest.mock import patch, MagicMock
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
    """Integration test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Start patcher and setup mocked get responses"""
        cls.get_patcher = patch("client.requests.get")
        cls.mock_get = cls.get_patcher.start()

        # Mock for org response
        mock_org_response = MagicMock()
        mock_org_response.json.return_value = cls.org_payload

        # Mock for repos response
        mock_repos_response = MagicMock()
        mock_repos_response.json.return_value = cls.repos_payload

        # Set side_effect to simulate sequential API calls
        cls.mock_get.side_effect = [mock_org_response, mock_repos_response]

    @classmethod
    def tearDownClass(cls):
        """Stop patcher"""
        cls.get_patcher.stop()

    def test_public_repos_integration(self):
        """Test public_repos method integration"""
        client = GithubOrgClient(self.org)
        self.assertEqual(client.public_repos(), self.expected_repos)
