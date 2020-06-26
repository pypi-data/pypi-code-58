# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class NodeTemplate(pulumi.CustomResource):
    cpu_overcommit_type: pulumi.Output[str]
    """
    CPU overcommit. Default value: "NONE" Possible values: ["ENABLED", "NONE"]
    """
    creation_timestamp: pulumi.Output[str]
    """
    Creation timestamp in RFC3339 text format.
    """
    description: pulumi.Output[str]
    """
    An optional textual description of the resource.
    """
    name: pulumi.Output[str]
    """
    Name of the resource.
    """
    node_affinity_labels: pulumi.Output[dict]
    """
    Labels to use for node affinity, which will be used in
    instance scheduling.
    """
    node_type: pulumi.Output[str]
    """
    Node type to use for nodes group that are created from this template.
    Only one of nodeTypeFlexibility and nodeType can be specified.
    """
    node_type_flexibility: pulumi.Output[dict]
    """
    Flexible properties for the desired node type. Node groups that
    use this node template will create nodes of a type that matches
    these properties. Only one of nodeTypeFlexibility and nodeType can
    be specified.  Structure is documented below.

      * `cpus` (`str`) - Number of virtual CPUs to use.
      * `localSsd` (`str`) - -
        Use local SSD
      * `memory` (`str`) - Physical memory available to the node, defined in MB.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    region: pulumi.Output[str]
    """
    Region where nodes using the node template will be created.
    If it is not provided, the provider region is used.
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    server_binding: pulumi.Output[dict]
    """
    The server binding policy for nodes using this template. Determines
    where the nodes should restart following a maintenance event.  Structure is documented below.

      * `type` (`str`) - Type of server binding policy. If `RESTART_NODE_ON_ANY_SERVER`,
        nodes using this template will restart on any physical server
        following a maintenance event.
        If `RESTART_NODE_ON_MINIMAL_SERVER`, nodes using this template
        will restart on the same physical server following a maintenance
        event, instead of being live migrated to or restarted on a new
        physical server. This option may be useful if you are using
        software licenses tied to the underlying server characteristics
        such as physical sockets or cores, to avoid the need for
        additional licenses when maintenance occurs. However, VMs on such
        nodes will experience outages while maintenance is applied.
    """
    def __init__(__self__, resource_name, opts=None, cpu_overcommit_type=None, description=None, name=None, node_affinity_labels=None, node_type=None, node_type_flexibility=None, project=None, region=None, server_binding=None, __props__=None, __name__=None, __opts__=None):
        """
        Represents a NodeTemplate resource. Node templates specify properties
        for creating sole-tenant nodes, such as node type, vCPU and memory
        requirements, node affinity labels, and region.

        To get more information about NodeTemplate, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/nodeTemplates)
        * How-to Guides
            * [Sole-Tenant Nodes](https://cloud.google.com/compute/docs/nodes/)

        ## Example Usage
        ### Node Template Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        template = gcp.compute.NodeTemplate("template",
            node_type="n1-node-96-624",
            region="us-central1")
        ```
        ### Node Template Server Binding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        central1a = gcp.compute.get_node_types(zone="us-central1-a")
        template = gcp.compute.NodeTemplate("template",
            region="us-central1",
            node_type="n1-node-96-624",
            node_affinity_labels={
                "foo": "baz",
            },
            server_binding={
                "type": "RESTART_NODE_ON_MINIMAL_SERVERS",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cpu_overcommit_type: CPU overcommit. Default value: "NONE" Possible values: ["ENABLED", "NONE"]
        :param pulumi.Input[str] description: An optional textual description of the resource.
        :param pulumi.Input[str] name: Name of the resource.
        :param pulumi.Input[dict] node_affinity_labels: Labels to use for node affinity, which will be used in
               instance scheduling.
        :param pulumi.Input[str] node_type: Node type to use for nodes group that are created from this template.
               Only one of nodeTypeFlexibility and nodeType can be specified.
        :param pulumi.Input[dict] node_type_flexibility: Flexible properties for the desired node type. Node groups that
               use this node template will create nodes of a type that matches
               these properties. Only one of nodeTypeFlexibility and nodeType can
               be specified.  Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where nodes using the node template will be created.
               If it is not provided, the provider region is used.
        :param pulumi.Input[dict] server_binding: The server binding policy for nodes using this template. Determines
               where the nodes should restart following a maintenance event.  Structure is documented below.

        The **node_type_flexibility** object supports the following:

          * `cpus` (`pulumi.Input[str]`) - Number of virtual CPUs to use.
          * `localSsd` (`pulumi.Input[str]`) - -
            Use local SSD
          * `memory` (`pulumi.Input[str]`) - Physical memory available to the node, defined in MB.

        The **server_binding** object supports the following:

          * `type` (`pulumi.Input[str]`) - Type of server binding policy. If `RESTART_NODE_ON_ANY_SERVER`,
            nodes using this template will restart on any physical server
            following a maintenance event.
            If `RESTART_NODE_ON_MINIMAL_SERVER`, nodes using this template
            will restart on the same physical server following a maintenance
            event, instead of being live migrated to or restarted on a new
            physical server. This option may be useful if you are using
            software licenses tied to the underlying server characteristics
            such as physical sockets or cores, to avoid the need for
            additional licenses when maintenance occurs. However, VMs on such
            nodes will experience outages while maintenance is applied.
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

            __props__['cpu_overcommit_type'] = cpu_overcommit_type
            __props__['description'] = description
            __props__['name'] = name
            __props__['node_affinity_labels'] = node_affinity_labels
            __props__['node_type'] = node_type
            __props__['node_type_flexibility'] = node_type_flexibility
            __props__['project'] = project
            __props__['region'] = region
            __props__['server_binding'] = server_binding
            __props__['creation_timestamp'] = None
            __props__['self_link'] = None
        super(NodeTemplate, __self__).__init__(
            'gcp:compute/nodeTemplate:NodeTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, cpu_overcommit_type=None, creation_timestamp=None, description=None, name=None, node_affinity_labels=None, node_type=None, node_type_flexibility=None, project=None, region=None, self_link=None, server_binding=None):
        """
        Get an existing NodeTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cpu_overcommit_type: CPU overcommit. Default value: "NONE" Possible values: ["ENABLED", "NONE"]
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional textual description of the resource.
        :param pulumi.Input[str] name: Name of the resource.
        :param pulumi.Input[dict] node_affinity_labels: Labels to use for node affinity, which will be used in
               instance scheduling.
        :param pulumi.Input[str] node_type: Node type to use for nodes group that are created from this template.
               Only one of nodeTypeFlexibility and nodeType can be specified.
        :param pulumi.Input[dict] node_type_flexibility: Flexible properties for the desired node type. Node groups that
               use this node template will create nodes of a type that matches
               these properties. Only one of nodeTypeFlexibility and nodeType can
               be specified.  Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where nodes using the node template will be created.
               If it is not provided, the provider region is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[dict] server_binding: The server binding policy for nodes using this template. Determines
               where the nodes should restart following a maintenance event.  Structure is documented below.

        The **node_type_flexibility** object supports the following:

          * `cpus` (`pulumi.Input[str]`) - Number of virtual CPUs to use.
          * `localSsd` (`pulumi.Input[str]`) - -
            Use local SSD
          * `memory` (`pulumi.Input[str]`) - Physical memory available to the node, defined in MB.

        The **server_binding** object supports the following:

          * `type` (`pulumi.Input[str]`) - Type of server binding policy. If `RESTART_NODE_ON_ANY_SERVER`,
            nodes using this template will restart on any physical server
            following a maintenance event.
            If `RESTART_NODE_ON_MINIMAL_SERVER`, nodes using this template
            will restart on the same physical server following a maintenance
            event, instead of being live migrated to or restarted on a new
            physical server. This option may be useful if you are using
            software licenses tied to the underlying server characteristics
            such as physical sockets or cores, to avoid the need for
            additional licenses when maintenance occurs. However, VMs on such
            nodes will experience outages while maintenance is applied.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cpu_overcommit_type"] = cpu_overcommit_type
        __props__["creation_timestamp"] = creation_timestamp
        __props__["description"] = description
        __props__["name"] = name
        __props__["node_affinity_labels"] = node_affinity_labels
        __props__["node_type"] = node_type
        __props__["node_type_flexibility"] = node_type_flexibility
        __props__["project"] = project
        __props__["region"] = region
        __props__["self_link"] = self_link
        __props__["server_binding"] = server_binding
        return NodeTemplate(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
