# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetSecretVersionResult:
    """
    A collection of values returned by getSecretVersion.
    """
    def __init__(__self__, arn=None, id=None, secret_binary=None, secret_id=None, secret_string=None, version_id=None, version_stage=None, version_stages=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The ARN of the secret.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if secret_binary and not isinstance(secret_binary, str):
            raise TypeError("Expected argument 'secret_binary' to be a str")
        __self__.secret_binary = secret_binary
        """
        The decrypted part of the protected secret information that was originally provided as a binary. Base64 encoded.
        """
        if secret_id and not isinstance(secret_id, str):
            raise TypeError("Expected argument 'secret_id' to be a str")
        __self__.secret_id = secret_id
        if secret_string and not isinstance(secret_string, str):
            raise TypeError("Expected argument 'secret_string' to be a str")
        __self__.secret_string = secret_string
        """
        The decrypted part of the protected secret information that was originally provided as a string.
        """
        if version_id and not isinstance(version_id, str):
            raise TypeError("Expected argument 'version_id' to be a str")
        __self__.version_id = version_id
        """
        The unique identifier of this version of the secret.
        """
        if version_stage and not isinstance(version_stage, str):
            raise TypeError("Expected argument 'version_stage' to be a str")
        __self__.version_stage = version_stage
        if version_stages and not isinstance(version_stages, list):
            raise TypeError("Expected argument 'version_stages' to be a list")
        __self__.version_stages = version_stages
class AwaitableGetSecretVersionResult(GetSecretVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretVersionResult(
            arn=self.arn,
            id=self.id,
            secret_binary=self.secret_binary,
            secret_id=self.secret_id,
            secret_string=self.secret_string,
            version_id=self.version_id,
            version_stage=self.version_stage,
            version_stages=self.version_stages)

def get_secret_version(secret_id=None,version_id=None,version_stage=None,opts=None):
    """
    Retrieve information about a Secrets Manager secret version, including its secret value. To retrieve secret metadata, see the `secretsmanager.Secret` data source.

    ## Example Usage
    ### Retrieve Current Secret Version

    By default, this data sources retrieves information based on the `AWSCURRENT` staging label.

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.secretsmanager.get_secret_version(secret_id=data["aws_secretsmanager_secret"]["example"]["id"])
    ```
    ### Retrieve Specific Secret Version

    ```python
    import pulumi
    import pulumi_aws as aws

    by_version_stage = aws.secretsmanager.get_secret_version(secret_id=data["aws_secretsmanager_secret"]["example"]["id"],
        version_stage="example")
    ```


    :param str secret_id: Specifies the secret containing the version that you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
    :param str version_id: Specifies the unique identifier of the version of the secret that you want to retrieve. Overrides `version_stage`.
    :param str version_stage: Specifies the secret version that you want to retrieve by the staging label attached to the version. Defaults to `AWSCURRENT`.
    """
    __args__ = dict()


    __args__['secretId'] = secret_id
    __args__['versionId'] = version_id
    __args__['versionStage'] = version_stage
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:secretsmanager/getSecretVersion:getSecretVersion', __args__, opts=opts).value

    return AwaitableGetSecretVersionResult(
        arn=__ret__.get('arn'),
        id=__ret__.get('id'),
        secret_binary=__ret__.get('secretBinary'),
        secret_id=__ret__.get('secretId'),
        secret_string=__ret__.get('secretString'),
        version_id=__ret__.get('versionId'),
        version_stage=__ret__.get('versionStage'),
        version_stages=__ret__.get('versionStages'))
