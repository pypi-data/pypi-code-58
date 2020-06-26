# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AdminMessage(object):
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
        'base_message': 'str',
        'more_information': 'str'
    }

    attribute_map = {
        'base_message': 'baseMessage',
        'more_information': 'moreInformation'
    }

    def __init__(self, base_message=None, more_information=None):  # noqa: E501
        """AdminMessage - a model defined in Swagger"""  # noqa: E501

        self._base_message = None
        self._more_information = None
        self.discriminator = None

        if base_message is not None:
            self.base_message = base_message
        if more_information is not None:
            self.more_information = more_information

    @property
    def base_message(self):
        """Gets the base_message of this AdminMessage.  # noqa: E501

          # noqa: E501

        :return: The base_message of this AdminMessage.  # noqa: E501
        :rtype: str
        """
        return self._base_message

    @base_message.setter
    def base_message(self, base_message):
        """Sets the base_message of this AdminMessage.

          # noqa: E501

        :param base_message: The base_message of this AdminMessage.  # noqa: E501
        :type: str
        """

        self._base_message = base_message

    @property
    def more_information(self):
        """Gets the more_information of this AdminMessage.  # noqa: E501

          # noqa: E501

        :return: The more_information of this AdminMessage.  # noqa: E501
        :rtype: str
        """
        return self._more_information

    @more_information.setter
    def more_information(self, more_information):
        """Sets the more_information of this AdminMessage.

          # noqa: E501

        :param more_information: The more_information of this AdminMessage.  # noqa: E501
        :type: str
        """

        self._more_information = more_information

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
        if issubclass(AdminMessage, dict):
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
        if not isinstance(other, AdminMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
