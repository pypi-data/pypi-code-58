# coding: utf-8

"""
    nlpapi

    The powerful Natural Language Processing APIs let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.api.language_detection_api import LanguageDetectionApi  # noqa: E501
from cloudmersive_nlp_api_client.rest import ApiException


class TestLanguageDetectionApi(unittest.TestCase):
    """LanguageDetectionApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_nlp_api_client.api.language_detection_api.LanguageDetectionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_language_detection_post(self):
        """Test case for language_detection_post

        Detect language of text  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
