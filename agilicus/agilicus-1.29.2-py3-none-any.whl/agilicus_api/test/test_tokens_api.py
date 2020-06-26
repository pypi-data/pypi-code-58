# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.06.26
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import agilicus_api
from agilicus_api.api.tokens_api import TokensApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestTokensApi(unittest.TestCase):
    """TokensApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.tokens_api.TokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_introspect_token(self):
        """Test case for create_introspect_token

        Introspect a token  # noqa: E501
        """
        pass

    def test_create_reissued_token(self):
        """Test case for create_reissued_token

        Issue a new token from another  # noqa: E501
        """
        pass

    def test_create_revoke_token_task(self):
        """Test case for create_revoke_token_task

        Revoke a token  # noqa: E501
        """
        pass

    def test_create_token(self):
        """Test case for create_token

        Create a token  # noqa: E501
        """
        pass

    def test_create_token_validation(self):
        """Test case for create_token_validation

        Validate a token request  # noqa: E501
        """
        pass

    def test_list_tokens(self):
        """Test case for list_tokens

        Query tokens  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
