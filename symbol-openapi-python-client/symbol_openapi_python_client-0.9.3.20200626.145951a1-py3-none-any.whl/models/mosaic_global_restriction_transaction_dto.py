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


class MosaicGlobalRestrictionTransactionDTO(object):
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
        'size': 'int',
        'signature': 'str',
        'signer_public_key': 'str',
        'version': 'int',
        'network': 'NetworkTypeEnum',
        'type': 'int',
        'max_fee': 'str',
        'deadline': 'str',
        'mosaic_id': 'str',
        'reference_mosaic_id': 'str',
        'restriction_key': 'str',
        'previous_restriction_value': 'str',
        'new_restriction_value': 'str',
        'previous_restriction_type': 'MosaicRestrictionTypeEnum',
        'new_restriction_type': 'MosaicRestrictionTypeEnum'
    }

    attribute_map = {
        'size': 'size',
        'signature': 'signature',
        'signer_public_key': 'signerPublicKey',
        'version': 'version',
        'network': 'network',
        'type': 'type',
        'max_fee': 'maxFee',
        'deadline': 'deadline',
        'mosaic_id': 'mosaicId',
        'reference_mosaic_id': 'referenceMosaicId',
        'restriction_key': 'restrictionKey',
        'previous_restriction_value': 'previousRestrictionValue',
        'new_restriction_value': 'newRestrictionValue',
        'previous_restriction_type': 'previousRestrictionType',
        'new_restriction_type': 'newRestrictionType'
    }

    def __init__(self, size=None, signature=None, signer_public_key=None, version=None, network=None, type=None, max_fee=None, deadline=None, mosaic_id=None, reference_mosaic_id=None, restriction_key=None, previous_restriction_value=None, new_restriction_value=None, previous_restriction_type=None, new_restriction_type=None, local_vars_configuration=None):  # noqa: E501
        """MosaicGlobalRestrictionTransactionDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._size = None
        self._signature = None
        self._signer_public_key = None
        self._version = None
        self._network = None
        self._type = None
        self._max_fee = None
        self._deadline = None
        self._mosaic_id = None
        self._reference_mosaic_id = None
        self._restriction_key = None
        self._previous_restriction_value = None
        self._new_restriction_value = None
        self._previous_restriction_type = None
        self._new_restriction_type = None
        self.discriminator = None

        self.size = size
        self.signature = signature
        self.signer_public_key = signer_public_key
        self.version = version
        self.network = network
        self.type = type
        self.max_fee = max_fee
        self.deadline = deadline
        self.mosaic_id = mosaic_id
        self.reference_mosaic_id = reference_mosaic_id
        self.restriction_key = restriction_key
        self.previous_restriction_value = previous_restriction_value
        self.new_restriction_value = new_restriction_value
        self.previous_restriction_type = previous_restriction_type
        self.new_restriction_type = new_restriction_type

    @property
    def size(self):
        """Gets the size of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501

        A number that allows uint 32 values.  # noqa: E501

        :return: The size of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MosaicGlobalRestrictionTransactionDTO.

        A number that allows uint 32 values.  # noqa: E501

        :param size: The size of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def signature(self):
        """Gets the signature of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501

        Entity's signature generated by the signer.  # noqa: E501

        :return: The signature of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this MosaicGlobalRestrictionTransactionDTO.

        Entity's signature generated by the signer.  # noqa: E501

        :param signature: The signature of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signature is None:  # noqa: E501
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def signer_public_key(self):
        """Gets the signer_public_key of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501

        Public key.  # noqa: E501

        :return: The signer_public_key of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._signer_public_key

    @signer_public_key.setter
    def signer_public_key(self, signer_public_key):
        """Sets the signer_public_key of this MosaicGlobalRestrictionTransactionDTO.

        Public key.  # noqa: E501

        :param signer_public_key: The signer_public_key of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signer_public_key is None:  # noqa: E501
            raise ValueError("Invalid value for `signer_public_key`, must not be `None`")  # noqa: E501

        self._signer_public_key = signer_public_key

    @property
    def version(self):
        """Gets the version of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501

        Entity version.  # noqa: E501

        :return: The version of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MosaicGlobalRestrictionTransactionDTO.

        Entity version.  # noqa: E501

        :param version: The version of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def network(self):
        """Gets the network of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501


        :return: The network of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: NetworkTypeEnum
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this MosaicGlobalRestrictionTransactionDTO.


        :param network: The network of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: NetworkTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and network is None:  # noqa: E501
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def type(self):
        """Gets the type of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501


        :return: The type of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MosaicGlobalRestrictionTransactionDTO.


        :param type: The type of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def max_fee(self):
        """Gets the max_fee of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501

        Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative).  # noqa: E501

        :return: The max_fee of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._max_fee

    @max_fee.setter
    def max_fee(self, max_fee):
        """Sets the max_fee of this MosaicGlobalRestrictionTransactionDTO.

        Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative).  # noqa: E501

        :param max_fee: The max_fee of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and max_fee is None:  # noqa: E501
            raise ValueError("Invalid value for `max_fee`, must not be `None`")  # noqa: E501

        self._max_fee = max_fee

    @property
    def deadline(self):
        """Gets the deadline of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501

        Duration expressed in number of blocks.  # noqa: E501

        :return: The deadline of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this MosaicGlobalRestrictionTransactionDTO.

        Duration expressed in number of blocks.  # noqa: E501

        :param deadline: The deadline of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and deadline is None:  # noqa: E501
            raise ValueError("Invalid value for `deadline`, must not be `None`")  # noqa: E501

        self._deadline = deadline

    @property
    def mosaic_id(self):
        """Gets the mosaic_id of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501

        Mosaic identifier. If the most significant bit of byte 0 is set, a namespaceId (alias) is used instead of the real mosaic identifier.   # noqa: E501

        :return: The mosaic_id of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._mosaic_id

    @mosaic_id.setter
    def mosaic_id(self, mosaic_id):
        """Sets the mosaic_id of this MosaicGlobalRestrictionTransactionDTO.

        Mosaic identifier. If the most significant bit of byte 0 is set, a namespaceId (alias) is used instead of the real mosaic identifier.   # noqa: E501

        :param mosaic_id: The mosaic_id of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mosaic_id is None:  # noqa: E501
            raise ValueError("Invalid value for `mosaic_id`, must not be `None`")  # noqa: E501

        self._mosaic_id = mosaic_id

    @property
    def reference_mosaic_id(self):
        """Gets the reference_mosaic_id of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501

        Mosaic identifier. If the most significant bit of byte 0 is set, a namespaceId (alias) is used instead of the real mosaic identifier.   # noqa: E501

        :return: The reference_mosaic_id of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._reference_mosaic_id

    @reference_mosaic_id.setter
    def reference_mosaic_id(self, reference_mosaic_id):
        """Sets the reference_mosaic_id of this MosaicGlobalRestrictionTransactionDTO.

        Mosaic identifier. If the most significant bit of byte 0 is set, a namespaceId (alias) is used instead of the real mosaic identifier.   # noqa: E501

        :param reference_mosaic_id: The reference_mosaic_id of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reference_mosaic_id is None:  # noqa: E501
            raise ValueError("Invalid value for `reference_mosaic_id`, must not be `None`")  # noqa: E501

        self._reference_mosaic_id = reference_mosaic_id

    @property
    def restriction_key(self):
        """Gets the restriction_key of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501

        Restriction key.  # noqa: E501

        :return: The restriction_key of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._restriction_key

    @restriction_key.setter
    def restriction_key(self, restriction_key):
        """Sets the restriction_key of this MosaicGlobalRestrictionTransactionDTO.

        Restriction key.  # noqa: E501

        :param restriction_key: The restriction_key of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and restriction_key is None:  # noqa: E501
            raise ValueError("Invalid value for `restriction_key`, must not be `None`")  # noqa: E501

        self._restriction_key = restriction_key

    @property
    def previous_restriction_value(self):
        """Gets the previous_restriction_value of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501

        Restriction value.  # noqa: E501

        :return: The previous_restriction_value of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._previous_restriction_value

    @previous_restriction_value.setter
    def previous_restriction_value(self, previous_restriction_value):
        """Sets the previous_restriction_value of this MosaicGlobalRestrictionTransactionDTO.

        Restriction value.  # noqa: E501

        :param previous_restriction_value: The previous_restriction_value of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and previous_restriction_value is None:  # noqa: E501
            raise ValueError("Invalid value for `previous_restriction_value`, must not be `None`")  # noqa: E501

        self._previous_restriction_value = previous_restriction_value

    @property
    def new_restriction_value(self):
        """Gets the new_restriction_value of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501

        Restriction value.  # noqa: E501

        :return: The new_restriction_value of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._new_restriction_value

    @new_restriction_value.setter
    def new_restriction_value(self, new_restriction_value):
        """Sets the new_restriction_value of this MosaicGlobalRestrictionTransactionDTO.

        Restriction value.  # noqa: E501

        :param new_restriction_value: The new_restriction_value of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and new_restriction_value is None:  # noqa: E501
            raise ValueError("Invalid value for `new_restriction_value`, must not be `None`")  # noqa: E501

        self._new_restriction_value = new_restriction_value

    @property
    def previous_restriction_type(self):
        """Gets the previous_restriction_type of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501


        :return: The previous_restriction_type of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: MosaicRestrictionTypeEnum
        """
        return self._previous_restriction_type

    @previous_restriction_type.setter
    def previous_restriction_type(self, previous_restriction_type):
        """Sets the previous_restriction_type of this MosaicGlobalRestrictionTransactionDTO.


        :param previous_restriction_type: The previous_restriction_type of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: MosaicRestrictionTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and previous_restriction_type is None:  # noqa: E501
            raise ValueError("Invalid value for `previous_restriction_type`, must not be `None`")  # noqa: E501

        self._previous_restriction_type = previous_restriction_type

    @property
    def new_restriction_type(self):
        """Gets the new_restriction_type of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501


        :return: The new_restriction_type of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :rtype: MosaicRestrictionTypeEnum
        """
        return self._new_restriction_type

    @new_restriction_type.setter
    def new_restriction_type(self, new_restriction_type):
        """Sets the new_restriction_type of this MosaicGlobalRestrictionTransactionDTO.


        :param new_restriction_type: The new_restriction_type of this MosaicGlobalRestrictionTransactionDTO.  # noqa: E501
        :type: MosaicRestrictionTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and new_restriction_type is None:  # noqa: E501
            raise ValueError("Invalid value for `new_restriction_type`, must not be `None`")  # noqa: E501

        self._new_restriction_type = new_restriction_type

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
        if not isinstance(other, MosaicGlobalRestrictionTransactionDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MosaicGlobalRestrictionTransactionDTO):
            return True

        return self.to_dict() != other.to_dict()
