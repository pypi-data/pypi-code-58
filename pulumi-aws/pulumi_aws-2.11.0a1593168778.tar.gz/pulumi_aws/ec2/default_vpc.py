# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class DefaultVpc(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of VPC
    """
    assign_generated_ipv6_cidr_block: pulumi.Output[bool]
    """
    Whether or not an Amazon-provided IPv6 CIDR
    block with a /56 prefix length for the VPC was assigned
    """
    cidr_block: pulumi.Output[str]
    """
    The CIDR block of the VPC
    """
    default_network_acl_id: pulumi.Output[str]
    """
    The ID of the network ACL created by default on VPC creation
    """
    default_route_table_id: pulumi.Output[str]
    """
    The ID of the route table created by default on VPC creation
    """
    default_security_group_id: pulumi.Output[str]
    """
    The ID of the security group created by default on VPC creation
    """
    dhcp_options_id: pulumi.Output[str]
    enable_classiclink: pulumi.Output[bool]
    """
    A boolean flag to enable/disable ClassicLink
    for the VPC. Only valid in regions and accounts that support EC2 Classic.
    See the [ClassicLink documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html) for more information. Defaults false.
    """
    enable_classiclink_dns_support: pulumi.Output[bool]
    enable_dns_hostnames: pulumi.Output[bool]
    """
    A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
    """
    enable_dns_support: pulumi.Output[bool]
    """
    A boolean flag to enable/disable DNS support in the VPC. Defaults true.
    """
    instance_tenancy: pulumi.Output[str]
    """
    Tenancy of instances spin up within VPC.
    """
    ipv6_association_id: pulumi.Output[str]
    """
    The association ID for the IPv6 CIDR block of the VPC
    """
    ipv6_cidr_block: pulumi.Output[str]
    """
    The IPv6 CIDR block of the VPC
    """
    main_route_table_id: pulumi.Output[str]
    """
    The ID of the main route table associated with
    this VPC. Note that you can change a VPC's main route table by using an
    `ec2.MainRouteTableAssociation`
    """
    owner_id: pulumi.Output[str]
    """
    The ID of the AWS account that owns the VPC.
    """
    tags: pulumi.Output[dict]
    """
    A map of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, enable_classiclink=None, enable_classiclink_dns_support=None, enable_dns_hostnames=None, enable_dns_support=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a resource to manage the [default AWS VPC](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/default-vpc.html)
        in the current region.

        For AWS accounts created after 2013-12-04, each region comes with a Default VPC.
        **This is an advanced resource**, and has special caveats to be aware of when
        using it. Please read this document in its entirety before using this resource.

        The `ec2.DefaultVpc` behaves differently from normal resources, in that
        this provider does not _create_ this resource, but instead "adopts" it
        into management.

        ## Example Usage

        Basic usage with tags:

        ```python
        import pulumi
        import pulumi_aws as aws

        default = aws.ec2.DefaultVpc("default", tags={
            "Name": "Default VPC",
        })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_classiclink: A boolean flag to enable/disable ClassicLink
               for the VPC. Only valid in regions and accounts that support EC2 Classic.
               See the [ClassicLink documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html) for more information. Defaults false.
        :param pulumi.Input[bool] enable_dns_hostnames: A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
        :param pulumi.Input[bool] enable_dns_support: A boolean flag to enable/disable DNS support in the VPC. Defaults true.
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.
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

            __props__['enable_classiclink'] = enable_classiclink
            __props__['enable_classiclink_dns_support'] = enable_classiclink_dns_support
            __props__['enable_dns_hostnames'] = enable_dns_hostnames
            __props__['enable_dns_support'] = enable_dns_support
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['assign_generated_ipv6_cidr_block'] = None
            __props__['cidr_block'] = None
            __props__['default_network_acl_id'] = None
            __props__['default_route_table_id'] = None
            __props__['default_security_group_id'] = None
            __props__['dhcp_options_id'] = None
            __props__['instance_tenancy'] = None
            __props__['ipv6_association_id'] = None
            __props__['ipv6_cidr_block'] = None
            __props__['main_route_table_id'] = None
            __props__['owner_id'] = None
        super(DefaultVpc, __self__).__init__(
            'aws:ec2/defaultVpc:DefaultVpc',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, assign_generated_ipv6_cidr_block=None, cidr_block=None, default_network_acl_id=None, default_route_table_id=None, default_security_group_id=None, dhcp_options_id=None, enable_classiclink=None, enable_classiclink_dns_support=None, enable_dns_hostnames=None, enable_dns_support=None, instance_tenancy=None, ipv6_association_id=None, ipv6_cidr_block=None, main_route_table_id=None, owner_id=None, tags=None):
        """
        Get an existing DefaultVpc resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of VPC
        :param pulumi.Input[bool] assign_generated_ipv6_cidr_block: Whether or not an Amazon-provided IPv6 CIDR
               block with a /56 prefix length for the VPC was assigned
        :param pulumi.Input[str] cidr_block: The CIDR block of the VPC
        :param pulumi.Input[str] default_network_acl_id: The ID of the network ACL created by default on VPC creation
        :param pulumi.Input[str] default_route_table_id: The ID of the route table created by default on VPC creation
        :param pulumi.Input[str] default_security_group_id: The ID of the security group created by default on VPC creation
        :param pulumi.Input[bool] enable_classiclink: A boolean flag to enable/disable ClassicLink
               for the VPC. Only valid in regions and accounts that support EC2 Classic.
               See the [ClassicLink documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html) for more information. Defaults false.
        :param pulumi.Input[bool] enable_dns_hostnames: A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
        :param pulumi.Input[bool] enable_dns_support: A boolean flag to enable/disable DNS support in the VPC. Defaults true.
        :param pulumi.Input[str] instance_tenancy: Tenancy of instances spin up within VPC.
        :param pulumi.Input[str] ipv6_association_id: The association ID for the IPv6 CIDR block of the VPC
        :param pulumi.Input[str] ipv6_cidr_block: The IPv6 CIDR block of the VPC
        :param pulumi.Input[str] main_route_table_id: The ID of the main route table associated with
               this VPC. Note that you can change a VPC's main route table by using an
               `ec2.MainRouteTableAssociation`
        :param pulumi.Input[str] owner_id: The ID of the AWS account that owns the VPC.
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["assign_generated_ipv6_cidr_block"] = assign_generated_ipv6_cidr_block
        __props__["cidr_block"] = cidr_block
        __props__["default_network_acl_id"] = default_network_acl_id
        __props__["default_route_table_id"] = default_route_table_id
        __props__["default_security_group_id"] = default_security_group_id
        __props__["dhcp_options_id"] = dhcp_options_id
        __props__["enable_classiclink"] = enable_classiclink
        __props__["enable_classiclink_dns_support"] = enable_classiclink_dns_support
        __props__["enable_dns_hostnames"] = enable_dns_hostnames
        __props__["enable_dns_support"] = enable_dns_support
        __props__["instance_tenancy"] = instance_tenancy
        __props__["ipv6_association_id"] = ipv6_association_id
        __props__["ipv6_cidr_block"] = ipv6_cidr_block
        __props__["main_route_table_id"] = main_route_table_id
        __props__["owner_id"] = owner_id
        __props__["tags"] = tags
        return DefaultVpc(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
