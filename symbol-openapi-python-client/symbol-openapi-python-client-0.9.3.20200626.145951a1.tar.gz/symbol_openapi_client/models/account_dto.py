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


class AccountDTO(object):
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
        'address': 'str',
        'address_height': 'str',
        'public_key': 'str',
        'public_key_height': 'str',
        'account_type': 'AccountTypeEnum',
        'supplemental_public_keys': 'list[AccountKeyDTO]',
        'activity_buckets': 'list[ActivityBucketDTO]',
        'mosaics': 'list[Mosaic]',
        'importance': 'str',
        'importance_height': 'str'
    }

    attribute_map = {
        'address': 'address',
        'address_height': 'addressHeight',
        'public_key': 'publicKey',
        'public_key_height': 'publicKeyHeight',
        'account_type': 'accountType',
        'supplemental_public_keys': 'supplementalPublicKeys',
        'activity_buckets': 'activityBuckets',
        'mosaics': 'mosaics',
        'importance': 'importance',
        'importance_height': 'importanceHeight'
    }

    def __init__(self, address=None, address_height=None, public_key=None, public_key_height=None, account_type=None, supplemental_public_keys=None, activity_buckets=None, mosaics=None, importance=None, importance_height=None, local_vars_configuration=None):  # noqa: E501
        """AccountDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._address_height = None
        self._public_key = None
        self._public_key_height = None
        self._account_type = None
        self._supplemental_public_keys = None
        self._activity_buckets = None
        self._mosaics = None
        self._importance = None
        self._importance_height = None
        self.discriminator = None

        self.address = address
        self.address_height = address_height
        self.public_key = public_key
        self.public_key_height = public_key_height
        self.account_type = account_type
        self.supplemental_public_keys = supplemental_public_keys
        self.activity_buckets = activity_buckets
        self.mosaics = mosaics
        self.importance = importance
        self.importance_height = importance_height

    @property
    def address(self):
        """Gets the address of this AccountDTO.  # noqa: E501

        Address expressed in hexadecimal base.  # noqa: E501

        :return: The address of this AccountDTO.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AccountDTO.

        Address expressed in hexadecimal base.  # noqa: E501

        :param address: The address of this AccountDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def address_height(self):
        """Gets the address_height of this AccountDTO.  # noqa: E501

        Height of the blockchain.  # noqa: E501

        :return: The address_height of this AccountDTO.  # noqa: E501
        :rtype: str
        """
        return self._address_height

    @address_height.setter
    def address_height(self, address_height):
        """Sets the address_height of this AccountDTO.

        Height of the blockchain.  # noqa: E501

        :param address_height: The address_height of this AccountDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and address_height is None:  # noqa: E501
            raise ValueError("Invalid value for `address_height`, must not be `None`")  # noqa: E501

        self._address_height = address_height

    @property
    def public_key(self):
        """Gets the public_key of this AccountDTO.  # noqa: E501

        Public key.  # noqa: E501

        :return: The public_key of this AccountDTO.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this AccountDTO.

        Public key.  # noqa: E501

        :param public_key: The public_key of this AccountDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and public_key is None:  # noqa: E501
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

    @property
    def public_key_height(self):
        """Gets the public_key_height of this AccountDTO.  # noqa: E501

        Height of the blockchain.  # noqa: E501

        :return: The public_key_height of this AccountDTO.  # noqa: E501
        :rtype: str
        """
        return self._public_key_height

    @public_key_height.setter
    def public_key_height(self, public_key_height):
        """Sets the public_key_height of this AccountDTO.

        Height of the blockchain.  # noqa: E501

        :param public_key_height: The public_key_height of this AccountDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and public_key_height is None:  # noqa: E501
            raise ValueError("Invalid value for `public_key_height`, must not be `None`")  # noqa: E501

        self._public_key_height = public_key_height

    @property
    def account_type(self):
        """Gets the account_type of this AccountDTO.  # noqa: E501


        :return: The account_type of this AccountDTO.  # noqa: E501
        :rtype: AccountTypeEnum
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this AccountDTO.


        :param account_type: The account_type of this AccountDTO.  # noqa: E501
        :type: AccountTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and account_type is None:  # noqa: E501
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

    @property
    def supplemental_public_keys(self):
        """Gets the supplemental_public_keys of this AccountDTO.  # noqa: E501


        :return: The supplemental_public_keys of this AccountDTO.  # noqa: E501
        :rtype: list[AccountKeyDTO]
        """
        return self._supplemental_public_keys

    @supplemental_public_keys.setter
    def supplemental_public_keys(self, supplemental_public_keys):
        """Sets the supplemental_public_keys of this AccountDTO.


        :param supplemental_public_keys: The supplemental_public_keys of this AccountDTO.  # noqa: E501
        :type: list[AccountKeyDTO]
        """
        if self.local_vars_configuration.client_side_validation and supplemental_public_keys is None:  # noqa: E501
            raise ValueError("Invalid value for `supplemental_public_keys`, must not be `None`")  # noqa: E501

        self._supplemental_public_keys = supplemental_public_keys

    @property
    def activity_buckets(self):
        """Gets the activity_buckets of this AccountDTO.  # noqa: E501


        :return: The activity_buckets of this AccountDTO.  # noqa: E501
        :rtype: list[ActivityBucketDTO]
        """
        return self._activity_buckets

    @activity_buckets.setter
    def activity_buckets(self, activity_buckets):
        """Sets the activity_buckets of this AccountDTO.


        :param activity_buckets: The activity_buckets of this AccountDTO.  # noqa: E501
        :type: list[ActivityBucketDTO]
        """
        if self.local_vars_configuration.client_side_validation and activity_buckets is None:  # noqa: E501
            raise ValueError("Invalid value for `activity_buckets`, must not be `None`")  # noqa: E501

        self._activity_buckets = activity_buckets

    @property
    def mosaics(self):
        """Gets the mosaics of this AccountDTO.  # noqa: E501

        Mosaic units owned.  # noqa: E501

        :return: The mosaics of this AccountDTO.  # noqa: E501
        :rtype: list[Mosaic]
        """
        return self._mosaics

    @mosaics.setter
    def mosaics(self, mosaics):
        """Sets the mosaics of this AccountDTO.

        Mosaic units owned.  # noqa: E501

        :param mosaics: The mosaics of this AccountDTO.  # noqa: E501
        :type: list[Mosaic]
        """
        if self.local_vars_configuration.client_side_validation and mosaics is None:  # noqa: E501
            raise ValueError("Invalid value for `mosaics`, must not be `None`")  # noqa: E501

        self._mosaics = mosaics

    @property
    def importance(self):
        """Gets the importance of this AccountDTO.  # noqa: E501

        Probability of an account to harvest the next block.  # noqa: E501

        :return: The importance of this AccountDTO.  # noqa: E501
        :rtype: str
        """
        return self._importance

    @importance.setter
    def importance(self, importance):
        """Sets the importance of this AccountDTO.

        Probability of an account to harvest the next block.  # noqa: E501

        :param importance: The importance of this AccountDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and importance is None:  # noqa: E501
            raise ValueError("Invalid value for `importance`, must not be `None`")  # noqa: E501

        self._importance = importance

    @property
    def importance_height(self):
        """Gets the importance_height of this AccountDTO.  # noqa: E501

        Height of the blockchain.  # noqa: E501

        :return: The importance_height of this AccountDTO.  # noqa: E501
        :rtype: str
        """
        return self._importance_height

    @importance_height.setter
    def importance_height(self, importance_height):
        """Sets the importance_height of this AccountDTO.

        Height of the blockchain.  # noqa: E501

        :param importance_height: The importance_height of this AccountDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and importance_height is None:  # noqa: E501
            raise ValueError("Invalid value for `importance_height`, must not be `None`")  # noqa: E501

        self._importance_height = importance_height

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
        if not isinstance(other, AccountDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountDTO):
            return True

        return self.to_dict() != other.to_dict()
