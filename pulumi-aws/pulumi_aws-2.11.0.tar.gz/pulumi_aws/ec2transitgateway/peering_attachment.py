# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class PeeringAttachment(pulumi.CustomResource):
    peer_account_id: pulumi.Output[str]
    """
    Account ID of EC2 Transit Gateway to peer with. Defaults to the account ID the current provider is currently connected to.
    """
    peer_region: pulumi.Output[str]
    """
    Region of EC2 Transit Gateway to peer with.
    """
    peer_transit_gateway_id: pulumi.Output[str]
    """
    Identifier of EC2 Transit Gateway to peer with.
    """
    tags: pulumi.Output[dict]
    """
    Key-value tags for the EC2 Transit Gateway Peering Attachment.
    """
    transit_gateway_id: pulumi.Output[str]
    """
    Identifier of EC2 Transit Gateway.
    """
    def __init__(__self__, resource_name, opts=None, peer_account_id=None, peer_region=None, peer_transit_gateway_id=None, tags=None, transit_gateway_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an EC2 Transit Gateway Peering Attachment.
        For examples of custom route table association and propagation, see the [EC2 Transit Gateway Networking Examples Guide](https://docs.aws.amazon.com/vpc/latest/tgw/TGW_Scenarios.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_pulumi as pulumi

        local = pulumi.providers.Aws("local", region="us-east-1")
        peer = pulumi.providers.Aws("peer", region="us-west-2")
        peer_region = aws.get_region()
        local_transit_gateway = aws.ec2transitgateway.TransitGateway("localTransitGateway", tags={
            "Name": "Local TGW",
        })
        peer_transit_gateway = aws.ec2transitgateway.TransitGateway("peerTransitGateway", tags={
            "Name": "Peer TGW",
        })
        example = aws.ec2transitgateway.PeeringAttachment("example",
            peer_account_id=peer_transit_gateway.owner_id,
            peer_region=peer_region.name,
            peer_transit_gateway_id=peer_transit_gateway.id,
            transit_gateway_id=local_transit_gateway.id,
            tags={
                "Name": "TGW Peering Requestor",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] peer_account_id: Account ID of EC2 Transit Gateway to peer with. Defaults to the account ID the current provider is currently connected to.
        :param pulumi.Input[str] peer_region: Region of EC2 Transit Gateway to peer with.
        :param pulumi.Input[str] peer_transit_gateway_id: Identifier of EC2 Transit Gateway to peer with.
        :param pulumi.Input[dict] tags: Key-value tags for the EC2 Transit Gateway Peering Attachment.
        :param pulumi.Input[str] transit_gateway_id: Identifier of EC2 Transit Gateway.
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

            __props__['peer_account_id'] = peer_account_id
            if peer_region is None:
                raise TypeError("Missing required property 'peer_region'")
            __props__['peer_region'] = peer_region
            if peer_transit_gateway_id is None:
                raise TypeError("Missing required property 'peer_transit_gateway_id'")
            __props__['peer_transit_gateway_id'] = peer_transit_gateway_id
            __props__['tags'] = tags
            if transit_gateway_id is None:
                raise TypeError("Missing required property 'transit_gateway_id'")
            __props__['transit_gateway_id'] = transit_gateway_id
        super(PeeringAttachment, __self__).__init__(
            'aws:ec2transitgateway/peeringAttachment:PeeringAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, peer_account_id=None, peer_region=None, peer_transit_gateway_id=None, tags=None, transit_gateway_id=None):
        """
        Get an existing PeeringAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] peer_account_id: Account ID of EC2 Transit Gateway to peer with. Defaults to the account ID the current provider is currently connected to.
        :param pulumi.Input[str] peer_region: Region of EC2 Transit Gateway to peer with.
        :param pulumi.Input[str] peer_transit_gateway_id: Identifier of EC2 Transit Gateway to peer with.
        :param pulumi.Input[dict] tags: Key-value tags for the EC2 Transit Gateway Peering Attachment.
        :param pulumi.Input[str] transit_gateway_id: Identifier of EC2 Transit Gateway.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["peer_account_id"] = peer_account_id
        __props__["peer_region"] = peer_region
        __props__["peer_transit_gateway_id"] = peer_transit_gateway_id
        __props__["tags"] = tags
        __props__["transit_gateway_id"] = transit_gateway_id
        return PeeringAttachment(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
