# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Meta
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import element


class Meta(element.Element):
    """ Metadata about a resource.

    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
    """

    resource_type = "Meta"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.lastUpdated = None
        """ When the resource version last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.profile = None
        """ Profiles this resource claims to conform to.
        List of `str` items referencing `['StructureDefinition']`. """

        self.security = None
        """ Security Labels applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """

        self.source = None
        """ Identifies where the resource comes from.
        Type `str`. """

        self.tag = None
        """ Tags applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """

        self.versionId = None
        """ Version specific identifier.
        Type `str`. """

        super(Meta, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Meta, self).elementProperties()
        js.extend(
            [
                (
                    "lastUpdated",
                    "lastUpdated",
                    fhirdate.FHIRDate,
                    "instant",
                    False,
                    None,
                    False,
                ),
                ("profile", "profile", str, "canonical", True, None, False),
                ("security", "security", coding.Coding, "Coding", True, None, False),
                ("source", "source", str, "uri", False, None, False),
                ("tag", "tag", coding.Coding, "Coding", True, None, False),
                ("versionId", "versionId", str, "id", False, None, False),
            ]
        )
        return js


try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + ".coding"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
