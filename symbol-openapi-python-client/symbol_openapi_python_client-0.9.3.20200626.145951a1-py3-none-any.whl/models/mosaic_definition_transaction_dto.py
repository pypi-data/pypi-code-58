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


class MosaicDefinitionTransactionDTO(object):
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
        'id': 'str',
        'duration': 'str',
        'nonce': 'int',
        'flags': 'int',
        'divisibility': 'int'
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
        'id': 'id',
        'duration': 'duration',
        'nonce': 'nonce',
        'flags': 'flags',
        'divisibility': 'divisibility'
    }

    def __init__(self, size=None, signature=None, signer_public_key=None, version=None, network=None, type=None, max_fee=None, deadline=None, id=None, duration=None, nonce=None, flags=None, divisibility=None, local_vars_configuration=None):  # noqa: E501
        """MosaicDefinitionTransactionDTO - a model defined in OpenAPI"""  # noqa: E501
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
        self._id = None
        self._duration = None
        self._nonce = None
        self._flags = None
        self._divisibility = None
        self.discriminator = None

        self.size = size
        self.signature = signature
        self.signer_public_key = signer_public_key
        self.version = version
        self.network = network
        self.type = type
        self.max_fee = max_fee
        self.deadline = deadline
        self.id = id
        self.duration = duration
        self.nonce = nonce
        self.flags = flags
        self.divisibility = divisibility

    @property
    def size(self):
        """Gets the size of this MosaicDefinitionTransactionDTO.  # noqa: E501

        A number that allows uint 32 values.  # noqa: E501

        :return: The size of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MosaicDefinitionTransactionDTO.

        A number that allows uint 32 values.  # noqa: E501

        :param size: The size of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def signature(self):
        """Gets the signature of this MosaicDefinitionTransactionDTO.  # noqa: E501

        Entity's signature generated by the signer.  # noqa: E501

        :return: The signature of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this MosaicDefinitionTransactionDTO.

        Entity's signature generated by the signer.  # noqa: E501

        :param signature: The signature of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signature is None:  # noqa: E501
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def signer_public_key(self):
        """Gets the signer_public_key of this MosaicDefinitionTransactionDTO.  # noqa: E501

        Public key.  # noqa: E501

        :return: The signer_public_key of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._signer_public_key

    @signer_public_key.setter
    def signer_public_key(self, signer_public_key):
        """Sets the signer_public_key of this MosaicDefinitionTransactionDTO.

        Public key.  # noqa: E501

        :param signer_public_key: The signer_public_key of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signer_public_key is None:  # noqa: E501
            raise ValueError("Invalid value for `signer_public_key`, must not be `None`")  # noqa: E501

        self._signer_public_key = signer_public_key

    @property
    def version(self):
        """Gets the version of this MosaicDefinitionTransactionDTO.  # noqa: E501

        Entity version.  # noqa: E501

        :return: The version of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MosaicDefinitionTransactionDTO.

        Entity version.  # noqa: E501

        :param version: The version of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def network(self):
        """Gets the network of this MosaicDefinitionTransactionDTO.  # noqa: E501


        :return: The network of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: NetworkTypeEnum
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this MosaicDefinitionTransactionDTO.


        :param network: The network of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: NetworkTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and network is None:  # noqa: E501
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def type(self):
        """Gets the type of this MosaicDefinitionTransactionDTO.  # noqa: E501


        :return: The type of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MosaicDefinitionTransactionDTO.


        :param type: The type of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def max_fee(self):
        """Gets the max_fee of this MosaicDefinitionTransactionDTO.  # noqa: E501

        Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative).  # noqa: E501

        :return: The max_fee of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._max_fee

    @max_fee.setter
    def max_fee(self, max_fee):
        """Sets the max_fee of this MosaicDefinitionTransactionDTO.

        Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative).  # noqa: E501

        :param max_fee: The max_fee of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and max_fee is None:  # noqa: E501
            raise ValueError("Invalid value for `max_fee`, must not be `None`")  # noqa: E501

        self._max_fee = max_fee

    @property
    def deadline(self):
        """Gets the deadline of this MosaicDefinitionTransactionDTO.  # noqa: E501

        Duration expressed in number of blocks.  # noqa: E501

        :return: The deadline of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this MosaicDefinitionTransactionDTO.

        Duration expressed in number of blocks.  # noqa: E501

        :param deadline: The deadline of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and deadline is None:  # noqa: E501
            raise ValueError("Invalid value for `deadline`, must not be `None`")  # noqa: E501

        self._deadline = deadline

    @property
    def id(self):
        """Gets the id of this MosaicDefinitionTransactionDTO.  # noqa: E501

        Mosaic identifier.  # noqa: E501

        :return: The id of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MosaicDefinitionTransactionDTO.

        Mosaic identifier.  # noqa: E501

        :param id: The id of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def duration(self):
        """Gets the duration of this MosaicDefinitionTransactionDTO.  # noqa: E501

        Duration expressed in number of blocks.  # noqa: E501

        :return: The duration of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this MosaicDefinitionTransactionDTO.

        Duration expressed in number of blocks.  # noqa: E501

        :param duration: The duration of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def nonce(self):
        """Gets the nonce of this MosaicDefinitionTransactionDTO.  # noqa: E501

        A number that allows uint 32 values.  # noqa: E501

        :return: The nonce of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this MosaicDefinitionTransactionDTO.

        A number that allows uint 32 values.  # noqa: E501

        :param nonce: The nonce of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and nonce is None:  # noqa: E501
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def flags(self):
        """Gets the flags of this MosaicDefinitionTransactionDTO.  # noqa: E501

        - 0x00 (none) - No flags present. - 0x01 (supplyMutable) - Mosaic supports supply changes even when mosaic owner owns partial supply. - 0x02 (transferable) - Mosaic supports transfers between arbitrary accounts. When not set, mosaic can only be transferred to and from mosaic owner. - 0x04 (restrictable) - Mosaic supports custom restrictions configured by mosaic owner.   # noqa: E501

        :return: The flags of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this MosaicDefinitionTransactionDTO.

        - 0x00 (none) - No flags present. - 0x01 (supplyMutable) - Mosaic supports supply changes even when mosaic owner owns partial supply. - 0x02 (transferable) - Mosaic supports transfers between arbitrary accounts. When not set, mosaic can only be transferred to and from mosaic owner. - 0x04 (restrictable) - Mosaic supports custom restrictions configured by mosaic owner.   # noqa: E501

        :param flags: The flags of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and flags is None:  # noqa: E501
            raise ValueError("Invalid value for `flags`, must not be `None`")  # noqa: E501

        self._flags = flags

    @property
    def divisibility(self):
        """Gets the divisibility of this MosaicDefinitionTransactionDTO.  # noqa: E501

        Determines up to what decimal place the mosaic can be divided. Divisibility of 3 means that a mosaic can be divided into smallest parts of 0.001 mosaics. The divisibility must be in the range of 0 and 6.   # noqa: E501

        :return: The divisibility of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._divisibility

    @divisibility.setter
    def divisibility(self, divisibility):
        """Sets the divisibility of this MosaicDefinitionTransactionDTO.

        Determines up to what decimal place the mosaic can be divided. Divisibility of 3 means that a mosaic can be divided into smallest parts of 0.001 mosaics. The divisibility must be in the range of 0 and 6.   # noqa: E501

        :param divisibility: The divisibility of this MosaicDefinitionTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and divisibility is None:  # noqa: E501
            raise ValueError("Invalid value for `divisibility`, must not be `None`")  # noqa: E501

        self._divisibility = divisibility

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
        if not isinstance(other, MosaicDefinitionTransactionDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MosaicDefinitionTransactionDTO):
            return True

        return self.to_dict() != other.to_dict()
