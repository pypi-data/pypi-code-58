# coding: utf-8

"""
    Adzerk Decision API

    Adzerk Decision API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from adzerk_decision_sdk.configuration import Configuration


class Decision(object):
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
        'ad_id': 'int',
        'creative_id': 'int',
        'flight_id': 'int',
        'campaign_id': 'int',
        'priority_id': 'int',
        'click_url': 'str',
        'contents': 'list[Content]',
        'impression_url': 'str',
        'events': 'list[Event]',
        'pricing': 'PricingData'
    }

    attribute_map = {
        'ad_id': 'adId',
        'creative_id': 'creativeId',
        'flight_id': 'flightId',
        'campaign_id': 'campaignId',
        'priority_id': 'priorityId',
        'click_url': 'clickUrl',
        'contents': 'contents',
        'impression_url': 'impressionUrl',
        'events': 'events',
        'pricing': 'pricing'
    }

    def __init__(self, ad_id=None, creative_id=None, flight_id=None, campaign_id=None, priority_id=None, click_url=None, contents=None, impression_url=None, events=None, pricing=None, local_vars_configuration=None):  # noqa: E501
        """Decision - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ad_id = None
        self._creative_id = None
        self._flight_id = None
        self._campaign_id = None
        self._priority_id = None
        self._click_url = None
        self._contents = None
        self._impression_url = None
        self._events = None
        self._pricing = None
        self.discriminator = None

        if ad_id is not None:
            self.ad_id = ad_id
        if creative_id is not None:
            self.creative_id = creative_id
        if flight_id is not None:
            self.flight_id = flight_id
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if priority_id is not None:
            self.priority_id = priority_id
        if click_url is not None:
            self.click_url = click_url
        if contents is not None:
            self.contents = contents
        if impression_url is not None:
            self.impression_url = impression_url
        if events is not None:
            self.events = events
        if pricing is not None:
            self.pricing = pricing

    @property
    def ad_id(self):
        """Gets the ad_id of this Decision.  # noqa: E501


        :return: The ad_id of this Decision.  # noqa: E501
        :rtype: int
        """
        return self._ad_id

    @ad_id.setter
    def ad_id(self, ad_id):
        """Sets the ad_id of this Decision.


        :param ad_id: The ad_id of this Decision.  # noqa: E501
        :type: int
        """

        self._ad_id = ad_id

    @property
    def creative_id(self):
        """Gets the creative_id of this Decision.  # noqa: E501


        :return: The creative_id of this Decision.  # noqa: E501
        :rtype: int
        """
        return self._creative_id

    @creative_id.setter
    def creative_id(self, creative_id):
        """Sets the creative_id of this Decision.


        :param creative_id: The creative_id of this Decision.  # noqa: E501
        :type: int
        """

        self._creative_id = creative_id

    @property
    def flight_id(self):
        """Gets the flight_id of this Decision.  # noqa: E501


        :return: The flight_id of this Decision.  # noqa: E501
        :rtype: int
        """
        return self._flight_id

    @flight_id.setter
    def flight_id(self, flight_id):
        """Sets the flight_id of this Decision.


        :param flight_id: The flight_id of this Decision.  # noqa: E501
        :type: int
        """

        self._flight_id = flight_id

    @property
    def campaign_id(self):
        """Gets the campaign_id of this Decision.  # noqa: E501


        :return: The campaign_id of this Decision.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this Decision.


        :param campaign_id: The campaign_id of this Decision.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def priority_id(self):
        """Gets the priority_id of this Decision.  # noqa: E501


        :return: The priority_id of this Decision.  # noqa: E501
        :rtype: int
        """
        return self._priority_id

    @priority_id.setter
    def priority_id(self, priority_id):
        """Sets the priority_id of this Decision.


        :param priority_id: The priority_id of this Decision.  # noqa: E501
        :type: int
        """

        self._priority_id = priority_id

    @property
    def click_url(self):
        """Gets the click_url of this Decision.  # noqa: E501


        :return: The click_url of this Decision.  # noqa: E501
        :rtype: str
        """
        return self._click_url

    @click_url.setter
    def click_url(self, click_url):
        """Sets the click_url of this Decision.


        :param click_url: The click_url of this Decision.  # noqa: E501
        :type: str
        """

        self._click_url = click_url

    @property
    def contents(self):
        """Gets the contents of this Decision.  # noqa: E501


        :return: The contents of this Decision.  # noqa: E501
        :rtype: list[Content]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this Decision.


        :param contents: The contents of this Decision.  # noqa: E501
        :type: list[Content]
        """

        self._contents = contents

    @property
    def impression_url(self):
        """Gets the impression_url of this Decision.  # noqa: E501


        :return: The impression_url of this Decision.  # noqa: E501
        :rtype: str
        """
        return self._impression_url

    @impression_url.setter
    def impression_url(self, impression_url):
        """Sets the impression_url of this Decision.


        :param impression_url: The impression_url of this Decision.  # noqa: E501
        :type: str
        """

        self._impression_url = impression_url

    @property
    def events(self):
        """Gets the events of this Decision.  # noqa: E501


        :return: The events of this Decision.  # noqa: E501
        :rtype: list[Event]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Decision.


        :param events: The events of this Decision.  # noqa: E501
        :type: list[Event]
        """

        self._events = events

    @property
    def pricing(self):
        """Gets the pricing of this Decision.  # noqa: E501


        :return: The pricing of this Decision.  # noqa: E501
        :rtype: PricingData
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this Decision.


        :param pricing: The pricing of this Decision.  # noqa: E501
        :type: PricingData
        """

        self._pricing = pricing

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
        if not isinstance(other, Decision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Decision):
            return True

        return self.to_dict() != other.to_dict()
