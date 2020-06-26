# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class SslCert(pulumi.CustomResource):
    cert: pulumi.Output[str]
    """
    The actual certificate data for this client certificate.
    """
    cert_serial_number: pulumi.Output[str]
    """
    The serial number extracted from the certificate data.
    """
    common_name: pulumi.Output[str]
    """
    The common name to be used in the certificate to identify the
    client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.
    """
    create_time: pulumi.Output[str]
    """
    The time when the certificate was created in RFC 3339 format,
    for example 2012-11-15T16:19:00.094Z.
    """
    expiration_time: pulumi.Output[str]
    """
    The time when the certificate expires in RFC 3339 format,
    for example 2012-11-15T16:19:00.094Z.
    """
    instance: pulumi.Output[str]
    """
    The name of the Cloud SQL instance. Changing this
    forces a new resource to be created.
    """
    private_key: pulumi.Output[str]
    """
    The private key associated with the client certificate.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs. If it
    is not provided, the provider project is used.
    """
    server_ca_cert: pulumi.Output[str]
    """
    The CA cert of the server this client cert was generated from.
    """
    sha1_fingerprint: pulumi.Output[str]
    """
    The SHA1 Fingerprint of the certificate.
    """
    def __init__(__self__, resource_name, opts=None, common_name=None, instance=None, project=None, __props__=None, __name__=None, __opts__=None):
        """
        Creates a new Google SQL SSL Cert on a Google SQL Instance. For more information, see the [official documentation](https://cloud.google.com/sql/), or the [JSON API](https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/sslCerts).

        ## Example Usage

        Example creating a SQL Client Certificate.

        ```python
        import pulumi
        import pulumi_gcp as gcp
        import pulumi_random as random

        db_name_suffix = random.RandomId("dbNameSuffix", byte_length=4)
        master = gcp.sql.DatabaseInstance("master", settings={
            "tier": "db-f1-micro",
        })
        client_cert = gcp.sql.SslCert("clientCert",
            common_name="client-name",
            instance=master.name)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] common_name: The common name to be used in the certificate to identify the
               client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. Changing this
               forces a new resource to be created.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
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

            if common_name is None:
                raise TypeError("Missing required property 'common_name'")
            __props__['common_name'] = common_name
            if instance is None:
                raise TypeError("Missing required property 'instance'")
            __props__['instance'] = instance
            __props__['project'] = project
            __props__['cert'] = None
            __props__['cert_serial_number'] = None
            __props__['create_time'] = None
            __props__['expiration_time'] = None
            __props__['private_key'] = None
            __props__['server_ca_cert'] = None
            __props__['sha1_fingerprint'] = None
        super(SslCert, __self__).__init__(
            'gcp:sql/sslCert:SslCert',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, cert=None, cert_serial_number=None, common_name=None, create_time=None, expiration_time=None, instance=None, private_key=None, project=None, server_ca_cert=None, sha1_fingerprint=None):
        """
        Get an existing SslCert resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cert: The actual certificate data for this client certificate.
        :param pulumi.Input[str] cert_serial_number: The serial number extracted from the certificate data.
        :param pulumi.Input[str] common_name: The common name to be used in the certificate to identify the
               client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.
        :param pulumi.Input[str] create_time: The time when the certificate was created in RFC 3339 format,
               for example 2012-11-15T16:19:00.094Z.
        :param pulumi.Input[str] expiration_time: The time when the certificate expires in RFC 3339 format,
               for example 2012-11-15T16:19:00.094Z.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. Changing this
               forces a new resource to be created.
        :param pulumi.Input[str] private_key: The private key associated with the client certificate.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] server_ca_cert: The CA cert of the server this client cert was generated from.
        :param pulumi.Input[str] sha1_fingerprint: The SHA1 Fingerprint of the certificate.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cert"] = cert
        __props__["cert_serial_number"] = cert_serial_number
        __props__["common_name"] = common_name
        __props__["create_time"] = create_time
        __props__["expiration_time"] = expiration_time
        __props__["instance"] = instance
        __props__["private_key"] = private_key
        __props__["project"] = project
        __props__["server_ca_cert"] = server_ca_cert
        __props__["sha1_fingerprint"] = sha1_fingerprint
        return SslCert(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
