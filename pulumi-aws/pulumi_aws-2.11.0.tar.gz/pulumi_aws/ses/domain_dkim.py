# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class DomainDkim(pulumi.CustomResource):
    dkim_tokens: pulumi.Output[list]
    """
    DKIM tokens generated by SES.
    These tokens should be used to create CNAME records used to verify SES Easy DKIM.
    See below for an example of how this might be achieved
    when the domain is hosted in Route 53 and managed by this provider.
    Find out more about verifying domains in Amazon SES
    in the [AWS SES docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html).
    """
    domain: pulumi.Output[str]
    """
    Verified domain name to generate DKIM tokens for.
    """
    def __init__(__self__, resource_name, opts=None, domain=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an SES domain DKIM generation resource.

        Domain ownership needs to be confirmed first using `ses.DomainIdentity` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_domain_identity = aws.ses.DomainIdentity("exampleDomainIdentity", domain="example.com")
        example_domain_dkim = aws.ses.DomainDkim("exampleDomainDkim", domain=example_domain_identity.domain)
        example_amazonses_dkim_record = []
        for range in [{"value": i} for i in range(0, 3)]:
            example_amazonses_dkim_record.append(aws.route53.Record(f"exampleAmazonsesDkimRecord-{range['value']}",
                name=example_domain_dkim.dkim_tokens[range["value"]].apply(lambda dkim_tokens: f"{dkim_tokens}._domainkey.example.com"),
                records=[example_domain_dkim.dkim_tokens[range["value"]].apply(lambda dkim_tokens: f"{dkim_tokens}.dkim.amazonses.com")],
                ttl="600",
                type="CNAME",
                zone_id="ABCDEFGHIJ123"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain: Verified domain name to generate DKIM tokens for.
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

            if domain is None:
                raise TypeError("Missing required property 'domain'")
            __props__['domain'] = domain
            __props__['dkim_tokens'] = None
        super(DomainDkim, __self__).__init__(
            'aws:ses/domainDkim:DomainDkim',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, dkim_tokens=None, domain=None):
        """
        Get an existing DomainDkim resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] dkim_tokens: DKIM tokens generated by SES.
               These tokens should be used to create CNAME records used to verify SES Easy DKIM.
               See below for an example of how this might be achieved
               when the domain is hosted in Route 53 and managed by this provider.
               Find out more about verifying domains in Amazon SES
               in the [AWS SES docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html).
        :param pulumi.Input[str] domain: Verified domain name to generate DKIM tokens for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["dkim_tokens"] = dkim_tokens
        __props__["domain"] = domain
        return DomainDkim(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
