# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LoginInformation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_password': 'str',
        'login_accounts': 'list[LoginAccount]'
    }

    attribute_map = {
        'api_password': 'apiPassword',
        'login_accounts': 'loginAccounts'
    }

    def __init__(self, api_password=None, login_accounts=None):  # noqa: E501
        """LoginInformation - a model defined in Swagger"""  # noqa: E501

        self._api_password = None
        self._login_accounts = None
        self.discriminator = None

        if api_password is not None:
            self.api_password = api_password
        if login_accounts is not None:
            self.login_accounts = login_accounts

    @property
    def api_password(self):
        """Gets the api_password of this LoginInformation.  # noqa: E501

        Contains a token that can be used for authentication in API calls instead of using the user name and password. Only returned if the `api_password=true` query string is added to the URL.  # noqa: E501

        :return: The api_password of this LoginInformation.  # noqa: E501
        :rtype: str
        """
        return self._api_password

    @api_password.setter
    def api_password(self, api_password):
        """Sets the api_password of this LoginInformation.

        Contains a token that can be used for authentication in API calls instead of using the user name and password. Only returned if the `api_password=true` query string is added to the URL.  # noqa: E501

        :param api_password: The api_password of this LoginInformation.  # noqa: E501
        :type: str
        """

        self._api_password = api_password

    @property
    def login_accounts(self):
        """Gets the login_accounts of this LoginInformation.  # noqa: E501

        The list of accounts that authenticating user is a member of.  # noqa: E501

        :return: The login_accounts of this LoginInformation.  # noqa: E501
        :rtype: list[LoginAccount]
        """
        return self._login_accounts

    @login_accounts.setter
    def login_accounts(self, login_accounts):
        """Sets the login_accounts of this LoginInformation.

        The list of accounts that authenticating user is a member of.  # noqa: E501

        :param login_accounts: The login_accounts of this LoginInformation.  # noqa: E501
        :type: list[LoginAccount]
        """

        self._login_accounts = login_accounts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LoginInformation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoginInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
