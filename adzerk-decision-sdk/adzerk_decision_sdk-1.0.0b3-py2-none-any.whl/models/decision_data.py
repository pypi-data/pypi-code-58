# coding: utf-8

"""
    Adzerk Decision API

    Adzerk Decision API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from adzerk_decision_sdk.configuration import Configuration


class DecisionData(object):
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
        'image_url': 'str',
        'file_name': 'str',
        'title': 'str',
        'width': 'int',
        'height': 'int',
        'custom_data': 'object'
    }

    attribute_map = {
        'image_url': 'imageUrl',
        'file_name': 'fileName',
        'title': 'title',
        'width': 'width',
        'height': 'height',
        'custom_data': 'customData'
    }

    def __init__(self, image_url=None, file_name=None, title=None, width=None, height=None, custom_data=None, local_vars_configuration=None):  # noqa: E501
        """DecisionData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._image_url = None
        self._file_name = None
        self._title = None
        self._width = None
        self._height = None
        self._custom_data = None
        self.discriminator = None

        if image_url is not None:
            self.image_url = image_url
        if file_name is not None:
            self.file_name = file_name
        if title is not None:
            self.title = title
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if custom_data is not None:
            self.custom_data = custom_data

    @property
    def image_url(self):
        """Gets the image_url of this DecisionData.  # noqa: E501


        :return: The image_url of this DecisionData.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this DecisionData.


        :param image_url: The image_url of this DecisionData.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def file_name(self):
        """Gets the file_name of this DecisionData.  # noqa: E501


        :return: The file_name of this DecisionData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DecisionData.


        :param file_name: The file_name of this DecisionData.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def title(self):
        """Gets the title of this DecisionData.  # noqa: E501


        :return: The title of this DecisionData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DecisionData.


        :param title: The title of this DecisionData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def width(self):
        """Gets the width of this DecisionData.  # noqa: E501


        :return: The width of this DecisionData.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DecisionData.


        :param width: The width of this DecisionData.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this DecisionData.  # noqa: E501


        :return: The height of this DecisionData.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DecisionData.


        :param height: The height of this DecisionData.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def custom_data(self):
        """Gets the custom_data of this DecisionData.  # noqa: E501


        :return: The custom_data of this DecisionData.  # noqa: E501
        :rtype: object
        """
        return self._custom_data

    @custom_data.setter
    def custom_data(self, custom_data):
        """Sets the custom_data of this DecisionData.


        :param custom_data: The custom_data of this DecisionData.  # noqa: E501
        :type: object
        """

        self._custom_data = custom_data

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
        if not isinstance(other, DecisionData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DecisionData):
            return True

        return self.to_dict() != other.to_dict()
