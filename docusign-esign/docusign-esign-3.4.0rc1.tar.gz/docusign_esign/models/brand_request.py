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


class BrandRequest(object):
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
        'brand_id': 'str'
    }

    attribute_map = {
        'brand_id': 'brandId'
    }

    def __init__(self, brand_id=None):  # noqa: E501
        """BrandRequest - a model defined in Swagger"""  # noqa: E501

        self._brand_id = None
        self.discriminator = None

        if brand_id is not None:
            self.brand_id = brand_id

    @property
    def brand_id(self):
        """Gets the brand_id of this BrandRequest.  # noqa: E501

        The ID of the brand used in API calls  # noqa: E501

        :return: The brand_id of this BrandRequest.  # noqa: E501
        :rtype: str
        """
        return self._brand_id

    @brand_id.setter
    def brand_id(self, brand_id):
        """Sets the brand_id of this BrandRequest.

        The ID of the brand used in API calls  # noqa: E501

        :param brand_id: The brand_id of this BrandRequest.  # noqa: E501
        :type: str
        """

        self._brand_id = brand_id

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
        if issubclass(BrandRequest, dict):
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
        if not isinstance(other, BrandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
