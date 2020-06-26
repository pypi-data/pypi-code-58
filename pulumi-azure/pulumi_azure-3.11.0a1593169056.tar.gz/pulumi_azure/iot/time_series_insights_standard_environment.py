# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class TimeSeriesInsightsStandardEnvironment(pulumi.CustomResource):
    data_retention_time: pulumi.Output[str]
    """
    Specifies the ISO8601 timespan specifying the minimum number of days the environment's events will be available for query. Changing this forces a new resource to be created.
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Azure IoT Time Series Insights Standard Environment. Changing this forces a new resource to be created. Must be globally unique.
    """
    partition_key: pulumi.Output[str]
    """
    The name of the event property which will be used to partition data. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the Azure IoT Time Series Insights Standard Environment.
    """
    sku_name: pulumi.Output[str]
    """
    Specifies the SKU Name for this IoT Time Series Insights Standard Environment. It is string consisting of two parts separated by an underscore(\_).The fist part is the `name`, valid values include: `S1` and `S2`. The second part is the `capacity` (e.g. the number of deployed units of the `sku`), which must be a positive `integer` (e.g. `S1_1`). Changing this forces a new resource to be created.
    """
    storage_limit_exceeded_behavior: pulumi.Output[str]
    """
    Specifies the behavior the IoT Time Series Insights service should take when the environment's capacity has been exceeded. Valid values include `PauseIngress` and `PurgeOldData`. Defaults to `PurgeOldData`.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, data_retention_time=None, location=None, name=None, partition_key=None, resource_group_name=None, sku_name=None, storage_limit_exceeded_behavior=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an Azure IoT Time Series Insights Standard Environment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="northeurope")
        example_time_series_insights_standard_environment = azure.iot.TimeSeriesInsightsStandardEnvironment("exampleTimeSeriesInsightsStandardEnvironment",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="S1_1",
            data_retention_time="P30D")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_retention_time: Specifies the ISO8601 timespan specifying the minimum number of days the environment's events will be available for query. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Azure IoT Time Series Insights Standard Environment. Changing this forces a new resource to be created. Must be globally unique.
        :param pulumi.Input[str] partition_key: The name of the event property which will be used to partition data. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Azure IoT Time Series Insights Standard Environment.
        :param pulumi.Input[str] sku_name: Specifies the SKU Name for this IoT Time Series Insights Standard Environment. It is string consisting of two parts separated by an underscore(\_).The fist part is the `name`, valid values include: `S1` and `S2`. The second part is the `capacity` (e.g. the number of deployed units of the `sku`), which must be a positive `integer` (e.g. `S1_1`). Changing this forces a new resource to be created.
        :param pulumi.Input[str] storage_limit_exceeded_behavior: Specifies the behavior the IoT Time Series Insights service should take when the environment's capacity has been exceeded. Valid values include `PauseIngress` and `PurgeOldData`. Defaults to `PurgeOldData`.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
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

            if data_retention_time is None:
                raise TypeError("Missing required property 'data_retention_time'")
            __props__['data_retention_time'] = data_retention_time
            __props__['location'] = location
            __props__['name'] = name
            __props__['partition_key'] = partition_key
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if sku_name is None:
                raise TypeError("Missing required property 'sku_name'")
            __props__['sku_name'] = sku_name
            __props__['storage_limit_exceeded_behavior'] = storage_limit_exceeded_behavior
            __props__['tags'] = tags
        super(TimeSeriesInsightsStandardEnvironment, __self__).__init__(
            'azure:iot/timeSeriesInsightsStandardEnvironment:TimeSeriesInsightsStandardEnvironment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, data_retention_time=None, location=None, name=None, partition_key=None, resource_group_name=None, sku_name=None, storage_limit_exceeded_behavior=None, tags=None):
        """
        Get an existing TimeSeriesInsightsStandardEnvironment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_retention_time: Specifies the ISO8601 timespan specifying the minimum number of days the environment's events will be available for query. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Azure IoT Time Series Insights Standard Environment. Changing this forces a new resource to be created. Must be globally unique.
        :param pulumi.Input[str] partition_key: The name of the event property which will be used to partition data. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Azure IoT Time Series Insights Standard Environment.
        :param pulumi.Input[str] sku_name: Specifies the SKU Name for this IoT Time Series Insights Standard Environment. It is string consisting of two parts separated by an underscore(\_).The fist part is the `name`, valid values include: `S1` and `S2`. The second part is the `capacity` (e.g. the number of deployed units of the `sku`), which must be a positive `integer` (e.g. `S1_1`). Changing this forces a new resource to be created.
        :param pulumi.Input[str] storage_limit_exceeded_behavior: Specifies the behavior the IoT Time Series Insights service should take when the environment's capacity has been exceeded. Valid values include `PauseIngress` and `PurgeOldData`. Defaults to `PurgeOldData`.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["data_retention_time"] = data_retention_time
        __props__["location"] = location
        __props__["name"] = name
        __props__["partition_key"] = partition_key
        __props__["resource_group_name"] = resource_group_name
        __props__["sku_name"] = sku_name
        __props__["storage_limit_exceeded_behavior"] = storage_limit_exceeded_behavior
        __props__["tags"] = tags
        return TimeSeriesInsightsStandardEnvironment(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
