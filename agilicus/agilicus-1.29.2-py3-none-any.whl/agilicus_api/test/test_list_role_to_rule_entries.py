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
from agilicus_api.models.list_role_to_rule_entries import ListRoleToRuleEntries  # noqa: E501
from agilicus_api.rest import ApiException

class TestListRoleToRuleEntries(unittest.TestCase):
    """ListRoleToRuleEntries unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListRoleToRuleEntries
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_role_to_rule_entries.ListRoleToRuleEntries()  # noqa: E501
        if include_optional :
            return ListRoleToRuleEntries(
                limit = 56, 
                role_to_rule_entries = [
                    agilicus_api.models.role_to_rule_entry.RoleToRuleEntry(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.role_to_rule_entry_spec.RoleToRuleEntrySpec(
                            role_id = '123', 
                            rule_id = '123', 
                            app_id = '123', 
                            org_id = '123', 
                            included = True, ), )
                    ]
            )
        else :
            return ListRoleToRuleEntries(
                limit = 56,
        )

    def testListRoleToRuleEntries(self):
        """Test ListRoleToRuleEntries"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
