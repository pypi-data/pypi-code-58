# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SmartSectionDisplaySettings(object):
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
        'cell_style': 'str',
        'collapsible_settings': 'SmartSectionCollapsibleDisplaySettings',
        'display': 'str',
        'display_label': 'str',
        'display_order': 'int',
        'display_page_number': 'int',
        'hide_label_when_opened': 'bool',
        'inline_outer_style': 'str',
        'label_when_opened': 'str',
        'pre_label': 'str',
        'scroll_to_top_when_opened': 'bool',
        'table_style': 'str'
    }

    attribute_map = {
        'cell_style': 'cellStyle',
        'collapsible_settings': 'collapsibleSettings',
        'display': 'display',
        'display_label': 'displayLabel',
        'display_order': 'displayOrder',
        'display_page_number': 'displayPageNumber',
        'hide_label_when_opened': 'hideLabelWhenOpened',
        'inline_outer_style': 'inlineOuterStyle',
        'label_when_opened': 'labelWhenOpened',
        'pre_label': 'preLabel',
        'scroll_to_top_when_opened': 'scrollToTopWhenOpened',
        'table_style': 'tableStyle'
    }

    def __init__(self, cell_style=None, collapsible_settings=None, display=None, display_label=None, display_order=None, display_page_number=None, hide_label_when_opened=None, inline_outer_style=None, label_when_opened=None, pre_label=None, scroll_to_top_when_opened=None, table_style=None):  # noqa: E501
        """SmartSectionDisplaySettings - a model defined in Swagger"""  # noqa: E501

        self._cell_style = None
        self._collapsible_settings = None
        self._display = None
        self._display_label = None
        self._display_order = None
        self._display_page_number = None
        self._hide_label_when_opened = None
        self._inline_outer_style = None
        self._label_when_opened = None
        self._pre_label = None
        self._scroll_to_top_when_opened = None
        self._table_style = None
        self.discriminator = None

        if cell_style is not None:
            self.cell_style = cell_style
        if collapsible_settings is not None:
            self.collapsible_settings = collapsible_settings
        if display is not None:
            self.display = display
        if display_label is not None:
            self.display_label = display_label
        if display_order is not None:
            self.display_order = display_order
        if display_page_number is not None:
            self.display_page_number = display_page_number
        if hide_label_when_opened is not None:
            self.hide_label_when_opened = hide_label_when_opened
        if inline_outer_style is not None:
            self.inline_outer_style = inline_outer_style
        if label_when_opened is not None:
            self.label_when_opened = label_when_opened
        if pre_label is not None:
            self.pre_label = pre_label
        if scroll_to_top_when_opened is not None:
            self.scroll_to_top_when_opened = scroll_to_top_when_opened
        if table_style is not None:
            self.table_style = table_style

    @property
    def cell_style(self):
        """Gets the cell_style of this SmartSectionDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The cell_style of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._cell_style

    @cell_style.setter
    def cell_style(self, cell_style):
        """Sets the cell_style of this SmartSectionDisplaySettings.

          # noqa: E501

        :param cell_style: The cell_style of this SmartSectionDisplaySettings.  # noqa: E501
        :type: str
        """

        self._cell_style = cell_style

    @property
    def collapsible_settings(self):
        """Gets the collapsible_settings of this SmartSectionDisplaySettings.  # noqa: E501


        :return: The collapsible_settings of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: SmartSectionCollapsibleDisplaySettings
        """
        return self._collapsible_settings

    @collapsible_settings.setter
    def collapsible_settings(self, collapsible_settings):
        """Sets the collapsible_settings of this SmartSectionDisplaySettings.


        :param collapsible_settings: The collapsible_settings of this SmartSectionDisplaySettings.  # noqa: E501
        :type: SmartSectionCollapsibleDisplaySettings
        """

        self._collapsible_settings = collapsible_settings

    @property
    def display(self):
        """Gets the display of this SmartSectionDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The display of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this SmartSectionDisplaySettings.

          # noqa: E501

        :param display: The display of this SmartSectionDisplaySettings.  # noqa: E501
        :type: str
        """

        self._display = display

    @property
    def display_label(self):
        """Gets the display_label of this SmartSectionDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The display_label of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._display_label

    @display_label.setter
    def display_label(self, display_label):
        """Sets the display_label of this SmartSectionDisplaySettings.

          # noqa: E501

        :param display_label: The display_label of this SmartSectionDisplaySettings.  # noqa: E501
        :type: str
        """

        self._display_label = display_label

    @property
    def display_order(self):
        """Gets the display_order of this SmartSectionDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The display_order of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this SmartSectionDisplaySettings.

          # noqa: E501

        :param display_order: The display_order of this SmartSectionDisplaySettings.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def display_page_number(self):
        """Gets the display_page_number of this SmartSectionDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The display_page_number of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: int
        """
        return self._display_page_number

    @display_page_number.setter
    def display_page_number(self, display_page_number):
        """Sets the display_page_number of this SmartSectionDisplaySettings.

          # noqa: E501

        :param display_page_number: The display_page_number of this SmartSectionDisplaySettings.  # noqa: E501
        :type: int
        """

        self._display_page_number = display_page_number

    @property
    def hide_label_when_opened(self):
        """Gets the hide_label_when_opened of this SmartSectionDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The hide_label_when_opened of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: bool
        """
        return self._hide_label_when_opened

    @hide_label_when_opened.setter
    def hide_label_when_opened(self, hide_label_when_opened):
        """Sets the hide_label_when_opened of this SmartSectionDisplaySettings.

          # noqa: E501

        :param hide_label_when_opened: The hide_label_when_opened of this SmartSectionDisplaySettings.  # noqa: E501
        :type: bool
        """

        self._hide_label_when_opened = hide_label_when_opened

    @property
    def inline_outer_style(self):
        """Gets the inline_outer_style of this SmartSectionDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The inline_outer_style of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._inline_outer_style

    @inline_outer_style.setter
    def inline_outer_style(self, inline_outer_style):
        """Sets the inline_outer_style of this SmartSectionDisplaySettings.

          # noqa: E501

        :param inline_outer_style: The inline_outer_style of this SmartSectionDisplaySettings.  # noqa: E501
        :type: str
        """

        self._inline_outer_style = inline_outer_style

    @property
    def label_when_opened(self):
        """Gets the label_when_opened of this SmartSectionDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The label_when_opened of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._label_when_opened

    @label_when_opened.setter
    def label_when_opened(self, label_when_opened):
        """Sets the label_when_opened of this SmartSectionDisplaySettings.

          # noqa: E501

        :param label_when_opened: The label_when_opened of this SmartSectionDisplaySettings.  # noqa: E501
        :type: str
        """

        self._label_when_opened = label_when_opened

    @property
    def pre_label(self):
        """Gets the pre_label of this SmartSectionDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The pre_label of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._pre_label

    @pre_label.setter
    def pre_label(self, pre_label):
        """Sets the pre_label of this SmartSectionDisplaySettings.

          # noqa: E501

        :param pre_label: The pre_label of this SmartSectionDisplaySettings.  # noqa: E501
        :type: str
        """

        self._pre_label = pre_label

    @property
    def scroll_to_top_when_opened(self):
        """Gets the scroll_to_top_when_opened of this SmartSectionDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The scroll_to_top_when_opened of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: bool
        """
        return self._scroll_to_top_when_opened

    @scroll_to_top_when_opened.setter
    def scroll_to_top_when_opened(self, scroll_to_top_when_opened):
        """Sets the scroll_to_top_when_opened of this SmartSectionDisplaySettings.

          # noqa: E501

        :param scroll_to_top_when_opened: The scroll_to_top_when_opened of this SmartSectionDisplaySettings.  # noqa: E501
        :type: bool
        """

        self._scroll_to_top_when_opened = scroll_to_top_when_opened

    @property
    def table_style(self):
        """Gets the table_style of this SmartSectionDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The table_style of this SmartSectionDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._table_style

    @table_style.setter
    def table_style(self, table_style):
        """Sets the table_style of this SmartSectionDisplaySettings.

          # noqa: E501

        :param table_style: The table_style of this SmartSectionDisplaySettings.  # noqa: E501
        :type: str
        """

        self._table_style = table_style

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
        if issubclass(SmartSectionDisplaySettings, dict):
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
        if not isinstance(other, SmartSectionDisplaySettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
