# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class ZoneVirtualNetworkLink(pulumi.CustomResource):
    name: pulumi.Output[str]
    """
    The name of the Private DNS Zone Virtual Network Link. Changing this forces a new resource to be created.
    """
    private_dns_zone_name: pulumi.Output[str]
    """
    The name of the Private DNS zone (without a terminating dot). Changing this forces a new resource to be created.
    """
    registration_enabled: pulumi.Output[bool]
    """
    Is auto-registration of virtual machine records in the virtual network in the Private DNS zone enabled? Defaults to `false`.
    """
    resource_group_name: pulumi.Output[str]
    """
    Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    virtual_network_id: pulumi.Output[str]
    """
    The Resource ID of the Virtual Network that should be linked to the DNS Zone. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, name=None, private_dns_zone_name=None, registration_enabled=None, resource_group_name=None, tags=None, virtual_network_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Enables you to manage Private DNS zone Virtual Network Links. These Links enable DNS resolution and registration inside Azure Virtual Networks using Azure Private DNS.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West US")
        example_zone = azure.privatedns.Zone("exampleZone", resource_group_name=example_resource_group.name)
        example_zone_virtual_network_link = azure.privatedns.ZoneVirtualNetworkLink("exampleZoneVirtualNetworkLink",
            resource_group_name=example_resource_group.name,
            private_dns_zone_name=example_zone.name,
            virtual_network_id=azurerm_virtual_network["example"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the Private DNS Zone Virtual Network Link. Changing this forces a new resource to be created.
        :param pulumi.Input[str] private_dns_zone_name: The name of the Private DNS zone (without a terminating dot). Changing this forces a new resource to be created.
        :param pulumi.Input[bool] registration_enabled: Is auto-registration of virtual machine records in the virtual network in the Private DNS zone enabled? Defaults to `false`.
        :param pulumi.Input[str] resource_group_name: Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] virtual_network_id: The Resource ID of the Virtual Network that should be linked to the DNS Zone. Changing this forces a new resource to be created.
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

            __props__['name'] = name
            if private_dns_zone_name is None:
                raise TypeError("Missing required property 'private_dns_zone_name'")
            __props__['private_dns_zone_name'] = private_dns_zone_name
            __props__['registration_enabled'] = registration_enabled
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            if virtual_network_id is None:
                raise TypeError("Missing required property 'virtual_network_id'")
            __props__['virtual_network_id'] = virtual_network_id
        super(ZoneVirtualNetworkLink, __self__).__init__(
            'azure:privatedns/zoneVirtualNetworkLink:ZoneVirtualNetworkLink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, name=None, private_dns_zone_name=None, registration_enabled=None, resource_group_name=None, tags=None, virtual_network_id=None):
        """
        Get an existing ZoneVirtualNetworkLink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the Private DNS Zone Virtual Network Link. Changing this forces a new resource to be created.
        :param pulumi.Input[str] private_dns_zone_name: The name of the Private DNS zone (without a terminating dot). Changing this forces a new resource to be created.
        :param pulumi.Input[bool] registration_enabled: Is auto-registration of virtual machine records in the virtual network in the Private DNS zone enabled? Defaults to `false`.
        :param pulumi.Input[str] resource_group_name: Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] virtual_network_id: The Resource ID of the Virtual Network that should be linked to the DNS Zone. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["name"] = name
        __props__["private_dns_zone_name"] = private_dns_zone_name
        __props__["registration_enabled"] = registration_enabled
        __props__["resource_group_name"] = resource_group_name
        __props__["tags"] = tags
        __props__["virtual_network_id"] = virtual_network_id
        return ZoneVirtualNetworkLink(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
