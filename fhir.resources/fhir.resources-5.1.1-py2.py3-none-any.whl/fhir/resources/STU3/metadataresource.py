# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MetadataResource
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import domainresource


class MetadataResource(domainresource.DomainResource):
    """ Common Ancestor declaration for definitional resources.

    Common Ancestor declaration for conformance and knowledge artifact
    resources.
    """

    resource_type = "MetadataResource"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the metadata resource.
        Type `str`. """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.jurisdiction = None
        """ Intended jurisdiction for metadata resource (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.name = None
        """ Name for this metadata resource (computer friendly).
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.title = None
        """ Name for this metadata resource (human friendly).
        Type `str`. """

        self.url = None
        """ Logical URI to reference this metadata resource (globally unique).
        Type `str`. """

        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the metadata resource.
        Type `str`. """

        super(MetadataResource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MetadataResource, self).elementProperties()
        js.extend(
            [
                (
                    "contact",
                    "contact",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                ("description", "description", str, "markdown", False, None, False),
                ("experimental", "experimental", bool, "boolean", False, None, False),
                (
                    "jurisdiction",
                    "jurisdiction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("name", "name", str, "string", False, None, False),
                ("publisher", "publisher", str, "string", False, None, False),
                ("status", "status", str, "code", False, None, True),
                ("title", "title", str, "string", False, None, False),
                ("url", "url", str, "uri", False, None, False),
                (
                    "useContext",
                    "useContext",
                    usagecontext.UsageContext,
                    "UsageContext",
                    True,
                    None,
                    False,
                ),
                ("version", "version", str, "string", False, None, False),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + ".contactdetail"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + ".usagecontext"]
