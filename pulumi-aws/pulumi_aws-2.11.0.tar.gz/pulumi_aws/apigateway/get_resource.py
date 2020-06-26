# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetResourceResult:
    """
    A collection of values returned by getResource.
    """
    def __init__(__self__, id=None, parent_id=None, path=None, path_part=None, rest_api_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if parent_id and not isinstance(parent_id, str):
            raise TypeError("Expected argument 'parent_id' to be a str")
        __self__.parent_id = parent_id
        """
        Set to the ID of the parent Resource.
        """
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        __self__.path = path
        if path_part and not isinstance(path_part, str):
            raise TypeError("Expected argument 'path_part' to be a str")
        __self__.path_part = path_part
        """
        Set to the path relative to the parent Resource.
        """
        if rest_api_id and not isinstance(rest_api_id, str):
            raise TypeError("Expected argument 'rest_api_id' to be a str")
        __self__.rest_api_id = rest_api_id
class AwaitableGetResourceResult(GetResourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceResult(
            id=self.id,
            parent_id=self.parent_id,
            path=self.path,
            path_part=self.path_part,
            rest_api_id=self.rest_api_id)

def get_resource(path=None,rest_api_id=None,opts=None):
    """
    Use this data source to get the id of a Resource in API Gateway.
    To fetch the Resource, you must provide the REST API id as well as the full path.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    my_rest_api = aws.apigateway.get_rest_api(name="my-rest-api")
    my_resource = aws.apigateway.get_resource(path="/endpoint/path",
        rest_api_id=my_rest_api.id)
    ```


    :param str path: The full path of the resource.  If no path is found, an error will be returned.
    :param str rest_api_id: The REST API id that owns the resource. If no REST API is found, an error will be returned.
    """
    __args__ = dict()


    __args__['path'] = path
    __args__['restApiId'] = rest_api_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:apigateway/getResource:getResource', __args__, opts=opts).value

    return AwaitableGetResourceResult(
        id=__ret__.get('id'),
        parent_id=__ret__.get('parentId'),
        path=__ret__.get('path'),
        path_part=__ret__.get('pathPart'),
        rest_api_id=__ret__.get('restApiId'))
