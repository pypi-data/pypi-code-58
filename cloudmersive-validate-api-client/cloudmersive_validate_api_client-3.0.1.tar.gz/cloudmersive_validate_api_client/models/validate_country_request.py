# coding: utf-8

"""
    validateapi

    The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ValidateCountryRequest(object):
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
        'raw_country_input': 'str'
    }

    attribute_map = {
        'raw_country_input': 'RawCountryInput'
    }

    def __init__(self, raw_country_input=None):  # noqa: E501
        """ValidateCountryRequest - a model defined in Swagger"""  # noqa: E501

        self._raw_country_input = None
        self.discriminator = None

        if raw_country_input is not None:
            self.raw_country_input = raw_country_input

    @property
    def raw_country_input(self):
        """Gets the raw_country_input of this ValidateCountryRequest.  # noqa: E501

        Raw country input - can be a two-letter code (FIPS 10-4 or ISO 3166-1), three-letter code (ISO 3166-1) or country name  # noqa: E501

        :return: The raw_country_input of this ValidateCountryRequest.  # noqa: E501
        :rtype: str
        """
        return self._raw_country_input

    @raw_country_input.setter
    def raw_country_input(self, raw_country_input):
        """Sets the raw_country_input of this ValidateCountryRequest.

        Raw country input - can be a two-letter code (FIPS 10-4 or ISO 3166-1), three-letter code (ISO 3166-1) or country name  # noqa: E501

        :param raw_country_input: The raw_country_input of this ValidateCountryRequest.  # noqa: E501
        :type: str
        """

        self._raw_country_input = raw_country_input

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
        if issubclass(ValidateCountryRequest, dict):
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
        if not isinstance(other, ValidateCountryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
