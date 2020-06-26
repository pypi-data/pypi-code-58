# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class ActiveSlot(pulumi.CustomResource):
    app_service_name: pulumi.Output[str]
    """
    The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.
    """
    app_service_slot_name: pulumi.Output[str]
    """
    The name of the App Service Slot which should be promoted to the Production Slot within the App Service.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, app_service_name=None, app_service_slot_name=None, resource_group_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Promotes an App Service Slot to Production within an App Service.

        > **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `appservice.AppService` resource will be overwritten when promoting a Slot using the `appservice.ActiveSlot` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_random as random

        server = random.RandomId("server")
        # ...
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup")
        # ...
        example_plan = azure.appservice.Plan("examplePlan")
        # ...
        example_app_service = azure.appservice.AppService("exampleAppService")
        # ...
        example_slot = azure.appservice.Slot("exampleSlot")
        # ...
        example_active_slot = azure.appservice.ActiveSlot("exampleActiveSlot",
            resource_group_name=example_resource_group.name,
            app_service_name=example_app_service.name,
            app_service_slot_name=example_slot.name)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.
        :param pulumi.Input[str] app_service_slot_name: The name of the App Service Slot which should be promoted to the Production Slot within the App Service.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
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

            if app_service_name is None:
                raise TypeError("Missing required property 'app_service_name'")
            __props__['app_service_name'] = app_service_name
            if app_service_slot_name is None:
                raise TypeError("Missing required property 'app_service_slot_name'")
            __props__['app_service_slot_name'] = app_service_slot_name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
        super(ActiveSlot, __self__).__init__(
            'azure:appservice/activeSlot:ActiveSlot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, app_service_name=None, app_service_slot_name=None, resource_group_name=None):
        """
        Get an existing ActiveSlot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.
        :param pulumi.Input[str] app_service_slot_name: The name of the App Service Slot which should be promoted to the Production Slot within the App Service.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["app_service_name"] = app_service_name
        __props__["app_service_slot_name"] = app_service_slot_name
        __props__["resource_group_name"] = resource_group_name
        return ActiveSlot(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
