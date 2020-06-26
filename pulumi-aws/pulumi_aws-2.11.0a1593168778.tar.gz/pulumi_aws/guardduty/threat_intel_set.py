# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class ThreatIntelSet(pulumi.CustomResource):
    activate: pulumi.Output[bool]
    """
    Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.
    """
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the GuardDuty ThreatIntelSet.
    """
    detector_id: pulumi.Output[str]
    """
    The detector ID of the GuardDuty.
    """
    format: pulumi.Output[str]
    """
    The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`
    """
    location: pulumi.Output[str]
    """
    The URI of the file that contains the ThreatIntelSet.
    """
    name: pulumi.Output[str]
    """
    The friendly name to identify the ThreatIntelSet.
    """
    tags: pulumi.Output[dict]
    """
    Key-value map of resource tags.
    """
    def __init__(__self__, resource_name, opts=None, activate=None, detector_id=None, format=None, location=None, name=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a resource to manage a GuardDuty ThreatIntelSet.

        > **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage ThreatIntelSets. ThreatIntelSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-threat-intel-set.html)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        master = aws.guardduty.Detector("master", enable=True)
        bucket = aws.s3.Bucket("bucket", acl="private")
        my_threat_intel_set_bucket_object = aws.s3.BucketObject("myThreatIntelSetBucketObject",
            acl="public-read",
            bucket=bucket.id,
            content=\"\"\"10.0.0.0/8

        \"\"\",
            key="MyThreatIntelSet")
        my_threat_intel_set_threat_intel_set = aws.guardduty.ThreatIntelSet("myThreatIntelSetThreatIntelSet",
            activate=True,
            detector_id=master.id,
            format="TXT",
            location=pulumi.Output.all(my_threat_intel_set_bucket_object.bucket, my_threat_intel_set_bucket_object.key).apply(lambda bucket, key: f"https://s3.amazonaws.com/{bucket}/{key}"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] activate: Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.
        :param pulumi.Input[str] detector_id: The detector ID of the GuardDuty.
        :param pulumi.Input[str] format: The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`
        :param pulumi.Input[str] location: The URI of the file that contains the ThreatIntelSet.
        :param pulumi.Input[str] name: The friendly name to identify the ThreatIntelSet.
        :param pulumi.Input[dict] tags: Key-value map of resource tags.
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

            if activate is None:
                raise TypeError("Missing required property 'activate'")
            __props__['activate'] = activate
            if detector_id is None:
                raise TypeError("Missing required property 'detector_id'")
            __props__['detector_id'] = detector_id
            if format is None:
                raise TypeError("Missing required property 'format'")
            __props__['format'] = format
            if location is None:
                raise TypeError("Missing required property 'location'")
            __props__['location'] = location
            __props__['name'] = name
            __props__['tags'] = tags
            __props__['arn'] = None
        super(ThreatIntelSet, __self__).__init__(
            'aws:guardduty/threatIntelSet:ThreatIntelSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, activate=None, arn=None, detector_id=None, format=None, location=None, name=None, tags=None):
        """
        Get an existing ThreatIntelSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] activate: Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the GuardDuty ThreatIntelSet.
        :param pulumi.Input[str] detector_id: The detector ID of the GuardDuty.
        :param pulumi.Input[str] format: The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`
        :param pulumi.Input[str] location: The URI of the file that contains the ThreatIntelSet.
        :param pulumi.Input[str] name: The friendly name to identify the ThreatIntelSet.
        :param pulumi.Input[dict] tags: Key-value map of resource tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["activate"] = activate
        __props__["arn"] = arn
        __props__["detector_id"] = detector_id
        __props__["format"] = format
        __props__["location"] = location
        __props__["name"] = name
        __props__["tags"] = tags
        return ThreatIntelSet(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
