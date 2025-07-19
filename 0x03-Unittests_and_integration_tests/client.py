#!/usr/bin/env python3
"""Github Org Client"""

import requests
from typing import Dict, List
from functools import lru_cache


class GithubOrgClient:
    """Github client for org info"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        self.org_name = org_name

    @property
    @lru_cache()
    def org(self) -> Dict:
        """Get org data from GitHub"""
        return requests.get(self.ORG_URL.format(org=self.org_name)).json()

    @property
    def _public_repos_url(self) -> str:
        """Extracts repos_url from org"""
        return self.org.get("repos_url", "")

    def public_repos(self) -> List[str]:
        """Fetches public repos"""
        repos = requests.get(self._public_repos_url).json()
        return [repo["name"] for repo in repos]

    def has_license(self, repo: Dict, license_key: str) -> bool:
        """Checks if repo has license"""
        try:
            return repo["license"]["key"] == license_key
        except Exception:
            return False
