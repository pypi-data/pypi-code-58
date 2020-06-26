# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Instance(pulumi.CustomResource):
    alternative_location_id: pulumi.Output[str]
    """
    Only applicable to STANDARD_HA tier which protects the instance
    against zonal failures by provisioning it across two zones.
    If provided, it must be a different zone from the one provided in
    [locationId].
    """
    authorized_network: pulumi.Output[str]
    """
    The full name of the Google Compute Engine network to which the
    instance is connected. If left unspecified, the default network
    will be used.
    """
    connect_mode: pulumi.Output[str]
    """
    The connection mode of the Redis instance.
    """
    create_time: pulumi.Output[str]
    """
    The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
    """
    current_location_id: pulumi.Output[str]
    """
    The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
    [locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
    [alternativeLocationId] and can change after a failover event.
    """
    display_name: pulumi.Output[str]
    """
    An arbitrary and optional user-provided name for the instance.
    """
    host: pulumi.Output[str]
    """
    Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
    """
    labels: pulumi.Output[dict]
    """
    Resource labels to represent user provided metadata.
    """
    location_id: pulumi.Output[str]
    """
    The zone where the instance will be provisioned. If not provided,
    the service will choose a zone for the instance. For STANDARD_HA tier,
    instances will be created across two zones for protection against
    zonal failures. If [alternativeLocationId] is also provided, it must
    be different from [locationId].
    """
    memory_size_gb: pulumi.Output[float]
    """
    Redis memory size in GiB.
    """
    name: pulumi.Output[str]
    """
    The ID of the instance or a fully qualified identifier for the instance.
    """
    port: pulumi.Output[float]
    """
    The port number of the exposed Redis endpoint.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    redis_configs: pulumi.Output[dict]
    """
    Redis configuration parameters, according to http://redis.io/topics/config.
    Please check Memorystore documentation for the list of supported parameters:
    https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
    """
    redis_version: pulumi.Output[str]
    """
    The version of Redis software. If not provided, latest supported
    version will be used. Currently, the supported values are:
    - REDIS_4_0 for Redis 4.0 compatibility
    - REDIS_3_2 for Redis 3.2 compatibility
    """
    region: pulumi.Output[str]
    """
    The name of the Redis region of the instance.
    """
    reserved_ip_range: pulumi.Output[str]
    """
    The CIDR range of internal addresses that are reserved for this
    instance. If not provided, the service will choose an unused /29
    block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
    unique and non-overlapping with existing subnets in an authorized
    network.
    """
    tier: pulumi.Output[str]
    """
    The service tier of the instance. Must be one of these values:
    - BASIC: standalone instance
    - STANDARD_HA: highly available primary/replica instances
    """
    def __init__(__self__, resource_name, opts=None, alternative_location_id=None, authorized_network=None, connect_mode=None, display_name=None, labels=None, location_id=None, memory_size_gb=None, name=None, project=None, redis_configs=None, redis_version=None, region=None, reserved_ip_range=None, tier=None, __props__=None, __name__=None, __opts__=None):
        """
        A Google Cloud Redis instance.

        To get more information about Instance, see:

        * [API documentation](https://cloud.google.com/memorystore/docs/redis/reference/rest/)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/memorystore/docs/redis/)

        ## Example Usage
        ### Redis Instance Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cache = gcp.redis.Instance("cache", memory_size_gb=1)
        ```
        ### Redis Instance Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        redis_network = gcp.compute.get_network(name="redis-test-network")
        cache = gcp.redis.Instance("cache",
            tier="STANDARD_HA",
            memory_size_gb=1,
            location_id="us-central1-a",
            alternative_location_id="us-central1-f",
            authorized_network=redis_network.id,
            redis_version="REDIS_3_2",
            display_name="Test Instance",
            reserved_ip_range="192.168.0.0/29",
            labels={
                "my_key": "my_val",
                "other_key": "other_val",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alternative_location_id: Only applicable to STANDARD_HA tier which protects the instance
               against zonal failures by provisioning it across two zones.
               If provided, it must be a different zone from the one provided in
               [locationId].
        :param pulumi.Input[str] authorized_network: The full name of the Google Compute Engine network to which the
               instance is connected. If left unspecified, the default network
               will be used.
        :param pulumi.Input[str] connect_mode: The connection mode of the Redis instance.
        :param pulumi.Input[str] display_name: An arbitrary and optional user-provided name for the instance.
        :param pulumi.Input[dict] labels: Resource labels to represent user provided metadata.
        :param pulumi.Input[str] location_id: The zone where the instance will be provisioned. If not provided,
               the service will choose a zone for the instance. For STANDARD_HA tier,
               instances will be created across two zones for protection against
               zonal failures. If [alternativeLocationId] is also provided, it must
               be different from [locationId].
        :param pulumi.Input[float] memory_size_gb: Redis memory size in GiB.
        :param pulumi.Input[str] name: The ID of the instance or a fully qualified identifier for the instance.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[dict] redis_configs: Redis configuration parameters, according to http://redis.io/topics/config.
               Please check Memorystore documentation for the list of supported parameters:
               https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
        :param pulumi.Input[str] redis_version: The version of Redis software. If not provided, latest supported
               version will be used. Currently, the supported values are:
               - REDIS_4_0 for Redis 4.0 compatibility
               - REDIS_3_2 for Redis 3.2 compatibility
        :param pulumi.Input[str] region: The name of the Redis region of the instance.
        :param pulumi.Input[str] reserved_ip_range: The CIDR range of internal addresses that are reserved for this
               instance. If not provided, the service will choose an unused /29
               block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
               unique and non-overlapping with existing subnets in an authorized
               network.
        :param pulumi.Input[str] tier: The service tier of the instance. Must be one of these values:
               - BASIC: standalone instance
               - STANDARD_HA: highly available primary/replica instances
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

            __props__['alternative_location_id'] = alternative_location_id
            __props__['authorized_network'] = authorized_network
            __props__['connect_mode'] = connect_mode
            __props__['display_name'] = display_name
            __props__['labels'] = labels
            __props__['location_id'] = location_id
            if memory_size_gb is None:
                raise TypeError("Missing required property 'memory_size_gb'")
            __props__['memory_size_gb'] = memory_size_gb
            __props__['name'] = name
            __props__['project'] = project
            __props__['redis_configs'] = redis_configs
            __props__['redis_version'] = redis_version
            __props__['region'] = region
            __props__['reserved_ip_range'] = reserved_ip_range
            __props__['tier'] = tier
            __props__['create_time'] = None
            __props__['current_location_id'] = None
            __props__['host'] = None
            __props__['port'] = None
        super(Instance, __self__).__init__(
            'gcp:redis/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, alternative_location_id=None, authorized_network=None, connect_mode=None, create_time=None, current_location_id=None, display_name=None, host=None, labels=None, location_id=None, memory_size_gb=None, name=None, port=None, project=None, redis_configs=None, redis_version=None, region=None, reserved_ip_range=None, tier=None):
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alternative_location_id: Only applicable to STANDARD_HA tier which protects the instance
               against zonal failures by provisioning it across two zones.
               If provided, it must be a different zone from the one provided in
               [locationId].
        :param pulumi.Input[str] authorized_network: The full name of the Google Compute Engine network to which the
               instance is connected. If left unspecified, the default network
               will be used.
        :param pulumi.Input[str] connect_mode: The connection mode of the Redis instance.
        :param pulumi.Input[str] create_time: The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
        :param pulumi.Input[str] current_location_id: The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
               [locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
               [alternativeLocationId] and can change after a failover event.
        :param pulumi.Input[str] display_name: An arbitrary and optional user-provided name for the instance.
        :param pulumi.Input[str] host: Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
        :param pulumi.Input[dict] labels: Resource labels to represent user provided metadata.
        :param pulumi.Input[str] location_id: The zone where the instance will be provisioned. If not provided,
               the service will choose a zone for the instance. For STANDARD_HA tier,
               instances will be created across two zones for protection against
               zonal failures. If [alternativeLocationId] is also provided, it must
               be different from [locationId].
        :param pulumi.Input[float] memory_size_gb: Redis memory size in GiB.
        :param pulumi.Input[str] name: The ID of the instance or a fully qualified identifier for the instance.
        :param pulumi.Input[float] port: The port number of the exposed Redis endpoint.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[dict] redis_configs: Redis configuration parameters, according to http://redis.io/topics/config.
               Please check Memorystore documentation for the list of supported parameters:
               https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
        :param pulumi.Input[str] redis_version: The version of Redis software. If not provided, latest supported
               version will be used. Currently, the supported values are:
               - REDIS_4_0 for Redis 4.0 compatibility
               - REDIS_3_2 for Redis 3.2 compatibility
        :param pulumi.Input[str] region: The name of the Redis region of the instance.
        :param pulumi.Input[str] reserved_ip_range: The CIDR range of internal addresses that are reserved for this
               instance. If not provided, the service will choose an unused /29
               block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
               unique and non-overlapping with existing subnets in an authorized
               network.
        :param pulumi.Input[str] tier: The service tier of the instance. Must be one of these values:
               - BASIC: standalone instance
               - STANDARD_HA: highly available primary/replica instances
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["alternative_location_id"] = alternative_location_id
        __props__["authorized_network"] = authorized_network
        __props__["connect_mode"] = connect_mode
        __props__["create_time"] = create_time
        __props__["current_location_id"] = current_location_id
        __props__["display_name"] = display_name
        __props__["host"] = host
        __props__["labels"] = labels
        __props__["location_id"] = location_id
        __props__["memory_size_gb"] = memory_size_gb
        __props__["name"] = name
        __props__["port"] = port
        __props__["project"] = project
        __props__["redis_configs"] = redis_configs
        __props__["redis_version"] = redis_version
        __props__["region"] = region
        __props__["reserved_ip_range"] = reserved_ip_range
        __props__["tier"] = tier
        return Instance(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
