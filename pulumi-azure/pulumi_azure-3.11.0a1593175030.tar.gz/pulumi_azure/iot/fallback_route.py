# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class FallbackRoute(pulumi.CustomResource):
    condition: pulumi.Output[str]
    """
    The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to `true` by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
    """
    enabled: pulumi.Output[bool]
    """
    Used to specify whether the fallback route is enabled.
    """
    endpoint_names: pulumi.Output[str]
    """
    The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.
    """
    iothub_name: pulumi.Output[str]
    """
    The name of the IoTHub to which this Fallback Route belongs. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, condition=None, enabled=None, endpoint_names=None, iothub_name=None, resource_group_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an IotHub Fallback Route

        ## Disclaimers

        > **Note:** Fallback route can be defined either directly on the `iot.IoTHub` resource, or using the `iot.FallbackRoute` resource - but the two cannot be used together. If both are used against the same IoTHub, spurious changes will occur.

        > **Note:** Since this resource is provisioned by default, the Azure Provider will not check for the presence of an existing resource prior to attempting to create it.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West US")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_container = azure.storage.Container("exampleContainer",
            storage_account_name=example_account.name,
            container_access_type="private")
        example_io_t_hub = azure.iot.IoTHub("exampleIoTHub",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            sku={
                "name": "S1",
                "capacity": "1",
            },
            tags={
                "purpose": "testing",
            })
        example_endpoint_storage_container = azure.iot.EndpointStorageContainer("exampleEndpointStorageContainer",
            resource_group_name=example_resource_group.name,
            iothub_name=example_io_t_hub.name,
            connection_string=example_account.primary_blob_connection_string,
            batch_frequency_in_seconds=60,
            max_chunk_size_in_bytes=10485760,
            container_name=example_container.name,
            encoding="Avro",
            file_name_format="{iothub}/{partition}_{YYYY}_{MM}_{DD}_{HH}_{mm}")
        example_fallback_route = azure.iot.FallbackRoute("exampleFallbackRoute",
            resource_group_name=example_resource_group.name,
            iothub_name=example_io_t_hub.name,
            condition="true",
            endpoint_names=[example_endpoint_storage_container.name],
            enabled=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] condition: The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to `true` by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        :param pulumi.Input[bool] enabled: Used to specify whether the fallback route is enabled.
        :param pulumi.Input[str] endpoint_names: The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.
        :param pulumi.Input[str] iothub_name: The name of the IoTHub to which this Fallback Route belongs. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.
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

            __props__['condition'] = condition
            if enabled is None:
                raise TypeError("Missing required property 'enabled'")
            __props__['enabled'] = enabled
            if endpoint_names is None:
                raise TypeError("Missing required property 'endpoint_names'")
            __props__['endpoint_names'] = endpoint_names
            if iothub_name is None:
                raise TypeError("Missing required property 'iothub_name'")
            __props__['iothub_name'] = iothub_name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
        super(FallbackRoute, __self__).__init__(
            'azure:iot/fallbackRoute:FallbackRoute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, condition=None, enabled=None, endpoint_names=None, iothub_name=None, resource_group_name=None):
        """
        Get an existing FallbackRoute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] condition: The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to `true` by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        :param pulumi.Input[bool] enabled: Used to specify whether the fallback route is enabled.
        :param pulumi.Input[str] endpoint_names: The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.
        :param pulumi.Input[str] iothub_name: The name of the IoTHub to which this Fallback Route belongs. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["condition"] = condition
        __props__["enabled"] = enabled
        __props__["endpoint_names"] = endpoint_names
        __props__["iothub_name"] = iothub_name
        __props__["resource_group_name"] = resource_group_name
        return FallbackRoute(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
