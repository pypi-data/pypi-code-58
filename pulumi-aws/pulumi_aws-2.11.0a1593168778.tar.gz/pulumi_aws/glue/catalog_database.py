# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class CatalogDatabase(pulumi.CustomResource):
    catalog_id: pulumi.Output[str]
    """
    ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.
    """
    description: pulumi.Output[str]
    """
    Description of the database.
    """
    location_uri: pulumi.Output[str]
    """
    The location of the database (for example, an HDFS path).
    """
    name: pulumi.Output[str]
    """
    The name of the database.
    """
    parameters: pulumi.Output[dict]
    """
    A list of key-value pairs that define parameters and properties of the database.
    """
    def __init__(__self__, resource_name, opts=None, catalog_id=None, description=None, location_uri=None, name=None, parameters=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Glue Catalog Database Resource. You can refer to the [Glue Developer Guide](http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) for a full explanation of the Glue Data Catalog functionality

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        aws_glue_catalog_database = aws.glue.CatalogDatabase("awsGlueCatalogDatabase", name="MyCatalogDatabase")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] catalog_id: ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.
        :param pulumi.Input[str] description: Description of the database.
        :param pulumi.Input[str] location_uri: The location of the database (for example, an HDFS path).
        :param pulumi.Input[str] name: The name of the database.
        :param pulumi.Input[dict] parameters: A list of key-value pairs that define parameters and properties of the database.
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

            __props__['catalog_id'] = catalog_id
            __props__['description'] = description
            __props__['location_uri'] = location_uri
            __props__['name'] = name
            __props__['parameters'] = parameters
        super(CatalogDatabase, __self__).__init__(
            'aws:glue/catalogDatabase:CatalogDatabase',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, catalog_id=None, description=None, location_uri=None, name=None, parameters=None):
        """
        Get an existing CatalogDatabase resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] catalog_id: ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.
        :param pulumi.Input[str] description: Description of the database.
        :param pulumi.Input[str] location_uri: The location of the database (for example, an HDFS path).
        :param pulumi.Input[str] name: The name of the database.
        :param pulumi.Input[dict] parameters: A list of key-value pairs that define parameters and properties of the database.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["catalog_id"] = catalog_id
        __props__["description"] = description
        __props__["location_uri"] = location_uri
        __props__["name"] = name
        __props__["parameters"] = parameters
        return CatalogDatabase(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
