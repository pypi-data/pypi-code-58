# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Note(pulumi.CustomResource):
    attestation_authority: pulumi.Output[dict]
    """
    Note kind that represents a logical attestation "role" or "authority".
    For example, an organization might have one AttestationAuthority for
    "QA" and one for "build". This Note is intended to act strictly as a
    grouping mechanism for the attached Occurrences (Attestations). This
    grouping mechanism also provides a security boundary, since IAM ACLs
    gate the ability for a principle to attach an Occurrence to a given
    Note. It also provides a single point of lookup to find all attached
    Attestation Occurrences, even if they don't all live in the same
    project.  Structure is documented below.

      * `hint` (`dict`) - This submessage provides human-readable hints about the purpose of
        the AttestationAuthority. Because the name of a Note acts as its
        resource reference, it is important to disambiguate the canonical
        name of the Note (which might be a UUID for security purposes)
        from "readable" names more suitable for debug output. Note that
        these hints should NOT be used to look up AttestationAuthorities
        in security sensitive contexts, such as when looking up
        Attestations to verify.  Structure is documented below.
        * `humanReadableName` (`str`) - The human readable name of this Attestation Authority, for
          example "qa".
    """
    create_time: pulumi.Output[str]
    """
    The time this note was created.
    """
    expiration_time: pulumi.Output[str]
    """
    Time of expiration for this note. Leave empty if note does not expire.
    """
    kind: pulumi.Output[str]
    """
    The type of analysis this note describes
    """
    long_description: pulumi.Output[str]
    """
    A detailed description of the note
    """
    name: pulumi.Output[str]
    """
    The name of the note.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    related_note_names: pulumi.Output[list]
    """
    Names of other notes related to this note.
    """
    related_urls: pulumi.Output[list]
    """
    URLs associated with this note and related metadata.  Structure is documented below.

      * `label` (`str`) - Label to describe usage of the URL
      * `url` (`str`) - Specific URL associated with the resource.
    """
    short_description: pulumi.Output[str]
    """
    A one sentence description of the note.
    """
    update_time: pulumi.Output[str]
    """
    The time this note was last updated.
    """
    def __init__(__self__, resource_name, opts=None, attestation_authority=None, expiration_time=None, long_description=None, name=None, project=None, related_note_names=None, related_urls=None, short_description=None, __props__=None, __name__=None, __opts__=None):
        """
        A Container Analysis note is a high-level piece of metadata that
        describes a type of analysis that can be done for a resource.

        To get more information about Note, see:

        * [API documentation](https://cloud.google.com/container-analysis/api/reference/rest/)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/container-analysis/)
            * [Creating Attestations (Occurrences)](https://cloud.google.com/binary-authorization/docs/making-attestations)

        ## Example Usage
        ### Container Analysis Note Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        note = gcp.containeranalysis.Note("note", attestation_authority={
            "hint": {
                "humanReadableName": "Attestor Note",
            },
        })
        ```
        ### Container Analysis Note Attestation Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        note = gcp.containeranalysis.Note("note",
            attestation_authority={
                "hint": {
                    "humanReadableName": "Attestor Note",
                },
            },
            expiration_time="2120-10-02T15:01:23.045123456Z",
            long_description="a longer description of test note",
            related_urls=[
                {
                    "label": "foo",
                    "url": "some.url",
                },
                {
                    "url": "google.com",
                },
            ],
            short_description="test note")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] attestation_authority: Note kind that represents a logical attestation "role" or "authority".
               For example, an organization might have one AttestationAuthority for
               "QA" and one for "build". This Note is intended to act strictly as a
               grouping mechanism for the attached Occurrences (Attestations). This
               grouping mechanism also provides a security boundary, since IAM ACLs
               gate the ability for a principle to attach an Occurrence to a given
               Note. It also provides a single point of lookup to find all attached
               Attestation Occurrences, even if they don't all live in the same
               project.  Structure is documented below.
        :param pulumi.Input[str] expiration_time: Time of expiration for this note. Leave empty if note does not expire.
        :param pulumi.Input[str] long_description: A detailed description of the note
        :param pulumi.Input[str] name: The name of the note.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[list] related_note_names: Names of other notes related to this note.
        :param pulumi.Input[list] related_urls: URLs associated with this note and related metadata.  Structure is documented below.
        :param pulumi.Input[str] short_description: A one sentence description of the note.

        The **attestation_authority** object supports the following:

          * `hint` (`pulumi.Input[dict]`) - This submessage provides human-readable hints about the purpose of
            the AttestationAuthority. Because the name of a Note acts as its
            resource reference, it is important to disambiguate the canonical
            name of the Note (which might be a UUID for security purposes)
            from "readable" names more suitable for debug output. Note that
            these hints should NOT be used to look up AttestationAuthorities
            in security sensitive contexts, such as when looking up
            Attestations to verify.  Structure is documented below.
            * `humanReadableName` (`pulumi.Input[str]`) - The human readable name of this Attestation Authority, for
              example "qa".

        The **related_urls** object supports the following:

          * `label` (`pulumi.Input[str]`) - Label to describe usage of the URL
          * `url` (`pulumi.Input[str]`) - Specific URL associated with the resource.
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

            if attestation_authority is None:
                raise TypeError("Missing required property 'attestation_authority'")
            __props__['attestation_authority'] = attestation_authority
            __props__['expiration_time'] = expiration_time
            __props__['long_description'] = long_description
            __props__['name'] = name
            __props__['project'] = project
            __props__['related_note_names'] = related_note_names
            __props__['related_urls'] = related_urls
            __props__['short_description'] = short_description
            __props__['create_time'] = None
            __props__['kind'] = None
            __props__['update_time'] = None
        super(Note, __self__).__init__(
            'gcp:containeranalysis/note:Note',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, attestation_authority=None, create_time=None, expiration_time=None, kind=None, long_description=None, name=None, project=None, related_note_names=None, related_urls=None, short_description=None, update_time=None):
        """
        Get an existing Note resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] attestation_authority: Note kind that represents a logical attestation "role" or "authority".
               For example, an organization might have one AttestationAuthority for
               "QA" and one for "build". This Note is intended to act strictly as a
               grouping mechanism for the attached Occurrences (Attestations). This
               grouping mechanism also provides a security boundary, since IAM ACLs
               gate the ability for a principle to attach an Occurrence to a given
               Note. It also provides a single point of lookup to find all attached
               Attestation Occurrences, even if they don't all live in the same
               project.  Structure is documented below.
        :param pulumi.Input[str] create_time: The time this note was created.
        :param pulumi.Input[str] expiration_time: Time of expiration for this note. Leave empty if note does not expire.
        :param pulumi.Input[str] kind: The type of analysis this note describes
        :param pulumi.Input[str] long_description: A detailed description of the note
        :param pulumi.Input[str] name: The name of the note.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[list] related_note_names: Names of other notes related to this note.
        :param pulumi.Input[list] related_urls: URLs associated with this note and related metadata.  Structure is documented below.
        :param pulumi.Input[str] short_description: A one sentence description of the note.
        :param pulumi.Input[str] update_time: The time this note was last updated.

        The **attestation_authority** object supports the following:

          * `hint` (`pulumi.Input[dict]`) - This submessage provides human-readable hints about the purpose of
            the AttestationAuthority. Because the name of a Note acts as its
            resource reference, it is important to disambiguate the canonical
            name of the Note (which might be a UUID for security purposes)
            from "readable" names more suitable for debug output. Note that
            these hints should NOT be used to look up AttestationAuthorities
            in security sensitive contexts, such as when looking up
            Attestations to verify.  Structure is documented below.
            * `humanReadableName` (`pulumi.Input[str]`) - The human readable name of this Attestation Authority, for
              example "qa".

        The **related_urls** object supports the following:

          * `label` (`pulumi.Input[str]`) - Label to describe usage of the URL
          * `url` (`pulumi.Input[str]`) - Specific URL associated with the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["attestation_authority"] = attestation_authority
        __props__["create_time"] = create_time
        __props__["expiration_time"] = expiration_time
        __props__["kind"] = kind
        __props__["long_description"] = long_description
        __props__["name"] = name
        __props__["project"] = project
        __props__["related_note_names"] = related_note_names
        __props__["related_urls"] = related_urls
        __props__["short_description"] = short_description
        __props__["update_time"] = update_time
        return Note(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
