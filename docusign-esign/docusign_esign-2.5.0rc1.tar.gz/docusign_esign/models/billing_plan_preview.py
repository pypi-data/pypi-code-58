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


class BillingPlanPreview(object):
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
        'currency_code': 'str',
        'invoice': 'BillingInvoice',
        'is_prorated': 'str',
        'subtotal_amount': 'str',
        'tax_amount': 'str',
        'total_amount': 'str'
    }

    attribute_map = {
        'currency_code': 'currencyCode',
        'invoice': 'invoice',
        'is_prorated': 'isProrated',
        'subtotal_amount': 'subtotalAmount',
        'tax_amount': 'taxAmount',
        'total_amount': 'totalAmount'
    }

    def __init__(self, currency_code=None, invoice=None, is_prorated=None, subtotal_amount=None, tax_amount=None, total_amount=None):  # noqa: E501
        """BillingPlanPreview - a model defined in Swagger"""  # noqa: E501

        self._currency_code = None
        self._invoice = None
        self._is_prorated = None
        self._subtotal_amount = None
        self._tax_amount = None
        self._total_amount = None
        self.discriminator = None

        if currency_code is not None:
            self.currency_code = currency_code
        if invoice is not None:
            self.invoice = invoice
        if is_prorated is not None:
            self.is_prorated = is_prorated
        if subtotal_amount is not None:
            self.subtotal_amount = subtotal_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount

    @property
    def currency_code(self):
        """Gets the currency_code of this BillingPlanPreview.  # noqa: E501

        Specifies the ISO currency code for the account.  # noqa: E501

        :return: The currency_code of this BillingPlanPreview.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this BillingPlanPreview.

        Specifies the ISO currency code for the account.  # noqa: E501

        :param currency_code: The currency_code of this BillingPlanPreview.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def invoice(self):
        """Gets the invoice of this BillingPlanPreview.  # noqa: E501


        :return: The invoice of this BillingPlanPreview.  # noqa: E501
        :rtype: BillingInvoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this BillingPlanPreview.


        :param invoice: The invoice of this BillingPlanPreview.  # noqa: E501
        :type: BillingInvoice
        """

        self._invoice = invoice

    @property
    def is_prorated(self):
        """Gets the is_prorated of this BillingPlanPreview.  # noqa: E501

          # noqa: E501

        :return: The is_prorated of this BillingPlanPreview.  # noqa: E501
        :rtype: str
        """
        return self._is_prorated

    @is_prorated.setter
    def is_prorated(self, is_prorated):
        """Sets the is_prorated of this BillingPlanPreview.

          # noqa: E501

        :param is_prorated: The is_prorated of this BillingPlanPreview.  # noqa: E501
        :type: str
        """

        self._is_prorated = is_prorated

    @property
    def subtotal_amount(self):
        """Gets the subtotal_amount of this BillingPlanPreview.  # noqa: E501

          # noqa: E501

        :return: The subtotal_amount of this BillingPlanPreview.  # noqa: E501
        :rtype: str
        """
        return self._subtotal_amount

    @subtotal_amount.setter
    def subtotal_amount(self, subtotal_amount):
        """Sets the subtotal_amount of this BillingPlanPreview.

          # noqa: E501

        :param subtotal_amount: The subtotal_amount of this BillingPlanPreview.  # noqa: E501
        :type: str
        """

        self._subtotal_amount = subtotal_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this BillingPlanPreview.  # noqa: E501

          # noqa: E501

        :return: The tax_amount of this BillingPlanPreview.  # noqa: E501
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this BillingPlanPreview.

          # noqa: E501

        :param tax_amount: The tax_amount of this BillingPlanPreview.  # noqa: E501
        :type: str
        """

        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        """Gets the total_amount of this BillingPlanPreview.  # noqa: E501

          # noqa: E501

        :return: The total_amount of this BillingPlanPreview.  # noqa: E501
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this BillingPlanPreview.

          # noqa: E501

        :param total_amount: The total_amount of this BillingPlanPreview.  # noqa: E501
        :type: str
        """

        self._total_amount = total_amount

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
        if issubclass(BillingPlanPreview, dict):
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
        if not isinstance(other, BillingPlanPreview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
