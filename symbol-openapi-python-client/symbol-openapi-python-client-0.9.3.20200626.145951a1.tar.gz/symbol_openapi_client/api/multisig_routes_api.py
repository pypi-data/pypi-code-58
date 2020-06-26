# coding: utf-8

"""
    ****************************************************************************
    Copyright (c) 2016-present,
    Jaguar0625, gimre, BloodyRookie, Tech Bureau, Corp. All rights reserved.

    This file is part of Catapult.

    Catapult is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Catapult is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with Catapult. If not, see <http://www.gnu.org/licenses/>.
    ****************************************************************************
    
    Catapult REST Endpoints
    OpenAPI Specification of catapult-rest 1.1.2  # noqa: E501
    The version of the OpenAPI document: 0.9.3
    Contact: contact@nem.foundation

    NOTE: This file is auto generated by Symbol OpenAPI Generator:
    https://github.com/nemtech/symbol-openapi-generator
    Do not edit this file manually.
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from symbol_openapi_client.api_client import ApiClient
from symbol_openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class MultisigRoutesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_account_multisig(self, address, **kwargs):  # noqa: E501
        """Get multisig account information  # noqa: E501

        Returns the multisig account information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_multisig(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str address: Account address. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: MultisigAccountInfoDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_account_multisig_with_http_info(address, **kwargs)  # noqa: E501

    def get_account_multisig_with_http_info(self, address, **kwargs):  # noqa: E501
        """Get multisig account information  # noqa: E501

        Returns the multisig account information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_multisig_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str address: Account address. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(MultisigAccountInfoDTO, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'address'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_multisig" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'address' is set
        if self.api_client.client_side_validation and ('address' not in local_var_params or  # noqa: E501
                                                        local_var_params['address'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `address` when calling `get_account_multisig`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in local_var_params:
            path_params['address'] = local_var_params['address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/account/{address}/multisig', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MultisigAccountInfoDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_account_multisig_graph(self, address, **kwargs):  # noqa: E501
        """Get multisig account graph information  # noqa: E501

        Returns the multisig account graph.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_multisig_graph(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str address: Account address. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[MultisigAccountGraphInfoDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_account_multisig_graph_with_http_info(address, **kwargs)  # noqa: E501

    def get_account_multisig_graph_with_http_info(self, address, **kwargs):  # noqa: E501
        """Get multisig account graph information  # noqa: E501

        Returns the multisig account graph.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_multisig_graph_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str address: Account address. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[MultisigAccountGraphInfoDTO], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'address'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_multisig_graph" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'address' is set
        if self.api_client.client_side_validation and ('address' not in local_var_params or  # noqa: E501
                                                        local_var_params['address'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `address` when calling `get_account_multisig_graph`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in local_var_params:
            path_params['address'] = local_var_params['address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/account/{address}/multisig/graph', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MultisigAccountGraphInfoDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
