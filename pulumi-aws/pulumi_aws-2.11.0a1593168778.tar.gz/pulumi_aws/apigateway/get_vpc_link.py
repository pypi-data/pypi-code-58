# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetVpcLinkResult:
    """
    A collection of values returned by getVpcLink.
    """
    def __init__(__self__, description=None, id=None, name=None, status=None, status_message=None, tags=None, target_arns=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the VPC link.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        Set to the ID of the found API Gateway VPC Link.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        __self__.status = status
        """
        The status of the VPC link.
        """
        if status_message and not isinstance(status_message, str):
            raise TypeError("Expected argument 'status_message' to be a str")
        __self__.status_message = status_message
        """
        The status message of the VPC link.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        Key-value map of resource tags
        """
        if target_arns and not isinstance(target_arns, list):
            raise TypeError("Expected argument 'target_arns' to be a list")
        __self__.target_arns = target_arns
        """
        The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.
        """
class AwaitableGetVpcLinkResult(GetVpcLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcLinkResult(
            description=self.description,
            id=self.id,
            name=self.name,
            status=self.status,
            status_message=self.status_message,
            tags=self.tags,
            target_arns=self.target_arns)

def get_vpc_link(name=None,tags=None,opts=None):
    """
    Use this data source to get the id of a VPC Link in
    API Gateway. To fetch the VPC Link you must provide a name to match against.
    As there is no unique name constraint on API Gateway VPC Links this data source will
    error if there is more than one match.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    my_api_gateway_vpc_link = aws.apigateway.get_vpc_link(name="my-vpc-link")
    ```


    :param str name: The name of the API Gateway VPC Link to look up. If no API Gateway VPC Link is found with this name, an error will be returned. 
           If multiple API Gateway VPC Links are found with this name, an error will be returned.
    :param dict tags: Key-value map of resource tags
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:apigateway/getVpcLink:getVpcLink', __args__, opts=opts).value

    return AwaitableGetVpcLinkResult(
        description=__ret__.get('description'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        status=__ret__.get('status'),
        status_message=__ret__.get('statusMessage'),
        tags=__ret__.get('tags'),
        target_arns=__ret__.get('targetArns'))
