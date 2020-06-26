# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Endpoint(pulumi.CustomResource):
    certificate_arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) for the certificate.
    """
    database_name: pulumi.Output[str]
    """
    The name of the endpoint database.
    """
    elasticsearch_settings: pulumi.Output[dict]
    """
    Configuration block with Elasticsearch settings. Detailed below.

      * `endpointUri` (`str`) - Endpoint for the Elasticsearch cluster.
      * `errorRetryDuration` (`float`) - Maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster. Defaults to `300`.
      * `fullLoadErrorPercentage` (`float`) - Maximum percentage of records that can fail to be written before a full load operation stops. Defaults to `10`.
      * `serviceAccessRoleArn` (`str`) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Elasticsearch cluster.
    """
    endpoint_arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) for the endpoint.
    """
    endpoint_id: pulumi.Output[str]
    """
    The database endpoint identifier.
    """
    endpoint_type: pulumi.Output[str]
    """
    The type of endpoint. Can be one of `source | target`.
    """
    engine_name: pulumi.Output[str]
    """
    The type of engine for the endpoint. Can be one of `aurora | aurora-postgresql| azuredb | db2 | docdb | dynamodb | elasticsearch | kafka | kinesis | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
    """
    extra_connection_attributes: pulumi.Output[str]
    """
    Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
    """
    kafka_settings: pulumi.Output[dict]
    """
    Configuration block with Kafka settings. Detailed below.

      * `broker` (`str`) - Kafka broker location. Specify in the form broker-hostname-or-ip:port.
      * `topic` (`str`) - Kafka topic for migration. Defaults to `kafka-default-topic`.
    """
    kinesis_settings: pulumi.Output[dict]
    """
    Configuration block with Kinesis settings. Detailed below.

      * `messageFormat` (`str`) - Output format for the records created. Defaults to `json`. Valid values are `json` and `json_unformatted` (a single line with no tab).
      * `serviceAccessRoleArn` (`str`) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Kinesis data stream.
      * `stream_arn` (`str`) - Amazon Resource Name (ARN) of the Kinesis data stream.
    """
    kms_key_arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
    """
    mongodb_settings: pulumi.Output[dict]
    """
    Configuration block with MongoDB settings. Detailed below.

      * `authMechanism` (`str`) - Authentication mechanism to access the MongoDB source endpoint. Defaults to `default`.
      * `authSource` (`str`) - Authentication database name. Not used when `auth_type` is `no`. Defaults to `admin`.
      * `auth_type` (`str`) - Authentication type to access the MongoDB source endpoint. Defaults to `password`.
      * `docsToInvestigate` (`str`) - Number of documents to preview to determine the document organization. Use this setting when `nesting_level` is set to `one`. Defaults to `1000`.
      * `extractDocId` (`str`) - Document ID. Use this setting when `nesting_level` is set to `none`. Defaults to `false`.
      * `nestingLevel` (`str`) - Specifies either document or table mode. Defaults to `none`. Valid values are `one` (table mode) and `none` (document mode).
    """
    password: pulumi.Output[str]
    """
    The password to be used to login to the endpoint database.
    """
    port: pulumi.Output[float]
    """
    The port used by the endpoint database.
    """
    s3_settings: pulumi.Output[dict]
    """
    Configuration block with S3 settings. Detailed below.

      * `bucketFolder` (`str`) - S3 Bucket Object prefix.
      * `bucket_name` (`str`) - S3 Bucket name.
      * `compressionType` (`str`) - Set to compress target files. Defaults to `NONE`. Valid values are `GZIP` and `NONE`.
      * `csvDelimiter` (`str`) - Delimiter used to separate columns in the source files. Defaults to `,`.
      * `csvRowDelimiter` (`str`) - Delimiter used to separate rows in the source files. Defaults to `\n`.
      * `externalTableDefinition` (`str`) - JSON document that describes how AWS DMS should interpret the data.
      * `serviceAccessRoleArn` (`str`) - Amazon Resource Name (ARN) of the IAM Role with permissions to read from or write to the S3 Bucket.
    """
    server_name: pulumi.Output[str]
    """
    The host name of the server.
    """
    service_access_role: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
    """
    ssl_mode: pulumi.Output[str]
    """
    The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
    """
    tags: pulumi.Output[dict]
    """
    A map of tags to assign to the resource.
    """
    username: pulumi.Output[str]
    """
    The user name to be used to login to the endpoint database.
    """
    def __init__(__self__, resource_name, opts=None, certificate_arn=None, database_name=None, elasticsearch_settings=None, endpoint_id=None, endpoint_type=None, engine_name=None, extra_connection_attributes=None, kafka_settings=None, kinesis_settings=None, kms_key_arn=None, mongodb_settings=None, password=None, port=None, s3_settings=None, server_name=None, service_access_role=None, ssl_mode=None, tags=None, username=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a DMS (Data Migration Service) endpoint resource. DMS endpoints can be created, updated, deleted, and imported.

        > **Note:** All arguments including the password will be stored in the raw state as plain-text.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create a new endpoint
        test = aws.dms.Endpoint("test",
            certificate_arn="arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012",
            database_name="test",
            endpoint_id="test-dms-endpoint-tf",
            endpoint_type="source",
            engine_name="aurora",
            extra_connection_attributes="",
            kms_key_arn="arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
            password="test",
            port=3306,
            server_name="test",
            ssl_mode="none",
            tags={
                "Name": "test",
            },
            username="test")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_arn: The Amazon Resource Name (ARN) for the certificate.
        :param pulumi.Input[str] database_name: The name of the endpoint database.
        :param pulumi.Input[dict] elasticsearch_settings: Configuration block with Elasticsearch settings. Detailed below.
        :param pulumi.Input[str] endpoint_id: The database endpoint identifier.
        :param pulumi.Input[str] endpoint_type: The type of endpoint. Can be one of `source | target`.
        :param pulumi.Input[str] engine_name: The type of engine for the endpoint. Can be one of `aurora | aurora-postgresql| azuredb | db2 | docdb | dynamodb | elasticsearch | kafka | kinesis | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
        :param pulumi.Input[str] extra_connection_attributes: Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
        :param pulumi.Input[dict] kafka_settings: Configuration block with Kafka settings. Detailed below.
        :param pulumi.Input[dict] kinesis_settings: Configuration block with Kinesis settings. Detailed below.
        :param pulumi.Input[str] kms_key_arn: The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
        :param pulumi.Input[dict] mongodb_settings: Configuration block with MongoDB settings. Detailed below.
        :param pulumi.Input[str] password: The password to be used to login to the endpoint database.
        :param pulumi.Input[float] port: The port used by the endpoint database.
        :param pulumi.Input[dict] s3_settings: Configuration block with S3 settings. Detailed below.
        :param pulumi.Input[str] server_name: The host name of the server.
        :param pulumi.Input[str] service_access_role: The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
        :param pulumi.Input[str] ssl_mode: The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] username: The user name to be used to login to the endpoint database.

        The **elasticsearch_settings** object supports the following:

          * `endpointUri` (`pulumi.Input[str]`) - Endpoint for the Elasticsearch cluster.
          * `errorRetryDuration` (`pulumi.Input[float]`) - Maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster. Defaults to `300`.
          * `fullLoadErrorPercentage` (`pulumi.Input[float]`) - Maximum percentage of records that can fail to be written before a full load operation stops. Defaults to `10`.
          * `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Elasticsearch cluster.

        The **kafka_settings** object supports the following:

          * `broker` (`pulumi.Input[str]`) - Kafka broker location. Specify in the form broker-hostname-or-ip:port.
          * `topic` (`pulumi.Input[str]`) - Kafka topic for migration. Defaults to `kafka-default-topic`.

        The **kinesis_settings** object supports the following:

          * `messageFormat` (`pulumi.Input[str]`) - Output format for the records created. Defaults to `json`. Valid values are `json` and `json_unformatted` (a single line with no tab).
          * `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Kinesis data stream.
          * `stream_arn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the Kinesis data stream.

        The **mongodb_settings** object supports the following:

          * `authMechanism` (`pulumi.Input[str]`) - Authentication mechanism to access the MongoDB source endpoint. Defaults to `default`.
          * `authSource` (`pulumi.Input[str]`) - Authentication database name. Not used when `auth_type` is `no`. Defaults to `admin`.
          * `auth_type` (`pulumi.Input[str]`) - Authentication type to access the MongoDB source endpoint. Defaults to `password`.
          * `docsToInvestigate` (`pulumi.Input[str]`) - Number of documents to preview to determine the document organization. Use this setting when `nesting_level` is set to `one`. Defaults to `1000`.
          * `extractDocId` (`pulumi.Input[str]`) - Document ID. Use this setting when `nesting_level` is set to `none`. Defaults to `false`.
          * `nestingLevel` (`pulumi.Input[str]`) - Specifies either document or table mode. Defaults to `none`. Valid values are `one` (table mode) and `none` (document mode).

        The **s3_settings** object supports the following:

          * `bucketFolder` (`pulumi.Input[str]`) - S3 Bucket Object prefix.
          * `bucket_name` (`pulumi.Input[str]`) - S3 Bucket name.
          * `compressionType` (`pulumi.Input[str]`) - Set to compress target files. Defaults to `NONE`. Valid values are `GZIP` and `NONE`.
          * `csvDelimiter` (`pulumi.Input[str]`) - Delimiter used to separate columns in the source files. Defaults to `,`.
          * `csvRowDelimiter` (`pulumi.Input[str]`) - Delimiter used to separate rows in the source files. Defaults to `\n`.
          * `externalTableDefinition` (`pulumi.Input[str]`) - JSON document that describes how AWS DMS should interpret the data.
          * `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to read from or write to the S3 Bucket.
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

            __props__['certificate_arn'] = certificate_arn
            __props__['database_name'] = database_name
            __props__['elasticsearch_settings'] = elasticsearch_settings
            if endpoint_id is None:
                raise TypeError("Missing required property 'endpoint_id'")
            __props__['endpoint_id'] = endpoint_id
            if endpoint_type is None:
                raise TypeError("Missing required property 'endpoint_type'")
            __props__['endpoint_type'] = endpoint_type
            if engine_name is None:
                raise TypeError("Missing required property 'engine_name'")
            __props__['engine_name'] = engine_name
            __props__['extra_connection_attributes'] = extra_connection_attributes
            __props__['kafka_settings'] = kafka_settings
            __props__['kinesis_settings'] = kinesis_settings
            __props__['kms_key_arn'] = kms_key_arn
            __props__['mongodb_settings'] = mongodb_settings
            __props__['password'] = password
            __props__['port'] = port
            __props__['s3_settings'] = s3_settings
            __props__['server_name'] = server_name
            __props__['service_access_role'] = service_access_role
            __props__['ssl_mode'] = ssl_mode
            __props__['tags'] = tags
            __props__['username'] = username
            __props__['endpoint_arn'] = None
        super(Endpoint, __self__).__init__(
            'aws:dms/endpoint:Endpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, certificate_arn=None, database_name=None, elasticsearch_settings=None, endpoint_arn=None, endpoint_id=None, endpoint_type=None, engine_name=None, extra_connection_attributes=None, kafka_settings=None, kinesis_settings=None, kms_key_arn=None, mongodb_settings=None, password=None, port=None, s3_settings=None, server_name=None, service_access_role=None, ssl_mode=None, tags=None, username=None):
        """
        Get an existing Endpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_arn: The Amazon Resource Name (ARN) for the certificate.
        :param pulumi.Input[str] database_name: The name of the endpoint database.
        :param pulumi.Input[dict] elasticsearch_settings: Configuration block with Elasticsearch settings. Detailed below.
        :param pulumi.Input[str] endpoint_arn: The Amazon Resource Name (ARN) for the endpoint.
        :param pulumi.Input[str] endpoint_id: The database endpoint identifier.
        :param pulumi.Input[str] endpoint_type: The type of endpoint. Can be one of `source | target`.
        :param pulumi.Input[str] engine_name: The type of engine for the endpoint. Can be one of `aurora | aurora-postgresql| azuredb | db2 | docdb | dynamodb | elasticsearch | kafka | kinesis | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
        :param pulumi.Input[str] extra_connection_attributes: Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
        :param pulumi.Input[dict] kafka_settings: Configuration block with Kafka settings. Detailed below.
        :param pulumi.Input[dict] kinesis_settings: Configuration block with Kinesis settings. Detailed below.
        :param pulumi.Input[str] kms_key_arn: The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
        :param pulumi.Input[dict] mongodb_settings: Configuration block with MongoDB settings. Detailed below.
        :param pulumi.Input[str] password: The password to be used to login to the endpoint database.
        :param pulumi.Input[float] port: The port used by the endpoint database.
        :param pulumi.Input[dict] s3_settings: Configuration block with S3 settings. Detailed below.
        :param pulumi.Input[str] server_name: The host name of the server.
        :param pulumi.Input[str] service_access_role: The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
        :param pulumi.Input[str] ssl_mode: The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] username: The user name to be used to login to the endpoint database.

        The **elasticsearch_settings** object supports the following:

          * `endpointUri` (`pulumi.Input[str]`) - Endpoint for the Elasticsearch cluster.
          * `errorRetryDuration` (`pulumi.Input[float]`) - Maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster. Defaults to `300`.
          * `fullLoadErrorPercentage` (`pulumi.Input[float]`) - Maximum percentage of records that can fail to be written before a full load operation stops. Defaults to `10`.
          * `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Elasticsearch cluster.

        The **kafka_settings** object supports the following:

          * `broker` (`pulumi.Input[str]`) - Kafka broker location. Specify in the form broker-hostname-or-ip:port.
          * `topic` (`pulumi.Input[str]`) - Kafka topic for migration. Defaults to `kafka-default-topic`.

        The **kinesis_settings** object supports the following:

          * `messageFormat` (`pulumi.Input[str]`) - Output format for the records created. Defaults to `json`. Valid values are `json` and `json_unformatted` (a single line with no tab).
          * `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Kinesis data stream.
          * `stream_arn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the Kinesis data stream.

        The **mongodb_settings** object supports the following:

          * `authMechanism` (`pulumi.Input[str]`) - Authentication mechanism to access the MongoDB source endpoint. Defaults to `default`.
          * `authSource` (`pulumi.Input[str]`) - Authentication database name. Not used when `auth_type` is `no`. Defaults to `admin`.
          * `auth_type` (`pulumi.Input[str]`) - Authentication type to access the MongoDB source endpoint. Defaults to `password`.
          * `docsToInvestigate` (`pulumi.Input[str]`) - Number of documents to preview to determine the document organization. Use this setting when `nesting_level` is set to `one`. Defaults to `1000`.
          * `extractDocId` (`pulumi.Input[str]`) - Document ID. Use this setting when `nesting_level` is set to `none`. Defaults to `false`.
          * `nestingLevel` (`pulumi.Input[str]`) - Specifies either document or table mode. Defaults to `none`. Valid values are `one` (table mode) and `none` (document mode).

        The **s3_settings** object supports the following:

          * `bucketFolder` (`pulumi.Input[str]`) - S3 Bucket Object prefix.
          * `bucket_name` (`pulumi.Input[str]`) - S3 Bucket name.
          * `compressionType` (`pulumi.Input[str]`) - Set to compress target files. Defaults to `NONE`. Valid values are `GZIP` and `NONE`.
          * `csvDelimiter` (`pulumi.Input[str]`) - Delimiter used to separate columns in the source files. Defaults to `,`.
          * `csvRowDelimiter` (`pulumi.Input[str]`) - Delimiter used to separate rows in the source files. Defaults to `\n`.
          * `externalTableDefinition` (`pulumi.Input[str]`) - JSON document that describes how AWS DMS should interpret the data.
          * `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to read from or write to the S3 Bucket.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["certificate_arn"] = certificate_arn
        __props__["database_name"] = database_name
        __props__["elasticsearch_settings"] = elasticsearch_settings
        __props__["endpoint_arn"] = endpoint_arn
        __props__["endpoint_id"] = endpoint_id
        __props__["endpoint_type"] = endpoint_type
        __props__["engine_name"] = engine_name
        __props__["extra_connection_attributes"] = extra_connection_attributes
        __props__["kafka_settings"] = kafka_settings
        __props__["kinesis_settings"] = kinesis_settings
        __props__["kms_key_arn"] = kms_key_arn
        __props__["mongodb_settings"] = mongodb_settings
        __props__["password"] = password
        __props__["port"] = port
        __props__["s3_settings"] = s3_settings
        __props__["server_name"] = server_name
        __props__["service_access_role"] = service_access_role
        __props__["ssl_mode"] = ssl_mode
        __props__["tags"] = tags
        __props__["username"] = username
        return Endpoint(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
