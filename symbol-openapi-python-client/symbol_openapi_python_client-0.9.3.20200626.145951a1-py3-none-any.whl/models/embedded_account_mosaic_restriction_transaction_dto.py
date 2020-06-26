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


class EmbeddedAccountMosaicRestrictionTransactionDTO(object):
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
        'signer_public_key': 'str',
        'version': 'int',
        'network': 'NetworkTypeEnum',
        'type': 'int',
        'restriction_flags': 'AccountRestrictionFlagsEnum',
        'restriction_additions': 'list[str]',
        'restriction_deletions': 'list[str]'
    }

    attribute_map = {
        'signer_public_key': 'signerPublicKey',
        'version': 'version',
        'network': 'network',
        'type': 'type',
        'restriction_flags': 'restrictionFlags',
        'restriction_additions': 'restrictionAdditions',
        'restriction_deletions': 'restrictionDeletions'
    }

    def __init__(self, signer_public_key=None, version=None, network=None, type=None, restriction_flags=None, restriction_additions=None, restriction_deletions=None, local_vars_configuration=None):  # noqa: E501
        """EmbeddedAccountMosaicRestrictionTransactionDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._signer_public_key = None
        self._version = None
        self._network = None
        self._type = None
        self._restriction_flags = None
        self._restriction_additions = None
        self._restriction_deletions = None
        self.discriminator = None

        self.signer_public_key = signer_public_key
        self.version = version
        self.network = network
        self.type = type
        self.restriction_flags = restriction_flags
        self.restriction_additions = restriction_additions
        self.restriction_deletions = restriction_deletions

    @property
    def signer_public_key(self):
        """Gets the signer_public_key of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501

        Public key.  # noqa: E501

        :return: The signer_public_key of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._signer_public_key

    @signer_public_key.setter
    def signer_public_key(self, signer_public_key):
        """Sets the signer_public_key of this EmbeddedAccountMosaicRestrictionTransactionDTO.

        Public key.  # noqa: E501

        :param signer_public_key: The signer_public_key of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signer_public_key is None:  # noqa: E501
            raise ValueError("Invalid value for `signer_public_key`, must not be `None`")  # noqa: E501

        self._signer_public_key = signer_public_key

    @property
    def version(self):
        """Gets the version of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501

        Entity version.  # noqa: E501

        :return: The version of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EmbeddedAccountMosaicRestrictionTransactionDTO.

        Entity version.  # noqa: E501

        :param version: The version of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def network(self):
        """Gets the network of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501


        :return: The network of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :rtype: NetworkTypeEnum
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this EmbeddedAccountMosaicRestrictionTransactionDTO.


        :param network: The network of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :type: NetworkTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and network is None:  # noqa: E501
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def type(self):
        """Gets the type of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501


        :return: The type of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EmbeddedAccountMosaicRestrictionTransactionDTO.


        :param type: The type of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def restriction_flags(self):
        """Gets the restriction_flags of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501


        :return: The restriction_flags of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :rtype: AccountRestrictionFlagsEnum
        """
        return self._restriction_flags

    @restriction_flags.setter
    def restriction_flags(self, restriction_flags):
        """Sets the restriction_flags of this EmbeddedAccountMosaicRestrictionTransactionDTO.


        :param restriction_flags: The restriction_flags of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :type: AccountRestrictionFlagsEnum
        """
        if self.local_vars_configuration.client_side_validation and restriction_flags is None:  # noqa: E501
            raise ValueError("Invalid value for `restriction_flags`, must not be `None`")  # noqa: E501

        self._restriction_flags = restriction_flags

    @property
    def restriction_additions(self):
        """Gets the restriction_additions of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501

        Account restriction additions.  # noqa: E501

        :return: The restriction_additions of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._restriction_additions

    @restriction_additions.setter
    def restriction_additions(self, restriction_additions):
        """Sets the restriction_additions of this EmbeddedAccountMosaicRestrictionTransactionDTO.

        Account restriction additions.  # noqa: E501

        :param restriction_additions: The restriction_additions of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and restriction_additions is None:  # noqa: E501
            raise ValueError("Invalid value for `restriction_additions`, must not be `None`")  # noqa: E501

        self._restriction_additions = restriction_additions

    @property
    def restriction_deletions(self):
        """Gets the restriction_deletions of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501

        Account restriction deletions.  # noqa: E501

        :return: The restriction_deletions of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._restriction_deletions

    @restriction_deletions.setter
    def restriction_deletions(self, restriction_deletions):
        """Sets the restriction_deletions of this EmbeddedAccountMosaicRestrictionTransactionDTO.

        Account restriction deletions.  # noqa: E501

        :param restriction_deletions: The restriction_deletions of this EmbeddedAccountMosaicRestrictionTransactionDTO.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and restriction_deletions is None:  # noqa: E501
            raise ValueError("Invalid value for `restriction_deletions`, must not be `None`")  # noqa: E501

        self._restriction_deletions = restriction_deletions

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
        if not isinstance(other, EmbeddedAccountMosaicRestrictionTransactionDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmbeddedAccountMosaicRestrictionTransactionDTO):
            return True

        return self.to_dict() != other.to_dict()
