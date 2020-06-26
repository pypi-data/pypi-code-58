# coding: utf-8

"""
    imageapi

    Image Recognition and Processing APIs let you use Machine Learning to recognize and process images, and also perform useful image modification operations.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PersonWithAge(object):
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
        'face_location': 'Face',
        'age_classification_confidence': 'float',
        'age_class': 'str',
        'age': 'float'
    }

    attribute_map = {
        'face_location': 'FaceLocation',
        'age_classification_confidence': 'AgeClassificationConfidence',
        'age_class': 'AgeClass',
        'age': 'Age'
    }

    def __init__(self, face_location=None, age_classification_confidence=None, age_class=None, age=None):  # noqa: E501
        """PersonWithAge - a model defined in Swagger"""  # noqa: E501

        self._face_location = None
        self._age_classification_confidence = None
        self._age_class = None
        self._age = None
        self.discriminator = None

        if face_location is not None:
            self.face_location = face_location
        if age_classification_confidence is not None:
            self.age_classification_confidence = age_classification_confidence
        if age_class is not None:
            self.age_class = age_class
        if age is not None:
            self.age = age

    @property
    def face_location(self):
        """Gets the face_location of this PersonWithAge.  # noqa: E501

        Location and other information about the person's face corresponding to this age classification  # noqa: E501

        :return: The face_location of this PersonWithAge.  # noqa: E501
        :rtype: Face
        """
        return self._face_location

    @face_location.setter
    def face_location(self, face_location):
        """Sets the face_location of this PersonWithAge.

        Location and other information about the person's face corresponding to this age classification  # noqa: E501

        :param face_location: The face_location of this PersonWithAge.  # noqa: E501
        :type: Face
        """

        self._face_location = face_location

    @property
    def age_classification_confidence(self):
        """Gets the age_classification_confidence of this PersonWithAge.  # noqa: E501

        Confidence level of age classification; possible values are between 0.0 and 1.0; higher is better, with values &gt; 0.50 being high confidence results  # noqa: E501

        :return: The age_classification_confidence of this PersonWithAge.  # noqa: E501
        :rtype: float
        """
        return self._age_classification_confidence

    @age_classification_confidence.setter
    def age_classification_confidence(self, age_classification_confidence):
        """Sets the age_classification_confidence of this PersonWithAge.

        Confidence level of age classification; possible values are between 0.0 and 1.0; higher is better, with values &gt; 0.50 being high confidence results  # noqa: E501

        :param age_classification_confidence: The age_classification_confidence of this PersonWithAge.  # noqa: E501
        :type: float
        """

        self._age_classification_confidence = age_classification_confidence

    @property
    def age_class(self):
        """Gets the age_class of this PersonWithAge.  # noqa: E501

        The person's age range classification result in years; possible values are \"0-2\", \"4-6\", \"8-13\", \"15-20\", \"25-32\", \"38-43\", \"48-53\", \"60+\"  # noqa: E501

        :return: The age_class of this PersonWithAge.  # noqa: E501
        :rtype: str
        """
        return self._age_class

    @age_class.setter
    def age_class(self, age_class):
        """Sets the age_class of this PersonWithAge.

        The person's age range classification result in years; possible values are \"0-2\", \"4-6\", \"8-13\", \"15-20\", \"25-32\", \"38-43\", \"48-53\", \"60+\"  # noqa: E501

        :param age_class: The age_class of this PersonWithAge.  # noqa: E501
        :type: str
        """

        self._age_class = age_class

    @property
    def age(self):
        """Gets the age of this PersonWithAge.  # noqa: E501


        :return: The age of this PersonWithAge.  # noqa: E501
        :rtype: float
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this PersonWithAge.


        :param age: The age of this PersonWithAge.  # noqa: E501
        :type: float
        """

        self._age = age

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
        if issubclass(PersonWithAge, dict):
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
        if not isinstance(other, PersonWithAge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
