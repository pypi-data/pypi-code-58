# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DocumentHtmlDefinitionOriginal(object):
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
        'document_id': 'str',
        'document_id_guid': 'str',
        'html_definition': 'DocumentHtmlDefinition'
    }

    attribute_map = {
        'document_id': 'documentId',
        'document_id_guid': 'documentIdGuid',
        'html_definition': 'htmlDefinition'
    }

    def __init__(self, document_id=None, document_id_guid=None, html_definition=None):  # noqa: E501
        """DocumentHtmlDefinitionOriginal - a model defined in Swagger"""  # noqa: E501

        self._document_id = None
        self._document_id_guid = None
        self._html_definition = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        if document_id_guid is not None:
            self.document_id_guid = document_id_guid
        if html_definition is not None:
            self.html_definition = html_definition

    @property
    def document_id(self):
        """Gets the document_id of this DocumentHtmlDefinitionOriginal.  # noqa: E501

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :return: The document_id of this DocumentHtmlDefinitionOriginal.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this DocumentHtmlDefinitionOriginal.

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :param document_id: The document_id of this DocumentHtmlDefinitionOriginal.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_id_guid(self):
        """Gets the document_id_guid of this DocumentHtmlDefinitionOriginal.  # noqa: E501

          # noqa: E501

        :return: The document_id_guid of this DocumentHtmlDefinitionOriginal.  # noqa: E501
        :rtype: str
        """
        return self._document_id_guid

    @document_id_guid.setter
    def document_id_guid(self, document_id_guid):
        """Sets the document_id_guid of this DocumentHtmlDefinitionOriginal.

          # noqa: E501

        :param document_id_guid: The document_id_guid of this DocumentHtmlDefinitionOriginal.  # noqa: E501
        :type: str
        """

        self._document_id_guid = document_id_guid

    @property
    def html_definition(self):
        """Gets the html_definition of this DocumentHtmlDefinitionOriginal.  # noqa: E501


        :return: The html_definition of this DocumentHtmlDefinitionOriginal.  # noqa: E501
        :rtype: DocumentHtmlDefinition
        """
        return self._html_definition

    @html_definition.setter
    def html_definition(self, html_definition):
        """Sets the html_definition of this DocumentHtmlDefinitionOriginal.


        :param html_definition: The html_definition of this DocumentHtmlDefinitionOriginal.  # noqa: E501
        :type: DocumentHtmlDefinition
        """

        self._html_definition = html_definition

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
        if issubclass(DocumentHtmlDefinitionOriginal, dict):
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
        if not isinstance(other, DocumentHtmlDefinitionOriginal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
