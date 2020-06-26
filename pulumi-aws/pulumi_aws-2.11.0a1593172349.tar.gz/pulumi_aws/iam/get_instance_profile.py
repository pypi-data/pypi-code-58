# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetInstanceProfileResult:
    """
    A collection of values returned by getInstanceProfile.
    """
    def __init__(__self__, arn=None, create_date=None, id=None, name=None, path=None, role_arn=None, role_id=None, role_name=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The Amazon Resource Name (ARN) specifying the instance profile.
        """
        if create_date and not isinstance(create_date, str):
            raise TypeError("Expected argument 'create_date' to be a str")
        __self__.create_date = create_date
        """
        The string representation of the date the instance profile
        was created.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        __self__.path = path
        """
        The path to the instance profile.
        """
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        __self__.role_arn = role_arn
        """
        The role arn associated with this instance profile.
        """
        if role_id and not isinstance(role_id, str):
            raise TypeError("Expected argument 'role_id' to be a str")
        __self__.role_id = role_id
        """
        The role id associated with this instance profile.
        """
        if role_name and not isinstance(role_name, str):
            raise TypeError("Expected argument 'role_name' to be a str")
        __self__.role_name = role_name
        """
        The role name associated with this instance profile.
        """
class AwaitableGetInstanceProfileResult(GetInstanceProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceProfileResult(
            arn=self.arn,
            create_date=self.create_date,
            id=self.id,
            name=self.name,
            path=self.path,
            role_arn=self.role_arn,
            role_id=self.role_id,
            role_name=self.role_name)

def get_instance_profile(name=None,opts=None):
    """
    This data source can be used to fetch information about a specific
    IAM instance profile. By using this data source, you can reference IAM
    instance profile properties without having to hard code ARNs as input.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.iam.get_instance_profile(name="an_example_instance_profile_name")
    ```


    :param str name: The friendly IAM instance profile name to match.
    """
    __args__ = dict()


    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:iam/getInstanceProfile:getInstanceProfile', __args__, opts=opts).value

    return AwaitableGetInstanceProfileResult(
        arn=__ret__.get('arn'),
        create_date=__ret__.get('createDate'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        path=__ret__.get('path'),
        role_arn=__ret__.get('roleArn'),
        role_id=__ret__.get('roleId'),
        role_name=__ret__.get('roleName'))
