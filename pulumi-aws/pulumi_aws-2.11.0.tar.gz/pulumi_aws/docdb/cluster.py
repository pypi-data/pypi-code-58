# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Cluster(pulumi.CustomResource):
    apply_immediately: pulumi.Output[bool]
    """
    Specifies whether any cluster modifications
    are applied immediately, or during the next maintenance window. Default is
    `false`.
    """
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of cluster
    """
    availability_zones: pulumi.Output[list]
    """
    A list of EC2 Availability Zones that
    instances in the DB cluster can be created in.
    """
    backup_retention_period: pulumi.Output[float]
    """
    The days to retain backups for. Default `1`
    """
    cluster_identifier: pulumi.Output[str]
    """
    The cluster identifier. If omitted, this provider will assign a random, unique identifier.
    """
    cluster_identifier_prefix: pulumi.Output[str]
    """
    Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.
    """
    cluster_members: pulumi.Output[list]
    """
    List of DocDB Instances that are a part of this cluster
    """
    cluster_resource_id: pulumi.Output[str]
    """
    The DocDB Cluster Resource ID
    """
    db_cluster_parameter_group_name: pulumi.Output[str]
    """
    A cluster parameter group to associate with the cluster.
    """
    db_subnet_group_name: pulumi.Output[str]
    """
    A DB subnet group to associate with this DB instance.
    """
    deletion_protection: pulumi.Output[bool]
    """
    A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
    """
    enabled_cloudwatch_logs_exports: pulumi.Output[list]
    """
    List of log types to export to cloudwatch. If omitted, no logs will be exported.
    The following log types are supported: `audit`, `profiler`.
    """
    endpoint: pulumi.Output[str]
    """
    The DNS address of the DocDB instance
    """
    engine: pulumi.Output[str]
    """
    The name of the database engine to be used for this DB cluster. Defaults to `docdb`. Valid Values: `docdb`
    """
    engine_version: pulumi.Output[str]
    """
    The database engine version. Updating this argument results in an outage.
    """
    final_snapshot_identifier: pulumi.Output[str]
    """
    The name of your final DB snapshot
    when this DB cluster is deleted. If omitted, no final snapshot will be
    made.
    """
    hosted_zone_id: pulumi.Output[str]
    """
    The Route53 Hosted Zone ID of the endpoint
    """
    kms_key_id: pulumi.Output[str]
    """
    The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
    """
    master_password: pulumi.Output[str]
    """
    Password for the master DB user. Note that this may
    show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.
    """
    master_username: pulumi.Output[str]
    """
    Username for the master DB user.
    """
    port: pulumi.Output[float]
    """
    The port on which the DB accepts connections
    """
    preferred_backup_window: pulumi.Output[str]
    """
    The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
    Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
    """
    preferred_maintenance_window: pulumi.Output[str]
    reader_endpoint: pulumi.Output[str]
    """
    A read-only endpoint for the DocDB cluster, automatically load-balanced across replicas
    """
    skip_final_snapshot: pulumi.Output[bool]
    """
    Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
    """
    snapshot_identifier: pulumi.Output[str]
    """
    Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
    """
    storage_encrypted: pulumi.Output[bool]
    """
    Specifies whether the DB cluster is encrypted. The default is `false`.
    """
    tags: pulumi.Output[dict]
    """
    A map of tags to assign to the DB cluster.
    """
    vpc_security_group_ids: pulumi.Output[list]
    """
    List of VPC security groups to associate
    with the Cluster
    """
    def __init__(__self__, resource_name, opts=None, apply_immediately=None, availability_zones=None, backup_retention_period=None, cluster_identifier=None, cluster_identifier_prefix=None, cluster_members=None, db_cluster_parameter_group_name=None, db_subnet_group_name=None, deletion_protection=None, enabled_cloudwatch_logs_exports=None, engine=None, engine_version=None, final_snapshot_identifier=None, kms_key_id=None, master_password=None, master_username=None, port=None, preferred_backup_window=None, preferred_maintenance_window=None, skip_final_snapshot=None, snapshot_identifier=None, storage_encrypted=None, tags=None, vpc_security_group_ids=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a DocDB Cluster.

        Changes to a DocDB Cluster can occur when you manually change a
        parameter, such as `port`, and are reflected in the next maintenance
        window. Because of this, this provider may report a difference in its planning
        phase because a modification has not yet taken place. You can use the
        `apply_immediately` flag to instruct the service to apply the change immediately
        (see documentation below).

        > **Note:** using `apply_immediately` can result in a brief downtime as the server reboots.
        **Note:** All arguments including the username and password will be stored in the raw state as plain-text.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        docdb = aws.docdb.Cluster("docdb",
            backup_retention_period=5,
            cluster_identifier="my-docdb-cluster",
            engine="docdb",
            master_password="mustbeeightchars",
            master_username="foo",
            preferred_backup_window="07:00-09:00",
            skip_final_snapshot=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] apply_immediately: Specifies whether any cluster modifications
               are applied immediately, or during the next maintenance window. Default is
               `false`.
        :param pulumi.Input[list] availability_zones: A list of EC2 Availability Zones that
               instances in the DB cluster can be created in.
        :param pulumi.Input[float] backup_retention_period: The days to retain backups for. Default `1`
        :param pulumi.Input[str] cluster_identifier: The cluster identifier. If omitted, this provider will assign a random, unique identifier.
        :param pulumi.Input[str] cluster_identifier_prefix: Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.
        :param pulumi.Input[list] cluster_members: List of DocDB Instances that are a part of this cluster
        :param pulumi.Input[str] db_cluster_parameter_group_name: A cluster parameter group to associate with the cluster.
        :param pulumi.Input[str] db_subnet_group_name: A DB subnet group to associate with this DB instance.
        :param pulumi.Input[bool] deletion_protection: A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
        :param pulumi.Input[list] enabled_cloudwatch_logs_exports: List of log types to export to cloudwatch. If omitted, no logs will be exported.
               The following log types are supported: `audit`, `profiler`.
        :param pulumi.Input[str] engine: The name of the database engine to be used for this DB cluster. Defaults to `docdb`. Valid Values: `docdb`
        :param pulumi.Input[str] engine_version: The database engine version. Updating this argument results in an outage.
        :param pulumi.Input[str] final_snapshot_identifier: The name of your final DB snapshot
               when this DB cluster is deleted. If omitted, no final snapshot will be
               made.
        :param pulumi.Input[str] kms_key_id: The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
        :param pulumi.Input[str] master_password: Password for the master DB user. Note that this may
               show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.
        :param pulumi.Input[str] master_username: Username for the master DB user.
        :param pulumi.Input[float] port: The port on which the DB accepts connections
        :param pulumi.Input[str] preferred_backup_window: The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
               Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
        :param pulumi.Input[bool] skip_final_snapshot: Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
        :param pulumi.Input[str] snapshot_identifier: Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
        :param pulumi.Input[bool] storage_encrypted: Specifies whether the DB cluster is encrypted. The default is `false`.
        :param pulumi.Input[dict] tags: A map of tags to assign to the DB cluster.
        :param pulumi.Input[list] vpc_security_group_ids: List of VPC security groups to associate
               with the Cluster
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

            __props__['apply_immediately'] = apply_immediately
            __props__['availability_zones'] = availability_zones
            __props__['backup_retention_period'] = backup_retention_period
            __props__['cluster_identifier'] = cluster_identifier
            __props__['cluster_identifier_prefix'] = cluster_identifier_prefix
            __props__['cluster_members'] = cluster_members
            __props__['db_cluster_parameter_group_name'] = db_cluster_parameter_group_name
            __props__['db_subnet_group_name'] = db_subnet_group_name
            __props__['deletion_protection'] = deletion_protection
            __props__['enabled_cloudwatch_logs_exports'] = enabled_cloudwatch_logs_exports
            __props__['engine'] = engine
            __props__['engine_version'] = engine_version
            __props__['final_snapshot_identifier'] = final_snapshot_identifier
            __props__['kms_key_id'] = kms_key_id
            __props__['master_password'] = master_password
            __props__['master_username'] = master_username
            __props__['port'] = port
            __props__['preferred_backup_window'] = preferred_backup_window
            __props__['preferred_maintenance_window'] = preferred_maintenance_window
            __props__['skip_final_snapshot'] = skip_final_snapshot
            __props__['snapshot_identifier'] = snapshot_identifier
            __props__['storage_encrypted'] = storage_encrypted
            __props__['tags'] = tags
            __props__['vpc_security_group_ids'] = vpc_security_group_ids
            __props__['arn'] = None
            __props__['cluster_resource_id'] = None
            __props__['endpoint'] = None
            __props__['hosted_zone_id'] = None
            __props__['reader_endpoint'] = None
        super(Cluster, __self__).__init__(
            'aws:docdb/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, apply_immediately=None, arn=None, availability_zones=None, backup_retention_period=None, cluster_identifier=None, cluster_identifier_prefix=None, cluster_members=None, cluster_resource_id=None, db_cluster_parameter_group_name=None, db_subnet_group_name=None, deletion_protection=None, enabled_cloudwatch_logs_exports=None, endpoint=None, engine=None, engine_version=None, final_snapshot_identifier=None, hosted_zone_id=None, kms_key_id=None, master_password=None, master_username=None, port=None, preferred_backup_window=None, preferred_maintenance_window=None, reader_endpoint=None, skip_final_snapshot=None, snapshot_identifier=None, storage_encrypted=None, tags=None, vpc_security_group_ids=None):
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] apply_immediately: Specifies whether any cluster modifications
               are applied immediately, or during the next maintenance window. Default is
               `false`.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of cluster
        :param pulumi.Input[list] availability_zones: A list of EC2 Availability Zones that
               instances in the DB cluster can be created in.
        :param pulumi.Input[float] backup_retention_period: The days to retain backups for. Default `1`
        :param pulumi.Input[str] cluster_identifier: The cluster identifier. If omitted, this provider will assign a random, unique identifier.
        :param pulumi.Input[str] cluster_identifier_prefix: Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.
        :param pulumi.Input[list] cluster_members: List of DocDB Instances that are a part of this cluster
        :param pulumi.Input[str] cluster_resource_id: The DocDB Cluster Resource ID
        :param pulumi.Input[str] db_cluster_parameter_group_name: A cluster parameter group to associate with the cluster.
        :param pulumi.Input[str] db_subnet_group_name: A DB subnet group to associate with this DB instance.
        :param pulumi.Input[bool] deletion_protection: A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
        :param pulumi.Input[list] enabled_cloudwatch_logs_exports: List of log types to export to cloudwatch. If omitted, no logs will be exported.
               The following log types are supported: `audit`, `profiler`.
        :param pulumi.Input[str] endpoint: The DNS address of the DocDB instance
        :param pulumi.Input[str] engine: The name of the database engine to be used for this DB cluster. Defaults to `docdb`. Valid Values: `docdb`
        :param pulumi.Input[str] engine_version: The database engine version. Updating this argument results in an outage.
        :param pulumi.Input[str] final_snapshot_identifier: The name of your final DB snapshot
               when this DB cluster is deleted. If omitted, no final snapshot will be
               made.
        :param pulumi.Input[str] hosted_zone_id: The Route53 Hosted Zone ID of the endpoint
        :param pulumi.Input[str] kms_key_id: The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
        :param pulumi.Input[str] master_password: Password for the master DB user. Note that this may
               show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.
        :param pulumi.Input[str] master_username: Username for the master DB user.
        :param pulumi.Input[float] port: The port on which the DB accepts connections
        :param pulumi.Input[str] preferred_backup_window: The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
               Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
        :param pulumi.Input[str] reader_endpoint: A read-only endpoint for the DocDB cluster, automatically load-balanced across replicas
        :param pulumi.Input[bool] skip_final_snapshot: Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
        :param pulumi.Input[str] snapshot_identifier: Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
        :param pulumi.Input[bool] storage_encrypted: Specifies whether the DB cluster is encrypted. The default is `false`.
        :param pulumi.Input[dict] tags: A map of tags to assign to the DB cluster.
        :param pulumi.Input[list] vpc_security_group_ids: List of VPC security groups to associate
               with the Cluster
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["apply_immediately"] = apply_immediately
        __props__["arn"] = arn
        __props__["availability_zones"] = availability_zones
        __props__["backup_retention_period"] = backup_retention_period
        __props__["cluster_identifier"] = cluster_identifier
        __props__["cluster_identifier_prefix"] = cluster_identifier_prefix
        __props__["cluster_members"] = cluster_members
        __props__["cluster_resource_id"] = cluster_resource_id
        __props__["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        __props__["db_subnet_group_name"] = db_subnet_group_name
        __props__["deletion_protection"] = deletion_protection
        __props__["enabled_cloudwatch_logs_exports"] = enabled_cloudwatch_logs_exports
        __props__["endpoint"] = endpoint
        __props__["engine"] = engine
        __props__["engine_version"] = engine_version
        __props__["final_snapshot_identifier"] = final_snapshot_identifier
        __props__["hosted_zone_id"] = hosted_zone_id
        __props__["kms_key_id"] = kms_key_id
        __props__["master_password"] = master_password
        __props__["master_username"] = master_username
        __props__["port"] = port
        __props__["preferred_backup_window"] = preferred_backup_window
        __props__["preferred_maintenance_window"] = preferred_maintenance_window
        __props__["reader_endpoint"] = reader_endpoint
        __props__["skip_final_snapshot"] = skip_final_snapshot
        __props__["snapshot_identifier"] = snapshot_identifier
        __props__["storage_encrypted"] = storage_encrypted
        __props__["tags"] = tags
        __props__["vpc_security_group_ids"] = vpc_security_group_ids
        return Cluster(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
