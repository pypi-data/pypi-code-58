# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetAddressResult:
    """
    A collection of values returned by getAddress.
    """
    def __init__(__self__, address=None, id=None, name=None, project=None, region=None, self_link=None, status=None):
        if address and not isinstance(address, str):
            raise TypeError("Expected argument 'address' to be a str")
        __self__.address = address
        """
        The IP of the created resource.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        __self__.project = project
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        __self__.self_link = self_link
        """
        The URI of the created resource.
        """
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        __self__.status = status
        """
        Indicates if the address is used. Possible values are: RESERVED or IN_USE.
        """
class AwaitableGetAddressResult(GetAddressResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAddressResult(
            address=self.address,
            id=self.id,
            name=self.name,
            project=self.project,
            region=self.region,
            self_link=self.self_link,
            status=self.status)

def get_address(name=None,project=None,region=None,opts=None):
    """
    Get the IP address from a static address. For more information see
    the official [API](https://cloud.google.com/compute/docs/reference/latest/addresses/get) documentation.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_address = gcp.compute.get_address(name="foobar")
    prod = gcp.dns.ManagedZone("prod", dns_name="prod.mydomain.com.")
    frontend = gcp.dns.RecordSet("frontend",
        type="A",
        ttl=300,
        managed_zone=prod.name,
        rrdatas=[my_address.address])
    ```


    :param str name: A unique name for the resource, required by GCE.
    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str region: The Region in which the created address reside.
           If it is not provided, the provider region is used.
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['project'] = project
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:compute/getAddress:getAddress', __args__, opts=opts).value

    return AwaitableGetAddressResult(
        address=__ret__.get('address'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        project=__ret__.get('project'),
        region=__ret__.get('region'),
        self_link=__ret__.get('selfLink'),
        status=__ret__.get('status'))
