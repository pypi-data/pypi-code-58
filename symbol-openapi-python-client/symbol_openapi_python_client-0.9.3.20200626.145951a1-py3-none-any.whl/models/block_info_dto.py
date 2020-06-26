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


class BlockInfoDTO(object):
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
        'id': 'str',
        'meta': 'BlockMetaDTO',
        'block': 'BlockDTO'
    }

    attribute_map = {
        'id': 'id',
        'meta': 'meta',
        'block': 'block'
    }

    def __init__(self, id=None, meta=None, block=None, local_vars_configuration=None):  # noqa: E501
        """BlockInfoDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._meta = None
        self._block = None
        self.discriminator = None

        self.id = id
        self.meta = meta
        self.block = block

    @property
    def id(self):
        """Gets the id of this BlockInfoDTO.  # noqa: E501

        Internal resource identifier.  # noqa: E501

        :return: The id of this BlockInfoDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BlockInfoDTO.

        Internal resource identifier.  # noqa: E501

        :param id: The id of this BlockInfoDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def meta(self):
        """Gets the meta of this BlockInfoDTO.  # noqa: E501


        :return: The meta of this BlockInfoDTO.  # noqa: E501
        :rtype: BlockMetaDTO
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this BlockInfoDTO.


        :param meta: The meta of this BlockInfoDTO.  # noqa: E501
        :type: BlockMetaDTO
        """
        if self.local_vars_configuration.client_side_validation and meta is None:  # noqa: E501
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        self._meta = meta

    @property
    def block(self):
        """Gets the block of this BlockInfoDTO.  # noqa: E501


        :return: The block of this BlockInfoDTO.  # noqa: E501
        :rtype: BlockDTO
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this BlockInfoDTO.


        :param block: The block of this BlockInfoDTO.  # noqa: E501
        :type: BlockDTO
        """
        if self.local_vars_configuration.client_side_validation and block is None:  # noqa: E501
            raise ValueError("Invalid value for `block`, must not be `None`")  # noqa: E501

        self._block = block

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
        if not isinstance(other, BlockInfoDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlockInfoDTO):
            return True

        return self.to_dict() != other.to_dict()
