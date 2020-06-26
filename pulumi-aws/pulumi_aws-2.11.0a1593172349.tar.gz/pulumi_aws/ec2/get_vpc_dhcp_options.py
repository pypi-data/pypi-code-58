# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetVpcDhcpOptionsResult:
    """
    A collection of values returned by getVpcDhcpOptions.
    """
    def __init__(__self__, arn=None, dhcp_options_id=None, domain_name=None, domain_name_servers=None, filters=None, id=None, netbios_name_servers=None, netbios_node_type=None, ntp_servers=None, owner_id=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The ARN of the DHCP Options Set.
        """
        if dhcp_options_id and not isinstance(dhcp_options_id, str):
            raise TypeError("Expected argument 'dhcp_options_id' to be a str")
        __self__.dhcp_options_id = dhcp_options_id
        """
        EC2 DHCP Options ID
        """
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        __self__.domain_name = domain_name
        """
        The suffix domain name to used when resolving non Fully Qualified Domain Names. e.g. the `search` value in the `/etc/resolv.conf` file.
        """
        if domain_name_servers and not isinstance(domain_name_servers, list):
            raise TypeError("Expected argument 'domain_name_servers' to be a list")
        __self__.domain_name_servers = domain_name_servers
        """
        List of name servers.
        """
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if netbios_name_servers and not isinstance(netbios_name_servers, list):
            raise TypeError("Expected argument 'netbios_name_servers' to be a list")
        __self__.netbios_name_servers = netbios_name_servers
        """
        List of NETBIOS name servers.
        """
        if netbios_node_type and not isinstance(netbios_node_type, str):
            raise TypeError("Expected argument 'netbios_node_type' to be a str")
        __self__.netbios_node_type = netbios_node_type
        """
        The NetBIOS node type (1, 2, 4, or 8). For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).
        """
        if ntp_servers and not isinstance(ntp_servers, list):
            raise TypeError("Expected argument 'ntp_servers' to be a list")
        __self__.ntp_servers = ntp_servers
        """
        List of NTP servers.
        """
        if owner_id and not isinstance(owner_id, str):
            raise TypeError("Expected argument 'owner_id' to be a str")
        __self__.owner_id = owner_id
        """
        The ID of the AWS account that owns the DHCP options set.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A map of tags assigned to the resource.
        """
class AwaitableGetVpcDhcpOptionsResult(GetVpcDhcpOptionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcDhcpOptionsResult(
            arn=self.arn,
            dhcp_options_id=self.dhcp_options_id,
            domain_name=self.domain_name,
            domain_name_servers=self.domain_name_servers,
            filters=self.filters,
            id=self.id,
            netbios_name_servers=self.netbios_name_servers,
            netbios_node_type=self.netbios_node_type,
            ntp_servers=self.ntp_servers,
            owner_id=self.owner_id,
            tags=self.tags)

def get_vpc_dhcp_options(dhcp_options_id=None,filters=None,tags=None,opts=None):
    """
    Retrieve information about an EC2 DHCP Options configuration.

    ## Example Usage
    ### Lookup by DHCP Options ID

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2.get_vpc_dhcp_options(dhcp_options_id="dopts-12345678")
    ```
    ### Lookup by Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2.get_vpc_dhcp_options(filters=[
        {
            "name": "key",
            "values": ["domain-name"],
        },
        {
            "name": "value",
            "values": ["example.com"],
        },
    ])
    ```


    :param str dhcp_options_id: The EC2 DHCP Options ID.
    :param list filters: List of custom filters as described below.
    :param dict tags: A map of tags assigned to the resource.

    The **filters** object supports the following:

      * `name` (`str`) - The name of the field to filter.
      * `values` (`list`) - Set of values for filtering.
    """
    __args__ = dict()


    __args__['dhcpOptionsId'] = dhcp_options_id
    __args__['filters'] = filters
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getVpcDhcpOptions:getVpcDhcpOptions', __args__, opts=opts).value

    return AwaitableGetVpcDhcpOptionsResult(
        arn=__ret__.get('arn'),
        dhcp_options_id=__ret__.get('dhcpOptionsId'),
        domain_name=__ret__.get('domainName'),
        domain_name_servers=__ret__.get('domainNameServers'),
        filters=__ret__.get('filters'),
        id=__ret__.get('id'),
        netbios_name_servers=__ret__.get('netbiosNameServers'),
        netbios_node_type=__ret__.get('netbiosNodeType'),
        ntp_servers=__ret__.get('ntpServers'),
        owner_id=__ret__.get('ownerId'),
        tags=__ret__.get('tags'))
