#!/usr/bin/python3
import unittest
from unittest.mock import PropertyMock, patch
from client import *
from parameterized import parameterized

class TestGithubOrgClient(unittest.TestCase):
  """github org client class"""
  
  @parameterized.expand([("google",),
                         ("abc")])
  @patch('client.get_json')
  def test_org(self, org, mock_getjson):
    """test that the correct org is returned"""
    new_client = GithubOrgClient(org_name=org)
    self.assertEqual(new_client._org_name, org)
    mock_getjson.return_value = {"payload": True}
    mock_getjson()
    mock_getjson.assert_called_once()
    
  @patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock)
  def test_public_repos_url(self, mock_property):
    """mocking a @property"""
    mock_property.return_value = {"payload": True}
    self.assertEqual(mock_property.return_value, {"payload": True})
    