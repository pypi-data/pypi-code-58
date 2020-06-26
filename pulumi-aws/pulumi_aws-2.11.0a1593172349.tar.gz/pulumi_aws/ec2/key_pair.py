# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class KeyPair(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The key pair ARN.
    """
    fingerprint: pulumi.Output[str]
    """
    The MD5 public key fingerprint as specified in section 4 of RFC 4716.
    """
    key_name: pulumi.Output[str]
    """
    The name for the key pair.
    """
    key_name_prefix: pulumi.Output[str]
    """
    Creates a unique name beginning with the specified prefix. Conflicts with `key_name`.
    """
    key_pair_id: pulumi.Output[str]
    """
    The key pair ID.
    """
    public_key: pulumi.Output[str]
    """
    The public key material.
    """
    tags: pulumi.Output[dict]
    """
    Key-value map of resource tags
    """
    def __init__(__self__, resource_name, opts=None, key_name=None, key_name_prefix=None, public_key=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an [EC2 key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) resource. A key pair is used to control login access to EC2 instances.

        Currently this resource requires an existing user-supplied key pair. This key pair's public key will be registered with AWS to allow logging-in to EC2 instances.

        When importing an existing key pair the public key material may be in any format supported by AWS. Supported formats (per the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws)) are:

        * OpenSSH public key format (the format in ~/.ssh/authorized_keys)
        * Base64 encoded DER format
        * SSH public key file format as specified in RFC4716

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        deployer = aws.ec2.KeyPair("deployer", public_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3F6tyPEFEzV0LX3X8BsXdMsQz1x2cEikKDEY0aIj41qgxMCP/iteneqXSIFZBp5vizPvaoIR3Um9xK7PGoW8giupGn+EPuxIA4cDM4vzOqOkiMPhz5XK0whEjkVzTo4+S0puvDZuwIsdiW9mxhJc7tgBNL0cYlWSYVkz4G/fslNfRPW5mYAM49f4fhtxPb5ok4Q2Lg9dPKVHO/Bgeu5woMc7RY0p1ej6D4CKFE6lymSDJpW0YHX/wqE9+cfEauh7xZcG0q9t2ta6F6fmX0agvpFyZo8aFbXeUBr7osSCJNgvavWbM/06niWrOvYX2xwWdhXmXSrbX8ZbabVohBK41 email@example.com")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_name: The name for the key pair.
        :param pulumi.Input[str] key_name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `key_name`.
        :param pulumi.Input[str] public_key: The public key material.
        :param pulumi.Input[dict] tags: Key-value map of resource tags
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

            __props__['key_name'] = key_name
            __props__['key_name_prefix'] = key_name_prefix
            if public_key is None:
                raise TypeError("Missing required property 'public_key'")
            __props__['public_key'] = public_key
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['fingerprint'] = None
            __props__['key_pair_id'] = None
        super(KeyPair, __self__).__init__(
            'aws:ec2/keyPair:KeyPair',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, fingerprint=None, key_name=None, key_name_prefix=None, key_pair_id=None, public_key=None, tags=None):
        """
        Get an existing KeyPair resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The key pair ARN.
        :param pulumi.Input[str] fingerprint: The MD5 public key fingerprint as specified in section 4 of RFC 4716.
        :param pulumi.Input[str] key_name: The name for the key pair.
        :param pulumi.Input[str] key_name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `key_name`.
        :param pulumi.Input[str] key_pair_id: The key pair ID.
        :param pulumi.Input[str] public_key: The public key material.
        :param pulumi.Input[dict] tags: Key-value map of resource tags
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["fingerprint"] = fingerprint
        __props__["key_name"] = key_name
        __props__["key_name_prefix"] = key_name_prefix
        __props__["key_pair_id"] = key_pair_id
        __props__["public_key"] = public_key
        __props__["tags"] = tags
        return KeyPair(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
