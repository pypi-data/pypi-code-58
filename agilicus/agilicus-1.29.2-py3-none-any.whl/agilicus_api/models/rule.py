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


class Rule(object):
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
        'host': 'str',
        'name': 'str',
        'method': 'str',
        'path': 'str',
        'query_parameters': 'list[RuleQueryParameter]',
        'body': 'RuleQueryBody'
    }

    attribute_map = {
        'host': 'host',
        'name': 'name',
        'method': 'method',
        'path': 'path',
        'query_parameters': 'query_parameters',
        'body': 'body'
    }

    def __init__(self, host=None, name=None, method=None, path=None, query_parameters=None, body=None, local_vars_configuration=None):  # noqa: E501
        """Rule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host = None
        self._name = None
        self._method = None
        self._path = None
        self._query_parameters = None
        self._body = None
        self.discriminator = None

        if host is not None:
            self.host = host
        self.name = name
        self.method = method
        self.path = path
        if query_parameters is not None:
            self.query_parameters = query_parameters
        if body is not None:
            self.body = body

    @property
    def host(self):
        """Gets the host of this Rule.  # noqa: E501

        hostname to apply authz rule to. Deprecated. This is now inferred from the Environment or Service to which the rule belongs.   # noqa: E501

        :return: The host of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Rule.

        hostname to apply authz rule to. Deprecated. This is now inferred from the Environment or Service to which the rule belongs.   # noqa: E501

        :param host: The host of this Rule.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def name(self):
        """Gets the name of this Rule.  # noqa: E501

        A meaningful name to help identifiy the rule. This may be used to refer to it elsewhere, or to at a glace understand its purpose.   # noqa: E501

        :return: The name of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Rule.

        A meaningful name to help identifiy the rule. This may be used to refer to it elsewhere, or to at a glace understand its purpose.   # noqa: E501

        :param name: The name of this Rule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def method(self):
        """Gets the method of this Rule.  # noqa: E501

        The HTTP method to allow.  # noqa: E501

        :return: The method of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Rule.

        The HTTP method to allow.  # noqa: E501

        :param method: The method of this Rule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and method is None:  # noqa: E501
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501
        allowed_values = ["get", "put", "post", "delete", "head", "options", "connect", "trace", "patch", "all"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def path(self):
        """Gets the path of this Rule.  # noqa: E501

        regex for HTTP path. Can be templatized with jinja2 using definitions collection.  # noqa: E501

        :return: The path of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Rule.

        regex for HTTP path. Can be templatized with jinja2 using definitions collection.  # noqa: E501

        :param path: The path of this Rule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def query_parameters(self):
        """Gets the query_parameters of this Rule.  # noqa: E501

        A set of constraints on the parameters specified in the query string.  # noqa: E501

        :return: The query_parameters of this Rule.  # noqa: E501
        :rtype: list[RuleQueryParameter]
        """
        return self._query_parameters

    @query_parameters.setter
    def query_parameters(self, query_parameters):
        """Sets the query_parameters of this Rule.

        A set of constraints on the parameters specified in the query string.  # noqa: E501

        :param query_parameters: The query_parameters of this Rule.  # noqa: E501
        :type: list[RuleQueryParameter]
        """

        self._query_parameters = query_parameters

    @property
    def body(self):
        """Gets the body of this Rule.  # noqa: E501


        :return: The body of this Rule.  # noqa: E501
        :rtype: RuleQueryBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Rule.


        :param body: The body of this Rule.  # noqa: E501
        :type: RuleQueryBody
        """

        self._body = body

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
        if not isinstance(other, Rule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rule):
            return True

        return self.to_dict() != other.to_dict()
