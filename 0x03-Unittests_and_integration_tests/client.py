#!/usr/bin/env python3
"""Client module containing GithubOrgClient"""

import requests


class GithubOrgClient:
    """GithubOrgClient class to interact with GitHub API"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name):
        self.org_name = org_name

    def org(self):
        """Return organization data from GitHub"""
        url = self.ORG_URL.format(org=self.org_name)
        return requests.get(url).json()

    @property
    def _public_repos_url(self):
        """Extracts the repos_url from the organization payload"""
        return self.org().get("repos_url")

    def public_repos(self, license=None):
        """Returns the list of public repositories for the org"""
        repos = requests.get(self._public_repos_url).json()
        if license is None:
            return [repo["name"] for repo in repos]
        return [repo["name"] for repo in repos if repo.get("license", {}).get("key") == license]
