# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class DedicatedHostGroup(pulumi.CustomResource):
    location: pulumi.Output[str]
    """
    The Azure location where the Dedicated Host Group exists. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Dedicated Host Group. Changing this forces a new resource to be created.
    """
    platform_fault_domain_count: pulumi.Output[float]
    """
    The number of fault domains that the Dedicated Host Group spans. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    Specifies the name of the resource group the Dedicated Host Group is located in. Changing this forces a new resource to be created.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    zones: pulumi.Output[str]
    """
    A list of Availability Zones in which the Dedicated Host Group should be located. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, location=None, name=None, platform_fault_domain_count=None, resource_group_name=None, tags=None, zones=None, __props__=None, __name__=None, __opts__=None):
        """
        Manage a Dedicated Host Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_dedicated_host_group = azure.compute.DedicatedHostGroup("exampleDedicatedHostGroup",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            platform_fault_domain_count=1)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The Azure location where the Dedicated Host Group exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Dedicated Host Group. Changing this forces a new resource to be created.
        :param pulumi.Input[float] platform_fault_domain_count: The number of fault domains that the Dedicated Host Group spans. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the resource group the Dedicated Host Group is located in. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zones: A list of Availability Zones in which the Dedicated Host Group should be located. Changing this forces a new resource to be created.
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

            __props__['location'] = location
            __props__['name'] = name
            if platform_fault_domain_count is None:
                raise TypeError("Missing required property 'platform_fault_domain_count'")
            __props__['platform_fault_domain_count'] = platform_fault_domain_count
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            __props__['zones'] = zones
        super(DedicatedHostGroup, __self__).__init__(
            'azure:compute/dedicatedHostGroup:DedicatedHostGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, location=None, name=None, platform_fault_domain_count=None, resource_group_name=None, tags=None, zones=None):
        """
        Get an existing DedicatedHostGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The Azure location where the Dedicated Host Group exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Dedicated Host Group. Changing this forces a new resource to be created.
        :param pulumi.Input[float] platform_fault_domain_count: The number of fault domains that the Dedicated Host Group spans. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the resource group the Dedicated Host Group is located in. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zones: A list of Availability Zones in which the Dedicated Host Group should be located. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["location"] = location
        __props__["name"] = name
        __props__["platform_fault_domain_count"] = platform_fault_domain_count
        __props__["resource_group_name"] = resource_group_name
        __props__["tags"] = tags
        __props__["zones"] = zones
        return DedicatedHostGroup(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
