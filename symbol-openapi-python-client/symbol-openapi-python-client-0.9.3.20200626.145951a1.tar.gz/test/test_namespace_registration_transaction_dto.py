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
from symbol_openapi_client.models.namespace_registration_transaction_dto import NamespaceRegistrationTransactionDTO  # noqa: E501
from symbol_openapi_client.rest import ApiException

class TestNamespaceRegistrationTransactionDTO(unittest.TestCase):
    """NamespaceRegistrationTransactionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NamespaceRegistrationTransactionDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = symbol_openapi_client.models.namespace_registration_transaction_dto.NamespaceRegistrationTransactionDTO()  # noqa: E501
        if include_optional :
            return NamespaceRegistrationTransactionDTO(
                size = 2222212828, 
                signature = '4B408BBEDF25F2AC8E0E44A6E51E3CCBA03885902055F75EB9FF50433532CA44BF9175FDA7502EEE2FC1617126E453A2BD692BAFDAAF06BC8EDEBA7961B3730D', 
                signer_public_key = 'AC1A6E1D8DE5B17D2C6B1293F1CAD3829EEACF38D09311BB3C8E5A880092DE26', 
                version = 56, 
                network = 144, 
                type = 56, 
                max_fee = '123456', 
                deadline = '200', 
                duration = '200', 
                parent_id = '85BBEA6CC462B244', 
                id = '85BBEA6CC462B244', 
                registration_type = 0, 
                name = '0'
            )
        else :
            return NamespaceRegistrationTransactionDTO(
                size = 2222212828,
                signature = '4B408BBEDF25F2AC8E0E44A6E51E3CCBA03885902055F75EB9FF50433532CA44BF9175FDA7502EEE2FC1617126E453A2BD692BAFDAAF06BC8EDEBA7961B3730D',
                signer_public_key = 'AC1A6E1D8DE5B17D2C6B1293F1CAD3829EEACF38D09311BB3C8E5A880092DE26',
                version = 56,
                network = 144,
                type = 56,
                max_fee = '123456',
                deadline = '200',
                duration = '200',
                parent_id = '85BBEA6CC462B244',
                id = '85BBEA6CC462B244',
                registration_type = 0,
                name = '0',
        )

    def testNamespaceRegistrationTransactionDTO(self):
        """Test NamespaceRegistrationTransactionDTO"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
