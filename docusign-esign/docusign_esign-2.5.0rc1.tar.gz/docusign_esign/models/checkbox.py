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


class Checkbox(object):
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
        'anchor_case_sensitive': 'str',
        'anchor_horizontal_alignment': 'str',
        'anchor_ignore_if_not_present': 'str',
        'anchor_match_whole_word': 'str',
        'anchor_string': 'str',
        'anchor_units': 'str',
        'anchor_x_offset': 'str',
        'anchor_y_offset': 'str',
        'conditional_parent_label': 'str',
        'conditional_parent_value': 'str',
        'custom_tab_id': 'str',
        'document_id': 'str',
        'error_details': 'ErrorDetails',
        'locked': 'str',
        'merge_field': 'MergeField',
        'name': 'str',
        'page_number': 'str',
        'recipient_id': 'str',
        'required': 'str',
        'require_initial_on_shared_change': 'str',
        'selected': 'str',
        'shared': 'str',
        'status': 'str',
        'tab_group_labels': 'list[str]',
        'tab_id': 'str',
        'tab_label': 'str',
        'tab_order': 'str',
        'template_locked': 'str',
        'template_required': 'str',
        'tooltip': 'str',
        'x_position': 'str',
        'y_position': 'str'
    }

    attribute_map = {
        'anchor_case_sensitive': 'anchorCaseSensitive',
        'anchor_horizontal_alignment': 'anchorHorizontalAlignment',
        'anchor_ignore_if_not_present': 'anchorIgnoreIfNotPresent',
        'anchor_match_whole_word': 'anchorMatchWholeWord',
        'anchor_string': 'anchorString',
        'anchor_units': 'anchorUnits',
        'anchor_x_offset': 'anchorXOffset',
        'anchor_y_offset': 'anchorYOffset',
        'conditional_parent_label': 'conditionalParentLabel',
        'conditional_parent_value': 'conditionalParentValue',
        'custom_tab_id': 'customTabId',
        'document_id': 'documentId',
        'error_details': 'errorDetails',
        'locked': 'locked',
        'merge_field': 'mergeField',
        'name': 'name',
        'page_number': 'pageNumber',
        'recipient_id': 'recipientId',
        'required': 'required',
        'require_initial_on_shared_change': 'requireInitialOnSharedChange',
        'selected': 'selected',
        'shared': 'shared',
        'status': 'status',
        'tab_group_labels': 'tabGroupLabels',
        'tab_id': 'tabId',
        'tab_label': 'tabLabel',
        'tab_order': 'tabOrder',
        'template_locked': 'templateLocked',
        'template_required': 'templateRequired',
        'tooltip': 'tooltip',
        'x_position': 'xPosition',
        'y_position': 'yPosition'
    }

    def __init__(self, anchor_case_sensitive=None, anchor_horizontal_alignment=None, anchor_ignore_if_not_present=None, anchor_match_whole_word=None, anchor_string=None, anchor_units=None, anchor_x_offset=None, anchor_y_offset=None, conditional_parent_label=None, conditional_parent_value=None, custom_tab_id=None, document_id=None, error_details=None, locked=None, merge_field=None, name=None, page_number=None, recipient_id=None, required=None, require_initial_on_shared_change=None, selected=None, shared=None, status=None, tab_group_labels=None, tab_id=None, tab_label=None, tab_order=None, template_locked=None, template_required=None, tooltip=None, x_position=None, y_position=None):  # noqa: E501
        """Checkbox - a model defined in Swagger"""  # noqa: E501

        self._anchor_case_sensitive = None
        self._anchor_horizontal_alignment = None
        self._anchor_ignore_if_not_present = None
        self._anchor_match_whole_word = None
        self._anchor_string = None
        self._anchor_units = None
        self._anchor_x_offset = None
        self._anchor_y_offset = None
        self._conditional_parent_label = None
        self._conditional_parent_value = None
        self._custom_tab_id = None
        self._document_id = None
        self._error_details = None
        self._locked = None
        self._merge_field = None
        self._name = None
        self._page_number = None
        self._recipient_id = None
        self._required = None
        self._require_initial_on_shared_change = None
        self._selected = None
        self._shared = None
        self._status = None
        self._tab_group_labels = None
        self._tab_id = None
        self._tab_label = None
        self._tab_order = None
        self._template_locked = None
        self._template_required = None
        self._tooltip = None
        self._x_position = None
        self._y_position = None
        self.discriminator = None

        if anchor_case_sensitive is not None:
            self.anchor_case_sensitive = anchor_case_sensitive
        if anchor_horizontal_alignment is not None:
            self.anchor_horizontal_alignment = anchor_horizontal_alignment
        if anchor_ignore_if_not_present is not None:
            self.anchor_ignore_if_not_present = anchor_ignore_if_not_present
        if anchor_match_whole_word is not None:
            self.anchor_match_whole_word = anchor_match_whole_word
        if anchor_string is not None:
            self.anchor_string = anchor_string
        if anchor_units is not None:
            self.anchor_units = anchor_units
        if anchor_x_offset is not None:
            self.anchor_x_offset = anchor_x_offset
        if anchor_y_offset is not None:
            self.anchor_y_offset = anchor_y_offset
        if conditional_parent_label is not None:
            self.conditional_parent_label = conditional_parent_label
        if conditional_parent_value is not None:
            self.conditional_parent_value = conditional_parent_value
        if custom_tab_id is not None:
            self.custom_tab_id = custom_tab_id
        if document_id is not None:
            self.document_id = document_id
        if error_details is not None:
            self.error_details = error_details
        if locked is not None:
            self.locked = locked
        if merge_field is not None:
            self.merge_field = merge_field
        if name is not None:
            self.name = name
        if page_number is not None:
            self.page_number = page_number
        if recipient_id is not None:
            self.recipient_id = recipient_id
        if required is not None:
            self.required = required
        if require_initial_on_shared_change is not None:
            self.require_initial_on_shared_change = require_initial_on_shared_change
        if selected is not None:
            self.selected = selected
        if shared is not None:
            self.shared = shared
        if status is not None:
            self.status = status
        if tab_group_labels is not None:
            self.tab_group_labels = tab_group_labels
        if tab_id is not None:
            self.tab_id = tab_id
        if tab_label is not None:
            self.tab_label = tab_label
        if tab_order is not None:
            self.tab_order = tab_order
        if template_locked is not None:
            self.template_locked = template_locked
        if template_required is not None:
            self.template_required = template_required
        if tooltip is not None:
            self.tooltip = tooltip
        if x_position is not None:
            self.x_position = x_position
        if y_position is not None:
            self.y_position = y_position

    @property
    def anchor_case_sensitive(self):
        """Gets the anchor_case_sensitive of this Checkbox.  # noqa: E501

        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.  # noqa: E501

        :return: The anchor_case_sensitive of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._anchor_case_sensitive

    @anchor_case_sensitive.setter
    def anchor_case_sensitive(self, anchor_case_sensitive):
        """Sets the anchor_case_sensitive of this Checkbox.

        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.  # noqa: E501

        :param anchor_case_sensitive: The anchor_case_sensitive of this Checkbox.  # noqa: E501
        :type: str
        """

        self._anchor_case_sensitive = anchor_case_sensitive

    @property
    def anchor_horizontal_alignment(self):
        """Gets the anchor_horizontal_alignment of this Checkbox.  # noqa: E501

        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.  # noqa: E501

        :return: The anchor_horizontal_alignment of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._anchor_horizontal_alignment

    @anchor_horizontal_alignment.setter
    def anchor_horizontal_alignment(self, anchor_horizontal_alignment):
        """Sets the anchor_horizontal_alignment of this Checkbox.

        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.  # noqa: E501

        :param anchor_horizontal_alignment: The anchor_horizontal_alignment of this Checkbox.  # noqa: E501
        :type: str
        """

        self._anchor_horizontal_alignment = anchor_horizontal_alignment

    @property
    def anchor_ignore_if_not_present(self):
        """Gets the anchor_ignore_if_not_present of this Checkbox.  # noqa: E501

        When set to **true**, this tab is ignored if anchorString is not found in the document.  # noqa: E501

        :return: The anchor_ignore_if_not_present of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._anchor_ignore_if_not_present

    @anchor_ignore_if_not_present.setter
    def anchor_ignore_if_not_present(self, anchor_ignore_if_not_present):
        """Sets the anchor_ignore_if_not_present of this Checkbox.

        When set to **true**, this tab is ignored if anchorString is not found in the document.  # noqa: E501

        :param anchor_ignore_if_not_present: The anchor_ignore_if_not_present of this Checkbox.  # noqa: E501
        :type: str
        """

        self._anchor_ignore_if_not_present = anchor_ignore_if_not_present

    @property
    def anchor_match_whole_word(self):
        """Gets the anchor_match_whole_word of this Checkbox.  # noqa: E501

        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.  # noqa: E501

        :return: The anchor_match_whole_word of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._anchor_match_whole_word

    @anchor_match_whole_word.setter
    def anchor_match_whole_word(self, anchor_match_whole_word):
        """Sets the anchor_match_whole_word of this Checkbox.

        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.  # noqa: E501

        :param anchor_match_whole_word: The anchor_match_whole_word of this Checkbox.  # noqa: E501
        :type: str
        """

        self._anchor_match_whole_word = anchor_match_whole_word

    @property
    def anchor_string(self):
        """Gets the anchor_string of this Checkbox.  # noqa: E501

        Anchor text information for a radio button.  # noqa: E501

        :return: The anchor_string of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._anchor_string

    @anchor_string.setter
    def anchor_string(self, anchor_string):
        """Sets the anchor_string of this Checkbox.

        Anchor text information for a radio button.  # noqa: E501

        :param anchor_string: The anchor_string of this Checkbox.  # noqa: E501
        :type: str
        """

        self._anchor_string = anchor_string

    @property
    def anchor_units(self):
        """Gets the anchor_units of this Checkbox.  # noqa: E501

        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.  # noqa: E501

        :return: The anchor_units of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._anchor_units

    @anchor_units.setter
    def anchor_units(self, anchor_units):
        """Sets the anchor_units of this Checkbox.

        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.  # noqa: E501

        :param anchor_units: The anchor_units of this Checkbox.  # noqa: E501
        :type: str
        """

        self._anchor_units = anchor_units

    @property
    def anchor_x_offset(self):
        """Gets the anchor_x_offset of this Checkbox.  # noqa: E501

        Specifies the X axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :return: The anchor_x_offset of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._anchor_x_offset

    @anchor_x_offset.setter
    def anchor_x_offset(self, anchor_x_offset):
        """Sets the anchor_x_offset of this Checkbox.

        Specifies the X axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :param anchor_x_offset: The anchor_x_offset of this Checkbox.  # noqa: E501
        :type: str
        """

        self._anchor_x_offset = anchor_x_offset

    @property
    def anchor_y_offset(self):
        """Gets the anchor_y_offset of this Checkbox.  # noqa: E501

        Specifies the Y axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :return: The anchor_y_offset of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._anchor_y_offset

    @anchor_y_offset.setter
    def anchor_y_offset(self, anchor_y_offset):
        """Sets the anchor_y_offset of this Checkbox.

        Specifies the Y axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :param anchor_y_offset: The anchor_y_offset of this Checkbox.  # noqa: E501
        :type: str
        """

        self._anchor_y_offset = anchor_y_offset

    @property
    def conditional_parent_label(self):
        """Gets the conditional_parent_label of this Checkbox.  # noqa: E501

        For conditional fields this is the TabLabel of the parent tab that controls this tab's visibility.  # noqa: E501

        :return: The conditional_parent_label of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._conditional_parent_label

    @conditional_parent_label.setter
    def conditional_parent_label(self, conditional_parent_label):
        """Sets the conditional_parent_label of this Checkbox.

        For conditional fields this is the TabLabel of the parent tab that controls this tab's visibility.  # noqa: E501

        :param conditional_parent_label: The conditional_parent_label of this Checkbox.  # noqa: E501
        :type: str
        """

        self._conditional_parent_label = conditional_parent_label

    @property
    def conditional_parent_value(self):
        """Gets the conditional_parent_value of this Checkbox.  # noqa: E501

        For conditional fields, this is the value of the parent tab that controls the tab's visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \"on\" as the value to show that the parent tab is active.   # noqa: E501

        :return: The conditional_parent_value of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._conditional_parent_value

    @conditional_parent_value.setter
    def conditional_parent_value(self, conditional_parent_value):
        """Sets the conditional_parent_value of this Checkbox.

        For conditional fields, this is the value of the parent tab that controls the tab's visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \"on\" as the value to show that the parent tab is active.   # noqa: E501

        :param conditional_parent_value: The conditional_parent_value of this Checkbox.  # noqa: E501
        :type: str
        """

        self._conditional_parent_value = conditional_parent_value

    @property
    def custom_tab_id(self):
        """Gets the custom_tab_id of this Checkbox.  # noqa: E501

        The DocuSign generated custom tab ID for the custom tab to be applied. This can only be used when adding new tabs for a recipient. When used, the new tab inherits all the custom tab properties.  # noqa: E501

        :return: The custom_tab_id of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._custom_tab_id

    @custom_tab_id.setter
    def custom_tab_id(self, custom_tab_id):
        """Sets the custom_tab_id of this Checkbox.

        The DocuSign generated custom tab ID for the custom tab to be applied. This can only be used when adding new tabs for a recipient. When used, the new tab inherits all the custom tab properties.  # noqa: E501

        :param custom_tab_id: The custom_tab_id of this Checkbox.  # noqa: E501
        :type: str
        """

        self._custom_tab_id = custom_tab_id

    @property
    def document_id(self):
        """Gets the document_id of this Checkbox.  # noqa: E501

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :return: The document_id of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Checkbox.

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :param document_id: The document_id of this Checkbox.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def error_details(self):
        """Gets the error_details of this Checkbox.  # noqa: E501


        :return: The error_details of this Checkbox.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this Checkbox.


        :param error_details: The error_details of this Checkbox.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def locked(self):
        """Gets the locked of this Checkbox.  # noqa: E501

        When set to **true**, the signer cannot change the data of the custom tab.  # noqa: E501

        :return: The locked of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this Checkbox.

        When set to **true**, the signer cannot change the data of the custom tab.  # noqa: E501

        :param locked: The locked of this Checkbox.  # noqa: E501
        :type: str
        """

        self._locked = locked

    @property
    def merge_field(self):
        """Gets the merge_field of this Checkbox.  # noqa: E501


        :return: The merge_field of this Checkbox.  # noqa: E501
        :rtype: MergeField
        """
        return self._merge_field

    @merge_field.setter
    def merge_field(self, merge_field):
        """Sets the merge_field of this Checkbox.


        :param merge_field: The merge_field of this Checkbox.  # noqa: E501
        :type: MergeField
        """

        self._merge_field = merge_field

    @property
    def name(self):
        """Gets the name of this Checkbox.  # noqa: E501

        Specifies the tool tip text for the tab.  # noqa: E501

        :return: The name of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Checkbox.

        Specifies the tool tip text for the tab.  # noqa: E501

        :param name: The name of this Checkbox.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def page_number(self):
        """Gets the page_number of this Checkbox.  # noqa: E501

        Specifies the page number on which the tab is located.  # noqa: E501

        :return: The page_number of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this Checkbox.

        Specifies the page number on which the tab is located.  # noqa: E501

        :param page_number: The page_number of this Checkbox.  # noqa: E501
        :type: str
        """

        self._page_number = page_number

    @property
    def recipient_id(self):
        """Gets the recipient_id of this Checkbox.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this Checkbox.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this Checkbox.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def required(self):
        """Gets the required of this Checkbox.  # noqa: E501

        When set to **true**, the signer is required to fill out this tab  # noqa: E501

        :return: The required of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this Checkbox.

        When set to **true**, the signer is required to fill out this tab  # noqa: E501

        :param required: The required of this Checkbox.  # noqa: E501
        :type: str
        """

        self._required = required

    @property
    def require_initial_on_shared_change(self):
        """Gets the require_initial_on_shared_change of this Checkbox.  # noqa: E501

        Optional element for field markup. When set to **true**, the signer is required to initial when they modify a shared field.  # noqa: E501

        :return: The require_initial_on_shared_change of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._require_initial_on_shared_change

    @require_initial_on_shared_change.setter
    def require_initial_on_shared_change(self, require_initial_on_shared_change):
        """Sets the require_initial_on_shared_change of this Checkbox.

        Optional element for field markup. When set to **true**, the signer is required to initial when they modify a shared field.  # noqa: E501

        :param require_initial_on_shared_change: The require_initial_on_shared_change of this Checkbox.  # noqa: E501
        :type: str
        """

        self._require_initial_on_shared_change = require_initial_on_shared_change

    @property
    def selected(self):
        """Gets the selected of this Checkbox.  # noqa: E501

        When set to **true**, the checkbox is selected.  # noqa: E501

        :return: The selected of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this Checkbox.

        When set to **true**, the checkbox is selected.  # noqa: E501

        :param selected: The selected of this Checkbox.  # noqa: E501
        :type: str
        """

        self._selected = selected

    @property
    def shared(self):
        """Gets the shared of this Checkbox.  # noqa: E501

        When set to **true**, this custom tab is shared.  # noqa: E501

        :return: The shared of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this Checkbox.

        When set to **true**, this custom tab is shared.  # noqa: E501

        :param shared: The shared of this Checkbox.  # noqa: E501
        :type: str
        """

        self._shared = shared

    @property
    def status(self):
        """Gets the status of this Checkbox.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Checkbox.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this Checkbox.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tab_group_labels(self):
        """Gets the tab_group_labels of this Checkbox.  # noqa: E501

          # noqa: E501

        :return: The tab_group_labels of this Checkbox.  # noqa: E501
        :rtype: list[str]
        """
        return self._tab_group_labels

    @tab_group_labels.setter
    def tab_group_labels(self, tab_group_labels):
        """Sets the tab_group_labels of this Checkbox.

          # noqa: E501

        :param tab_group_labels: The tab_group_labels of this Checkbox.  # noqa: E501
        :type: list[str]
        """

        self._tab_group_labels = tab_group_labels

    @property
    def tab_id(self):
        """Gets the tab_id of this Checkbox.  # noqa: E501

        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].       # noqa: E501

        :return: The tab_id of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._tab_id

    @tab_id.setter
    def tab_id(self, tab_id):
        """Sets the tab_id of this Checkbox.

        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].       # noqa: E501

        :param tab_id: The tab_id of this Checkbox.  # noqa: E501
        :type: str
        """

        self._tab_id = tab_id

    @property
    def tab_label(self):
        """Gets the tab_label of this Checkbox.  # noqa: E501

        The label string associated with the tab.  # noqa: E501

        :return: The tab_label of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._tab_label

    @tab_label.setter
    def tab_label(self, tab_label):
        """Sets the tab_label of this Checkbox.

        The label string associated with the tab.  # noqa: E501

        :param tab_label: The tab_label of this Checkbox.  # noqa: E501
        :type: str
        """

        self._tab_label = tab_label

    @property
    def tab_order(self):
        """Gets the tab_order of this Checkbox.  # noqa: E501

          # noqa: E501

        :return: The tab_order of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._tab_order

    @tab_order.setter
    def tab_order(self, tab_order):
        """Sets the tab_order of this Checkbox.

          # noqa: E501

        :param tab_order: The tab_order of this Checkbox.  # noqa: E501
        :type: str
        """

        self._tab_order = tab_order

    @property
    def template_locked(self):
        """Gets the template_locked of this Checkbox.  # noqa: E501

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :return: The template_locked of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._template_locked

    @template_locked.setter
    def template_locked(self, template_locked):
        """Sets the template_locked of this Checkbox.

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :param template_locked: The template_locked of this Checkbox.  # noqa: E501
        :type: str
        """

        self._template_locked = template_locked

    @property
    def template_required(self):
        """Gets the template_required of this Checkbox.  # noqa: E501

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :return: The template_required of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._template_required

    @template_required.setter
    def template_required(self, template_required):
        """Sets the template_required of this Checkbox.

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :param template_required: The template_required of this Checkbox.  # noqa: E501
        :type: str
        """

        self._template_required = template_required

    @property
    def tooltip(self):
        """Gets the tooltip of this Checkbox.  # noqa: E501

          # noqa: E501

        :return: The tooltip of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this Checkbox.

          # noqa: E501

        :param tooltip: The tooltip of this Checkbox.  # noqa: E501
        :type: str
        """

        self._tooltip = tooltip

    @property
    def x_position(self):
        """Gets the x_position of this Checkbox.  # noqa: E501

        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :return: The x_position of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._x_position

    @x_position.setter
    def x_position(self, x_position):
        """Sets the x_position of this Checkbox.

        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :param x_position: The x_position of this Checkbox.  # noqa: E501
        :type: str
        """

        self._x_position = x_position

    @property
    def y_position(self):
        """Gets the y_position of this Checkbox.  # noqa: E501

        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :return: The y_position of this Checkbox.  # noqa: E501
        :rtype: str
        """
        return self._y_position

    @y_position.setter
    def y_position(self, y_position):
        """Sets the y_position of this Checkbox.

        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :param y_position: The y_position of this Checkbox.  # noqa: E501
        :type: str
        """

        self._y_position = y_position

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
        if issubclass(Checkbox, dict):
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
        if not isinstance(other, Checkbox):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
