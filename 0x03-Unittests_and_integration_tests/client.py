#!/usr/bin/env python3
"""GithubOrgClient module"""

import requests


def get_json(url):
    """GET JSON from a URL"""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """Github Organization Client"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def org(self):
        """Fetch the organization info"""
        return get_json(self.ORG_URL.format(self.org_name))

    def has_license(self, repo, license_key):
        """Check if the repo has a specific license"""
        try:
            return repo.get("license", {}).get("key") == license_key
        except AttributeError:
            return False
