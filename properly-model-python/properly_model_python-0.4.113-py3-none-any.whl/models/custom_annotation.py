# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from properly_model_python.models.base_model_ import Model
from properly_model_python import util


class CustomAnnotation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, value: object=None, annotation_group: str=None):  # noqa: E501
        """CustomAnnotation - a model defined in Swagger

        :param id: The id of this CustomAnnotation.  # noqa: E501
        :type id: str
        :param value: The value of this CustomAnnotation.  # noqa: E501
        :type value: object
        :param annotation_group: The annotation_group of this CustomAnnotation.  # noqa: E501
        :type annotation_group: str
        """
        self.swagger_types = {
            'id': str,
            'value': object,
            'annotation_group': str
        }

        self.attribute_map = {
            'id': 'id',
            'value': 'value',
            'annotation_group': 'annotationGroup'
        }

        self._id = id
        self._value = value
        self._annotation_group = annotation_group

    @classmethod
    def from_dict(cls, dikt) -> 'CustomAnnotation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CustomAnnotation of this CustomAnnotation.  # noqa: E501
        :rtype: CustomAnnotation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this CustomAnnotation.


        :return: The id of this CustomAnnotation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this CustomAnnotation.


        :param id: The id of this CustomAnnotation.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def value(self) -> object:
        """Gets the value of this CustomAnnotation.


        :return: The value of this CustomAnnotation.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value: object):
        """Sets the value of this CustomAnnotation.


        :param value: The value of this CustomAnnotation.
        :type value: object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def annotation_group(self) -> str:
        """Gets the annotation_group of this CustomAnnotation.


        :return: The annotation_group of this CustomAnnotation.
        :rtype: str
        """
        return self._annotation_group

    @annotation_group.setter
    def annotation_group(self, annotation_group: str):
        """Sets the annotation_group of this CustomAnnotation.


        :param annotation_group: The annotation_group of this CustomAnnotation.
        :type annotation_group: str
        """
        if annotation_group is None:
            raise ValueError("Invalid value for `annotation_group`, must not be `None`")  # noqa: E501

        self._annotation_group = annotation_group
