#!/usr/bin/env python3
"""testing client.py methods"""
import unittest
from unittest.mock import MagicMock, PropertyMock, patch

from parameterized import parameterized

from client import *


class TestGithubOrgClient(unittest.TestCase):
    """GitHub org client class"""

    @parameterized.expand([("google",),
                           ("abc")])
    @patch('client.get_json')
    def test_org(self, org, mock_getjson: MagicMock) -> None:
        """test that the correct org is returned"""
        new_client = GithubOrgClient(org_name=org)
        self.assertEqual(new_client._org_name, org)
        mock_getjson.return_value = {"payload": True}
        mock_getjson()
        mock_getjson.assert_called_once()

    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos_url(self, mock_property: MagicMock) -> None:
        """mocking a @property"""
        mock_property.return_value = {"payload": True}
        self.assertEqual(mock_property.return_value, {"payload": True})
        
    
    @patch('client.get_json')
    def test_public_repos(self, mock_get: MagicMock) -> None:
        """test public repos function"""
        # using patch as a context manager
        with patch.object(GithubOrgClient, "_public_repos_url",
                          MagicMock(return_value="https://api.github.com/orgs/google/repos")) as mock_repos_url:
            repo_url = GithubOrgClient._public_repos_url(mock_repos_url)
            # give the mock get request of the repos url a mock response
            mock_get.return_value = [
                                        {
                                        "id": 123,
                                        "name": "repo1",
                                        "description": "description of repo1",
                                        "owner": {
                                            "login": "user1",
                                            "id": 456
                                        },
                                        "html_url": "https://github.com/user1/repo1",
                                        "stargazers_count": 10,
                                        "language": "Python",
                                        "created_at": "2022-04-22T11:11:11Z",
                                        "updated_at": "2022-04-23T12:12:12Z"
                                        },
                                        {
                                        "id": 234,
                                        "name": "repo2",
                                        "description": "description of repo2",
                                        "owner": {
                                            "login": "user2",
                                            "id": 567
                                        },
                                        "html_url": "https://github.com/user2/repo2",
                                        "stargazers_count": 20,
                                        "language": "JavaScript",
                                        "created_at": "2022-04-22T13:13:13Z",
                                        "updated_at": "2022-04-23T14:14:14Z"
                                        }
                                    ]
            json_resp = mock_get(repo_url)
            
            self.assertEqual(json_resp, mock_get.return_value)
            mock_get.assert_called_once()
        
        