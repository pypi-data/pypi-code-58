# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetAccountResult:
    """
    A collection of values returned by getAccount.
    """
    def __init__(__self__, capabilities=None, consistency_policies=None, enable_automatic_failover=None, enable_multiple_write_locations=None, endpoint=None, geo_locations=None, id=None, ip_range_filter=None, is_virtual_network_filter_enabled=None, kind=None, location=None, name=None, offer_type=None, primary_master_key=None, primary_readonly_master_key=None, read_endpoints=None, resource_group_name=None, secondary_master_key=None, secondary_readonly_master_key=None, tags=None, virtual_network_rules=None, write_endpoints=None):
        if capabilities and not isinstance(capabilities, list):
            raise TypeError("Expected argument 'capabilities' to be a list")
        __self__.capabilities = capabilities
        """
        Capabilities enabled on this Cosmos DB account.
        """
        if consistency_policies and not isinstance(consistency_policies, list):
            raise TypeError("Expected argument 'consistency_policies' to be a list")
        __self__.consistency_policies = consistency_policies
        if enable_automatic_failover and not isinstance(enable_automatic_failover, bool):
            raise TypeError("Expected argument 'enable_automatic_failover' to be a bool")
        __self__.enable_automatic_failover = enable_automatic_failover
        """
        If automatic failover is enabled for this CosmosDB Account.
        """
        if enable_multiple_write_locations and not isinstance(enable_multiple_write_locations, bool):
            raise TypeError("Expected argument 'enable_multiple_write_locations' to be a bool")
        __self__.enable_multiple_write_locations = enable_multiple_write_locations
        """
        If multi-master is enabled for this Cosmos DB account.
        """
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        __self__.endpoint = endpoint
        """
        The endpoint used to connect to the CosmosDB account.
        """
        if geo_locations and not isinstance(geo_locations, list):
            raise TypeError("Expected argument 'geo_locations' to be a list")
        __self__.geo_locations = geo_locations
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if ip_range_filter and not isinstance(ip_range_filter, str):
            raise TypeError("Expected argument 'ip_range_filter' to be a str")
        __self__.ip_range_filter = ip_range_filter
        """
        The current IP Filter for this CosmosDB account
        """
        if is_virtual_network_filter_enabled and not isinstance(is_virtual_network_filter_enabled, bool):
            raise TypeError("Expected argument 'is_virtual_network_filter_enabled' to be a bool")
        __self__.is_virtual_network_filter_enabled = is_virtual_network_filter_enabled
        """
        If virtual network filtering is enabled for this Cosmos DB account.
        """
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        __self__.kind = kind
        """
        The Kind of the CosmosDB account.
        """
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        """
        The name of the Azure region hosting replicated data.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if offer_type and not isinstance(offer_type, str):
            raise TypeError("Expected argument 'offer_type' to be a str")
        __self__.offer_type = offer_type
        """
        The Offer Type to used by this CosmosDB Account.
        """
        if primary_master_key and not isinstance(primary_master_key, str):
            raise TypeError("Expected argument 'primary_master_key' to be a str")
        __self__.primary_master_key = primary_master_key
        """
        The Primary master key for the CosmosDB Account.
        """
        if primary_readonly_master_key and not isinstance(primary_readonly_master_key, str):
            raise TypeError("Expected argument 'primary_readonly_master_key' to be a str")
        __self__.primary_readonly_master_key = primary_readonly_master_key
        """
        The Primary read-only master Key for the CosmosDB Account.
        """
        if read_endpoints and not isinstance(read_endpoints, list):
            raise TypeError("Expected argument 'read_endpoints' to be a list")
        __self__.read_endpoints = read_endpoints
        """
        A list of read endpoints available for this CosmosDB account.
        """
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if secondary_master_key and not isinstance(secondary_master_key, str):
            raise TypeError("Expected argument 'secondary_master_key' to be a str")
        __self__.secondary_master_key = secondary_master_key
        """
        The Secondary master key for the CosmosDB Account.
        """
        if secondary_readonly_master_key and not isinstance(secondary_readonly_master_key, str):
            raise TypeError("Expected argument 'secondary_readonly_master_key' to be a str")
        __self__.secondary_readonly_master_key = secondary_readonly_master_key
        """
        The Secondary read-only master key for the CosmosDB Account.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags assigned to the resource.
        """
        if virtual_network_rules and not isinstance(virtual_network_rules, list):
            raise TypeError("Expected argument 'virtual_network_rules' to be a list")
        __self__.virtual_network_rules = virtual_network_rules
        """
        Subnets that are allowed to access this CosmosDB account.
        """
        if write_endpoints and not isinstance(write_endpoints, list):
            raise TypeError("Expected argument 'write_endpoints' to be a list")
        __self__.write_endpoints = write_endpoints
        """
        A list of write endpoints available for this CosmosDB account.
        """
class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            capabilities=self.capabilities,
            consistency_policies=self.consistency_policies,
            enable_automatic_failover=self.enable_automatic_failover,
            enable_multiple_write_locations=self.enable_multiple_write_locations,
            endpoint=self.endpoint,
            geo_locations=self.geo_locations,
            id=self.id,
            ip_range_filter=self.ip_range_filter,
            is_virtual_network_filter_enabled=self.is_virtual_network_filter_enabled,
            kind=self.kind,
            location=self.location,
            name=self.name,
            offer_type=self.offer_type,
            primary_master_key=self.primary_master_key,
            primary_readonly_master_key=self.primary_readonly_master_key,
            read_endpoints=self.read_endpoints,
            resource_group_name=self.resource_group_name,
            secondary_master_key=self.secondary_master_key,
            secondary_readonly_master_key=self.secondary_readonly_master_key,
            tags=self.tags,
            virtual_network_rules=self.virtual_network_rules,
            write_endpoints=self.write_endpoints)

def get_account(name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing CosmosDB (formally DocumentDB) Account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.cosmosdb.get_account(name="tfex-cosmosdb-account",
        resource_group_name="tfex-cosmosdb-account-rg")
    pulumi.export("cosmosdbAccountEndpoint", data["azurerm_cosmosdb_account"]["jobs"]["endpoint"])
    ```


    :param str name: Specifies the name of the CosmosDB Account.
    :param str resource_group_name: Specifies the name of the resource group in which the CosmosDB Account resides.
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:cosmosdb/getAccount:getAccount', __args__, opts=opts).value

    return AwaitableGetAccountResult(
        capabilities=__ret__.get('capabilities'),
        consistency_policies=__ret__.get('consistencyPolicies'),
        enable_automatic_failover=__ret__.get('enableAutomaticFailover'),
        enable_multiple_write_locations=__ret__.get('enableMultipleWriteLocations'),
        endpoint=__ret__.get('endpoint'),
        geo_locations=__ret__.get('geoLocations'),
        id=__ret__.get('id'),
        ip_range_filter=__ret__.get('ipRangeFilter'),
        is_virtual_network_filter_enabled=__ret__.get('isVirtualNetworkFilterEnabled'),
        kind=__ret__.get('kind'),
        location=__ret__.get('location'),
        name=__ret__.get('name'),
        offer_type=__ret__.get('offerType'),
        primary_master_key=__ret__.get('primaryMasterKey'),
        primary_readonly_master_key=__ret__.get('primaryReadonlyMasterKey'),
        read_endpoints=__ret__.get('readEndpoints'),
        resource_group_name=__ret__.get('resourceGroupName'),
        secondary_master_key=__ret__.get('secondaryMasterKey'),
        secondary_readonly_master_key=__ret__.get('secondaryReadonlyMasterKey'),
        tags=__ret__.get('tags'),
        virtual_network_rules=__ret__.get('virtualNetworkRules'),
        write_endpoints=__ret__.get('writeEndpoints'))
