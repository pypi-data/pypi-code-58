# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RiskAssessment
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class RiskAssessment(domainresource.DomainResource):
    """ Potential outcomes for a subject with likelihood.

    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """

    resource_type = "RiskAssessment"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.basedOn = None
        """ Request fulfilled by this assessment.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.basis = None
        """ Information used in assessment.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.code = None
        """ Type of assessment.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.comment = None
        """ Comments on the risk assessment.
        Type `str`. """

        self.condition = None
        """ Condition assessed.
        Type `FHIRReference` referencing `['Condition']` (represented as `dict` in JSON). """

        self.context = None
        """ Where was assessment performed?.
        Type `FHIRReference` referencing `['Encounter'], ['EpisodeOfCare']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Unique identifier for the assessment.
        Type `Identifier` (represented as `dict` in JSON). """

        self.method = None
        """ Evaluation mechanism.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.mitigation = None
        """ How to reduce risk.
        Type `str`. """

        self.occurrenceDateTime = None
        """ When was assessment made?.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.occurrencePeriod = None
        """ When was assessment made?.
        Type `Period` (represented as `dict` in JSON). """

        self.parent = None
        """ Part of this occurrence.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.performer = None
        """ Who did assessment?.
        Type `FHIRReference` referencing `['Practitioner'], ['Device']` (represented as `dict` in JSON). """

        self.prediction = None
        """ Outcome predicted.
        List of `RiskAssessmentPrediction` items (represented as `dict` in JSON). """

        self.reasonCodeableConcept = None
        """ Why the assessment was necessary?.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why the assessment was necessary?.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.status = None
        """ registered | preliminary | final | amended +.
        Type `str`. """

        self.subject = None
        """ Who/what does assessment apply to?.
        Type `FHIRReference` referencing `['Patient'], ['Group']` (represented as `dict` in JSON). """

        super(RiskAssessment, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskAssessment, self).elementProperties()
        js.extend(
            [
                (
                    "basedOn",
                    "basedOn",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "basis",
                    "basis",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("comment", "comment", str, "string", False, None, False),
                (
                    "condition",
                    "condition",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "context",
                    "context",
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
                    False,
                    None,
                    False,
                ),
                (
                    "method",
                    "method",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("mitigation", "mitigation", str, "string", False, None, False),
                (
                    "occurrenceDateTime",
                    "occurrenceDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "occurrence",
                    False,
                ),
                (
                    "occurrencePeriod",
                    "occurrencePeriod",
                    period.Period,
                    "Period",
                    False,
                    "occurrence",
                    False,
                ),
                (
                    "parent",
                    "parent",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "performer",
                    "performer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "prediction",
                    "prediction",
                    RiskAssessmentPrediction,
                    "RiskAssessmentPrediction",
                    True,
                    None,
                    False,
                ),
                (
                    "reasonCodeableConcept",
                    "reasonCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "reason",
                    False,
                ),
                (
                    "reasonReference",
                    "reasonReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "reason",
                    False,
                ),
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
            ]
        )
        return js


class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """ Outcome predicted.

    Describes the expected outcome for the subject.
    """

    resource_type = "RiskAssessmentPrediction"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.outcome = None
        """ Possible outcome for the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.probabilityDecimal = None
        """ Likelihood of specified outcome.
        Type `float`. """

        self.probabilityRange = None
        """ Likelihood of specified outcome.
        Type `Range` (represented as `dict` in JSON). """

        self.qualitativeRisk = None
        """ Likelihood of specified outcome as a qualitative value.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.rationale = None
        """ Explanation of prediction.
        Type `str`. """

        self.relativeRisk = None
        """ Relative likelihood.
        Type `float`. """

        self.whenPeriod = None
        """ Timeframe or age range.
        Type `Period` (represented as `dict` in JSON). """

        self.whenRange = None
        """ Timeframe or age range.
        Type `Range` (represented as `dict` in JSON). """

        super(RiskAssessmentPrediction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskAssessmentPrediction, self).elementProperties()
        js.extend(
            [
                (
                    "outcome",
                    "outcome",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "probabilityDecimal",
                    "probabilityDecimal",
                    float,
                    "decimal",
                    False,
                    "probability",
                    False,
                ),
                (
                    "probabilityRange",
                    "probabilityRange",
                    range.Range,
                    "Range",
                    False,
                    "probability",
                    False,
                ),
                (
                    "qualitativeRisk",
                    "qualitativeRisk",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("rationale", "rationale", str, "string", False, None, False),
                ("relativeRisk", "relativeRisk", float, "decimal", False, None, False),
                (
                    "whenPeriod",
                    "whenPeriod",
                    period.Period,
                    "Period",
                    False,
                    "when",
                    False,
                ),
                ("whenRange", "whenRange", range.Range, "Range", False, "when", False),
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
