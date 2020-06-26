# coding: utf-8

"""
    configapi

    Config API lets you easily manage configuration at scale.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HttpWwwFormUrlEncodedParameter(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'key_name': 'str',
        'key_value': 'str',
        'use_output_from_previous_task': 'TaskOutputReference'
    }

    attribute_map = {
        'key_name': 'KeyName',
        'key_value': 'KeyValue',
        'use_output_from_previous_task': 'UseOutputFromPreviousTask'
    }

    def __init__(self, key_name=None, key_value=None, use_output_from_previous_task=None):  # noqa: E501
        """HttpWwwFormUrlEncodedParameter - a model defined in Swagger"""  # noqa: E501

        self._key_name = None
        self._key_value = None
        self._use_output_from_previous_task = None
        self.discriminator = None

        if key_name is not None:
            self.key_name = key_name
        if key_value is not None:
            self.key_value = key_value
        if use_output_from_previous_task is not None:
            self.use_output_from_previous_task = use_output_from_previous_task

    @property
    def key_name(self):
        """Gets the key_name of this HttpWwwFormUrlEncodedParameter.  # noqa: E501

        Key name of the parameter  # noqa: E501

        :return: The key_name of this HttpWwwFormUrlEncodedParameter.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this HttpWwwFormUrlEncodedParameter.

        Key name of the parameter  # noqa: E501

        :param key_name: The key_name of this HttpWwwFormUrlEncodedParameter.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

    @property
    def key_value(self):
        """Gets the key_value of this HttpWwwFormUrlEncodedParameter.  # noqa: E501

        Key value of the paramer (must be of type text); if set, do not use UseOutputFromPreviousTask  # noqa: E501

        :return: The key_value of this HttpWwwFormUrlEncodedParameter.  # noqa: E501
        :rtype: str
        """
        return self._key_value

    @key_value.setter
    def key_value(self, key_value):
        """Sets the key_value of this HttpWwwFormUrlEncodedParameter.

        Key value of the paramer (must be of type text); if set, do not use UseOutputFromPreviousTask  # noqa: E501

        :param key_value: The key_value of this HttpWwwFormUrlEncodedParameter.  # noqa: E501
        :type: str
        """

        self._key_value = key_value

    @property
    def use_output_from_previous_task(self):
        """Gets the use_output_from_previous_task of this HttpWwwFormUrlEncodedParameter.  # noqa: E501

        Optional; use the output from a previous task as the input to this parameter.  Set to null (default) to ignore.  # noqa: E501

        :return: The use_output_from_previous_task of this HttpWwwFormUrlEncodedParameter.  # noqa: E501
        :rtype: TaskOutputReference
        """
        return self._use_output_from_previous_task

    @use_output_from_previous_task.setter
    def use_output_from_previous_task(self, use_output_from_previous_task):
        """Sets the use_output_from_previous_task of this HttpWwwFormUrlEncodedParameter.

        Optional; use the output from a previous task as the input to this parameter.  Set to null (default) to ignore.  # noqa: E501

        :param use_output_from_previous_task: The use_output_from_previous_task of this HttpWwwFormUrlEncodedParameter.  # noqa: E501
        :type: TaskOutputReference
        """

        self._use_output_from_previous_task = use_output_from_previous_task

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(HttpWwwFormUrlEncodedParameter, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HttpWwwFormUrlEncodedParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
