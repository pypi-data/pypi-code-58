# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetResourcePolicyResult:
    """
    A collection of values returned by getResourcePolicy.
    """
    def __init__(__self__, description=None, id=None, name=None, project=None, region=None, self_link=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        Description of this Resource Policy.
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
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        __self__.project = project
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        __self__.self_link = self_link
        """
        The URI of the resource.
        """
class AwaitableGetResourcePolicyResult(GetResourcePolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourcePolicyResult(
            description=self.description,
            id=self.id,
            name=self.name,
            project=self.project,
            region=self.region,
            self_link=self.self_link)

def get_resource_policy(name=None,project=None,region=None,opts=None):
    """
    Provide access to a Resource Policy's attributes. For more information see [the official documentation](https://cloud.google.com/compute/docs/disks/scheduled-snapshots) or the [API](https://cloud.google.com/compute/docs/reference/rest/beta/resourcePolicies).

    ```python
    import pulumi
    import pulumi_gcp as gcp

    daily = gcp.compute.get_resource_policy(name="daily",
        region="us-central1")
    ```


    :param str name: The name of the Resource Policy.
    :param str project: Project from which to list the Resource Policy. Defaults to project declared in the provider.
    :param str region: Region where the Resource Policy resides.
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['project'] = project
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:compute/getResourcePolicy:getResourcePolicy', __args__, opts=opts).value

    return AwaitableGetResourcePolicyResult(
        description=__ret__.get('description'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        project=__ret__.get('project'),
        region=__ret__.get('region'),
        self_link=__ret__.get('selfLink'))
