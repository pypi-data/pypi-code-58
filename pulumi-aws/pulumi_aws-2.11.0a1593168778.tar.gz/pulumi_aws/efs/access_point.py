# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class AccessPoint(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Amazon Resource Name of the access point.
    """
    file_system_arn: pulumi.Output[str]
    """
    Amazon Resource Name of the file system.
    """
    file_system_id: pulumi.Output[str]
    """
    The ID of the file system for which the access point is intended.
    """
    owner_id: pulumi.Output[str]
    posix_user: pulumi.Output[dict]
    """
    The operating system user and group applied to all file system requests made using the access point. See Posix User below.

      * `gid` (`float`) - The POSIX group ID used for all file system operations using this access point.
      * `secondaryGids` (`list`) - Secondary POSIX group IDs used for all file system operations using this access point.
      * `uid` (`float`) - The POSIX user ID used for all file system operations using this access point.
    """
    root_directory: pulumi.Output[dict]
    """
    Specifies the directory on the Amazon EFS file system that the access point provides access to. See Root Directory below.

      * `creationInfo` (`dict`) - Specifies the POSIX IDs and permissions to apply to the access point's Root Directory. See Creation Info below.
        * `ownerGid` (`float`) - Specifies the POSIX group ID to apply to the `root_directory`.
        * `ownerUid` (`float`) - Specifies the POSIX user ID to apply to the `root_directory`.
        * `permissions` (`str`) - Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.

      * `path` (`str`) - Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide `creation_info`.
    """
    tags: pulumi.Output[dict]
    """
    Key-value mapping of resource tags.
    """
    def __init__(__self__, resource_name, opts=None, file_system_id=None, posix_user=None, root_directory=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an Elastic File System (EFS) access point.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.efs.AccessPoint("test", file_system_id=aws_efs_file_system["foo"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] file_system_id: The ID of the file system for which the access point is intended.
        :param pulumi.Input[dict] posix_user: The operating system user and group applied to all file system requests made using the access point. See Posix User below.
        :param pulumi.Input[dict] root_directory: Specifies the directory on the Amazon EFS file system that the access point provides access to. See Root Directory below.
        :param pulumi.Input[dict] tags: Key-value mapping of resource tags.

        The **posix_user** object supports the following:

          * `gid` (`pulumi.Input[float]`) - The POSIX group ID used for all file system operations using this access point.
          * `secondaryGids` (`pulumi.Input[list]`) - Secondary POSIX group IDs used for all file system operations using this access point.
          * `uid` (`pulumi.Input[float]`) - The POSIX user ID used for all file system operations using this access point.

        The **root_directory** object supports the following:

          * `creationInfo` (`pulumi.Input[dict]`) - Specifies the POSIX IDs and permissions to apply to the access point's Root Directory. See Creation Info below.
            * `ownerGid` (`pulumi.Input[float]`) - Specifies the POSIX group ID to apply to the `root_directory`.
            * `ownerUid` (`pulumi.Input[float]`) - Specifies the POSIX user ID to apply to the `root_directory`.
            * `permissions` (`pulumi.Input[str]`) - Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.

          * `path` (`pulumi.Input[str]`) - Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide `creation_info`.
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

            if file_system_id is None:
                raise TypeError("Missing required property 'file_system_id'")
            __props__['file_system_id'] = file_system_id
            __props__['posix_user'] = posix_user
            __props__['root_directory'] = root_directory
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['file_system_arn'] = None
            __props__['owner_id'] = None
        super(AccessPoint, __self__).__init__(
            'aws:efs/accessPoint:AccessPoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, file_system_arn=None, file_system_id=None, owner_id=None, posix_user=None, root_directory=None, tags=None):
        """
        Get an existing AccessPoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name of the access point.
        :param pulumi.Input[str] file_system_arn: Amazon Resource Name of the file system.
        :param pulumi.Input[str] file_system_id: The ID of the file system for which the access point is intended.
        :param pulumi.Input[dict] posix_user: The operating system user and group applied to all file system requests made using the access point. See Posix User below.
        :param pulumi.Input[dict] root_directory: Specifies the directory on the Amazon EFS file system that the access point provides access to. See Root Directory below.
        :param pulumi.Input[dict] tags: Key-value mapping of resource tags.

        The **posix_user** object supports the following:

          * `gid` (`pulumi.Input[float]`) - The POSIX group ID used for all file system operations using this access point.
          * `secondaryGids` (`pulumi.Input[list]`) - Secondary POSIX group IDs used for all file system operations using this access point.
          * `uid` (`pulumi.Input[float]`) - The POSIX user ID used for all file system operations using this access point.

        The **root_directory** object supports the following:

          * `creationInfo` (`pulumi.Input[dict]`) - Specifies the POSIX IDs and permissions to apply to the access point's Root Directory. See Creation Info below.
            * `ownerGid` (`pulumi.Input[float]`) - Specifies the POSIX group ID to apply to the `root_directory`.
            * `ownerUid` (`pulumi.Input[float]`) - Specifies the POSIX user ID to apply to the `root_directory`.
            * `permissions` (`pulumi.Input[str]`) - Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.

          * `path` (`pulumi.Input[str]`) - Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide `creation_info`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["file_system_arn"] = file_system_arn
        __props__["file_system_id"] = file_system_id
        __props__["owner_id"] = owner_id
        __props__["posix_user"] = posix_user
        __props__["root_directory"] = root_directory
        __props__["tags"] = tags
        return AccessPoint(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
