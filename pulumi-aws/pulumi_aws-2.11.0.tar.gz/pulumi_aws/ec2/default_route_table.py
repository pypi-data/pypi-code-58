# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class DefaultRouteTable(pulumi.CustomResource):
    default_route_table_id: pulumi.Output[str]
    """
    The ID of the Default Routing Table.
    """
    owner_id: pulumi.Output[str]
    """
    The ID of the AWS account that owns the route table
    """
    propagating_vgws: pulumi.Output[list]
    """
    A list of virtual gateways for propagation.
    """
    routes: pulumi.Output[list]
    """
    A list of route objects. Their keys are documented below.

      * `cidr_block` (`str`) - The CIDR block of the route.
      * `egress_only_gateway_id` (`str`) - Identifier of a VPC Egress Only Internet Gateway.
      * `gateway_id` (`str`) - Identifier of a VPC internet gateway or a virtual private gateway.
      * `instance_id` (`str`) - Identifier of an EC2 instance.
      * `ipv6_cidr_block` (`str`) - The Ipv6 CIDR block of the route
      * `nat_gateway_id` (`str`) - Identifier of a VPC NAT gateway.
      * `network_interface_id` (`str`) - Identifier of an EC2 network interface.
      * `transit_gateway_id` (`str`) - Identifier of an EC2 Transit Gateway.
      * `vpc_peering_connection_id` (`str`) - Identifier of a VPC peering connection.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    vpc_id: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, default_route_table_id=None, propagating_vgws=None, routes=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a resource to manage a Default VPC Routing Table.

        Each VPC created in AWS comes with a Default Route Table that can be managed, but not
        destroyed. **This is an advanced resource**, and has special caveats to be aware
        of when using it. Please read this document in its entirety before using this
        resource. It is recommended you **do not** use both `ec2.DefaultRouteTable` to
        manage the default route table **and** use the `ec2.MainRouteTableAssociation`,
        due to possible conflict in routes.

        The `ec2.DefaultRouteTable` behaves differently from normal resources, in that
        this provider does not _create_ this resource, but instead attempts to "adopt" it
        into management. We can do this because each VPC created has a Default Route
        Table that cannot be destroyed, and is created with a single route.

        When this provider first adopts the Default Route Table, it **immediately removes all
        defined routes**. It then proceeds to create any routes specified in the
        configuration. This step is required so that only the routes specified in the
        configuration present in the Default Route Table.

        For more information about Route Tables, see the AWS Documentation on
        [Route Tables][aws-route-tables].

        For more information about managing normal Route Tables in this provider, see our
        documentation on [ec2.RouteTable][tf-route-tables].

        > **NOTE on Route Tables and Routes:** This provider currently
        provides both a standalone Route resource and a Route Table resource with routes
        defined in-line. At this time you cannot use a Route Table with in-line routes
        in conjunction with any Route resources. Doing so will cause
        a conflict of rule settings and will overwrite routes.

        ## Example Usage
        ### With Tags

        ```python
        import pulumi
        import pulumi_aws as aws

        default_route_table = aws.ec2.DefaultRouteTable("defaultRouteTable",
            default_route_table_id=aws_vpc["foo"]["default_route_table_id"],
            routes=[{}],
            tags={
                "Name": "default table",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_route_table_id: The ID of the Default Routing Table.
        :param pulumi.Input[list] propagating_vgws: A list of virtual gateways for propagation.
        :param pulumi.Input[list] routes: A list of route objects. Their keys are documented below.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.

        The **routes** object supports the following:

          * `cidr_block` (`pulumi.Input[str]`) - The CIDR block of the route.
          * `egress_only_gateway_id` (`pulumi.Input[str]`) - Identifier of a VPC Egress Only Internet Gateway.
          * `gateway_id` (`pulumi.Input[str]`) - Identifier of a VPC internet gateway or a virtual private gateway.
          * `instance_id` (`pulumi.Input[str]`) - Identifier of an EC2 instance.
          * `ipv6_cidr_block` (`pulumi.Input[str]`) - The Ipv6 CIDR block of the route
          * `nat_gateway_id` (`pulumi.Input[str]`) - Identifier of a VPC NAT gateway.
          * `network_interface_id` (`pulumi.Input[str]`) - Identifier of an EC2 network interface.
          * `transit_gateway_id` (`pulumi.Input[str]`) - Identifier of an EC2 Transit Gateway.
          * `vpc_peering_connection_id` (`pulumi.Input[str]`) - Identifier of a VPC peering connection.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if default_route_table_id is None:
                raise TypeError("Missing required property 'default_route_table_id'")
            __props__['default_route_table_id'] = default_route_table_id
            __props__['propagating_vgws'] = propagating_vgws
            __props__['routes'] = routes
            __props__['tags'] = tags
            __props__['owner_id'] = None
            __props__['vpc_id'] = None
        super(DefaultRouteTable, __self__).__init__(
            'aws:ec2/defaultRouteTable:DefaultRouteTable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, default_route_table_id=None, owner_id=None, propagating_vgws=None, routes=None, tags=None, vpc_id=None):
        """
        Get an existing DefaultRouteTable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_route_table_id: The ID of the Default Routing Table.
        :param pulumi.Input[str] owner_id: The ID of the AWS account that owns the route table
        :param pulumi.Input[list] propagating_vgws: A list of virtual gateways for propagation.
        :param pulumi.Input[list] routes: A list of route objects. Their keys are documented below.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.

        The **routes** object supports the following:

          * `cidr_block` (`pulumi.Input[str]`) - The CIDR block of the route.
          * `egress_only_gateway_id` (`pulumi.Input[str]`) - Identifier of a VPC Egress Only Internet Gateway.
          * `gateway_id` (`pulumi.Input[str]`) - Identifier of a VPC internet gateway or a virtual private gateway.
          * `instance_id` (`pulumi.Input[str]`) - Identifier of an EC2 instance.
          * `ipv6_cidr_block` (`pulumi.Input[str]`) - The Ipv6 CIDR block of the route
          * `nat_gateway_id` (`pulumi.Input[str]`) - Identifier of a VPC NAT gateway.
          * `network_interface_id` (`pulumi.Input[str]`) - Identifier of an EC2 network interface.
          * `transit_gateway_id` (`pulumi.Input[str]`) - Identifier of an EC2 Transit Gateway.
          * `vpc_peering_connection_id` (`pulumi.Input[str]`) - Identifier of a VPC peering connection.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["default_route_table_id"] = default_route_table_id
        __props__["owner_id"] = owner_id
        __props__["propagating_vgws"] = propagating_vgws
        __props__["routes"] = routes
        __props__["tags"] = tags
        __props__["vpc_id"] = vpc_id
        return DefaultRouteTable(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
