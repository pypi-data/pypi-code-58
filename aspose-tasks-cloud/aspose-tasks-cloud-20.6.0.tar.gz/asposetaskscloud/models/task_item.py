# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TaskItem.py">
#   Copyright (c) 2020 Aspose.Tasks Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six


class TaskItem(object):
    """A task&#39;s brief info 
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'Link',
        'uid': 'int',
        'id': 'int',
        'name': 'str',
        'start': 'datetime',
        'finish': 'datetime',
        'duration': 'str'
    }

    attribute_map = {
        'link': 'link',
        'uid': 'uid',
        'id': 'id',
        'name': 'name',
        'start': 'start',
        'finish': 'finish',
        'duration': 'duration'
    }

    def __init__(self, link=None, uid=None, id=None, name=None, start=None, finish=None, duration=None):  # noqa: E501
        """TaskItem - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._uid = None
        self._id = None
        self._name = None
        self._start = None
        self._finish = None
        self._duration = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if uid is not None:
            self.uid = uid
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if start is not None:
            self.start = start
        if finish is not None:
            self.finish = finish
        if duration is not None:
            self.duration = duration

    @property
    def link(self):
        """Gets the link of this TaskItem.  # noqa: E501


        :return: The link of this TaskItem.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TaskItem.


        :param link: The link of this TaskItem.  # noqa: E501
        :type: Link
        """
        self._link = link
    @property
    def uid(self):
        """Gets the uid of this TaskItem.  # noqa: E501


        :return: The uid of this TaskItem.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this TaskItem.


        :param uid: The uid of this TaskItem.  # noqa: E501
        :type: int
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        self._uid = uid
    @property
    def id(self):
        """Gets the id of this TaskItem.  # noqa: E501


        :return: The id of this TaskItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskItem.


        :param id: The id of this TaskItem.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        self._id = id
    @property
    def name(self):
        """Gets the name of this TaskItem.  # noqa: E501


        :return: The name of this TaskItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskItem.


        :param name: The name of this TaskItem.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def start(self):
        """Gets the start of this TaskItem.  # noqa: E501


        :return: The start of this TaskItem.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TaskItem.


        :param start: The start of this TaskItem.  # noqa: E501
        :type: datetime
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501
        self._start = start
    @property
    def finish(self):
        """Gets the finish of this TaskItem.  # noqa: E501


        :return: The finish of this TaskItem.  # noqa: E501
        :rtype: datetime
        """
        return self._finish

    @finish.setter
    def finish(self, finish):
        """Sets the finish of this TaskItem.


        :param finish: The finish of this TaskItem.  # noqa: E501
        :type: datetime
        """
        if finish is None:
            raise ValueError("Invalid value for `finish`, must not be `None`")  # noqa: E501
        self._finish = finish
    @property
    def duration(self):
        """Gets the duration of this TaskItem.  # noqa: E501

        The duration of a task.  # noqa: E501

        :return: The duration of this TaskItem.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TaskItem.

        The duration of a task.  # noqa: E501

        :param duration: The duration of this TaskItem.  # noqa: E501
        :type: str
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501
        self._duration = duration
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
