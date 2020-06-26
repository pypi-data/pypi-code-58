# coding: utf-8

"""
    ****************************************************************************
    Copyright (c) 2016-present,
    Jaguar0625, gimre, BloodyRookie, Tech Bureau, Corp. All rights reserved.

    This file is part of Catapult.

    Catapult is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Catapult is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with Catapult. If not, see <http://www.gnu.org/licenses/>.
    ****************************************************************************
    
    Catapult REST Endpoints
    OpenAPI Specification of catapult-rest 1.1.2  # noqa: E501
    The version of the OpenAPI document: 0.9.3
    Contact: contact@nem.foundation

    NOTE: This file is auto generated by Symbol OpenAPI Generator:
    https://github.com/nemtech/symbol-openapi-generator
    Do not edit this file manually.
"""


from __future__ import absolute_import

import unittest

import symbol_openapi_client
from symbol_openapi_client.api.mosaic_routes_api import MosaicRoutesApi  # noqa: E501
from symbol_openapi_client.rest import ApiException


class TestMosaicRoutesApi(unittest.TestCase):
    """MosaicRoutesApi unit test stubs"""

    def setUp(self):
        self.api = symbol_openapi_client.api.mosaic_routes_api.MosaicRoutesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_mosaic(self):
        """Test case for get_mosaic

        Get mosaic information  # noqa: E501
        """
        pass

    def test_get_mosaics(self):
        """Test case for get_mosaics

        Get mosaics information for an array of mosaics  # noqa: E501
        """
        pass

    def test_search_mosaics(self):
        """Test case for search_mosaics

        Get mosaics  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
