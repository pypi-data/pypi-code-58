# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from properly_model_python.search_models.models.base_model_ import Model
from properly_model_python.search_models import util
from properly_model_python.search_models.models.person import Person
from properly_model_python.search_models.models.simple_listing import SimpleListing
from properly_model_python.search_models.models.search import Search


class SearchNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str = None, searcher: Person = None, search: Search = None, new_results: List[SimpleListing] = None, changed_results: List[SimpleListing] = None, unsubscribe_url: str = None):  # noqa: E501
        """SearchNotification - a model defined in Swagger

        :param id: The id of this SearchNotification.  # noqa: E501
        :type id: str
        :param searcher: The searcher of this SearchNotification.  # noqa: E501
        :type searcher: Person
        :param search: The search of this SearchNotification.  # noqa: E501
        :type search: Search
        :param new_results: The new_results of this SearchNotification.  # noqa: E501
        :type new_results: List[SimpleListing]
        :param changed_results: The changed_results of this SearchNotification.  # noqa: E501
        :type changed_results: List[SimpleListing]
        :param unsubscribe_url: The unsubscribe_url of this SearchNotification.  # noqa: E501
        :type unsubscribe_url: str
        """
        self.swagger_types = {
            'id': str,
            'searcher': Person,
            'search': Search,
            'new_results': List[SimpleListing],
            'changed_results': List[SimpleListing],
            'unsubscribe_url': str
        }

        self.attribute_map = {
            'id': 'id',
            'searcher': 'searcher',
            'search': 'search',
            'new_results': 'newResults',
            'changed_results': 'changedResults',
            'unsubscribe_url': 'unsubscribeUrl'
        }

        self._id = id
        self._searcher = searcher
        self._search = search
        self._new_results = new_results
        self._changed_results = changed_results
        self._unsubscribe_url = unsubscribe_url

    @classmethod
    def from_dict(cls, dikt) -> 'SearchNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SearchNotification of this SearchNotification.  # noqa: E501
        :rtype: SearchNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this SearchNotification.

        identifies the difference notification  # noqa: E501

        :return: The id of this SearchNotification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SearchNotification.

        identifies the difference notification  # noqa: E501

        :param id: The id of this SearchNotification.
        :type id: str
        """

        self._id = id

    @property
    def searcher(self) -> Person:
        """Gets the searcher of this SearchNotification.


        :return: The searcher of this SearchNotification.
        :rtype: Person
        """
        return self._searcher

    @searcher.setter
    def searcher(self, searcher: Person):
        """Sets the searcher of this SearchNotification.


        :param searcher: The searcher of this SearchNotification.
        :type searcher: Person
        """

        self._searcher = searcher

    @property
    def search(self) -> Search:
        """Gets the search of this SearchNotification.


        :return: The search of this SearchNotification.
        :rtype: Search
        """
        return self._search

    @search.setter
    def search(self, search: Search):
        """Sets the search of this SearchNotification.


        :param search: The search of this SearchNotification.
        :type search: Search
        """

        self._search = search

    @property
    def new_results(self) -> List[SimpleListing]:
        """Gets the new_results of this SearchNotification.


        :return: The new_results of this SearchNotification.
        :rtype: List[SimpleListing]
        """
        return self._new_results

    @new_results.setter
    def new_results(self, new_results: List[SimpleListing]):
        """Sets the new_results of this SearchNotification.


        :param new_results: The new_results of this SearchNotification.
        :type new_results: List[SimpleListing]
        """

        self._new_results = new_results

    @property
    def changed_results(self) -> List[SimpleListing]:
        """Gets the changed_results of this SearchNotification.


        :return: The changed_results of this SearchNotification.
        :rtype: List[SimpleListing]
        """
        return self._changed_results

    @changed_results.setter
    def changed_results(self, changed_results: List[SimpleListing]):
        """Sets the changed_results of this SearchNotification.


        :param changed_results: The changed_results of this SearchNotification.
        :type changed_results: List[SimpleListing]
        """

        self._changed_results = changed_results

    @property
    def unsubscribe_url(self) -> str:
        """Gets the unsubscribe_url of this SearchNotification.

        A url which will unsubscribe the authenicated user from the search.  # noqa: E501

        :return: The unsubscribe_url of this SearchNotification.
        :rtype: str
        """
        return self._unsubscribe_url

    @unsubscribe_url.setter
    def unsubscribe_url(self, unsubscribe_url: str):
        """Sets the unsubscribe_url of this SearchNotification.

        A url which will unsubscribe the authenicated user from the search.  # noqa: E501

        :param unsubscribe_url: The unsubscribe_url of this SearchNotification.
        :type unsubscribe_url: str
        """

        self._unsubscribe_url = unsubscribe_url
