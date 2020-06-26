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


class NewAccountSummary(object):
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
        'account_id': 'str',
        'account_id_guid': 'str',
        'account_name': 'str',
        'api_password': 'str',
        'base_url': 'str',
        'billing_plan_preview': 'BillingPlanPreview',
        'user_id': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'account_id_guid': 'accountIdGuid',
        'account_name': 'accountName',
        'api_password': 'apiPassword',
        'base_url': 'baseUrl',
        'billing_plan_preview': 'billingPlanPreview',
        'user_id': 'userId'
    }

    def __init__(self, account_id=None, account_id_guid=None, account_name=None, api_password=None, base_url=None, billing_plan_preview=None, user_id=None):  # noqa: E501
        """NewAccountSummary - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._account_id_guid = None
        self._account_name = None
        self._api_password = None
        self._base_url = None
        self._billing_plan_preview = None
        self._user_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_id_guid is not None:
            self.account_id_guid = account_id_guid
        if account_name is not None:
            self.account_name = account_name
        if api_password is not None:
            self.api_password = api_password
        if base_url is not None:
            self.base_url = base_url
        if billing_plan_preview is not None:
            self.billing_plan_preview = billing_plan_preview
        if user_id is not None:
            self.user_id = user_id

    @property
    def account_id(self):
        """Gets the account_id of this NewAccountSummary.  # noqa: E501

        The account ID associated with the envelope.  # noqa: E501

        :return: The account_id of this NewAccountSummary.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this NewAccountSummary.

        The account ID associated with the envelope.  # noqa: E501

        :param account_id: The account_id of this NewAccountSummary.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_id_guid(self):
        """Gets the account_id_guid of this NewAccountSummary.  # noqa: E501

        The GUID associated with the account ID.  # noqa: E501

        :return: The account_id_guid of this NewAccountSummary.  # noqa: E501
        :rtype: str
        """
        return self._account_id_guid

    @account_id_guid.setter
    def account_id_guid(self, account_id_guid):
        """Sets the account_id_guid of this NewAccountSummary.

        The GUID associated with the account ID.  # noqa: E501

        :param account_id_guid: The account_id_guid of this NewAccountSummary.  # noqa: E501
        :type: str
        """

        self._account_id_guid = account_id_guid

    @property
    def account_name(self):
        """Gets the account_name of this NewAccountSummary.  # noqa: E501

        The account name for the new account.  # noqa: E501

        :return: The account_name of this NewAccountSummary.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this NewAccountSummary.

        The account name for the new account.  # noqa: E501

        :param account_name: The account_name of this NewAccountSummary.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def api_password(self):
        """Gets the api_password of this NewAccountSummary.  # noqa: E501

        Contains a token that can be used for authentication in API calls instead of using the user name and password.  # noqa: E501

        :return: The api_password of this NewAccountSummary.  # noqa: E501
        :rtype: str
        """
        return self._api_password

    @api_password.setter
    def api_password(self, api_password):
        """Sets the api_password of this NewAccountSummary.

        Contains a token that can be used for authentication in API calls instead of using the user name and password.  # noqa: E501

        :param api_password: The api_password of this NewAccountSummary.  # noqa: E501
        :type: str
        """

        self._api_password = api_password

    @property
    def base_url(self):
        """Gets the base_url of this NewAccountSummary.  # noqa: E501

        The URL that should be used for successive calls to this account. It includes the protocal (https), the DocuSign server where the account is located, and the account number. Use this Url to make API calls against this account. Many of the API calls provide Uri's that are relative to this baseUrl.  # noqa: E501

        :return: The base_url of this NewAccountSummary.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this NewAccountSummary.

        The URL that should be used for successive calls to this account. It includes the protocal (https), the DocuSign server where the account is located, and the account number. Use this Url to make API calls against this account. Many of the API calls provide Uri's that are relative to this baseUrl.  # noqa: E501

        :param base_url: The base_url of this NewAccountSummary.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def billing_plan_preview(self):
        """Gets the billing_plan_preview of this NewAccountSummary.  # noqa: E501


        :return: The billing_plan_preview of this NewAccountSummary.  # noqa: E501
        :rtype: BillingPlanPreview
        """
        return self._billing_plan_preview

    @billing_plan_preview.setter
    def billing_plan_preview(self, billing_plan_preview):
        """Sets the billing_plan_preview of this NewAccountSummary.


        :param billing_plan_preview: The billing_plan_preview of this NewAccountSummary.  # noqa: E501
        :type: BillingPlanPreview
        """

        self._billing_plan_preview = billing_plan_preview

    @property
    def user_id(self):
        """Gets the user_id of this NewAccountSummary.  # noqa: E501

        Specifies the user ID of the new user.  # noqa: E501

        :return: The user_id of this NewAccountSummary.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NewAccountSummary.

        Specifies the user ID of the new user.  # noqa: E501

        :param user_id: The user_id of this NewAccountSummary.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(NewAccountSummary, dict):
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
        if not isinstance(other, NewAccountSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
