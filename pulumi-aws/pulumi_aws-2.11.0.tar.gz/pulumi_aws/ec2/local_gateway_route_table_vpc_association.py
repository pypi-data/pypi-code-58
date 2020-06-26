# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class LocalGatewayRouteTableVpcAssociation(pulumi.CustomResource):
    local_gateway_id: pulumi.Output[str]
    local_gateway_route_table_id: pulumi.Output[str]
    """
    Identifier of EC2 Local Gateway Route Table.
    """
    tags: pulumi.Output[dict]
    """
    Key-value map of resource tags.
    """
    vpc_id: pulumi.Output[str]
    """
    Identifier of EC2 VPC.
    """
    def __init__(__self__, resource_name, opts=None, local_gateway_route_table_id=None, tags=None, vpc_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an EC2 Local Gateway Route Table VPC Association. More information can be found in the [Outposts User Guide](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#vpc-associations).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_local_gateway_route_table = aws.ec2.get_local_gateway_route_table(outpost_arn="arn:aws:outposts:us-west-2:123456789012:outpost/op-1234567890abcdef")
        example_vpc = aws.ec2.Vpc("exampleVpc", cidr_block="10.0.0.0/16")
        example_local_gateway_route_table_vpc_association = aws.ec2.LocalGatewayRouteTableVpcAssociation("exampleLocalGatewayRouteTableVpcAssociation",
            local_gateway_route_table_id=example_local_gateway_route_table.id,
            vpc_id=example_vpc.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] local_gateway_route_table_id: Identifier of EC2 Local Gateway Route Table.
        :param pulumi.Input[dict] tags: Key-value map of resource tags.
        :param pulumi.Input[str] vpc_id: Identifier of EC2 VPC.
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

            if local_gateway_route_table_id is None:
                raise TypeError("Missing required property 'local_gateway_route_table_id'")
            __props__['local_gateway_route_table_id'] = local_gateway_route_table_id
            __props__['tags'] = tags
            if vpc_id is None:
                raise TypeError("Missing required property 'vpc_id'")
            __props__['vpc_id'] = vpc_id
            __props__['local_gateway_id'] = None
        super(LocalGatewayRouteTableVpcAssociation, __self__).__init__(
            'aws:ec2/localGatewayRouteTableVpcAssociation:LocalGatewayRouteTableVpcAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, local_gateway_id=None, local_gateway_route_table_id=None, tags=None, vpc_id=None):
        """
        Get an existing LocalGatewayRouteTableVpcAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] local_gateway_route_table_id: Identifier of EC2 Local Gateway Route Table.
        :param pulumi.Input[dict] tags: Key-value map of resource tags.
        :param pulumi.Input[str] vpc_id: Identifier of EC2 VPC.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["local_gateway_id"] = local_gateway_id
        __props__["local_gateway_route_table_id"] = local_gateway_route_table_id
        __props__["tags"] = tags
        __props__["vpc_id"] = vpc_id
        return LocalGatewayRouteTableVpcAssociation(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
