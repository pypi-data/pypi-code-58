# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetWorkflowResult:
    """
    A collection of values returned by getWorkflow.
    """
    def __init__(__self__, access_endpoint=None, connector_endpoint_ip_addresses=None, connector_outbound_ip_addresses=None, id=None, location=None, logic_app_integration_account_id=None, name=None, parameters=None, resource_group_name=None, tags=None, workflow_endpoint_ip_addresses=None, workflow_outbound_ip_addresses=None, workflow_schema=None, workflow_version=None):
        if access_endpoint and not isinstance(access_endpoint, str):
            raise TypeError("Expected argument 'access_endpoint' to be a str")
        __self__.access_endpoint = access_endpoint
        """
        The Access Endpoint for the Logic App Workflow
        """
        if connector_endpoint_ip_addresses and not isinstance(connector_endpoint_ip_addresses, list):
            raise TypeError("Expected argument 'connector_endpoint_ip_addresses' to be a list")
        __self__.connector_endpoint_ip_addresses = connector_endpoint_ip_addresses
        """
        The list of access endpoint ip addresses of connector.
        """
        if connector_outbound_ip_addresses and not isinstance(connector_outbound_ip_addresses, list):
            raise TypeError("Expected argument 'connector_outbound_ip_addresses' to be a list")
        __self__.connector_outbound_ip_addresses = connector_outbound_ip_addresses
        """
        The list of outgoing ip addresses of connector.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        """
        The Azure location where the Logic App Workflow exists.
        """
        if logic_app_integration_account_id and not isinstance(logic_app_integration_account_id, str):
            raise TypeError("Expected argument 'logic_app_integration_account_id' to be a str")
        __self__.logic_app_integration_account_id = logic_app_integration_account_id
        """
        The ID of the integration account linked by this Logic App Workflow.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        __self__.parameters = parameters
        """
        A map of Key-Value pairs.
        """
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags assigned to the resource.
        """
        if workflow_endpoint_ip_addresses and not isinstance(workflow_endpoint_ip_addresses, list):
            raise TypeError("Expected argument 'workflow_endpoint_ip_addresses' to be a list")
        __self__.workflow_endpoint_ip_addresses = workflow_endpoint_ip_addresses
        """
        The list of access endpoint ip addresses of workflow.
        """
        if workflow_outbound_ip_addresses and not isinstance(workflow_outbound_ip_addresses, list):
            raise TypeError("Expected argument 'workflow_outbound_ip_addresses' to be a list")
        __self__.workflow_outbound_ip_addresses = workflow_outbound_ip_addresses
        """
        The list of outgoing ip addresses of workflow.
        """
        if workflow_schema and not isinstance(workflow_schema, str):
            raise TypeError("Expected argument 'workflow_schema' to be a str")
        __self__.workflow_schema = workflow_schema
        """
        The Schema used for this Logic App Workflow.
        """
        if workflow_version and not isinstance(workflow_version, str):
            raise TypeError("Expected argument 'workflow_version' to be a str")
        __self__.workflow_version = workflow_version
        """
        The version of the Schema used for this Logic App Workflow. Defaults to `1.0.0.0`.
        """
class AwaitableGetWorkflowResult(GetWorkflowResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkflowResult(
            access_endpoint=self.access_endpoint,
            connector_endpoint_ip_addresses=self.connector_endpoint_ip_addresses,
            connector_outbound_ip_addresses=self.connector_outbound_ip_addresses,
            id=self.id,
            location=self.location,
            logic_app_integration_account_id=self.logic_app_integration_account_id,
            name=self.name,
            parameters=self.parameters,
            resource_group_name=self.resource_group_name,
            tags=self.tags,
            workflow_endpoint_ip_addresses=self.workflow_endpoint_ip_addresses,
            workflow_outbound_ip_addresses=self.workflow_outbound_ip_addresses,
            workflow_schema=self.workflow_schema,
            workflow_version=self.workflow_version)

def get_workflow(name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing Logic App Workflow.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.logicapps.get_workflow(name="workflow1",
        resource_group_name="my-resource-group")
    pulumi.export("accessEndpoint", example.access_endpoint)
    ```


    :param str name: The name of the Logic App Workflow.
    :param str resource_group_name: The name of the Resource Group in which the Logic App Workflow exists.
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:logicapps/getWorkflow:getWorkflow', __args__, opts=opts).value

    return AwaitableGetWorkflowResult(
        access_endpoint=__ret__.get('accessEndpoint'),
        connector_endpoint_ip_addresses=__ret__.get('connectorEndpointIpAddresses'),
        connector_outbound_ip_addresses=__ret__.get('connectorOutboundIpAddresses'),
        id=__ret__.get('id'),
        location=__ret__.get('location'),
        logic_app_integration_account_id=__ret__.get('logicAppIntegrationAccountId'),
        name=__ret__.get('name'),
        parameters=__ret__.get('parameters'),
        resource_group_name=__ret__.get('resourceGroupName'),
        tags=__ret__.get('tags'),
        workflow_endpoint_ip_addresses=__ret__.get('workflowEndpointIpAddresses'),
        workflow_outbound_ip_addresses=__ret__.get('workflowOutboundIpAddresses'),
        workflow_schema=__ret__.get('workflowSchema'),
        workflow_version=__ret__.get('workflowVersion'))
