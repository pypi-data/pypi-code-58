# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class DiskResourcePolicyAttachment(pulumi.CustomResource):
    disk: pulumi.Output[str]
    """
    The name of the disk in which the resource policies are attached to.
    """
    name: pulumi.Output[str]
    """
    The resource policy to be attached to the disk for scheduling snapshot
    creation. Do not specify the self link.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    zone: pulumi.Output[str]
    """
    A reference to the zone where the disk resides.
    """
    def __init__(__self__, resource_name, opts=None, disk=None, name=None, project=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        Adds existing resource policies to a disk. You can only add one policy
        which will be applied to this disk for scheduling snapshot creation.

        > **Note:** This resource does not support regional disks (`compute.RegionDisk`). For regional disks, please refer to the `compute.RegionDiskResourcePolicyAttachment` resource.

        ## Example Usage
        ### Disk Resource Policy Attachment Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_image = gcp.compute.get_image(family="debian-9",
            project="debian-cloud")
        ssd = gcp.compute.Disk("ssd",
            image=my_image.self_link,
            size=50,
            type="pd-ssd",
            zone="us-central1-a")
        attachment = gcp.compute.DiskResourcePolicyAttachment("attachment",
            disk=ssd.name,
            zone="us-central1-a")
        policy = gcp.compute.ResourcePolicy("policy",
            region="us-central1",
            snapshot_schedule_policy={
                "schedule": {
                    "daily_schedule": {
                        "daysInCycle": 1,
                        "startTime": "04:00",
                    },
                },
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] disk: The name of the disk in which the resource policies are attached to.
        :param pulumi.Input[str] name: The resource policy to be attached to the disk for scheduling snapshot
               creation. Do not specify the self link.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] zone: A reference to the zone where the disk resides.
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

            if disk is None:
                raise TypeError("Missing required property 'disk'")
            __props__['disk'] = disk
            __props__['name'] = name
            __props__['project'] = project
            __props__['zone'] = zone
        super(DiskResourcePolicyAttachment, __self__).__init__(
            'gcp:compute/diskResourcePolicyAttachment:DiskResourcePolicyAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, disk=None, name=None, project=None, zone=None):
        """
        Get an existing DiskResourcePolicyAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] disk: The name of the disk in which the resource policies are attached to.
        :param pulumi.Input[str] name: The resource policy to be attached to the disk for scheduling snapshot
               creation. Do not specify the self link.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] zone: A reference to the zone where the disk resides.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["disk"] = disk
        __props__["name"] = name
        __props__["project"] = project
        __props__["zone"] = zone
        return DiskResourcePolicyAttachment(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
