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
from agilicus_api.api.diagnostics_api import DiagnosticsApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestDiagnosticsApi(unittest.TestCase):
    """DiagnosticsApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.diagnostics_api.DiagnosticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_logs(self):
        """Test case for list_logs

        Retrieve application logs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
