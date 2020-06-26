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
import datetime

import symbol_openapi_client
from symbol_openapi_client.models.mosaic_network_properties_dto import MosaicNetworkPropertiesDTO  # noqa: E501
from symbol_openapi_client.rest import ApiException

class TestMosaicNetworkPropertiesDTO(unittest.TestCase):
    """MosaicNetworkPropertiesDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MosaicNetworkPropertiesDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = symbol_openapi_client.models.mosaic_network_properties_dto.MosaicNetworkPropertiesDTO()  # noqa: E501
        if include_optional :
            return MosaicNetworkPropertiesDTO(
                max_mosaics_per_account = '10000', 
                max_mosaic_duration = '3650d', 
                max_mosaic_divisibility = '6', 
                mosaic_rental_fee_sink_address = 'SAAA244WMCB2JXGNQTQHQOS45TGBFF4V2MJBVOQ', 
                mosaic_rental_fee = '500'
            )
        else :
            return MosaicNetworkPropertiesDTO(
        )

    def testMosaicNetworkPropertiesDTO(self):
        """Test MosaicNetworkPropertiesDTO"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
