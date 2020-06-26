# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class LocationSmb(pulumi.CustomResource):
    agent_arns: pulumi.Output[list]
    """
    A list of DataSync Agent ARNs with which this location will be associated.
    """
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the DataSync Location.
    """
    domain: pulumi.Output[str]
    """
    The name of the Windows domain the SMB server belongs to.
    """
    mount_options: pulumi.Output[dict]
    """
    Configuration block containing mount options used by DataSync to access the SMB Server. Can be `AUTOMATIC`, `SMB2`, or `SMB3`.

      * `version` (`str`) - The specific SMB version that you want DataSync to use for mounting your SMB share. Valid values: `AUTOMATIC`, `SMB2`, and `SMB3`. Default: `AUTOMATIC`
    """
    password: pulumi.Output[str]
    """
    The password of the user who can mount the share and has file permissions in the SMB.
    """
    server_hostname: pulumi.Output[str]
    """
    Specifies the IP address or DNS name of the SMB server. The DataSync Agent(s) use this to mount the SMB share.
    """
    subdirectory: pulumi.Output[str]
    """
    Subdirectory to perform actions as source or destination. Should be exported by the NFS server.
    """
    tags: pulumi.Output[dict]
    """
    Key-value pairs of resource tags to assign to the DataSync Location.
    """
    uri: pulumi.Output[str]
    user: pulumi.Output[str]
    """
    The user who can mount the share and has file and folder permissions in the SMB share.
    """
    def __init__(__self__, resource_name, opts=None, agent_arns=None, domain=None, mount_options=None, password=None, server_hostname=None, subdirectory=None, tags=None, user=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a SMB Location within AWS DataSync.

        > **NOTE:** The DataSync Agents must be available before creating this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.datasync.LocationSmb("example",
            agent_arns=[aws_datasync_agent["example"]["arn"]],
            password="ANotGreatPassword",
            server_hostname="smb.example.com",
            subdirectory="/exported/path",
            user="Guest")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] agent_arns: A list of DataSync Agent ARNs with which this location will be associated.
        :param pulumi.Input[str] domain: The name of the Windows domain the SMB server belongs to.
        :param pulumi.Input[dict] mount_options: Configuration block containing mount options used by DataSync to access the SMB Server. Can be `AUTOMATIC`, `SMB2`, or `SMB3`.
        :param pulumi.Input[str] password: The password of the user who can mount the share and has file permissions in the SMB.
        :param pulumi.Input[str] server_hostname: Specifies the IP address or DNS name of the SMB server. The DataSync Agent(s) use this to mount the SMB share.
        :param pulumi.Input[str] subdirectory: Subdirectory to perform actions as source or destination. Should be exported by the NFS server.
        :param pulumi.Input[dict] tags: Key-value pairs of resource tags to assign to the DataSync Location.
        :param pulumi.Input[str] user: The user who can mount the share and has file and folder permissions in the SMB share.

        The **mount_options** object supports the following:

          * `version` (`pulumi.Input[str]`) - The specific SMB version that you want DataSync to use for mounting your SMB share. Valid values: `AUTOMATIC`, `SMB2`, and `SMB3`. Default: `AUTOMATIC`
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

            if agent_arns is None:
                raise TypeError("Missing required property 'agent_arns'")
            __props__['agent_arns'] = agent_arns
            __props__['domain'] = domain
            __props__['mount_options'] = mount_options
            if password is None:
                raise TypeError("Missing required property 'password'")
            __props__['password'] = password
            if server_hostname is None:
                raise TypeError("Missing required property 'server_hostname'")
            __props__['server_hostname'] = server_hostname
            if subdirectory is None:
                raise TypeError("Missing required property 'subdirectory'")
            __props__['subdirectory'] = subdirectory
            __props__['tags'] = tags
            if user is None:
                raise TypeError("Missing required property 'user'")
            __props__['user'] = user
            __props__['arn'] = None
            __props__['uri'] = None
        super(LocationSmb, __self__).__init__(
            'aws:datasync/locationSmb:LocationSmb',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, agent_arns=None, arn=None, domain=None, mount_options=None, password=None, server_hostname=None, subdirectory=None, tags=None, uri=None, user=None):
        """
        Get an existing LocationSmb resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] agent_arns: A list of DataSync Agent ARNs with which this location will be associated.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the DataSync Location.
        :param pulumi.Input[str] domain: The name of the Windows domain the SMB server belongs to.
        :param pulumi.Input[dict] mount_options: Configuration block containing mount options used by DataSync to access the SMB Server. Can be `AUTOMATIC`, `SMB2`, or `SMB3`.
        :param pulumi.Input[str] password: The password of the user who can mount the share and has file permissions in the SMB.
        :param pulumi.Input[str] server_hostname: Specifies the IP address or DNS name of the SMB server. The DataSync Agent(s) use this to mount the SMB share.
        :param pulumi.Input[str] subdirectory: Subdirectory to perform actions as source or destination. Should be exported by the NFS server.
        :param pulumi.Input[dict] tags: Key-value pairs of resource tags to assign to the DataSync Location.
        :param pulumi.Input[str] user: The user who can mount the share and has file and folder permissions in the SMB share.

        The **mount_options** object supports the following:

          * `version` (`pulumi.Input[str]`) - The specific SMB version that you want DataSync to use for mounting your SMB share. Valid values: `AUTOMATIC`, `SMB2`, and `SMB3`. Default: `AUTOMATIC`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["agent_arns"] = agent_arns
        __props__["arn"] = arn
        __props__["domain"] = domain
        __props__["mount_options"] = mount_options
        __props__["password"] = password
        __props__["server_hostname"] = server_hostname
        __props__["subdirectory"] = subdirectory
        __props__["tags"] = tags
        __props__["uri"] = uri
        __props__["user"] = user
        return LocationSmb(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
