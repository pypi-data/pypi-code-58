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


import pprint
import re  # noqa: F401

import six

from symbol_openapi_client.configuration import Configuration


class TransactionFeesDTO(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'average_fee_multiplier': 'int',
        'median_fee_multiplier': 'int',
        'highest_fee_multiplier': 'int',
        'lowest_fee_multiplier': 'int'
    }

    attribute_map = {
        'average_fee_multiplier': 'averageFeeMultiplier',
        'median_fee_multiplier': 'medianFeeMultiplier',
        'highest_fee_multiplier': 'highestFeeMultiplier',
        'lowest_fee_multiplier': 'lowestFeeMultiplier'
    }

    def __init__(self, average_fee_multiplier=None, median_fee_multiplier=None, highest_fee_multiplier=None, lowest_fee_multiplier=None, local_vars_configuration=None):  # noqa: E501
        """TransactionFeesDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._average_fee_multiplier = None
        self._median_fee_multiplier = None
        self._highest_fee_multiplier = None
        self._lowest_fee_multiplier = None
        self.discriminator = None

        self.average_fee_multiplier = average_fee_multiplier
        self.median_fee_multiplier = median_fee_multiplier
        self.highest_fee_multiplier = highest_fee_multiplier
        self.lowest_fee_multiplier = lowest_fee_multiplier

    @property
    def average_fee_multiplier(self):
        """Gets the average_fee_multiplier of this TransactionFeesDTO.  # noqa: E501

        Fee multiplier applied to transactions contained in block.  # noqa: E501

        :return: The average_fee_multiplier of this TransactionFeesDTO.  # noqa: E501
        :rtype: int
        """
        return self._average_fee_multiplier

    @average_fee_multiplier.setter
    def average_fee_multiplier(self, average_fee_multiplier):
        """Sets the average_fee_multiplier of this TransactionFeesDTO.

        Fee multiplier applied to transactions contained in block.  # noqa: E501

        :param average_fee_multiplier: The average_fee_multiplier of this TransactionFeesDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and average_fee_multiplier is None:  # noqa: E501
            raise ValueError("Invalid value for `average_fee_multiplier`, must not be `None`")  # noqa: E501

        self._average_fee_multiplier = average_fee_multiplier

    @property
    def median_fee_multiplier(self):
        """Gets the median_fee_multiplier of this TransactionFeesDTO.  # noqa: E501

        Fee multiplier applied to transactions contained in block.  # noqa: E501

        :return: The median_fee_multiplier of this TransactionFeesDTO.  # noqa: E501
        :rtype: int
        """
        return self._median_fee_multiplier

    @median_fee_multiplier.setter
    def median_fee_multiplier(self, median_fee_multiplier):
        """Sets the median_fee_multiplier of this TransactionFeesDTO.

        Fee multiplier applied to transactions contained in block.  # noqa: E501

        :param median_fee_multiplier: The median_fee_multiplier of this TransactionFeesDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and median_fee_multiplier is None:  # noqa: E501
            raise ValueError("Invalid value for `median_fee_multiplier`, must not be `None`")  # noqa: E501

        self._median_fee_multiplier = median_fee_multiplier

    @property
    def highest_fee_multiplier(self):
        """Gets the highest_fee_multiplier of this TransactionFeesDTO.  # noqa: E501

        Fee multiplier applied to transactions contained in block.  # noqa: E501

        :return: The highest_fee_multiplier of this TransactionFeesDTO.  # noqa: E501
        :rtype: int
        """
        return self._highest_fee_multiplier

    @highest_fee_multiplier.setter
    def highest_fee_multiplier(self, highest_fee_multiplier):
        """Sets the highest_fee_multiplier of this TransactionFeesDTO.

        Fee multiplier applied to transactions contained in block.  # noqa: E501

        :param highest_fee_multiplier: The highest_fee_multiplier of this TransactionFeesDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and highest_fee_multiplier is None:  # noqa: E501
            raise ValueError("Invalid value for `highest_fee_multiplier`, must not be `None`")  # noqa: E501

        self._highest_fee_multiplier = highest_fee_multiplier

    @property
    def lowest_fee_multiplier(self):
        """Gets the lowest_fee_multiplier of this TransactionFeesDTO.  # noqa: E501

        Fee multiplier applied to transactions contained in block.  # noqa: E501

        :return: The lowest_fee_multiplier of this TransactionFeesDTO.  # noqa: E501
        :rtype: int
        """
        return self._lowest_fee_multiplier

    @lowest_fee_multiplier.setter
    def lowest_fee_multiplier(self, lowest_fee_multiplier):
        """Sets the lowest_fee_multiplier of this TransactionFeesDTO.

        Fee multiplier applied to transactions contained in block.  # noqa: E501

        :param lowest_fee_multiplier: The lowest_fee_multiplier of this TransactionFeesDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and lowest_fee_multiplier is None:  # noqa: E501
            raise ValueError("Invalid value for `lowest_fee_multiplier`, must not be `None`")  # noqa: E501

        self._lowest_fee_multiplier = lowest_fee_multiplier

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransactionFeesDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionFeesDTO):
            return True

        return self.to_dict() != other.to_dict()
