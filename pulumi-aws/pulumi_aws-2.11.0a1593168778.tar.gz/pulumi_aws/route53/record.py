# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Record(pulumi.CustomResource):
    aliases: pulumi.Output[list]
    """
    An alias block. Conflicts with `ttl` & `records`.
    Alias record documented below.

      * `evaluateTargetHealth` (`bool`) - Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
      * `name` (`str`) - DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
      * `zone_id` (`str`) - Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See `resource_elb.zone_id` for example.
    """
    allow_overwrite: pulumi.Output[bool]
    """
    Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
    """
    failover_routing_policies: pulumi.Output[list]
    """
    A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.

      * `type` (`str`) - `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
    """
    fqdn: pulumi.Output[str]
    """
    [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
    """
    geolocation_routing_policies: pulumi.Output[list]
    """
    A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.

      * `continent` (`str`) - A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
      * `country` (`str`) - A two-character country code or `*` to indicate a default resource record set.
      * `subdivision` (`str`) - A subdivision code for a country.
    """
    health_check_id: pulumi.Output[str]
    """
    The health check the record should be associated with.
    """
    latency_routing_policies: pulumi.Output[list]
    """
    A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.

      * `region` (`str`) - An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency
    """
    multivalue_answer_routing_policy: pulumi.Output[bool]
    """
    Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
    """
    name: pulumi.Output[str]
    """
    DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
    """
    records: pulumi.Output[list]
    """
    A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
    """
    set_identifier: pulumi.Output[str]
    """
    Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
    """
    ttl: pulumi.Output[float]
    """
    The TTL of the record.
    """
    type: pulumi.Output[str]
    """
    `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
    """
    weighted_routing_policies: pulumi.Output[list]
    """
    A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.

      * `weight` (`float`) - A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
    """
    zone_id: pulumi.Output[str]
    """
    Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See `resource_elb.zone_id` for example.
    """
    def __init__(__self__, resource_name, opts=None, aliases=None, allow_overwrite=None, failover_routing_policies=None, geolocation_routing_policies=None, health_check_id=None, latency_routing_policies=None, multivalue_answer_routing_policy=None, name=None, records=None, set_identifier=None, ttl=None, type=None, weighted_routing_policies=None, zone_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Route53 record resource.

        ## Example Usage
        ### Simple routing policy

        ```python
        import pulumi
        import pulumi_aws as aws

        www = aws.route53.Record("www",
            name="www.example.com",
            records=[aws_eip["lb"]["public_ip"]],
            ttl="300",
            type="A",
            zone_id=aws_route53_zone["primary"]["zone_id"])
        ```
        ### Weighted routing policy
        Other routing policies are configured similarly. See [AWS Route53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html) for details.

        ```python
        import pulumi
        import pulumi_aws as aws

        www_dev = aws.route53.Record("www-dev",
            name="www",
            records=["dev.example.com"],
            set_identifier="dev",
            ttl="5",
            type="CNAME",
            weighted_routing_policies=[{
                "weight": 10,
            }],
            zone_id=aws_route53_zone["primary"]["zone_id"])
        www_live = aws.route53.Record("www-live",
            name="www",
            records=["live.example.com"],
            set_identifier="live",
            ttl="5",
            type="CNAME",
            weighted_routing_policies=[{
                "weight": 90,
            }],
            zone_id=aws_route53_zone["primary"]["zone_id"])
        ```
        ### Alias record
        See [related part of AWS Route53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)
        to understand differences between alias and non-alias records.

        TTL for all alias records is [60 seconds](https://aws.amazon.com/route53/faqs/#dns_failover_do_i_need_to_adjust),
        you cannot change this, therefore `ttl` has to be omitted in alias records.

        ```python
        import pulumi
        import pulumi_aws as aws

        main = aws.elb.LoadBalancer("main",
            availability_zones=["us-east-1c"],
            listeners=[{
                "instance_port": 80,
                "instanceProtocol": "http",
                "lb_port": 80,
                "lbProtocol": "http",
            }])
        www = aws.route53.Record("www",
            aliases=[{
                "evaluateTargetHealth": True,
                "name": main.dns_name,
                "zone_id": main.zone_id,
            }],
            name="example.com",
            type="A",
            zone_id=aws_route53_zone["primary"]["zone_id"])
        ```
        ### NS and SOA Record Management

        When creating Route 53 zones, the `NS` and `SOA` records for the zone are automatically created. Enabling the `allow_overwrite` argument will allow managing these records in a single deployment without the requirement for `import`.

        ```python
        import pulumi
        import pulumi_aws as aws

        example_zone = aws.route53.Zone("exampleZone")
        example_record = aws.route53.Record("exampleRecord",
            allow_overwrite=True,
            name="test.example.com",
            records=[
                example_zone.name_servers[0],
                example_zone.name_servers[1],
                example_zone.name_servers[2],
                example_zone.name_servers[3],
            ],
            ttl=30,
            type="NS",
            zone_id=example_zone.zone_id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] aliases: An alias block. Conflicts with `ttl` & `records`.
               Alias record documented below.
        :param pulumi.Input[bool] allow_overwrite: Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
        :param pulumi.Input[list] failover_routing_policies: A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[list] geolocation_routing_policies: A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[str] health_check_id: The health check the record should be associated with.
        :param pulumi.Input[list] latency_routing_policies: A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[bool] multivalue_answer_routing_policy: Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
        :param pulumi.Input[str] name: DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
        :param pulumi.Input[list] records: A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
        :param pulumi.Input[str] set_identifier: Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
        :param pulumi.Input[float] ttl: The TTL of the record.
        :param pulumi.Input[dict] type: `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
        :param pulumi.Input[list] weighted_routing_policies: A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[str] zone_id: Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See `resource_elb.zone_id` for example.

        The **aliases** object supports the following:

          * `evaluateTargetHealth` (`pulumi.Input[bool]`) - Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
          * `name` (`pulumi.Input[str]`) - DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
          * `zone_id` (`pulumi.Input[str]`) - Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See `resource_elb.zone_id` for example.

        The **failover_routing_policies** object supports the following:

          * `type` (`pulumi.Input[str]`) - `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets

        The **geolocation_routing_policies** object supports the following:

          * `continent` (`pulumi.Input[str]`) - A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
          * `country` (`pulumi.Input[str]`) - A two-character country code or `*` to indicate a default resource record set.
          * `subdivision` (`pulumi.Input[str]`) - A subdivision code for a country.

        The **latency_routing_policies** object supports the following:

          * `region` (`pulumi.Input[str]`) - An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency

        The **weighted_routing_policies** object supports the following:

          * `weight` (`pulumi.Input[float]`) - A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
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

            __props__['aliases'] = aliases
            __props__['allow_overwrite'] = allow_overwrite
            __props__['failover_routing_policies'] = failover_routing_policies
            __props__['geolocation_routing_policies'] = geolocation_routing_policies
            __props__['health_check_id'] = health_check_id
            __props__['latency_routing_policies'] = latency_routing_policies
            __props__['multivalue_answer_routing_policy'] = multivalue_answer_routing_policy
            if name is None:
                raise TypeError("Missing required property 'name'")
            __props__['name'] = name
            __props__['records'] = records
            __props__['set_identifier'] = set_identifier
            __props__['ttl'] = ttl
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['weighted_routing_policies'] = weighted_routing_policies
            if zone_id is None:
                raise TypeError("Missing required property 'zone_id'")
            __props__['zone_id'] = zone_id
            __props__['fqdn'] = None
        super(Record, __self__).__init__(
            'aws:route53/record:Record',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, aliases=None, allow_overwrite=None, failover_routing_policies=None, fqdn=None, geolocation_routing_policies=None, health_check_id=None, latency_routing_policies=None, multivalue_answer_routing_policy=None, name=None, records=None, set_identifier=None, ttl=None, type=None, weighted_routing_policies=None, zone_id=None):
        """
        Get an existing Record resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] aliases: An alias block. Conflicts with `ttl` & `records`.
               Alias record documented below.
        :param pulumi.Input[bool] allow_overwrite: Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
        :param pulumi.Input[list] failover_routing_policies: A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[str] fqdn: [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
        :param pulumi.Input[list] geolocation_routing_policies: A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[str] health_check_id: The health check the record should be associated with.
        :param pulumi.Input[list] latency_routing_policies: A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[bool] multivalue_answer_routing_policy: Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
        :param pulumi.Input[str] name: DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
        :param pulumi.Input[list] records: A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
        :param pulumi.Input[str] set_identifier: Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
        :param pulumi.Input[float] ttl: The TTL of the record.
        :param pulumi.Input[dict] type: `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
        :param pulumi.Input[list] weighted_routing_policies: A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[str] zone_id: Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See `resource_elb.zone_id` for example.

        The **aliases** object supports the following:

          * `evaluateTargetHealth` (`pulumi.Input[bool]`) - Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
          * `name` (`pulumi.Input[str]`) - DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
          * `zone_id` (`pulumi.Input[str]`) - Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See `resource_elb.zone_id` for example.

        The **failover_routing_policies** object supports the following:

          * `type` (`pulumi.Input[str]`) - `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets

        The **geolocation_routing_policies** object supports the following:

          * `continent` (`pulumi.Input[str]`) - A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
          * `country` (`pulumi.Input[str]`) - A two-character country code or `*` to indicate a default resource record set.
          * `subdivision` (`pulumi.Input[str]`) - A subdivision code for a country.

        The **latency_routing_policies** object supports the following:

          * `region` (`pulumi.Input[str]`) - An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency

        The **weighted_routing_policies** object supports the following:

          * `weight` (`pulumi.Input[float]`) - A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["aliases"] = aliases
        __props__["allow_overwrite"] = allow_overwrite
        __props__["failover_routing_policies"] = failover_routing_policies
        __props__["fqdn"] = fqdn
        __props__["geolocation_routing_policies"] = geolocation_routing_policies
        __props__["health_check_id"] = health_check_id
        __props__["latency_routing_policies"] = latency_routing_policies
        __props__["multivalue_answer_routing_policy"] = multivalue_answer_routing_policy
        __props__["name"] = name
        __props__["records"] = records
        __props__["set_identifier"] = set_identifier
        __props__["ttl"] = ttl
        __props__["type"] = type
        __props__["weighted_routing_policies"] = weighted_routing_policies
        __props__["zone_id"] = zone_id
        return Record(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
