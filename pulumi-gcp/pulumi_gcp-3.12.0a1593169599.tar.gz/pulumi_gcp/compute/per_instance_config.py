# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class PerInstanceConfig(pulumi.CustomResource):
    instance_group_manager: pulumi.Output[str]
    """
    The instance group manager this instance config is part of.
    """
    minimal_action: pulumi.Output[str]
    """
    The minimal action to perform on the instance during an update.
    Default is `NONE`. Possible values are:
    * REPLACE
    * RESTART
    * REFRESH
    * NONE
    """
    most_disruptive_allowed_action: pulumi.Output[str]
    """
    The most disruptive action to perform on the instance during an update.
    Default is `REPLACE`. Possible values are:
    * REPLACE
    * RESTART
    * REFRESH
    * NONE
    """
    name: pulumi.Output[str]
    """
    The name for this per-instance config and its corresponding instance.
    """
    preserved_state: pulumi.Output[dict]
    """
    The preserved state for this instance.  Structure is documented below.

      * `disks` (`list`) - Stateful disks for the instance.  Structure is documented below.
        * `deleteRule` (`str`) - A value that prescribes what should happen to the stateful disk when the VM instance is deleted.
          The available options are `NEVER` and `ON_PERMANENT_INSTANCE_DELETION`.
          `NEVER` detatch the disk when the VM is deleted, but not delete the disk.
          `ON_PERMANENT_INSTANCE_DELETION` will delete the stateful disk when the VM is permanently
          deleted from the instance group.
        * `device_name` (`str`) - A unique device name that is reflected into the /dev/ tree of a Linux operating system running within the instance.
        * `mode` (`str`) - The mode of the disk.
        * `source` (`str`) - The URI of an existing persistent disk to attach under the specified device-name in the format
          `projects/project-id/zones/zone/disks/disk-name`.

      * `metadata` (`dict`) - Preserved metadata defined for this instance. This is a list of key->value pairs.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    remove_instance_state_on_destroy: pulumi.Output[bool]
    """
    When true, deleting this config will immediately remove any specified state from the underlying instance.
    When false, deleting this config will *not* immediately remove any state from the underlying instance.
    State will be removed on the next instance recreation or update.
    """
    zone: pulumi.Output[str]
    """
    Zone where the containing instance group manager is located
    """
    def __init__(__self__, resource_name, opts=None, instance_group_manager=None, minimal_action=None, most_disruptive_allowed_action=None, name=None, preserved_state=None, project=None, remove_instance_state_on_destroy=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        A config defined for a single managed instance that belongs to an instance group manager. It preserves the instance name
        across instance group manager operations and can define stateful disks or metadata that are unique to the instance.

        To get more information about PerInstanceConfig, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/compute/docs/instance-groups/stateful-migs#per-instance_configs)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_group_manager: The instance group manager this instance config is part of.
        :param pulumi.Input[str] minimal_action: The minimal action to perform on the instance during an update.
               Default is `NONE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update.
               Default is `REPLACE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] name: The name for this per-instance config and its corresponding instance.
        :param pulumi.Input[dict] preserved_state: The preserved state for this instance.  Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[bool] remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance.
               When false, deleting this config will *not* immediately remove any state from the underlying instance.
               State will be removed on the next instance recreation or update.
        :param pulumi.Input[str] zone: Zone where the containing instance group manager is located

        The **preserved_state** object supports the following:

          * `disks` (`pulumi.Input[list]`) - Stateful disks for the instance.  Structure is documented below.
            * `deleteRule` (`pulumi.Input[str]`) - A value that prescribes what should happen to the stateful disk when the VM instance is deleted.
              The available options are `NEVER` and `ON_PERMANENT_INSTANCE_DELETION`.
              `NEVER` detatch the disk when the VM is deleted, but not delete the disk.
              `ON_PERMANENT_INSTANCE_DELETION` will delete the stateful disk when the VM is permanently
              deleted from the instance group.
            * `device_name` (`pulumi.Input[str]`) - A unique device name that is reflected into the /dev/ tree of a Linux operating system running within the instance.
            * `mode` (`pulumi.Input[str]`) - The mode of the disk.
            * `source` (`pulumi.Input[str]`) - The URI of an existing persistent disk to attach under the specified device-name in the format
              `projects/project-id/zones/zone/disks/disk-name`.

          * `metadata` (`pulumi.Input[dict]`) - Preserved metadata defined for this instance. This is a list of key->value pairs.
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

            if instance_group_manager is None:
                raise TypeError("Missing required property 'instance_group_manager'")
            __props__['instance_group_manager'] = instance_group_manager
            __props__['minimal_action'] = minimal_action
            __props__['most_disruptive_allowed_action'] = most_disruptive_allowed_action
            __props__['name'] = name
            __props__['preserved_state'] = preserved_state
            __props__['project'] = project
            __props__['remove_instance_state_on_destroy'] = remove_instance_state_on_destroy
            if zone is None:
                raise TypeError("Missing required property 'zone'")
            __props__['zone'] = zone
        super(PerInstanceConfig, __self__).__init__(
            'gcp:compute/perInstanceConfig:PerInstanceConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, instance_group_manager=None, minimal_action=None, most_disruptive_allowed_action=None, name=None, preserved_state=None, project=None, remove_instance_state_on_destroy=None, zone=None):
        """
        Get an existing PerInstanceConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_group_manager: The instance group manager this instance config is part of.
        :param pulumi.Input[str] minimal_action: The minimal action to perform on the instance during an update.
               Default is `NONE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update.
               Default is `REPLACE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] name: The name for this per-instance config and its corresponding instance.
        :param pulumi.Input[dict] preserved_state: The preserved state for this instance.  Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[bool] remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance.
               When false, deleting this config will *not* immediately remove any state from the underlying instance.
               State will be removed on the next instance recreation or update.
        :param pulumi.Input[str] zone: Zone where the containing instance group manager is located

        The **preserved_state** object supports the following:

          * `disks` (`pulumi.Input[list]`) - Stateful disks for the instance.  Structure is documented below.
            * `deleteRule` (`pulumi.Input[str]`) - A value that prescribes what should happen to the stateful disk when the VM instance is deleted.
              The available options are `NEVER` and `ON_PERMANENT_INSTANCE_DELETION`.
              `NEVER` detatch the disk when the VM is deleted, but not delete the disk.
              `ON_PERMANENT_INSTANCE_DELETION` will delete the stateful disk when the VM is permanently
              deleted from the instance group.
            * `device_name` (`pulumi.Input[str]`) - A unique device name that is reflected into the /dev/ tree of a Linux operating system running within the instance.
            * `mode` (`pulumi.Input[str]`) - The mode of the disk.
            * `source` (`pulumi.Input[str]`) - The URI of an existing persistent disk to attach under the specified device-name in the format
              `projects/project-id/zones/zone/disks/disk-name`.

          * `metadata` (`pulumi.Input[dict]`) - Preserved metadata defined for this instance. This is a list of key->value pairs.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["instance_group_manager"] = instance_group_manager
        __props__["minimal_action"] = minimal_action
        __props__["most_disruptive_allowed_action"] = most_disruptive_allowed_action
        __props__["name"] = name
        __props__["preserved_state"] = preserved_state
        __props__["project"] = project
        __props__["remove_instance_state_on_destroy"] = remove_instance_state_on_destroy
        __props__["zone"] = zone
        return PerInstanceConfig(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
