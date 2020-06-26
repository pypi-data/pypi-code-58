# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentManifest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class DocumentManifest(domainresource.DomainResource):
    """ A list that defines a set of documents.

    A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """

    resource_type = "DocumentManifest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.author = None
        """ Who and/or what authored the DocumentManifest.
        List of `FHIRReference` items referencing `['Practitioner', 'PractitionerRole', 'Organization', 'Device', 'Patient', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.content = None
        """ Items in manifest.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.created = None
        """ When this document manifest created.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Human-readable description (title).
        Type `str`. """

        self.identifier = None
        """ Other identifiers for the manifest.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.masterIdentifier = None
        """ Unique Identifier for the set of documents.
        Type `Identifier` (represented as `dict` in JSON). """

        self.recipient = None
        """ Intended to get notified about this set of documents.
        List of `FHIRReference` items referencing `['Patient', 'Practitioner', 'PractitionerRole', 'RelatedPerson', 'Organization']` (represented as `dict` in JSON). """

        self.related = None
        """ Related things.
        List of `DocumentManifestRelated` items (represented as `dict` in JSON). """

        self.source = None
        """ The source system/application/software.
        Type `str`. """

        self.status = None
        """ current | superseded | entered-in-error.
        Type `str`. """

        self.subject = None
        """ The subject of the set of documents.
        Type `FHIRReference` referencing `['Patient', 'Practitioner', 'Group', 'Device']` (represented as `dict` in JSON). """

        self.type = None
        """ Kind of document set.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(DocumentManifest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DocumentManifest, self).elementProperties()
        js.extend(
            [
                (
                    "author",
                    "author",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "content",
                    "content",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    True,
                ),
                (
                    "created",
                    "created",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                (
                    "masterIdentifier",
                    "masterIdentifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                (
                    "recipient",
                    "recipient",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "related",
                    "related",
                    DocumentManifestRelated,
                    "DocumentManifestRelated",
                    True,
                    None,
                    False,
                ),
                ("source", "source", str, "uri", False, None, False),
                ("status", "status", str, "code", False, None, True),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class DocumentManifestRelated(backboneelement.BackboneElement):
    """ Related things.

    Related identifiers or resources associated with the DocumentManifest.
    """

    resource_type = "DocumentManifestRelated"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Identifiers of things that are related.
        Type `Identifier` (represented as `dict` in JSON). """

        self.ref = None
        """ Related Resource.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        super(DocumentManifestRelated, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DocumentManifestRelated, self).elementProperties()
        js.extend(
            [
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                (
                    "ref",
                    "ref",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
