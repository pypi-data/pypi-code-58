# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class NetworkWatcherFlowLog(pulumi.CustomResource):
    enabled: pulumi.Output[bool]
    """
    Boolean flag to enable/disable traffic analytics.
    """
    network_security_group_id: pulumi.Output[str]
    """
    The ID of the Network Security Group for which to enable flow logs for. Changing this forces a new resource to be created.
    """
    network_watcher_name: pulumi.Output[str]
    """
    The name of the Network Watcher. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which the Network Watcher was deployed. Changing this forces a new resource to be created.
    """
    retention_policy: pulumi.Output[dict]
    """
    A `retention_policy` block as documented below.

      * `days` (`float`) - The number of days to retain flow log records.
      * `enabled` (`bool`) - Boolean flag to enable/disable traffic analytics.
    """
    storage_account_id: pulumi.Output[str]
    """
    The ID of the Storage Account where flow logs are stored.
    """
    traffic_analytics: pulumi.Output[dict]
    """
    A `traffic_analytics` block as documented below.

      * `enabled` (`bool`) - Boolean flag to enable/disable traffic analytics.
      * `intervalInMinutes` (`float`) - How frequently service should do flow analytics in minutes.
      * `workspace_id` (`str`) - The resource guid of the attached workspace.
      * `workspaceRegion` (`str`) - The location of the attached workspace.
      * `workspace_resource_id` (`str`) - The resource ID of the attached workspace.
    """
    version: pulumi.Output[float]
    """
    The version (revision) of the flow log. Possible values are `1` and `2`.
    """
    def __init__(__self__, resource_name, opts=None, enabled=None, network_security_group_id=None, network_watcher_name=None, resource_group_name=None, retention_policy=None, storage_account_id=None, traffic_analytics=None, version=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Network Watcher Flow Log.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        test_resource_group = azure.core.ResourceGroup("testResourceGroup", location="eastus")
        test_network_security_group = azure.network.NetworkSecurityGroup("testNetworkSecurityGroup",
            location=test_resource_group.location,
            resource_group_name=test_resource_group.name)
        test_network_watcher = azure.network.NetworkWatcher("testNetworkWatcher",
            location=test_resource_group.location,
            resource_group_name=test_resource_group.name)
        test_account = azure.storage.Account("testAccount",
            resource_group_name=test_resource_group.name,
            location=test_resource_group.location,
            account_tier="Standard",
            account_kind="StorageV2",
            account_replication_type="LRS",
            enable_https_traffic_only=True)
        test_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("testAnalyticsWorkspace",
            location=test_resource_group.location,
            resource_group_name=test_resource_group.name,
            sku="PerGB2018")
        test_network_watcher_flow_log = azure.network.NetworkWatcherFlowLog("testNetworkWatcherFlowLog",
            network_watcher_name=test_network_watcher.name,
            resource_group_name=test_resource_group.name,
            network_security_group_id=test_network_security_group.id,
            storage_account_id=test_account.id,
            enabled=True,
            retention_policy={
                "enabled": True,
                "days": 7,
            },
            traffic_analytics={
                "enabled": True,
                "workspace_id": test_analytics_workspace.workspace_id,
                "workspaceRegion": test_analytics_workspace.location,
                "workspace_resource_id": test_analytics_workspace.id,
                "intervalInMinutes": 10,
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Boolean flag to enable/disable traffic analytics.
        :param pulumi.Input[str] network_security_group_id: The ID of the Network Security Group for which to enable flow logs for. Changing this forces a new resource to be created.
        :param pulumi.Input[str] network_watcher_name: The name of the Network Watcher. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Network Watcher was deployed. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] retention_policy: A `retention_policy` block as documented below.
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account where flow logs are stored.
        :param pulumi.Input[dict] traffic_analytics: A `traffic_analytics` block as documented below.
        :param pulumi.Input[float] version: The version (revision) of the flow log. Possible values are `1` and `2`.

        The **retention_policy** object supports the following:

          * `days` (`pulumi.Input[float]`) - The number of days to retain flow log records.
          * `enabled` (`pulumi.Input[bool]`) - Boolean flag to enable/disable traffic analytics.

        The **traffic_analytics** object supports the following:

          * `enabled` (`pulumi.Input[bool]`) - Boolean flag to enable/disable traffic analytics.
          * `intervalInMinutes` (`pulumi.Input[float]`) - How frequently service should do flow analytics in minutes.
          * `workspace_id` (`pulumi.Input[str]`) - The resource guid of the attached workspace.
          * `workspaceRegion` (`pulumi.Input[str]`) - The location of the attached workspace.
          * `workspace_resource_id` (`pulumi.Input[str]`) - The resource ID of the attached workspace.
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

            if enabled is None:
                raise TypeError("Missing required property 'enabled'")
            __props__['enabled'] = enabled
            if network_security_group_id is None:
                raise TypeError("Missing required property 'network_security_group_id'")
            __props__['network_security_group_id'] = network_security_group_id
            if network_watcher_name is None:
                raise TypeError("Missing required property 'network_watcher_name'")
            __props__['network_watcher_name'] = network_watcher_name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if retention_policy is None:
                raise TypeError("Missing required property 'retention_policy'")
            __props__['retention_policy'] = retention_policy
            if storage_account_id is None:
                raise TypeError("Missing required property 'storage_account_id'")
            __props__['storage_account_id'] = storage_account_id
            __props__['traffic_analytics'] = traffic_analytics
            __props__['version'] = version
        super(NetworkWatcherFlowLog, __self__).__init__(
            'azure:network/networkWatcherFlowLog:NetworkWatcherFlowLog',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, enabled=None, network_security_group_id=None, network_watcher_name=None, resource_group_name=None, retention_policy=None, storage_account_id=None, traffic_analytics=None, version=None):
        """
        Get an existing NetworkWatcherFlowLog resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Boolean flag to enable/disable traffic analytics.
        :param pulumi.Input[str] network_security_group_id: The ID of the Network Security Group for which to enable flow logs for. Changing this forces a new resource to be created.
        :param pulumi.Input[str] network_watcher_name: The name of the Network Watcher. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Network Watcher was deployed. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] retention_policy: A `retention_policy` block as documented below.
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account where flow logs are stored.
        :param pulumi.Input[dict] traffic_analytics: A `traffic_analytics` block as documented below.
        :param pulumi.Input[float] version: The version (revision) of the flow log. Possible values are `1` and `2`.

        The **retention_policy** object supports the following:

          * `days` (`pulumi.Input[float]`) - The number of days to retain flow log records.
          * `enabled` (`pulumi.Input[bool]`) - Boolean flag to enable/disable traffic analytics.

        The **traffic_analytics** object supports the following:

          * `enabled` (`pulumi.Input[bool]`) - Boolean flag to enable/disable traffic analytics.
          * `intervalInMinutes` (`pulumi.Input[float]`) - How frequently service should do flow analytics in minutes.
          * `workspace_id` (`pulumi.Input[str]`) - The resource guid of the attached workspace.
          * `workspaceRegion` (`pulumi.Input[str]`) - The location of the attached workspace.
          * `workspace_resource_id` (`pulumi.Input[str]`) - The resource ID of the attached workspace.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["enabled"] = enabled
        __props__["network_security_group_id"] = network_security_group_id
        __props__["network_watcher_name"] = network_watcher_name
        __props__["resource_group_name"] = resource_group_name
        __props__["retention_policy"] = retention_policy
        __props__["storage_account_id"] = storage_account_id
        __props__["traffic_analytics"] = traffic_analytics
        __props__["version"] = version
        return NetworkWatcherFlowLog(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
