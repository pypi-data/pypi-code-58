# coding: utf-8

"""
    nlpapiv2

    The powerful Natural Language Processing APIs (v2) let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CheckSentenceResponse(object):
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
        'incorrect_count': 'int',
        'words': 'list[CorrectWordInSentence]'
    }

    attribute_map = {
        'incorrect_count': 'IncorrectCount',
        'words': 'Words'
    }

    def __init__(self, incorrect_count=None, words=None):  # noqa: E501
        """CheckSentenceResponse - a model defined in Swagger"""  # noqa: E501

        self._incorrect_count = None
        self._words = None
        self.discriminator = None

        if incorrect_count is not None:
            self.incorrect_count = incorrect_count
        if words is not None:
            self.words = words

    @property
    def incorrect_count(self):
        """Gets the incorrect_count of this CheckSentenceResponse.  # noqa: E501

        Number of incorrect words  # noqa: E501

        :return: The incorrect_count of this CheckSentenceResponse.  # noqa: E501
        :rtype: int
        """
        return self._incorrect_count

    @incorrect_count.setter
    def incorrect_count(self, incorrect_count):
        """Sets the incorrect_count of this CheckSentenceResponse.

        Number of incorrect words  # noqa: E501

        :param incorrect_count: The incorrect_count of this CheckSentenceResponse.  # noqa: E501
        :type: int
        """

        self._incorrect_count = incorrect_count

    @property
    def words(self):
        """Gets the words of this CheckSentenceResponse.  # noqa: E501

        Words in the sentence, both correct and incorrect  # noqa: E501

        :return: The words of this CheckSentenceResponse.  # noqa: E501
        :rtype: list[CorrectWordInSentence]
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this CheckSentenceResponse.

        Words in the sentence, both correct and incorrect  # noqa: E501

        :param words: The words of this CheckSentenceResponse.  # noqa: E501
        :type: list[CorrectWordInSentence]
        """

        self._words = words

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
        if issubclass(CheckSentenceResponse, dict):
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
        if not isinstance(other, CheckSentenceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
