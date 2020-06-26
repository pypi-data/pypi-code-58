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


class MosaicDTO(object):
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
        'supply': 'str',
        'start_height': 'str',
        'owner_address': 'str',
        'revision': 'int',
        'flags': 'int',
        'divisibility': 'int',
        'duration': 'str'
    }

    attribute_map = {
        'id': 'id',
        'supply': 'supply',
        'start_height': 'startHeight',
        'owner_address': 'ownerAddress',
        'revision': 'revision',
        'flags': 'flags',
        'divisibility': 'divisibility',
        'duration': 'duration'
    }

    def __init__(self, id=None, supply=None, start_height=None, owner_address=None, revision=None, flags=None, divisibility=None, duration=None, local_vars_configuration=None):  # noqa: E501
        """MosaicDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._supply = None
        self._start_height = None
        self._owner_address = None
        self._revision = None
        self._flags = None
        self._divisibility = None
        self._duration = None
        self.discriminator = None

        self.id = id
        self.supply = supply
        self.start_height = start_height
        self.owner_address = owner_address
        self.revision = revision
        self.flags = flags
        self.divisibility = divisibility
        self.duration = duration

    @property
    def id(self):
        """Gets the id of this MosaicDTO.  # noqa: E501

        Mosaic identifier.  # noqa: E501

        :return: The id of this MosaicDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MosaicDTO.

        Mosaic identifier.  # noqa: E501

        :param id: The id of this MosaicDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def supply(self):
        """Gets the supply of this MosaicDTO.  # noqa: E501

        Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative).  # noqa: E501

        :return: The supply of this MosaicDTO.  # noqa: E501
        :rtype: str
        """
        return self._supply

    @supply.setter
    def supply(self, supply):
        """Sets the supply of this MosaicDTO.

        Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative).  # noqa: E501

        :param supply: The supply of this MosaicDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and supply is None:  # noqa: E501
            raise ValueError("Invalid value for `supply`, must not be `None`")  # noqa: E501

        self._supply = supply

    @property
    def start_height(self):
        """Gets the start_height of this MosaicDTO.  # noqa: E501

        Height of the blockchain.  # noqa: E501

        :return: The start_height of this MosaicDTO.  # noqa: E501
        :rtype: str
        """
        return self._start_height

    @start_height.setter
    def start_height(self, start_height):
        """Sets the start_height of this MosaicDTO.

        Height of the blockchain.  # noqa: E501

        :param start_height: The start_height of this MosaicDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and start_height is None:  # noqa: E501
            raise ValueError("Invalid value for `start_height`, must not be `None`")  # noqa: E501

        self._start_height = start_height

    @property
    def owner_address(self):
        """Gets the owner_address of this MosaicDTO.  # noqa: E501

        Address expressed in hexadecimal base.  # noqa: E501

        :return: The owner_address of this MosaicDTO.  # noqa: E501
        :rtype: str
        """
        return self._owner_address

    @owner_address.setter
    def owner_address(self, owner_address):
        """Sets the owner_address of this MosaicDTO.

        Address expressed in hexadecimal base.  # noqa: E501

        :param owner_address: The owner_address of this MosaicDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner_address is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_address`, must not be `None`")  # noqa: E501

        self._owner_address = owner_address

    @property
    def revision(self):
        """Gets the revision of this MosaicDTO.  # noqa: E501

        A number that allows uint 32 values.  # noqa: E501

        :return: The revision of this MosaicDTO.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this MosaicDTO.

        A number that allows uint 32 values.  # noqa: E501

        :param revision: The revision of this MosaicDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and revision is None:  # noqa: E501
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def flags(self):
        """Gets the flags of this MosaicDTO.  # noqa: E501

        - 0x00 (none) - No flags present. - 0x01 (supplyMutable) - Mosaic supports supply changes even when mosaic owner owns partial supply. - 0x02 (transferable) - Mosaic supports transfers between arbitrary accounts. When not set, mosaic can only be transferred to and from mosaic owner. - 0x04 (restrictable) - Mosaic supports custom restrictions configured by mosaic owner.   # noqa: E501

        :return: The flags of this MosaicDTO.  # noqa: E501
        :rtype: int
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this MosaicDTO.

        - 0x00 (none) - No flags present. - 0x01 (supplyMutable) - Mosaic supports supply changes even when mosaic owner owns partial supply. - 0x02 (transferable) - Mosaic supports transfers between arbitrary accounts. When not set, mosaic can only be transferred to and from mosaic owner. - 0x04 (restrictable) - Mosaic supports custom restrictions configured by mosaic owner.   # noqa: E501

        :param flags: The flags of this MosaicDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and flags is None:  # noqa: E501
            raise ValueError("Invalid value for `flags`, must not be `None`")  # noqa: E501

        self._flags = flags

    @property
    def divisibility(self):
        """Gets the divisibility of this MosaicDTO.  # noqa: E501

        Determines up to what decimal place the mosaic can be divided. Divisibility of 3 means that a mosaic can be divided into smallest parts of 0.001 mosaics. The divisibility must be in the range of 0 and 6.   # noqa: E501

        :return: The divisibility of this MosaicDTO.  # noqa: E501
        :rtype: int
        """
        return self._divisibility

    @divisibility.setter
    def divisibility(self, divisibility):
        """Sets the divisibility of this MosaicDTO.

        Determines up to what decimal place the mosaic can be divided. Divisibility of 3 means that a mosaic can be divided into smallest parts of 0.001 mosaics. The divisibility must be in the range of 0 and 6.   # noqa: E501

        :param divisibility: The divisibility of this MosaicDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and divisibility is None:  # noqa: E501
            raise ValueError("Invalid value for `divisibility`, must not be `None`")  # noqa: E501

        self._divisibility = divisibility

    @property
    def duration(self):
        """Gets the duration of this MosaicDTO.  # noqa: E501

        Duration expressed in number of blocks.  # noqa: E501

        :return: The duration of this MosaicDTO.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this MosaicDTO.

        Duration expressed in number of blocks.  # noqa: E501

        :param duration: The duration of this MosaicDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

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
        if not isinstance(other, MosaicDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MosaicDTO):
            return True

        return self.to_dict() != other.to_dict()
