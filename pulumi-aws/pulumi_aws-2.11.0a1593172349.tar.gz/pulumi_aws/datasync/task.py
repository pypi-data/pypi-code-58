# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Task(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the DataSync Task.
    """
    cloudwatch_log_group_arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.
    """
    destination_location_arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of destination DataSync Location.
    """
    name: pulumi.Output[str]
    """
    Name of the DataSync Task.
    """
    options: pulumi.Output[dict]
    """
    Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.

      * `atime` (`str`) - A file metadata that shows the last time a file was accessed (that is when the file was read or written to). If set to `BEST_EFFORT`, the DataSync Task attempts to preserve the original (that is, the version before sync `PREPARING` phase) `atime` attribute on all source files. Valid values: `BEST_EFFORT`, `NONE`. Default: `BEST_EFFORT`.
      * `bytesPerSecond` (`float`) - Limits the bandwidth utilized. For example, to set a maximum of 1 MB, set this value to `1048576`. Value values: `-1` or greater. Default: `-1` (unlimited).
      * `gid` (`str`) - Group identifier of the file's owners. Valid values: `BOTH`, `INT_VALUE`, `NAME`, `NONE`. Default: `INT_VALUE` (preserve integer value of the ID).
      * `mtime` (`str`) - A file metadata that indicates the last time a file was modified (written to) before the sync `PREPARING` phase. Value values: `NONE`, `PRESERVE`. Default: `PRESERVE`.
      * `posixPermissions` (`str`) - Determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file. Valid values: `NONE`, `PRESERVE`. Default: `PRESERVE`.
      * `preserveDeletedFiles` (`str`) - Whether files deleted in the source should be removed or preserved in the destination file system. Valid values: `PRESERVE`, `REMOVE`. Default: `PRESERVE`.
      * `preserveDevices` (`str`) - Whether the DataSync Task should preserve the metadata of block and character devices in the source files system, and recreate the files with that device name and metadata on the destination. The DataSync Task can’t sync the actual contents of such devices, because many of the devices are non-terminal and don’t return an end of file (EOF) marker. Valid values: `NONE`, `PRESERVE`. Default: `NONE` (ignore special devices).
      * `uid` (`str`) - User identifier of the file's owners. Valid values: `BOTH`, `INT_VALUE`, `NAME`, `NONE`. Default: `INT_VALUE` (preserve integer value of the ID).
      * `verifyMode` (`str`) - Whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred. Valid values: `NONE`, `POINT_IN_TIME_CONSISTENT`, `ONLY_FILES_TRANSFERRED`. Default: `POINT_IN_TIME_CONSISTENT`.
    """
    source_location_arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of source DataSync Location.
    """
    tags: pulumi.Output[dict]
    """
    Key-value pairs of resource tags to assign to the DataSync Task.
    """
    def __init__(__self__, resource_name, opts=None, cloudwatch_log_group_arn=None, destination_location_arn=None, name=None, options=None, source_location_arn=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an AWS DataSync Task, which represents a configuration for synchronization. Starting an execution of these DataSync Tasks (actually synchronizing files) is performed outside of this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.datasync.Task("example",
            destination_location_arn=aws_datasync_location_s3["destination"]["arn"],
            options={
                "bytesPerSecond": -1,
            },
            source_location_arn=aws_datasync_location_nfs["source"]["arn"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloudwatch_log_group_arn: Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.
        :param pulumi.Input[str] destination_location_arn: Amazon Resource Name (ARN) of destination DataSync Location.
        :param pulumi.Input[str] name: Name of the DataSync Task.
        :param pulumi.Input[dict] options: Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.
        :param pulumi.Input[str] source_location_arn: Amazon Resource Name (ARN) of source DataSync Location.
        :param pulumi.Input[dict] tags: Key-value pairs of resource tags to assign to the DataSync Task.

        The **options** object supports the following:

          * `atime` (`pulumi.Input[str]`) - A file metadata that shows the last time a file was accessed (that is when the file was read or written to). If set to `BEST_EFFORT`, the DataSync Task attempts to preserve the original (that is, the version before sync `PREPARING` phase) `atime` attribute on all source files. Valid values: `BEST_EFFORT`, `NONE`. Default: `BEST_EFFORT`.
          * `bytesPerSecond` (`pulumi.Input[float]`) - Limits the bandwidth utilized. For example, to set a maximum of 1 MB, set this value to `1048576`. Value values: `-1` or greater. Default: `-1` (unlimited).
          * `gid` (`pulumi.Input[str]`) - Group identifier of the file's owners. Valid values: `BOTH`, `INT_VALUE`, `NAME`, `NONE`. Default: `INT_VALUE` (preserve integer value of the ID).
          * `mtime` (`pulumi.Input[str]`) - A file metadata that indicates the last time a file was modified (written to) before the sync `PREPARING` phase. Value values: `NONE`, `PRESERVE`. Default: `PRESERVE`.
          * `posixPermissions` (`pulumi.Input[str]`) - Determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file. Valid values: `NONE`, `PRESERVE`. Default: `PRESERVE`.
          * `preserveDeletedFiles` (`pulumi.Input[str]`) - Whether files deleted in the source should be removed or preserved in the destination file system. Valid values: `PRESERVE`, `REMOVE`. Default: `PRESERVE`.
          * `preserveDevices` (`pulumi.Input[str]`) - Whether the DataSync Task should preserve the metadata of block and character devices in the source files system, and recreate the files with that device name and metadata on the destination. The DataSync Task can’t sync the actual contents of such devices, because many of the devices are non-terminal and don’t return an end of file (EOF) marker. Valid values: `NONE`, `PRESERVE`. Default: `NONE` (ignore special devices).
          * `uid` (`pulumi.Input[str]`) - User identifier of the file's owners. Valid values: `BOTH`, `INT_VALUE`, `NAME`, `NONE`. Default: `INT_VALUE` (preserve integer value of the ID).
          * `verifyMode` (`pulumi.Input[str]`) - Whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred. Valid values: `NONE`, `POINT_IN_TIME_CONSISTENT`, `ONLY_FILES_TRANSFERRED`. Default: `POINT_IN_TIME_CONSISTENT`.
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

            __props__['cloudwatch_log_group_arn'] = cloudwatch_log_group_arn
            if destination_location_arn is None:
                raise TypeError("Missing required property 'destination_location_arn'")
            __props__['destination_location_arn'] = destination_location_arn
            __props__['name'] = name
            __props__['options'] = options
            if source_location_arn is None:
                raise TypeError("Missing required property 'source_location_arn'")
            __props__['source_location_arn'] = source_location_arn
            __props__['tags'] = tags
            __props__['arn'] = None
        super(Task, __self__).__init__(
            'aws:datasync/task:Task',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, cloudwatch_log_group_arn=None, destination_location_arn=None, name=None, options=None, source_location_arn=None, tags=None):
        """
        Get an existing Task resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the DataSync Task.
        :param pulumi.Input[str] cloudwatch_log_group_arn: Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.
        :param pulumi.Input[str] destination_location_arn: Amazon Resource Name (ARN) of destination DataSync Location.
        :param pulumi.Input[str] name: Name of the DataSync Task.
        :param pulumi.Input[dict] options: Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.
        :param pulumi.Input[str] source_location_arn: Amazon Resource Name (ARN) of source DataSync Location.
        :param pulumi.Input[dict] tags: Key-value pairs of resource tags to assign to the DataSync Task.

        The **options** object supports the following:

          * `atime` (`pulumi.Input[str]`) - A file metadata that shows the last time a file was accessed (that is when the file was read or written to). If set to `BEST_EFFORT`, the DataSync Task attempts to preserve the original (that is, the version before sync `PREPARING` phase) `atime` attribute on all source files. Valid values: `BEST_EFFORT`, `NONE`. Default: `BEST_EFFORT`.
          * `bytesPerSecond` (`pulumi.Input[float]`) - Limits the bandwidth utilized. For example, to set a maximum of 1 MB, set this value to `1048576`. Value values: `-1` or greater. Default: `-1` (unlimited).
          * `gid` (`pulumi.Input[str]`) - Group identifier of the file's owners. Valid values: `BOTH`, `INT_VALUE`, `NAME`, `NONE`. Default: `INT_VALUE` (preserve integer value of the ID).
          * `mtime` (`pulumi.Input[str]`) - A file metadata that indicates the last time a file was modified (written to) before the sync `PREPARING` phase. Value values: `NONE`, `PRESERVE`. Default: `PRESERVE`.
          * `posixPermissions` (`pulumi.Input[str]`) - Determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file. Valid values: `NONE`, `PRESERVE`. Default: `PRESERVE`.
          * `preserveDeletedFiles` (`pulumi.Input[str]`) - Whether files deleted in the source should be removed or preserved in the destination file system. Valid values: `PRESERVE`, `REMOVE`. Default: `PRESERVE`.
          * `preserveDevices` (`pulumi.Input[str]`) - Whether the DataSync Task should preserve the metadata of block and character devices in the source files system, and recreate the files with that device name and metadata on the destination. The DataSync Task can’t sync the actual contents of such devices, because many of the devices are non-terminal and don’t return an end of file (EOF) marker. Valid values: `NONE`, `PRESERVE`. Default: `NONE` (ignore special devices).
          * `uid` (`pulumi.Input[str]`) - User identifier of the file's owners. Valid values: `BOTH`, `INT_VALUE`, `NAME`, `NONE`. Default: `INT_VALUE` (preserve integer value of the ID).
          * `verifyMode` (`pulumi.Input[str]`) - Whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred. Valid values: `NONE`, `POINT_IN_TIME_CONSISTENT`, `ONLY_FILES_TRANSFERRED`. Default: `POINT_IN_TIME_CONSISTENT`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["cloudwatch_log_group_arn"] = cloudwatch_log_group_arn
        __props__["destination_location_arn"] = destination_location_arn
        __props__["name"] = name
        __props__["options"] = options
        __props__["source_location_arn"] = source_location_arn
        __props__["tags"] = tags
        return Task(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
