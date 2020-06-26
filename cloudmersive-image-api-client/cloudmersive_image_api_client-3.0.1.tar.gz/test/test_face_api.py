# coding: utf-8

"""
    imageapi

    Image Recognition and Processing APIs let you use Machine Learning to recognize and process images, and also perform useful image modification operations.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_image_api_client
from cloudmersive_image_api_client.api.face_api import FaceApi  # noqa: E501
from cloudmersive_image_api_client.rest import ApiException


class TestFaceApi(unittest.TestCase):
    """FaceApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_image_api_client.api.face_api.FaceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_face_crop_first(self):
        """Test case for face_crop_first

        Crop image to face (square)  # noqa: E501
        """
        pass

    def test_face_crop_first_round(self):
        """Test case for face_crop_first_round

        Crop image to face (round)  # noqa: E501
        """
        pass

    def test_face_locate(self):
        """Test case for face_locate

        Find faces in an image  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
