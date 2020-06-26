# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CarePlan
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class CarePlan(domainresource.DomainResource):
    """ Healthcare plan for patient or group.

    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """

    resource_type = "CarePlan"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.activity = None
        """ Action to occur as part of plan.
        List of `CarePlanActivity` items (represented as `dict` in JSON). """

        self.addresses = None
        """ Health issues this plan addresses.
        List of `FHIRReference` items referencing `['Condition']` (represented as `dict` in JSON). """

        self.author = None
        """ Who is the designated responsible party.
        Type `FHIRReference` referencing `['Patient', 'Practitioner', 'PractitionerRole', 'Device', 'RelatedPerson', 'Organization', 'CareTeam']` (represented as `dict` in JSON). """

        self.basedOn = None
        """ Fulfills CarePlan.
        List of `FHIRReference` items referencing `['CarePlan']` (represented as `dict` in JSON). """

        self.careTeam = None
        """ Who's involved in plan?.
        List of `FHIRReference` items referencing `['CareTeam']` (represented as `dict` in JSON). """

        self.category = None
        """ Type of plan.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.contributor = None
        """ Who provided the content of the care plan.
        List of `FHIRReference` items referencing `['Patient', 'Practitioner', 'PractitionerRole', 'Device', 'RelatedPerson', 'Organization', 'CareTeam']` (represented as `dict` in JSON). """

        self.created = None
        """ Date record was first recorded.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Summary of nature of plan.
        Type `str`. """

        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.goal = None
        """ Desired outcome of plan.
        List of `FHIRReference` items referencing `['Goal']` (represented as `dict` in JSON). """

        self.identifier = None
        """ External Ids for this plan.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items referencing `['PlanDefinition', 'Questionnaire', 'Measure', 'ActivityDefinition', 'OperationDefinition']`. """

        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """

        self.intent = None
        """ proposal | plan | order | option.
        Type `str`. """

        self.note = None
        """ Comments about the plan.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.partOf = None
        """ Part of referenced CarePlan.
        List of `FHIRReference` items referencing `['CarePlan']` (represented as `dict` in JSON). """

        self.period = None
        """ Time period plan covers.
        Type `Period` (represented as `dict` in JSON). """

        self.replaces = None
        """ CarePlan replaced by this CarePlan.
        List of `FHIRReference` items referencing `['CarePlan']` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """

        self.subject = None
        """ Who the care plan is for.
        Type `FHIRReference` referencing `['Patient', 'Group']` (represented as `dict` in JSON). """

        self.supportingInfo = None
        """ Information considered as part of plan.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.title = None
        """ Human-friendly name for the care plan.
        Type `str`. """

        super(CarePlan, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CarePlan, self).elementProperties()
        js.extend(
            [
                (
                    "activity",
                    "activity",
                    CarePlanActivity,
                    "CarePlanActivity",
                    True,
                    None,
                    False,
                ),
                (
                    "addresses",
                    "addresses",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "author",
                    "author",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "basedOn",
                    "basedOn",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "careTeam",
                    "careTeam",
                    fhirreference.FHIRReference,
                    "Reference",
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
                    "contributor",
                    "contributor",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
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
                    "encounter",
                    "encounter",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "goal",
                    "goal",
                    fhirreference.FHIRReference,
                    "Reference",
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
                    "instantiatesCanonical",
                    "instantiatesCanonical",
                    str,
                    "canonical",
                    True,
                    None,
                    False,
                ),
                ("instantiatesUri", "instantiatesUri", str, "uri", True, None, False),
                ("intent", "intent", str, "code", False, None, True),
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
                    "partOf",
                    "partOf",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                (
                    "replaces",
                    "replaces",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
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
                    True,
                ),
                (
                    "supportingInfo",
                    "supportingInfo",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("title", "title", str, "string", False, None, False),
            ]
        )
        return js


class CarePlanActivity(backboneelement.BackboneElement):
    """ Action to occur as part of plan.

    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """

    resource_type = "CarePlanActivity"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.detail = None
        """ In-line definition of activity.
        Type `CarePlanActivityDetail` (represented as `dict` in JSON). """

        self.outcomeCodeableConcept = None
        """ Results of the activity.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.outcomeReference = None
        """ Appointment, Encounter, Procedure, etc..
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.progress = None
        """ Comments about the activity status/progress.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.reference = None
        """ Activity details defined in specific resource.
        Type `FHIRReference` referencing `['Appointment', 'CommunicationRequest', 'DeviceRequest', 'MedicationRequest', 'NutritionOrder', 'Task', 'ServiceRequest', 'VisionPrescription', 'RequestGroup']` (represented as `dict` in JSON). """

        super(CarePlanActivity, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CarePlanActivity, self).elementProperties()
        js.extend(
            [
                (
                    "detail",
                    "detail",
                    CarePlanActivityDetail,
                    "CarePlanActivityDetail",
                    False,
                    None,
                    False,
                ),
                (
                    "outcomeCodeableConcept",
                    "outcomeCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "outcomeReference",
                    "outcomeReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "progress",
                    "progress",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                (
                    "reference",
                    "reference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class CarePlanActivityDetail(backboneelement.BackboneElement):
    """ In-line definition of activity.

    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """

    resource_type = "CarePlanActivityDetail"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.dailyAmount = None
        """ How to consume/day?.
        Type `Quantity` (represented as `dict` in JSON). """

        self.description = None
        """ Extra info describing activity to perform.
        Type `str`. """

        self.doNotPerform = None
        """ If true, activity is prohibiting action.
        Type `bool`. """

        self.goal = None
        """ Goals this activity relates to.
        List of `FHIRReference` items referencing `['Goal']` (represented as `dict` in JSON). """

        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items referencing `['PlanDefinition', 'ActivityDefinition', 'Questionnaire', 'Measure', 'OperationDefinition']`. """

        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """

        self.kind = None
        """ Appointment | CommunicationRequest | DeviceRequest |
        MedicationRequest | NutritionOrder | Task | ServiceRequest |
        VisionPrescription.
        Type `str`. """

        self.location = None
        """ Where it should happen.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.performer = None
        """ Who will be responsible?.
        List of `FHIRReference` items referencing `['Practitioner', 'PractitionerRole', 'Organization', 'RelatedPerson', 'Patient', 'CareTeam', 'HealthcareService', 'Device']` (represented as `dict` in JSON). """

        self.productCodeableConcept = None
        """ What is to be administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.productReference = None
        """ What is to be administered/supplied.
        Type `FHIRReference` referencing `['Medication', 'Substance']` (represented as `dict` in JSON). """

        self.quantity = None
        """ How much to administer/supply/consume.
        Type `Quantity` (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Why activity should be done or why activity was prohibited.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why activity is needed.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'DiagnosticReport', 'DocumentReference']` (represented as `dict` in JSON). """

        self.scheduledPeriod = None
        """ When activity is to occur.
        Type `Period` (represented as `dict` in JSON). """

        self.scheduledString = None
        """ When activity is to occur.
        Type `str`. """

        self.scheduledTiming = None
        """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """

        self.status = None
        """ not-started | scheduled | in-progress | on-hold | completed |
        cancelled | stopped | unknown | entered-in-error.
        Type `str`. """

        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(CarePlanActivityDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CarePlanActivityDetail, self).elementProperties()
        js.extend(
            [
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
                    "dailyAmount",
                    "dailyAmount",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
                ("doNotPerform", "doNotPerform", bool, "boolean", False, None, False),
                (
                    "goal",
                    "goal",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "instantiatesCanonical",
                    "instantiatesCanonical",
                    str,
                    "canonical",
                    True,
                    None,
                    False,
                ),
                ("instantiatesUri", "instantiatesUri", str, "uri", True, None, False),
                ("kind", "kind", str, "code", False, None, False),
                (
                    "location",
                    "location",
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
                    True,
                    None,
                    False,
                ),
                (
                    "productCodeableConcept",
                    "productCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "product",
                    False,
                ),
                (
                    "productReference",
                    "productReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "product",
                    False,
                ),
                (
                    "quantity",
                    "quantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "reasonCode",
                    "reasonCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "reasonReference",
                    "reasonReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "scheduledPeriod",
                    "scheduledPeriod",
                    period.Period,
                    "Period",
                    False,
                    "scheduled",
                    False,
                ),
                (
                    "scheduledString",
                    "scheduledString",
                    str,
                    "string",
                    False,
                    "scheduled",
                    False,
                ),
                (
                    "scheduledTiming",
                    "scheduledTiming",
                    timing.Timing,
                    "Timing",
                    False,
                    "scheduled",
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "statusReason",
                    "statusReason",
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
