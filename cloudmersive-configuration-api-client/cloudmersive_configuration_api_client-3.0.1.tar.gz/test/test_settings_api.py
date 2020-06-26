# coding: utf-8

"""
    configapi

    Config API lets you easily manage configuration at scale.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_configuration_api_client
from cloudmersive_configuration_api_client.api.settings_api import SettingsApi  # noqa: E501
from cloudmersive_configuration_api_client.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_configuration_api_client.api.settings_api.SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_settings_create_setting(self):
        """Test case for settings_create_setting

        Create a setting in the specified bucket  # noqa: E501
        """
        pass

    def test_settings_list_settings(self):
        """Test case for settings_list_settings

        Enumerate the settings in a bucket  # noqa: E501
        """
        pass

    def test_settings_update_setting(self):
        """Test case for settings_update_setting

        Update a setting  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
