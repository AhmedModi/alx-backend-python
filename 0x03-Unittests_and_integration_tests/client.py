#!/usr/bin/env python3
"""GithubOrgClient class"""

import requests
from typing import List, Dict
from utils import get_json


class GithubOrgClient:
    """Client for GitHub organization info"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str):
        """Initialize client with organization name"""
        self.org_name = org_name

    @property
    def org(self) -> Dict:
        """Fetch organization info"""
        return get_json(self.ORG_URL.format(org=self.org_name))

    @property
    def _public_repos_url(self) -> str:
        """Return the URL for the public repos"""
        return self.org.get("repos_url", "")

    def public_repos(self, license: str = None) -> List[str]:
        """Return names of all public repositories"""
        repos = get_json(self._public_repos_url)
        repo_names = [repo["name"] for repo in repos]

        if license:
            repo_names = [
                repo["name"]
                for repo in repos
                if self.has_license(repo, license)
            ]

        return repo_names

    @staticmethod
    def has_license(repo: Dict, license_key: str) -> bool:
        """Check if the repo has a specific license"""
        try:
            return repo.get("license", {}).get("key") == license_key
        except AttributeError:
            return False
