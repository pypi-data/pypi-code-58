# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class RiskEvidenceSynthesis(domainresource.DomainResource):
    """ A quantified estimate of risk based on a body of evidence.

    The RiskEvidenceSynthesis resource describes the likelihood of an outcome
    in a population plus exposure state where the risk estimate is derived from
    a combination of research studies.
    """

    resource_type = "RiskEvidenceSynthesis"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.approvalDate = None
        """ When the risk evidence synthesis was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.certainty = None
        """ How certain is the risk.
        List of `RiskEvidenceSynthesisCertainty` items (represented as `dict` in JSON). """

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
        """ Natural language description of the risk evidence synthesis.
        Type `str`. """

        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.effectivePeriod = None
        """ When the risk evidence synthesis is expected to be used.
        Type `Period` (represented as `dict` in JSON). """

        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.exposure = None
        """ What exposure?.
        Type `FHIRReference` referencing `['EvidenceVariable']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Additional identifier for the risk evidence synthesis.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for risk evidence synthesis (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.lastReviewDate = None
        """ When the risk evidence synthesis was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.name = None
        """ Name for this risk evidence synthesis (computer friendly).
        Type `str`. """

        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.outcome = None
        """ What outcome?.
        Type `FHIRReference` referencing `['EvidenceVariable']` (represented as `dict` in JSON). """

        self.population = None
        """ What population?.
        Type `FHIRReference` referencing `['EvidenceVariable']` (represented as `dict` in JSON). """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """

        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.riskEstimate = None
        """ What was the estimated risk.
        Type `RiskEvidenceSynthesisRiskEstimate` (represented as `dict` in JSON). """

        self.sampleSize = None
        """ What sample size was involved?.
        Type `RiskEvidenceSynthesisSampleSize` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.studyType = None
        """ Type of study.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.synthesisType = None
        """ Type of synthesis.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.title = None
        """ Name for this risk evidence synthesis (human friendly).
        Type `str`. """

        self.topic = None
        """ The category of the EffectEvidenceSynthesis, such as Education,
        Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.url = None
        """ Canonical identifier for this risk evidence synthesis, represented
        as a URI (globally unique).
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the risk evidence synthesis.
        Type `str`. """

        super(RiskEvidenceSynthesis, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesis, self).elementProperties()
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
                    "certainty",
                    "certainty",
                    RiskEvidenceSynthesisCertainty,
                    "RiskEvidenceSynthesisCertainty",
                    True,
                    None,
                    False,
                ),
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
                (
                    "exposure",
                    "exposure",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
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
                ("name", "name", str, "string", False, None, False),
                (
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                (
                    "outcome",
                    "outcome",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "population",
                    "population",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("publisher", "publisher", str, "string", False, None, False),
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
                (
                    "riskEstimate",
                    "riskEstimate",
                    RiskEvidenceSynthesisRiskEstimate,
                    "RiskEvidenceSynthesisRiskEstimate",
                    False,
                    None,
                    False,
                ),
                (
                    "sampleSize",
                    "sampleSize",
                    RiskEvidenceSynthesisSampleSize,
                    "RiskEvidenceSynthesisSampleSize",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "studyType",
                    "studyType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "synthesisType",
                    "synthesisType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
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


class RiskEvidenceSynthesisCertainty(backboneelement.BackboneElement):
    """ How certain is the risk.

    A description of the certainty of the risk estimate.
    """

    resource_type = "RiskEvidenceSynthesisCertainty"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.certaintySubcomponent = None
        """ A component that contributes to the overall certainty.
        List of `RiskEvidenceSynthesisCertaintyCertaintySubcomponent` items (represented as `dict` in JSON). """

        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.rating = None
        """ Certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(RiskEvidenceSynthesisCertainty, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertainty, self).elementProperties()
        js.extend(
            [
                (
                    "certaintySubcomponent",
                    "certaintySubcomponent",
                    RiskEvidenceSynthesisCertaintyCertaintySubcomponent,
                    "RiskEvidenceSynthesisCertaintyCertaintySubcomponent",
                    True,
                    None,
                    False,
                ),
                (
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                (
                    "rating",
                    "rating",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class RiskEvidenceSynthesisCertaintyCertaintySubcomponent(
    backboneelement.BackboneElement
):
    """ A component that contributes to the overall certainty.

    A description of a component of the overall certainty.
    """

    resource_type = "RiskEvidenceSynthesisCertaintyCertaintySubcomponent"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.rating = None
        """ Subcomponent certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.type = None
        """ Type of subcomponent of certainty rating.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(
            RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self
        ).elementProperties()
        js.extend(
            [
                (
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                (
                    "rating",
                    "rating",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
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


class RiskEvidenceSynthesisRiskEstimate(backboneelement.BackboneElement):
    """ What was the estimated risk.

    The estimated risk of the outcome.
    """

    resource_type = "RiskEvidenceSynthesisRiskEstimate"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.denominatorCount = None
        """ Sample size for group measured.
        Type `int`. """

        self.description = None
        """ Description of risk estimate.
        Type `str`. """

        self.numeratorCount = None
        """ Number with the outcome.
        Type `int`. """

        self.precisionEstimate = None
        """ How precise the estimate is.
        List of `RiskEvidenceSynthesisRiskEstimatePrecisionEstimate` items (represented as `dict` in JSON). """

        self.type = None
        """ Type of risk estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.unitOfMeasure = None
        """ What unit is the outcome described in?.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.value = None
        """ Point estimate.
        Type `float`. """

        super(RiskEvidenceSynthesisRiskEstimate, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimate, self).elementProperties()
        js.extend(
            [
                (
                    "denominatorCount",
                    "denominatorCount",
                    int,
                    "integer",
                    False,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
                (
                    "numeratorCount",
                    "numeratorCount",
                    int,
                    "integer",
                    False,
                    None,
                    False,
                ),
                (
                    "precisionEstimate",
                    "precisionEstimate",
                    RiskEvidenceSynthesisRiskEstimatePrecisionEstimate,
                    "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate",
                    True,
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
                (
                    "unitOfMeasure",
                    "unitOfMeasure",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("value", "value", float, "decimal", False, None, False),
            ]
        )
        return js


class RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(
    backboneelement.BackboneElement
):
    """ How precise the estimate is.

    A description of the precision of the estimate for the effect.
    """

    resource_type = "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.from_fhir = None
        """ Lower bound.
        Type `float`. """

        self.level = None
        """ Level of confidence interval.
        Type `float`. """

        self.to = None
        """ Upper bound.
        Type `float`. """

        self.type = None
        """ Type of precision estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(
            RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self
        ).elementProperties()
        js.extend(
            [
                ("from_fhir", "from", float, "decimal", False, None, False),
                ("level", "level", float, "decimal", False, None, False),
                ("to", "to", float, "decimal", False, None, False),
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


class RiskEvidenceSynthesisSampleSize(backboneelement.BackboneElement):
    """ What sample size was involved?.

    A description of the size of the sample involved in the synthesis.
    """

    resource_type = "RiskEvidenceSynthesisSampleSize"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Description of sample size.
        Type `str`. """

        self.numberOfParticipants = None
        """ How many participants?.
        Type `int`. """

        self.numberOfStudies = None
        """ How many studies?.
        Type `int`. """

        super(RiskEvidenceSynthesisSampleSize, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisSampleSize, self).elementProperties()
        js.extend(
            [
                ("description", "description", str, "string", False, None, False),
                (
                    "numberOfParticipants",
                    "numberOfParticipants",
                    int,
                    "integer",
                    False,
                    None,
                    False,
                ),
                (
                    "numberOfStudies",
                    "numberOfStudies",
                    int,
                    "integer",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + ".annotation"]
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
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + ".usagecontext"]
