# coding: utf-8

"""
    KAMONOHASHI API

    A platform for deep learning  # noqa: E501

    OpenAPI spec version: v1
    Contact: kamonohashi-support@jp.nssol.nipponsteel.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StorageListResultInfo(object):
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
        'dirs': 'list[StorageDirInfo]',
        'exceeded': 'bool',
        'files': 'list[InfosStorageFileInfo]'
    }

    attribute_map = {
        'dirs': 'dirs',
        'exceeded': 'exceeded',
        'files': 'files'
    }

    def __init__(self, dirs=None, exceeded=None, files=None):  # noqa: E501
        """StorageListResultInfo - a model defined in Swagger"""  # noqa: E501

        self._dirs = None
        self._exceeded = None
        self._files = None
        self.discriminator = None

        if dirs is not None:
            self.dirs = dirs
        if exceeded is not None:
            self.exceeded = exceeded
        if files is not None:
            self.files = files

    @property
    def dirs(self):
        """Gets the dirs of this StorageListResultInfo.  # noqa: E501


        :return: The dirs of this StorageListResultInfo.  # noqa: E501
        :rtype: list[StorageDirInfo]
        """
        return self._dirs

    @dirs.setter
    def dirs(self, dirs):
        """Sets the dirs of this StorageListResultInfo.


        :param dirs: The dirs of this StorageListResultInfo.  # noqa: E501
        :type: list[StorageDirInfo]
        """

        self._dirs = dirs

    @property
    def exceeded(self):
        """Gets the exceeded of this StorageListResultInfo.  # noqa: E501


        :return: The exceeded of this StorageListResultInfo.  # noqa: E501
        :rtype: bool
        """
        return self._exceeded

    @exceeded.setter
    def exceeded(self, exceeded):
        """Sets the exceeded of this StorageListResultInfo.


        :param exceeded: The exceeded of this StorageListResultInfo.  # noqa: E501
        :type: bool
        """

        self._exceeded = exceeded

    @property
    def files(self):
        """Gets the files of this StorageListResultInfo.  # noqa: E501


        :return: The files of this StorageListResultInfo.  # noqa: E501
        :rtype: list[InfosStorageFileInfo]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this StorageListResultInfo.


        :param files: The files of this StorageListResultInfo.  # noqa: E501
        :type: list[InfosStorageFileInfo]
        """

        self._files = files

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
        if issubclass(StorageListResultInfo, dict):
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
        if not isinstance(other, StorageListResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
