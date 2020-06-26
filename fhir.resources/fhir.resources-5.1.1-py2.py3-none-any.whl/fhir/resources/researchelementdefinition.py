# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class ResearchElementDefinition(domainresource.DomainResource):
    """ A population, intervention, or exposure definition.

    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """

    resource_type = "ResearchElementDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.approvalDate = None
        """ When the research element definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.characteristic = None
        """ What defines the members of the research element.
        List of `ResearchElementDefinitionCharacteristic` items (represented as `dict` in JSON). """

        self.comment = None
        """ Used for footnotes or explanatory notes.
        List of `str` items. """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the research element definition.
        Type `str`. """

        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.effectivePeriod = None
        """ When the research element definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """

        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.identifier = None
        """ Additional identifier for the research element definition.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for research element definition (if
        applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.lastReviewDate = None
        """ When the research element definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.library = None
        """ Logic used by the ResearchElementDefinition.
        List of `str` items referencing `['Library']`. """

        self.name = None
        """ Name for this research element definition (computer friendly).
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this research element definition is defined.
        Type `str`. """

        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """

        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.shortTitle = None
        """ Title for use in informal contexts.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.subjectCodeableConcept = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subjectReference = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `FHIRReference` referencing `['Group']` (represented as `dict` in JSON). """

        self.subtitle = None
        """ Subordinate title of the ResearchElementDefinition.
        Type `str`. """

        self.title = None
        """ Name for this research element definition (human friendly).
        Type `str`. """

        self.topic = None
        """ The category of the ResearchElementDefinition, such as Education,
        Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.type = None
        """ population | exposure | outcome.
        Type `str`. """

        self.url = None
        """ Canonical identifier for this research element definition,
        represented as a URI (globally unique).
        Type `str`. """

        self.usage = None
        """ Describes the clinical usage of the ResearchElementDefinition.
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.variableType = None
        """ dichotomous | continuous | descriptive.
        Type `str`. """

        self.version = None
        """ Business version of the research element definition.
        Type `str`. """

        super(ResearchElementDefinition, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ResearchElementDefinition, self).elementProperties()
        js.extend(
            [
                (
                    "approvalDate",
                    "approvalDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    None,
                    False,
                ),
                (
                    "author",
                    "author",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                (
                    "characteristic",
                    "characteristic",
                    ResearchElementDefinitionCharacteristic,
                    "ResearchElementDefinitionCharacteristic",
                    True,
                    None,
                    True,
                ),
                ("comment", "comment", str, "string", True, None, False),
                (
                    "contact",
                    "contact",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("copyright", "copyright", str, "markdown", False, None, False),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                ("description", "description", str, "markdown", False, None, False),
                (
                    "editor",
                    "editor",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                (
                    "effectivePeriod",
                    "effectivePeriod",
                    period.Period,
                    "Period",
                    False,
                    None,
                    False,
                ),
                (
                    "endorser",
                    "endorser",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("experimental", "experimental", bool, "boolean", False, None, False),
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
                    "jurisdiction",
                    "jurisdiction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "lastReviewDate",
                    "lastReviewDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    None,
                    False,
                ),
                ("library", "library", str, "canonical", True, None, False),
                ("name", "name", str, "string", False, None, False),
                ("publisher", "publisher", str, "string", False, None, False),
                ("purpose", "purpose", str, "markdown", False, None, False),
                (
                    "relatedArtifact",
                    "relatedArtifact",
                    relatedartifact.RelatedArtifact,
                    "RelatedArtifact",
                    True,
                    None,
                    False,
                ),
                (
                    "reviewer",
                    "reviewer",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("shortTitle", "shortTitle", str, "string", False, None, False),
                ("status", "status", str, "code", False, None, True),
                (
                    "subjectCodeableConcept",
                    "subjectCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "subject",
                    False,
                ),
                (
                    "subjectReference",
                    "subjectReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "subject",
                    False,
                ),
                ("subtitle", "subtitle", str, "string", False, None, False),
                ("title", "title", str, "string", False, None, False),
                (
                    "topic",
                    "topic",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("type", "type", str, "code", False, None, True),
                ("url", "url", str, "uri", False, None, False),
                ("usage", "usage", str, "string", False, None, False),
                (
                    "useContext",
                    "useContext",
                    usagecontext.UsageContext,
                    "UsageContext",
                    True,
                    None,
                    False,
                ),
                ("variableType", "variableType", str, "code", False, None, False),
                ("version", "version", str, "string", False, None, False),
            ]
        )
        return js


class ResearchElementDefinitionCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the research element.

    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """

    resource_type = "ResearchElementDefinitionCharacteristic"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.definitionCanonical = None
        """ What code or expression defines members?.
        Type `str` referencing `['ValueSet']`. """

        self.definitionCodeableConcept = None
        """ What code or expression defines members?.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.definitionDataRequirement = None
        """ What code or expression defines members?.
        Type `DataRequirement` (represented as `dict` in JSON). """

        self.definitionExpression = None
        """ What code or expression defines members?.
        Type `Expression` (represented as `dict` in JSON). """

        self.exclude = None
        """ Whether the characteristic includes or excludes members.
        Type `bool`. """

        self.participantEffectiveDateTime = None
        """ What time period do participants cover.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.participantEffectiveDescription = None
        """ What time period do participants cover.
        Type `str`. """

        self.participantEffectiveDuration = None
        """ What time period do participants cover.
        Type `Duration` (represented as `dict` in JSON). """

        self.participantEffectiveGroupMeasure = None
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `str`. """

        self.participantEffectivePeriod = None
        """ What time period do participants cover.
        Type `Period` (represented as `dict` in JSON). """

        self.participantEffectiveTimeFromStart = None
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """

        self.participantEffectiveTiming = None
        """ What time period do participants cover.
        Type `Timing` (represented as `dict` in JSON). """

        self.studyEffectiveDateTime = None
        """ What time period does the study cover.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.studyEffectiveDescription = None
        """ What time period does the study cover.
        Type `str`. """

        self.studyEffectiveDuration = None
        """ What time period does the study cover.
        Type `Duration` (represented as `dict` in JSON). """

        self.studyEffectiveGroupMeasure = None
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `str`. """

        self.studyEffectivePeriod = None
        """ What time period does the study cover.
        Type `Period` (represented as `dict` in JSON). """

        self.studyEffectiveTimeFromStart = None
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """

        self.studyEffectiveTiming = None
        """ What time period does the study cover.
        Type `Timing` (represented as `dict` in JSON). """

        self.unitOfMeasure = None
        """ What unit is the outcome described in?.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.usageContext = None
        """ What code/value pairs define members?.
        List of `UsageContext` items (represented as `dict` in JSON). """

        super(ResearchElementDefinitionCharacteristic, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ResearchElementDefinitionCharacteristic, self).elementProperties()
        js.extend(
            [
                (
                    "definitionCanonical",
                    "definitionCanonical",
                    str,
                    "canonical",
                    False,
                    "definition",
                    True,
                ),
                (
                    "definitionCodeableConcept",
                    "definitionCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "definition",
                    True,
                ),
                (
                    "definitionDataRequirement",
                    "definitionDataRequirement",
                    datarequirement.DataRequirement,
                    "DataRequirement",
                    False,
                    "definition",
                    True,
                ),
                (
                    "definitionExpression",
                    "definitionExpression",
                    expression.Expression,
                    "Expression",
                    False,
                    "definition",
                    True,
                ),
                ("exclude", "exclude", bool, "boolean", False, None, False),
                (
                    "participantEffectiveDateTime",
                    "participantEffectiveDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "participantEffective",
                    False,
                ),
                (
                    "participantEffectiveDescription",
                    "participantEffectiveDescription",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "participantEffectiveDuration",
                    "participantEffectiveDuration",
                    duration.Duration,
                    "Duration",
                    False,
                    "participantEffective",
                    False,
                ),
                (
                    "participantEffectiveGroupMeasure",
                    "participantEffectiveGroupMeasure",
                    str,
                    "code",
                    False,
                    None,
                    False,
                ),
                (
                    "participantEffectivePeriod",
                    "participantEffectivePeriod",
                    period.Period,
                    "Period",
                    False,
                    "participantEffective",
                    False,
                ),
                (
                    "participantEffectiveTimeFromStart",
                    "participantEffectiveTimeFromStart",
                    duration.Duration,
                    "Duration",
                    False,
                    None,
                    False,
                ),
                (
                    "participantEffectiveTiming",
                    "participantEffectiveTiming",
                    timing.Timing,
                    "Timing",
                    False,
                    "participantEffective",
                    False,
                ),
                (
                    "studyEffectiveDateTime",
                    "studyEffectiveDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "studyEffective",
                    False,
                ),
                (
                    "studyEffectiveDescription",
                    "studyEffectiveDescription",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "studyEffectiveDuration",
                    "studyEffectiveDuration",
                    duration.Duration,
                    "Duration",
                    False,
                    "studyEffective",
                    False,
                ),
                (
                    "studyEffectiveGroupMeasure",
                    "studyEffectiveGroupMeasure",
                    str,
                    "code",
                    False,
                    None,
                    False,
                ),
                (
                    "studyEffectivePeriod",
                    "studyEffectivePeriod",
                    period.Period,
                    "Period",
                    False,
                    "studyEffective",
                    False,
                ),
                (
                    "studyEffectiveTimeFromStart",
                    "studyEffectiveTimeFromStart",
                    duration.Duration,
                    "Duration",
                    False,
                    None,
                    False,
                ),
                (
                    "studyEffectiveTiming",
                    "studyEffectiveTiming",
                    timing.Timing,
                    "Timing",
                    False,
                    "studyEffective",
                    False,
                ),
                (
                    "unitOfMeasure",
                    "unitOfMeasure",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "usageContext",
                    "usageContext",
                    usagecontext.UsageContext,
                    "UsageContext",
                    True,
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
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + ".contactdetail"]
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + ".datarequirement"]
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + ".duration"]
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + ".expression"]
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + ".relatedartifact"]
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + ".usagecontext"]
