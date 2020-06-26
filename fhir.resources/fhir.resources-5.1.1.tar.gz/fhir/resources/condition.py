# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Condition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Condition(domainresource.DomainResource):
    """ Detailed information about conditions, problems or diagnoses.

    A clinical condition, problem, diagnosis, or other event, situation, issue,
    or clinical concept that has risen to a level of concern.
    """

    resource_type = "Condition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.abatementAge = None
        """ When in resolution/remission.
        Type `Age` (represented as `dict` in JSON). """

        self.abatementDateTime = None
        """ When in resolution/remission.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.abatementPeriod = None
        """ When in resolution/remission.
        Type `Period` (represented as `dict` in JSON). """

        self.abatementRange = None
        """ When in resolution/remission.
        Type `Range` (represented as `dict` in JSON). """

        self.abatementString = None
        """ When in resolution/remission.
        Type `str`. """

        self.asserter = None
        """ Person who asserts this condition.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Patient', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.bodySite = None
        """ Anatomical location, if relevant.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.category = None
        """ problem-list-item | encounter-diagnosis.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.clinicalStatus = None
        """ active | recurrence | relapse | inactive | remission | resolved.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.code = None
        """ Identification of the condition, problem or diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.evidence = None
        """ Supporting evidence.
        List of `ConditionEvidence` items (represented as `dict` in JSON). """

        self.identifier = None
        """ External Ids for this condition.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.note = None
        """ Additional information about the Condition.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.onsetAge = None
        """ Estimated or actual date,  date-time, or age.
        Type `Age` (represented as `dict` in JSON). """

        self.onsetDateTime = None
        """ Estimated or actual date,  date-time, or age.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.onsetPeriod = None
        """ Estimated or actual date,  date-time, or age.
        Type `Period` (represented as `dict` in JSON). """

        self.onsetRange = None
        """ Estimated or actual date,  date-time, or age.
        Type `Range` (represented as `dict` in JSON). """

        self.onsetString = None
        """ Estimated or actual date,  date-time, or age.
        Type `str`. """

        self.recordedDate = None
        """ Date record was first recorded.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.recorder = None
        """ Who recorded the condition.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Patient', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.severity = None
        """ Subjective severity of condition.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.stage = None
        """ Stage/grade, usually assessed formally.
        List of `ConditionStage` items (represented as `dict` in JSON). """

        self.subject = None
        """ Who has the condition?.
        Type `FHIRReference` referencing `['Patient', 'Group']` (represented as `dict` in JSON). """

        self.verificationStatus = None
        """ unconfirmed | provisional | differential | confirmed | refuted |
        entered-in-error.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(Condition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Condition, self).elementProperties()
        js.extend(
            [
                (
                    "abatementAge",
                    "abatementAge",
                    age.Age,
                    "Age",
                    False,
                    "abatement",
                    False,
                ),
                (
                    "abatementDateTime",
                    "abatementDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "abatement",
                    False,
                ),
                (
                    "abatementPeriod",
                    "abatementPeriod",
                    period.Period,
                    "Period",
                    False,
                    "abatement",
                    False,
                ),
                (
                    "abatementRange",
                    "abatementRange",
                    range.Range,
                    "Range",
                    False,
                    "abatement",
                    False,
                ),
                (
                    "abatementString",
                    "abatementString",
                    str,
                    "string",
                    False,
                    "abatement",
                    False,
                ),
                (
                    "asserter",
                    "asserter",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "bodySite",
                    "bodySite",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "clinicalStatus",
                    "clinicalStatus",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
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
                (
                    "encounter",
                    "encounter",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "evidence",
                    "evidence",
                    ConditionEvidence,
                    "ConditionEvidence",
                    True,
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
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                ("onsetAge", "onsetAge", age.Age, "Age", False, "onset", False),
                (
                    "onsetDateTime",
                    "onsetDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "onset",
                    False,
                ),
                (
                    "onsetPeriod",
                    "onsetPeriod",
                    period.Period,
                    "Period",
                    False,
                    "onset",
                    False,
                ),
                (
                    "onsetRange",
                    "onsetRange",
                    range.Range,
                    "Range",
                    False,
                    "onset",
                    False,
                ),
                ("onsetString", "onsetString", str, "string", False, "onset", False),
                (
                    "recordedDate",
                    "recordedDate",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "recorder",
                    "recorder",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "severity",
                    "severity",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("stage", "stage", ConditionStage, "ConditionStage", True, None, False),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "verificationStatus",
                    "verificationStatus",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class ConditionEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.

    Supporting evidence / manifestations that are the basis of the Condition's
    verification status, such as evidence that confirmed or refuted the
    condition.
    """

    resource_type = "ConditionEvidence"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Manifestation/symptom.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.detail = None
        """ Supporting information found elsewhere.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        super(ConditionEvidence, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConditionEvidence, self).elementProperties()
        js.extend(
            [
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "detail",
                    "detail",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class ConditionStage(backboneelement.BackboneElement):
    """ Stage/grade, usually assessed formally.

    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """

    resource_type = "ConditionStage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.assessment = None
        """ Formal record of assessment.
        List of `FHIRReference` items referencing `['ClinicalImpression', 'DiagnosticReport', 'Observation']` (represented as `dict` in JSON). """

        self.summary = None
        """ Simple summary (disease specific).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.type = None
        """ Kind of staging.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ConditionStage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConditionStage, self).elementProperties()
        js.extend(
            [
                (
                    "assessment",
                    "assessment",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "summary",
                    "summary",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
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


try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + ".age"]
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + ".annotation"]
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
