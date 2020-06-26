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


class ChallengeAnswerSpec(object):
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
        'answer': 'str',
        'challenge_id': 'str'
    }

    attribute_map = {
        'answer': 'answer',
        'challenge_id': 'challenge_id'
    }

    def __init__(self, answer=None, challenge_id=None, local_vars_configuration=None):  # noqa: E501
        """ChallengeAnswerSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._answer = None
        self._challenge_id = None
        self.discriminator = None

        self.answer = answer
        if challenge_id is not None:
            self.challenge_id = challenge_id

    @property
    def answer(self):
        """Gets the answer of this ChallengeAnswerSpec.  # noqa: E501

        An opaque string used to answer the challenge.  # noqa: E501

        :return: The answer of this ChallengeAnswerSpec.  # noqa: E501
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this ChallengeAnswerSpec.

        An opaque string used to answer the challenge.  # noqa: E501

        :param answer: The answer of this ChallengeAnswerSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and answer is None:  # noqa: E501
            raise ValueError("Invalid value for `answer`, must not be `None`")  # noqa: E501

        self._answer = answer

    @property
    def challenge_id(self):
        """Gets the challenge_id of this ChallengeAnswerSpec.  # noqa: E501

        The id of the challenge being answered. This is not required. It is present for consistency.   # noqa: E501

        :return: The challenge_id of this ChallengeAnswerSpec.  # noqa: E501
        :rtype: str
        """
        return self._challenge_id

    @challenge_id.setter
    def challenge_id(self, challenge_id):
        """Sets the challenge_id of this ChallengeAnswerSpec.

        The id of the challenge being answered. This is not required. It is present for consistency.   # noqa: E501

        :param challenge_id: The challenge_id of this ChallengeAnswerSpec.  # noqa: E501
        :type: str
        """

        self._challenge_id = challenge_id

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
        if not isinstance(other, ChallengeAnswerSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChallengeAnswerSpec):
            return True

        return self.to_dict() != other.to_dict()
