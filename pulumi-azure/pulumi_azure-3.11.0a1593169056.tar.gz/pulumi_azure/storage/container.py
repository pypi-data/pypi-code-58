# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Container(pulumi.CustomResource):
    container_access_type: pulumi.Output[str]
    """
    The Access Level configured for this Container. Possible values are `blob`, `container` or `private`. Defaults to `private`.
    """
    has_immutability_policy: pulumi.Output[bool]
    """
    Is there an Immutability Policy configured on this Storage Container?
    """
    has_legal_hold: pulumi.Output[bool]
    """
    Is there a Legal Hold configured on this Storage Container?
    """
    metadata: pulumi.Output[dict]
    """
    A mapping of MetaData for this Container.
    """
    name: pulumi.Output[str]
    """
    The name of the Container which should be created within the Storage Account.
    """
    resource_manager_id: pulumi.Output[str]
    """
    The Resource Manager ID of this Storage Container.
    """
    storage_account_name: pulumi.Output[str]
    """
    The name of the Storage Account where the Container should be created.
    """
    def __init__(__self__, resource_name, opts=None, container_access_type=None, metadata=None, name=None, storage_account_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Container within an Azure Storage Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS",
            tags={
                "environment": "staging",
            })
        example_container = azure.storage.Container("exampleContainer",
            storage_account_name=example_account.name,
            container_access_type="private")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_access_type: The Access Level configured for this Container. Possible values are `blob`, `container` or `private`. Defaults to `private`.
        :param pulumi.Input[dict] metadata: A mapping of MetaData for this Container.
        :param pulumi.Input[str] name: The name of the Container which should be created within the Storage Account.
        :param pulumi.Input[str] storage_account_name: The name of the Storage Account where the Container should be created.
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

            __props__['container_access_type'] = container_access_type
            __props__['metadata'] = metadata
            __props__['name'] = name
            if storage_account_name is None:
                raise TypeError("Missing required property 'storage_account_name'")
            __props__['storage_account_name'] = storage_account_name
            __props__['has_immutability_policy'] = None
            __props__['has_legal_hold'] = None
            __props__['resource_manager_id'] = None
        super(Container, __self__).__init__(
            'azure:storage/container:Container',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, container_access_type=None, has_immutability_policy=None, has_legal_hold=None, metadata=None, name=None, resource_manager_id=None, storage_account_name=None):
        """
        Get an existing Container resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_access_type: The Access Level configured for this Container. Possible values are `blob`, `container` or `private`. Defaults to `private`.
        :param pulumi.Input[bool] has_immutability_policy: Is there an Immutability Policy configured on this Storage Container?
        :param pulumi.Input[bool] has_legal_hold: Is there a Legal Hold configured on this Storage Container?
        :param pulumi.Input[dict] metadata: A mapping of MetaData for this Container.
        :param pulumi.Input[str] name: The name of the Container which should be created within the Storage Account.
        :param pulumi.Input[str] resource_manager_id: The Resource Manager ID of this Storage Container.
        :param pulumi.Input[str] storage_account_name: The name of the Storage Account where the Container should be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["container_access_type"] = container_access_type
        __props__["has_immutability_policy"] = has_immutability_policy
        __props__["has_legal_hold"] = has_legal_hold
        __props__["metadata"] = metadata
        __props__["name"] = name
        __props__["resource_manager_id"] = resource_manager_id
        __props__["storage_account_name"] = storage_account_name
        return Container(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
