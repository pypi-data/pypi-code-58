# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class FolderSink(pulumi.CustomResource):
    bigquery_options: pulumi.Output[dict]
    """
    Options that affect sinks exporting data to BigQuery. Structure documented below.

      * `usePartitionedTables` (`bool`) - Whether to use [BigQuery's partition tables](https://cloud.google.com/bigquery/docs/partitioned-tables).
        By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned
        tables the date suffix is no longer present and [special query syntax](https://cloud.google.com/bigquery/docs/querying-partitioned-tables)
        has to be used instead. In both cases, tables are sharded based on UTC timezone.
    """
    destination: pulumi.Output[str]
    """
    The destination of the sink (or, in other words, where logs are written to). Can be a
    Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
    "storage.googleapis.com/[GCS_BUCKET]"
    "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
    "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
    The writer associated with the sink must have access to write to the above resource.
    """
    filter: pulumi.Output[str]
    """
    The filter to apply when exporting logs. Only log entries that match the filter are exported.
    See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
    write a filter.
    """
    folder: pulumi.Output[str]
    """
    The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
    accepted.
    """
    include_children: pulumi.Output[bool]
    """
    Whether or not to include children folders in the sink export. If true, logs
    associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
    """
    name: pulumi.Output[str]
    """
    The name of the logging sink.
    """
    writer_identity: pulumi.Output[str]
    """
    The identity associated with this sink. This identity must be granted write access to the
    configured `destination`.
    """
    def __init__(__self__, resource_name, opts=None, bigquery_options=None, destination=None, filter=None, folder=None, include_children=None, name=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a folder-level logging sink. For more information see
        [the official documentation](https://cloud.google.com/logging/docs/) and
        [Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs).

        Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
        granted to the credentials used with this provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        log_bucket = gcp.storage.Bucket("log-bucket")
        my_folder = gcp.organizations.Folder("my-folder",
            display_name="My folder",
            parent="organizations/123456")
        my_sink = gcp.logging.FolderSink("my-sink",
            folder=my_folder.name,
            destination=log_bucket.name.apply(lambda name: f"storage.googleapis.com/{name}"),
            filter="resource.type = gce_instance AND severity >= WARN")
        log_writer = gcp.projects.IAMBinding("log-writer",
            role="roles/storage.objectCreator",
            members=[my_sink.writer_identity])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] bigquery_options: Options that affect sinks exporting data to BigQuery. Structure documented below.
        :param pulumi.Input[str] destination: The destination of the sink (or, in other words, where logs are written to). Can be a
               Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
               "storage.googleapis.com/[GCS_BUCKET]"
               "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
               "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
               The writer associated with the sink must have access to write to the above resource.
        :param pulumi.Input[str] filter: The filter to apply when exporting logs. Only log entries that match the filter are exported.
               See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
               write a filter.
        :param pulumi.Input[str] folder: The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
               accepted.
        :param pulumi.Input[bool] include_children: Whether or not to include children folders in the sink export. If true, logs
               associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
        :param pulumi.Input[str] name: The name of the logging sink.

        The **bigquery_options** object supports the following:

          * `usePartitionedTables` (`pulumi.Input[bool]`) - Whether to use [BigQuery's partition tables](https://cloud.google.com/bigquery/docs/partitioned-tables).
            By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned
            tables the date suffix is no longer present and [special query syntax](https://cloud.google.com/bigquery/docs/querying-partitioned-tables)
            has to be used instead. In both cases, tables are sharded based on UTC timezone.
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

            __props__['bigquery_options'] = bigquery_options
            if destination is None:
                raise TypeError("Missing required property 'destination'")
            __props__['destination'] = destination
            __props__['filter'] = filter
            if folder is None:
                raise TypeError("Missing required property 'folder'")
            __props__['folder'] = folder
            __props__['include_children'] = include_children
            __props__['name'] = name
            __props__['writer_identity'] = None
        super(FolderSink, __self__).__init__(
            'gcp:logging/folderSink:FolderSink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, bigquery_options=None, destination=None, filter=None, folder=None, include_children=None, name=None, writer_identity=None):
        """
        Get an existing FolderSink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] bigquery_options: Options that affect sinks exporting data to BigQuery. Structure documented below.
        :param pulumi.Input[str] destination: The destination of the sink (or, in other words, where logs are written to). Can be a
               Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
               "storage.googleapis.com/[GCS_BUCKET]"
               "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
               "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
               The writer associated with the sink must have access to write to the above resource.
        :param pulumi.Input[str] filter: The filter to apply when exporting logs. Only log entries that match the filter are exported.
               See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
               write a filter.
        :param pulumi.Input[str] folder: The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
               accepted.
        :param pulumi.Input[bool] include_children: Whether or not to include children folders in the sink export. If true, logs
               associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
        :param pulumi.Input[str] name: The name of the logging sink.
        :param pulumi.Input[str] writer_identity: The identity associated with this sink. This identity must be granted write access to the
               configured `destination`.

        The **bigquery_options** object supports the following:

          * `usePartitionedTables` (`pulumi.Input[bool]`) - Whether to use [BigQuery's partition tables](https://cloud.google.com/bigquery/docs/partitioned-tables).
            By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned
            tables the date suffix is no longer present and [special query syntax](https://cloud.google.com/bigquery/docs/querying-partitioned-tables)
            has to be used instead. In both cases, tables are sharded based on UTC timezone.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["bigquery_options"] = bigquery_options
        __props__["destination"] = destination
        __props__["filter"] = filter
        __props__["folder"] = folder
        __props__["include_children"] = include_children
        __props__["name"] = name
        __props__["writer_identity"] = writer_identity
        return FolderSink(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
