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


class TransactionMetaDTO(object):
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
        'height': 'str',
        'hash': 'str',
        'merkle_component_hash': 'str',
        'index': 'int'
    }

    attribute_map = {
        'height': 'height',
        'hash': 'hash',
        'merkle_component_hash': 'merkleComponentHash',
        'index': 'index'
    }

    def __init__(self, height=None, hash=None, merkle_component_hash=None, index=None, local_vars_configuration=None):  # noqa: E501
        """TransactionMetaDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._height = None
        self._hash = None
        self._merkle_component_hash = None
        self._index = None
        self.discriminator = None

        self.height = height
        self.hash = hash
        self.merkle_component_hash = merkle_component_hash
        self.index = index

    @property
    def height(self):
        """Gets the height of this TransactionMetaDTO.  # noqa: E501

        Height of the blockchain.  # noqa: E501

        :return: The height of this TransactionMetaDTO.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this TransactionMetaDTO.

        Height of the blockchain.  # noqa: E501

        :param height: The height of this TransactionMetaDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def hash(self):
        """Gets the hash of this TransactionMetaDTO.  # noqa: E501


        :return: The hash of this TransactionMetaDTO.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this TransactionMetaDTO.


        :param hash: The hash of this TransactionMetaDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hash is None:  # noqa: E501
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501

        self._hash = hash

    @property
    def merkle_component_hash(self):
        """Gets the merkle_component_hash of this TransactionMetaDTO.  # noqa: E501


        :return: The merkle_component_hash of this TransactionMetaDTO.  # noqa: E501
        :rtype: str
        """
        return self._merkle_component_hash

    @merkle_component_hash.setter
    def merkle_component_hash(self, merkle_component_hash):
        """Sets the merkle_component_hash of this TransactionMetaDTO.


        :param merkle_component_hash: The merkle_component_hash of this TransactionMetaDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and merkle_component_hash is None:  # noqa: E501
            raise ValueError("Invalid value for `merkle_component_hash`, must not be `None`")  # noqa: E501

        self._merkle_component_hash = merkle_component_hash

    @property
    def index(self):
        """Gets the index of this TransactionMetaDTO.  # noqa: E501

        Transaction index within the block.  # noqa: E501

        :return: The index of this TransactionMetaDTO.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this TransactionMetaDTO.

        Transaction index within the block.  # noqa: E501

        :param index: The index of this TransactionMetaDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and index is None:  # noqa: E501
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

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
        if not isinstance(other, TransactionMetaDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionMetaDTO):
            return True

        return self.to_dict() != other.to_dict()
