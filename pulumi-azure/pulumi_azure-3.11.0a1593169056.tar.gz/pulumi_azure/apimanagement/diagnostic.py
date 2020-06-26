# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Diagnostic(pulumi.CustomResource):
    api_management_logger_id: pulumi.Output[str]
    """
    The id of the target API Management Logger where the API Management Diagnostic should be saved.
    """
    api_management_name: pulumi.Output[str]
    """
    The Name of the API Management Service where this Diagnostic should be created. Changing this forces a new resource to be created.
    """
    enabled: pulumi.Output[bool]
    identifier: pulumi.Output[str]
    """
    The diagnostic identifier for the API Management Service. At this time the only supported value is `applicationinsights`. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, api_management_logger_id=None, api_management_name=None, enabled=None, identifier=None, resource_group_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an API Management Service Diagnostic.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_insights = azure.appinsights.Insights("exampleInsights",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            application_type="web")
        example_service = azure.apimanagement.Service("exampleService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            publisher_name="My Company",
            publisher_email="company@mycompany.io",
            sku_name="Developer_1")
        example_logger = azure.apimanagement.Logger("exampleLogger",
            api_management_name=example_service.name,
            resource_group_name=example_resource_group.name,
            application_insights={
                "instrumentation_key": example_insights.instrumentation_key,
            })
        example_diagnostic = azure.apimanagement.Diagnostic("exampleDiagnostic",
            identifier="applicationinsights",
            resource_group_name=example_resource_group.name,
            api_management_name=example_service.name,
            api_management_logger_id=example_logger.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_logger_id: The id of the target API Management Logger where the API Management Diagnostic should be saved.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this Diagnostic should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] identifier: The diagnostic identifier for the API Management Service. At this time the only supported value is `applicationinsights`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
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

            if api_management_logger_id is None:
                raise TypeError("Missing required property 'api_management_logger_id'")
            __props__['api_management_logger_id'] = api_management_logger_id
            if api_management_name is None:
                raise TypeError("Missing required property 'api_management_name'")
            __props__['api_management_name'] = api_management_name
            if enabled is not None:
                warnings.warn("this property has been removed from the API and will be removed in version 3.0 of the provider", DeprecationWarning)
                pulumi.log.warn("enabled is deprecated: this property has been removed from the API and will be removed in version 3.0 of the provider")
            __props__['enabled'] = enabled
            if identifier is None:
                raise TypeError("Missing required property 'identifier'")
            __props__['identifier'] = identifier
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
        super(Diagnostic, __self__).__init__(
            'azure:apimanagement/diagnostic:Diagnostic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, api_management_logger_id=None, api_management_name=None, enabled=None, identifier=None, resource_group_name=None):
        """
        Get an existing Diagnostic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_logger_id: The id of the target API Management Logger where the API Management Diagnostic should be saved.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this Diagnostic should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] identifier: The diagnostic identifier for the API Management Service. At this time the only supported value is `applicationinsights`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_management_logger_id"] = api_management_logger_id
        __props__["api_management_name"] = api_management_name
        __props__["enabled"] = enabled
        __props__["identifier"] = identifier
        __props__["resource_group_name"] = resource_group_name
        return Diagnostic(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
