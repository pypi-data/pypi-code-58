# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetVpcEndpointResult:
    """
    A collection of values returned by getVpcEndpoint.
    """
    def __init__(__self__, cidr_blocks=None, dns_entries=None, filters=None, id=None, network_interface_ids=None, owner_id=None, policy=None, prefix_list_id=None, private_dns_enabled=None, requester_managed=None, route_table_ids=None, security_group_ids=None, service_name=None, state=None, subnet_ids=None, tags=None, vpc_endpoint_type=None, vpc_id=None):
        if cidr_blocks and not isinstance(cidr_blocks, list):
            raise TypeError("Expected argument 'cidr_blocks' to be a list")
        __self__.cidr_blocks = cidr_blocks
        """
        The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type `Gateway`.
        """
        if dns_entries and not isinstance(dns_entries, list):
            raise TypeError("Expected argument 'dns_entries' to be a list")
        __self__.dns_entries = dns_entries
        """
        The DNS entries for the VPC Endpoint. Applicable for endpoints of type `Interface`. DNS blocks are documented below.
        """
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        if network_interface_ids and not isinstance(network_interface_ids, list):
            raise TypeError("Expected argument 'network_interface_ids' to be a list")
        __self__.network_interface_ids = network_interface_ids
        """
        One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type `Interface`.
        """
        if owner_id and not isinstance(owner_id, str):
            raise TypeError("Expected argument 'owner_id' to be a str")
        __self__.owner_id = owner_id
        """
        The ID of the AWS account that owns the VPC endpoint.
        """
        if policy and not isinstance(policy, str):
            raise TypeError("Expected argument 'policy' to be a str")
        __self__.policy = policy
        """
        The policy document associated with the VPC Endpoint. Applicable for endpoints of type `Gateway`.
        """
        if prefix_list_id and not isinstance(prefix_list_id, str):
            raise TypeError("Expected argument 'prefix_list_id' to be a str")
        __self__.prefix_list_id = prefix_list_id
        """
        The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.
        """
        if private_dns_enabled and not isinstance(private_dns_enabled, bool):
            raise TypeError("Expected argument 'private_dns_enabled' to be a bool")
        __self__.private_dns_enabled = private_dns_enabled
        """
        Whether or not the VPC is associated with a private hosted zone - `true` or `false`. Applicable for endpoints of type `Interface`.
        """
        if requester_managed and not isinstance(requester_managed, bool):
            raise TypeError("Expected argument 'requester_managed' to be a bool")
        __self__.requester_managed = requester_managed
        """
        Whether or not the VPC Endpoint is being managed by its service - `true` or `false`.
        """
        if route_table_ids and not isinstance(route_table_ids, list):
            raise TypeError("Expected argument 'route_table_ids' to be a list")
        __self__.route_table_ids = route_table_ids
        """
        One or more route tables associated with the VPC Endpoint. Applicable for endpoints of type `Gateway`.
        """
        if security_group_ids and not isinstance(security_group_ids, list):
            raise TypeError("Expected argument 'security_group_ids' to be a list")
        __self__.security_group_ids = security_group_ids
        """
        One or more security groups associated with the network interfaces. Applicable for endpoints of type `Interface`.
        """
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        __self__.service_name = service_name
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        __self__.state = state
        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError("Expected argument 'subnet_ids' to be a list")
        __self__.subnet_ids = subnet_ids
        """
        One or more subnets in which the VPC Endpoint is located. Applicable for endpoints of type `Interface`.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        if vpc_endpoint_type and not isinstance(vpc_endpoint_type, str):
            raise TypeError("Expected argument 'vpc_endpoint_type' to be a str")
        __self__.vpc_endpoint_type = vpc_endpoint_type
        """
        The VPC Endpoint type, `Gateway` or `Interface`.
        """
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        __self__.vpc_id = vpc_id
class AwaitableGetVpcEndpointResult(GetVpcEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcEndpointResult(
            cidr_blocks=self.cidr_blocks,
            dns_entries=self.dns_entries,
            filters=self.filters,
            id=self.id,
            network_interface_ids=self.network_interface_ids,
            owner_id=self.owner_id,
            policy=self.policy,
            prefix_list_id=self.prefix_list_id,
            private_dns_enabled=self.private_dns_enabled,
            requester_managed=self.requester_managed,
            route_table_ids=self.route_table_ids,
            security_group_ids=self.security_group_ids,
            service_name=self.service_name,
            state=self.state,
            subnet_ids=self.subnet_ids,
            tags=self.tags,
            vpc_endpoint_type=self.vpc_endpoint_type,
            vpc_id=self.vpc_id)

def get_vpc_endpoint(filters=None,id=None,service_name=None,state=None,tags=None,vpc_id=None,opts=None):
    """
    The VPC Endpoint data source provides details about
    a specific VPC endpoint.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    s3 = aws.ec2.get_vpc_endpoint(service_name="com.amazonaws.us-west-2.s3",
        vpc_id=aws_vpc["foo"]["id"])
    private_s3 = aws.ec2.VpcEndpointRouteTableAssociation("privateS3",
        route_table_id=aws_route_table["private"]["id"],
        vpc_endpoint_id=s3.id)
    ```


    :param list filters: Custom filter block as described below.
    :param str id: The ID of the specific VPC Endpoint to retrieve.
    :param str service_name: The service name of the specific VPC Endpoint to retrieve. For AWS services the service name is usually in the form `com.amazonaws.<region>.<service>` (the SageMaker Notebook service is an exception to this rule, the service name is in the form `aws.sagemaker.<region>.notebook`).
    :param str state: The state of the specific VPC Endpoint to retrieve.
    :param dict tags: A map of tags, each pair of which must exactly match
           a pair on the specific VPC Endpoint to retrieve.
    :param str vpc_id: The ID of the VPC in which the specific VPC Endpoint is used.

    The **filters** object supports the following:

      * `name` (`str`) - The name of the field to filter by, as defined by
        [the underlying AWS API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.html).
      * `values` (`list`) - Set of values that are accepted for the given field.
        A VPC Endpoint will be selected if any one of the given values matches.
    """
    __args__ = dict()


    __args__['filters'] = filters
    __args__['id'] = id
    __args__['serviceName'] = service_name
    __args__['state'] = state
    __args__['tags'] = tags
    __args__['vpcId'] = vpc_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getVpcEndpoint:getVpcEndpoint', __args__, opts=opts).value

    return AwaitableGetVpcEndpointResult(
        cidr_blocks=__ret__.get('cidrBlocks'),
        dns_entries=__ret__.get('dnsEntries'),
        filters=__ret__.get('filters'),
        id=__ret__.get('id'),
        network_interface_ids=__ret__.get('networkInterfaceIds'),
        owner_id=__ret__.get('ownerId'),
        policy=__ret__.get('policy'),
        prefix_list_id=__ret__.get('prefixListId'),
        private_dns_enabled=__ret__.get('privateDnsEnabled'),
        requester_managed=__ret__.get('requesterManaged'),
        route_table_ids=__ret__.get('routeTableIds'),
        security_group_ids=__ret__.get('securityGroupIds'),
        service_name=__ret__.get('serviceName'),
        state=__ret__.get('state'),
        subnet_ids=__ret__.get('subnetIds'),
        tags=__ret__.get('tags'),
        vpc_endpoint_type=__ret__.get('vpcEndpointType'),
        vpc_id=__ret__.get('vpcId'))
