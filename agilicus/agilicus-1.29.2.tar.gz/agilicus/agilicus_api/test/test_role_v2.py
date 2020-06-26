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
import datetime

import agilicus_api
from agilicus_api.models.role_v2 import RoleV2  # noqa: E501
from agilicus_api.rest import ApiException

class TestRoleV2(unittest.TestCase):
    """RoleV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoleV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.role_v2.RoleV2()  # noqa: E501
        if include_optional :
            return RoleV2(
                metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                spec = agilicus_api.models.role_spec.RoleSpec(
                    app_id = '123', 
                    name = 'owner', 
                    comments = 'This role allows access to all read-only endpoints of the application. Assign this role to anybody who needs to be able to interact with the application in a read-only fashion, such as an auditor.', 
                    included = [
                        agilicus_api.models.included_role.IncludedRole(
                            role_id = '123', )
                        ], 
                    org_id = '123', )
            )
        else :
            return RoleV2(
                spec = agilicus_api.models.role_spec.RoleSpec(
                    app_id = '123', 
                    name = 'owner', 
                    comments = 'This role allows access to all read-only endpoints of the application. Assign this role to anybody who needs to be able to interact with the application in a read-only fashion, such as an auditor.', 
                    included = [
                        agilicus_api.models.included_role.IncludedRole(
                            role_id = '123', )
                        ], 
                    org_id = '123', ),
        )

    def testRoleV2(self):
        """Test RoleV2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
