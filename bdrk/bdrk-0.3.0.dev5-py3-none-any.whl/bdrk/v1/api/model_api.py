# coding: utf-8

"""
    Bedrock

    API documentation for Bedrock platform  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from bdrk.v1.api_client import ApiClient
from bdrk.v1.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ModelApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_artefact_details(self, model_id, artefact_id, project_id, **kwargs):  # noqa: E501
        """get_artefact_details  # noqa: E501

        Get artefact via model collection public id and artefact ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_artefact_details(model_id, artefact_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_id: public id of the model artefact collection (required)
        :param Int artefact_id: entity id of the model artefact (required)
        :param str project_id: Project ID of model. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ModelArtefactSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_artefact_details_with_http_info(model_id, artefact_id, project_id, **kwargs)  # noqa: E501

    def get_artefact_details_with_http_info(self, model_id, artefact_id, project_id, **kwargs):  # noqa: E501
        """get_artefact_details  # noqa: E501

        Get artefact via model collection public id and artefact ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_artefact_details_with_http_info(model_id, artefact_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_id: public id of the model artefact collection (required)
        :param Int artefact_id: entity id of the model artefact (required)
        :param str project_id: Project ID of model. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ModelArtefactSchema, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['model_id', 'artefact_id', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_artefact_details" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in local_var_params or
                local_var_params['model_id'] is None):
            raise ApiValueError("Missing the required parameter `model_id` when calling `get_artefact_details`")  # noqa: E501
        # verify the required parameter 'artefact_id' is set
        if ('artefact_id' not in local_var_params or
                local_var_params['artefact_id'] is None):
            raise ApiValueError("Missing the required parameter `artefact_id` when calling `get_artefact_details`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in local_var_params or
                local_var_params['project_id'] is None):
            raise ApiValueError("Missing the required parameter `project_id` when calling `get_artefact_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']  # noqa: E501
        if 'artefact_id' in local_var_params:
            path_params['artefact_id'] = local_var_params['artefact_id']  # noqa: E501

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessTokenAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/model/{model_id}/artefact/{artefact_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelArtefactSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_artefact_download_url(self, model_id, artefact_id, **kwargs):  # noqa: E501
        """get_artefact_download_url  # noqa: E501

        Gets signed URL for downloading the model artefact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_artefact_download_url(model_id, artefact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_id: public id of the model artefact collection (required)
        :param str artefact_id: entity id of the model artefact (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ArtefactDownloadUrlSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_artefact_download_url_with_http_info(model_id, artefact_id, **kwargs)  # noqa: E501

    def get_artefact_download_url_with_http_info(self, model_id, artefact_id, **kwargs):  # noqa: E501
        """get_artefact_download_url  # noqa: E501

        Gets signed URL for downloading the model artefact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_artefact_download_url_with_http_info(model_id, artefact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_id: public id of the model artefact collection (required)
        :param str artefact_id: entity id of the model artefact (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ArtefactDownloadUrlSchema, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['model_id', 'artefact_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_artefact_download_url" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in local_var_params or
                local_var_params['model_id'] is None):
            raise ApiValueError("Missing the required parameter `model_id` when calling `get_artefact_download_url`")  # noqa: E501
        # verify the required parameter 'artefact_id' is set
        if ('artefact_id' not in local_var_params or
                local_var_params['artefact_id'] is None):
            raise ApiValueError("Missing the required parameter `artefact_id` when calling `get_artefact_download_url`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']  # noqa: E501
        if 'artefact_id' in local_var_params:
            path_params['artefact_id'] = local_var_params['artefact_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessTokenAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/model/{model_id}/artefact/{artefact_id}/download_url', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArtefactDownloadUrlSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
