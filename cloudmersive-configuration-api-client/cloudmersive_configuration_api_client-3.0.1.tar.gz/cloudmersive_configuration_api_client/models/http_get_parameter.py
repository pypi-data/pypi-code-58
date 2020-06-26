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


class HttpGetParameter(object):
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
        'parameter_name': 'str',
        'parameter_value': 'str',
        'use_output_from_previous_task': 'TaskOutputReference'
    }

    attribute_map = {
        'parameter_name': 'ParameterName',
        'parameter_value': 'ParameterValue',
        'use_output_from_previous_task': 'UseOutputFromPreviousTask'
    }

    def __init__(self, parameter_name=None, parameter_value=None, use_output_from_previous_task=None):  # noqa: E501
        """HttpGetParameter - a model defined in Swagger"""  # noqa: E501

        self._parameter_name = None
        self._parameter_value = None
        self._use_output_from_previous_task = None
        self.discriminator = None

        if parameter_name is not None:
            self.parameter_name = parameter_name
        if parameter_value is not None:
            self.parameter_value = parameter_value
        if use_output_from_previous_task is not None:
            self.use_output_from_previous_task = use_output_from_previous_task

    @property
    def parameter_name(self):
        """Gets the parameter_name of this HttpGetParameter.  # noqa: E501

        Name of the parameter  # noqa: E501

        :return: The parameter_name of this HttpGetParameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this HttpGetParameter.

        Name of the parameter  # noqa: E501

        :param parameter_name: The parameter_name of this HttpGetParameter.  # noqa: E501
        :type: str
        """

        self._parameter_name = parameter_name

    @property
    def parameter_value(self):
        """Gets the parameter_value of this HttpGetParameter.  # noqa: E501

        Value of the parameter  # noqa: E501

        :return: The parameter_value of this HttpGetParameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value):
        """Sets the parameter_value of this HttpGetParameter.

        Value of the parameter  # noqa: E501

        :param parameter_value: The parameter_value of this HttpGetParameter.  # noqa: E501
        :type: str
        """

        self._parameter_value = parameter_value

    @property
    def use_output_from_previous_task(self):
        """Gets the use_output_from_previous_task of this HttpGetParameter.  # noqa: E501

        Optional; use the output from a previous task as the input to this parameter.  Set to null (default) to ignore.  # noqa: E501

        :return: The use_output_from_previous_task of this HttpGetParameter.  # noqa: E501
        :rtype: TaskOutputReference
        """
        return self._use_output_from_previous_task

    @use_output_from_previous_task.setter
    def use_output_from_previous_task(self, use_output_from_previous_task):
        """Sets the use_output_from_previous_task of this HttpGetParameter.

        Optional; use the output from a previous task as the input to this parameter.  Set to null (default) to ignore.  # noqa: E501

        :param use_output_from_previous_task: The use_output_from_previous_task of this HttpGetParameter.  # noqa: E501
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
        if issubclass(HttpGetParameter, dict):
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
        if not isinstance(other, HttpGetParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
