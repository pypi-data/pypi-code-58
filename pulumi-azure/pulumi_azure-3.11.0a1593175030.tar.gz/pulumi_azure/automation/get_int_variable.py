# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetIntVariableResult:
    """
    A collection of values returned by getIntVariable.
    """
    def __init__(__self__, automation_account_name=None, description=None, encrypted=None, id=None, name=None, resource_group_name=None, value=None):
        if automation_account_name and not isinstance(automation_account_name, str):
            raise TypeError("Expected argument 'automation_account_name' to be a str")
        __self__.automation_account_name = automation_account_name
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the Automation Variable.
        """
        if encrypted and not isinstance(encrypted, bool):
            raise TypeError("Expected argument 'encrypted' to be a bool")
        __self__.encrypted = encrypted
        """
        Specifies if the Automation Variable is encrypted. Defaults to `false`.
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
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if value and not isinstance(value, float):
            raise TypeError("Expected argument 'value' to be a float")
        __self__.value = value
        """
        The value of the Automation Variable as a `integer`.
        """
class AwaitableGetIntVariableResult(GetIntVariableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIntVariableResult(
            automation_account_name=self.automation_account_name,
            description=self.description,
            encrypted=self.encrypted,
            id=self.id,
            name=self.name,
            resource_group_name=self.resource_group_name,
            value=self.value)

def get_int_variable(automation_account_name=None,name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing Automation Int Variable.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.automation.get_int_variable(name="tfex-example-var",
        resource_group_name="tfex-example-rg",
        automation_account_name="tfex-example-account")
    pulumi.export("variableId", example.id)
    ```


    :param str automation_account_name: The name of the automation account in which the Automation Variable exists.
    :param str name: The name of the Automation Variable.
    :param str resource_group_name: The Name of the Resource Group where the automation account exists.
    """
    __args__ = dict()


    __args__['automationAccountName'] = automation_account_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:automation/getIntVariable:getIntVariable', __args__, opts=opts).value

    return AwaitableGetIntVariableResult(
        automation_account_name=__ret__.get('automationAccountName'),
        description=__ret__.get('description'),
        encrypted=__ret__.get('encrypted'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        resource_group_name=__ret__.get('resourceGroupName'),
        value=__ret__.get('value'))
