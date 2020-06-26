# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.06.26
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class CreateTokenRequest(object):
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
        'sub': 'str',
        'org': 'str',
        'roles': 'dict(str, str)',
        'audiences': 'list[str]',
        'time_validity': 'TimeValidity',
        'hosts': 'list[HostPermissions]',
        'token_validity': 'TokenValidity',
        'session': 'str',
        'scopes': 'list[str]'
    }

    attribute_map = {
        'sub': 'sub',
        'org': 'org',
        'roles': 'roles',
        'audiences': 'audiences',
        'time_validity': 'time_validity',
        'hosts': 'hosts',
        'token_validity': 'token_validity',
        'session': 'session',
        'scopes': 'scopes'
    }

    def __init__(self, sub=None, org=None, roles=None, audiences=None, time_validity=None, hosts=None, token_validity=None, session=None, scopes=None, local_vars_configuration=None):  # noqa: E501
        """CreateTokenRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sub = None
        self._org = None
        self._roles = None
        self._audiences = None
        self._time_validity = None
        self._hosts = None
        self._token_validity = None
        self._session = None
        self._scopes = None
        self.discriminator = None

        self.sub = sub
        self.org = org
        if roles is not None:
            self.roles = roles
        self.audiences = audiences
        self.time_validity = time_validity
        if hosts is not None:
            self.hosts = hosts
        if token_validity is not None:
            self.token_validity = token_validity
        if session is not None:
            self.session = session
        if scopes is not None:
            self.scopes = scopes

    @property
    def sub(self):
        """Gets the sub of this CreateTokenRequest.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The sub of this CreateTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub

    @sub.setter
    def sub(self, sub):
        """Sets the sub of this CreateTokenRequest.

        Unique identifier  # noqa: E501

        :param sub: The sub of this CreateTokenRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sub is None:  # noqa: E501
            raise ValueError("Invalid value for `sub`, must not be `None`")  # noqa: E501

        self._sub = sub

    @property
    def org(self):
        """Gets the org of this CreateTokenRequest.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The org of this CreateTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this CreateTokenRequest.

        Unique identifier  # noqa: E501

        :param org: The org of this CreateTokenRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org is None:  # noqa: E501
            raise ValueError("Invalid value for `org`, must not be `None`")  # noqa: E501

        self._org = org

    @property
    def roles(self):
        """Gets the roles of this CreateTokenRequest.  # noqa: E501

        associative mapping of an application to a role  # noqa: E501

        :return: The roles of this CreateTokenRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this CreateTokenRequest.

        associative mapping of an application to a role  # noqa: E501

        :param roles: The roles of this CreateTokenRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._roles = roles

    @property
    def audiences(self):
        """Gets the audiences of this CreateTokenRequest.  # noqa: E501

        array of audiences  # noqa: E501

        :return: The audiences of this CreateTokenRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences):
        """Sets the audiences of this CreateTokenRequest.

        array of audiences  # noqa: E501

        :param audiences: The audiences of this CreateTokenRequest.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and audiences is None:  # noqa: E501
            raise ValueError("Invalid value for `audiences`, must not be `None`")  # noqa: E501

        self._audiences = audiences

    @property
    def time_validity(self):
        """Gets the time_validity of this CreateTokenRequest.  # noqa: E501


        :return: The time_validity of this CreateTokenRequest.  # noqa: E501
        :rtype: TimeValidity
        """
        return self._time_validity

    @time_validity.setter
    def time_validity(self, time_validity):
        """Sets the time_validity of this CreateTokenRequest.


        :param time_validity: The time_validity of this CreateTokenRequest.  # noqa: E501
        :type: TimeValidity
        """
        if self.local_vars_configuration.client_side_validation and time_validity is None:  # noqa: E501
            raise ValueError("Invalid value for `time_validity`, must not be `None`")  # noqa: E501

        self._time_validity = time_validity

    @property
    def hosts(self):
        """Gets the hosts of this CreateTokenRequest.  # noqa: E501

        array of valid hosts  # noqa: E501

        :return: The hosts of this CreateTokenRequest.  # noqa: E501
        :rtype: list[HostPermissions]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this CreateTokenRequest.

        array of valid hosts  # noqa: E501

        :param hosts: The hosts of this CreateTokenRequest.  # noqa: E501
        :type: list[HostPermissions]
        """

        self._hosts = hosts

    @property
    def token_validity(self):
        """Gets the token_validity of this CreateTokenRequest.  # noqa: E501


        :return: The token_validity of this CreateTokenRequest.  # noqa: E501
        :rtype: TokenValidity
        """
        return self._token_validity

    @token_validity.setter
    def token_validity(self, token_validity):
        """Sets the token_validity of this CreateTokenRequest.


        :param token_validity: The token_validity of this CreateTokenRequest.  # noqa: E501
        :type: TokenValidity
        """

        self._token_validity = token_validity

    @property
    def session(self):
        """Gets the session of this CreateTokenRequest.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The session of this CreateTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this CreateTokenRequest.

        Unique identifier  # noqa: E501

        :param session: The session of this CreateTokenRequest.  # noqa: E501
        :type: str
        """

        self._session = session

    @property
    def scopes(self):
        """Gets the scopes of this CreateTokenRequest.  # noqa: E501

        The list of scopes requested for the access token. Multiple scopes are seperated by a space character. Ex. urn:agilicus:users urn:agilicus:issuers. An optional is specified with an ? at the end. Optional scopes are used when the permission is requested but not required. Ex. urn:agilicus:users?  # noqa: E501

        :return: The scopes of this CreateTokenRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this CreateTokenRequest.

        The list of scopes requested for the access token. Multiple scopes are seperated by a space character. Ex. urn:agilicus:users urn:agilicus:issuers. An optional is specified with an ? at the end. Optional scopes are used when the permission is requested but not required. Ex. urn:agilicus:users?  # noqa: E501

        :param scopes: The scopes of this CreateTokenRequest.  # noqa: E501
        :type: list[str]
        """

        self._scopes = scopes

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
        if not isinstance(other, CreateTokenRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTokenRequest):
            return True

        return self.to_dict() != other.to_dict()
