# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetClusterNodePoolResult:
    """
    A collection of values returned by getClusterNodePool.
    """
    def __init__(__self__, availability_zones=None, enable_auto_scaling=None, enable_node_public_ip=None, eviction_policy=None, id=None, kubernetes_cluster_name=None, max_count=None, max_pods=None, min_count=None, mode=None, name=None, node_count=None, node_labels=None, node_taints=None, orchestrator_version=None, os_disk_size_gb=None, os_type=None, priority=None, resource_group_name=None, spot_max_price=None, tags=None, vm_size=None, vnet_subnet_id=None):
        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError("Expected argument 'availability_zones' to be a list")
        __self__.availability_zones = availability_zones
        """
        A list of Availability Zones in which the Nodes in this Node Pool exists.
        """
        if enable_auto_scaling and not isinstance(enable_auto_scaling, bool):
            raise TypeError("Expected argument 'enable_auto_scaling' to be a bool")
        __self__.enable_auto_scaling = enable_auto_scaling
        """
        Does this Node Pool have Auto-Scaling enabled?
        """
        if enable_node_public_ip and not isinstance(enable_node_public_ip, bool):
            raise TypeError("Expected argument 'enable_node_public_ip' to be a bool")
        __self__.enable_node_public_ip = enable_node_public_ip
        """
        Do nodes in this Node Pool have a Public IP Address?
        """
        if eviction_policy and not isinstance(eviction_policy, str):
            raise TypeError("Expected argument 'eviction_policy' to be a str")
        __self__.eviction_policy = eviction_policy
        """
        The eviction policy used for Virtual Machines in the Virtual Machine Scale Set, when `priority` is set to `Spot`.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if kubernetes_cluster_name and not isinstance(kubernetes_cluster_name, str):
            raise TypeError("Expected argument 'kubernetes_cluster_name' to be a str")
        __self__.kubernetes_cluster_name = kubernetes_cluster_name
        if max_count and not isinstance(max_count, float):
            raise TypeError("Expected argument 'max_count' to be a float")
        __self__.max_count = max_count
        """
        The maximum number of Nodes allowed when auto-scaling is enabled.
        """
        if max_pods and not isinstance(max_pods, float):
            raise TypeError("Expected argument 'max_pods' to be a float")
        __self__.max_pods = max_pods
        """
        The maximum number of Pods allowed on each Node in this Node Pool.
        """
        if min_count and not isinstance(min_count, float):
            raise TypeError("Expected argument 'min_count' to be a float")
        __self__.min_count = min_count
        """
        The minimum number of Nodes allowed when auto-scaling is enabled.
        """
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        __self__.mode = mode
        """
        The Mode for this Node Pool, specifying how these Nodes should be used (for either System or User resources).
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if node_count and not isinstance(node_count, float):
            raise TypeError("Expected argument 'node_count' to be a float")
        __self__.node_count = node_count
        """
        The current number of Nodes in the Node Pool.
        """
        if node_labels and not isinstance(node_labels, dict):
            raise TypeError("Expected argument 'node_labels' to be a dict")
        __self__.node_labels = node_labels
        """
        A map of Kubernetes Labels applied to each Node in this Node Pool.
        """
        if node_taints and not isinstance(node_taints, list):
            raise TypeError("Expected argument 'node_taints' to be a list")
        __self__.node_taints = node_taints
        """
        A map of Kubernetes Taints applied to each Node in this Node Pool.
        """
        if orchestrator_version and not isinstance(orchestrator_version, str):
            raise TypeError("Expected argument 'orchestrator_version' to be a str")
        __self__.orchestrator_version = orchestrator_version
        """
        The version of Kubernetes configured on each Node in this Node Pool.
        """
        if os_disk_size_gb and not isinstance(os_disk_size_gb, float):
            raise TypeError("Expected argument 'os_disk_size_gb' to be a float")
        __self__.os_disk_size_gb = os_disk_size_gb
        """
        The size of the OS Disk on each Node in this Node Pool.
        """
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        __self__.os_type = os_type
        """
        The operating system used on each Node in this Node Pool.
        """
        if priority and not isinstance(priority, str):
            raise TypeError("Expected argument 'priority' to be a str")
        __self__.priority = priority
        """
        The priority of the Virtual Machines in the Virtual Machine Scale Set backing this Node Pool.
        """
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if spot_max_price and not isinstance(spot_max_price, float):
            raise TypeError("Expected argument 'spot_max_price' to be a float")
        __self__.spot_max_price = spot_max_price
        """
        The maximum price being paid for Virtual Machines in this Scale Set. `-1` means the current on-demand price for a Virtual Machine.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags assigned to the Kubernetes Cluster Node Pool.
        """
        if vm_size and not isinstance(vm_size, str):
            raise TypeError("Expected argument 'vm_size' to be a str")
        __self__.vm_size = vm_size
        """
        The size of the Virtual Machines used in the Virtual Machine Scale Set backing this Node Pool.
        """
        if vnet_subnet_id and not isinstance(vnet_subnet_id, str):
            raise TypeError("Expected argument 'vnet_subnet_id' to be a str")
        __self__.vnet_subnet_id = vnet_subnet_id
        """
        The ID of the Subnet in which this Node Pool exists.
        """
class AwaitableGetClusterNodePoolResult(GetClusterNodePoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterNodePoolResult(
            availability_zones=self.availability_zones,
            enable_auto_scaling=self.enable_auto_scaling,
            enable_node_public_ip=self.enable_node_public_ip,
            eviction_policy=self.eviction_policy,
            id=self.id,
            kubernetes_cluster_name=self.kubernetes_cluster_name,
            max_count=self.max_count,
            max_pods=self.max_pods,
            min_count=self.min_count,
            mode=self.mode,
            name=self.name,
            node_count=self.node_count,
            node_labels=self.node_labels,
            node_taints=self.node_taints,
            orchestrator_version=self.orchestrator_version,
            os_disk_size_gb=self.os_disk_size_gb,
            os_type=self.os_type,
            priority=self.priority,
            resource_group_name=self.resource_group_name,
            spot_max_price=self.spot_max_price,
            tags=self.tags,
            vm_size=self.vm_size,
            vnet_subnet_id=self.vnet_subnet_id)

def get_cluster_node_pool(kubernetes_cluster_name=None,name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing Kubernetes Cluster Node Pool.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.containerservice.get_cluster_node_pool(name="existing",
        kubernetes_cluster_name="existing-cluster",
        resource_group_name="existing-resource-group")
    pulumi.export("id", example.id)
    ```


    :param str kubernetes_cluster_name: The Name of the Kubernetes Cluster where this Node Pool is located.
    :param str name: The name of this Kubernetes Cluster Node Pool.
    :param str resource_group_name: The name of the Resource Group where the Kubernetes Cluster exists.
    """
    __args__ = dict()


    __args__['kubernetesClusterName'] = kubernetes_cluster_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:containerservice/getClusterNodePool:getClusterNodePool', __args__, opts=opts).value

    return AwaitableGetClusterNodePoolResult(
        availability_zones=__ret__.get('availabilityZones'),
        enable_auto_scaling=__ret__.get('enableAutoScaling'),
        enable_node_public_ip=__ret__.get('enableNodePublicIp'),
        eviction_policy=__ret__.get('evictionPolicy'),
        id=__ret__.get('id'),
        kubernetes_cluster_name=__ret__.get('kubernetesClusterName'),
        max_count=__ret__.get('maxCount'),
        max_pods=__ret__.get('maxPods'),
        min_count=__ret__.get('minCount'),
        mode=__ret__.get('mode'),
        name=__ret__.get('name'),
        node_count=__ret__.get('nodeCount'),
        node_labels=__ret__.get('nodeLabels'),
        node_taints=__ret__.get('nodeTaints'),
        orchestrator_version=__ret__.get('orchestratorVersion'),
        os_disk_size_gb=__ret__.get('osDiskSizeGb'),
        os_type=__ret__.get('osType'),
        priority=__ret__.get('priority'),
        resource_group_name=__ret__.get('resourceGroupName'),
        spot_max_price=__ret__.get('spotMaxPrice'),
        tags=__ret__.get('tags'),
        vm_size=__ret__.get('vmSize'),
        vnet_subnet_id=__ret__.get('vnetSubnetId'))
