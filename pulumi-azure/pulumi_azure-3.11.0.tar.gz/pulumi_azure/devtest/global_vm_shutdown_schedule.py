# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class GlobalVMShutdownSchedule(pulumi.CustomResource):
    daily_recurrence_time: pulumi.Output[str]
    """
    The time each day when the schedule takes effect. Must match the format HHmm where HH is 00-23 and mm is 00-59 (e.g. 0930, 2300, etc.)
    """
    enabled: pulumi.Output[bool]
    """
    Whether to enable the schedule. Possible values are `true` and `false`. Defaults to `true`.
    """
    location: pulumi.Output[str]
    """
    The location where the schedule is created. Changing this forces a new resource to be created.
    """
    notification_settings: pulumi.Output[dict]
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    timezone: pulumi.Output[str]
    """
    The time zone ID (e.g. Pacific Standard time). Refer to this guide for a [full list of accepted time zone names](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
    """
    virtual_machine_id: pulumi.Output[str]
    """
    The resource ID of the target ARM-based Virtual Machine. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, daily_recurrence_time=None, enabled=None, location=None, notification_settings=None, tags=None, timezone=None, virtual_machine_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages automated shutdown schedules for Azure VMs that are not within an Azure DevTest Lab. While this is part of the DevTest Labs service in Azure,
        this resource applies only to standard VMs, not DevTest Lab VMs. To manage automated shutdown schedules for DevTest Lab VMs, reference the
        `devtest.Schedule` resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="eastus")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefix="10.0.2.0/24")
        example_network_interface = azure.network.NetworkInterface("exampleNetworkInterface",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            ip_configuration=[{
                "name": "testconfiguration1",
                "subnet_id": example_subnet.id,
                "privateIpAddressAllocation": "Dynamic",
            }])
        example_linux_virtual_machine = azure.compute.LinuxVirtualMachine("exampleLinuxVirtualMachine",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            network_interface_ids=[example_network_interface.id],
            size="Standard_B2s",
            source_image_reference={
                "publisher": "Canonical",
                "offer": "UbuntuServer",
                "sku": "16.04-LTS",
                "version": "latest",
            },
            os_disk={
                "name": "myosdisk-%d",
                "caching": "ReadWrite",
                "managedDiskType": "Standard_LRS",
            },
            admin_username="testadmin",
            admin_password="Password1234!",
            disable_password_authentication=False)
        example_global_vm_shutdown_schedule = azure.devtest.GlobalVMShutdownSchedule("exampleGlobalVMShutdownSchedule",
            virtual_machine_id=azurerm_virtual_machine["example"]["id"],
            location=example_resource_group.location,
            enabled=True,
            daily_recurrence_time="1100",
            timezone="Pacific Standard Time",
            notification_settings={
                "enabled": True,
                "timeInMinutes": "60",
                "webhookUrl": "https://sample-webhook-url.example.com",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] daily_recurrence_time: The time each day when the schedule takes effect. Must match the format HHmm where HH is 00-23 and mm is 00-59 (e.g. 0930, 2300, etc.)
        :param pulumi.Input[bool] enabled: Whether to enable the schedule. Possible values are `true` and `false`. Defaults to `true`.
        :param pulumi.Input[str] location: The location where the schedule is created. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] timezone: The time zone ID (e.g. Pacific Standard time). Refer to this guide for a [full list of accepted time zone names](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        :param pulumi.Input[str] virtual_machine_id: The resource ID of the target ARM-based Virtual Machine. Changing this forces a new resource to be created.

        The **notification_settings** object supports the following:

          * `enabled` (`pulumi.Input[bool]`) - Whether to enable pre-shutdown notifications. Possible values are `true` and `false`. Defaults to `false`
          * `timeInMinutes` (`pulumi.Input[float]`) - Time in minutes between 15 and 120 before a shutdown event at which a notification will be sent. Defaults to `30`.
          * `webhookUrl` (`pulumi.Input[str]`) - The webhook URL to which the notification will be sent. Required if `enabled` is `true`. Optional otherwise.
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

            if daily_recurrence_time is None:
                raise TypeError("Missing required property 'daily_recurrence_time'")
            __props__['daily_recurrence_time'] = daily_recurrence_time
            __props__['enabled'] = enabled
            __props__['location'] = location
            if notification_settings is None:
                raise TypeError("Missing required property 'notification_settings'")
            __props__['notification_settings'] = notification_settings
            __props__['tags'] = tags
            if timezone is None:
                raise TypeError("Missing required property 'timezone'")
            __props__['timezone'] = timezone
            if virtual_machine_id is None:
                raise TypeError("Missing required property 'virtual_machine_id'")
            __props__['virtual_machine_id'] = virtual_machine_id
        super(GlobalVMShutdownSchedule, __self__).__init__(
            'azure:devtest/globalVMShutdownSchedule:GlobalVMShutdownSchedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, daily_recurrence_time=None, enabled=None, location=None, notification_settings=None, tags=None, timezone=None, virtual_machine_id=None):
        """
        Get an existing GlobalVMShutdownSchedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] daily_recurrence_time: The time each day when the schedule takes effect. Must match the format HHmm where HH is 00-23 and mm is 00-59 (e.g. 0930, 2300, etc.)
        :param pulumi.Input[bool] enabled: Whether to enable the schedule. Possible values are `true` and `false`. Defaults to `true`.
        :param pulumi.Input[str] location: The location where the schedule is created. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] timezone: The time zone ID (e.g. Pacific Standard time). Refer to this guide for a [full list of accepted time zone names](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        :param pulumi.Input[str] virtual_machine_id: The resource ID of the target ARM-based Virtual Machine. Changing this forces a new resource to be created.

        The **notification_settings** object supports the following:

          * `enabled` (`pulumi.Input[bool]`) - Whether to enable pre-shutdown notifications. Possible values are `true` and `false`. Defaults to `false`
          * `timeInMinutes` (`pulumi.Input[float]`) - Time in minutes between 15 and 120 before a shutdown event at which a notification will be sent. Defaults to `30`.
          * `webhookUrl` (`pulumi.Input[str]`) - The webhook URL to which the notification will be sent. Required if `enabled` is `true`. Optional otherwise.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["daily_recurrence_time"] = daily_recurrence_time
        __props__["enabled"] = enabled
        __props__["location"] = location
        __props__["notification_settings"] = notification_settings
        __props__["tags"] = tags
        __props__["timezone"] = timezone
        __props__["virtual_machine_id"] = virtual_machine_id
        return GlobalVMShutdownSchedule(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
