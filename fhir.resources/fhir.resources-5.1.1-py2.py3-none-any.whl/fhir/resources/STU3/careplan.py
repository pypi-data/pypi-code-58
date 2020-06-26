# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CarePlan
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
        """ Who is responsible for contents of the plan.
        List of `FHIRReference` items referencing `['Patient'], ['Practitioner'], ['RelatedPerson'], ['Organization'], ['CareTeam']` (represented as `dict` in JSON). """

        self.basedOn = None
        """ Fulfills care plan.
        List of `FHIRReference` items referencing `['CarePlan']` (represented as `dict` in JSON). """

        self.careTeam = None
        """ Who's involved in plan?.
        List of `FHIRReference` items referencing `['CareTeam']` (represented as `dict` in JSON). """

        self.category = None
        """ Type of plan.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.context = None
        """ Created in context of.
        Type `FHIRReference` referencing `['Encounter'], ['EpisodeOfCare']` (represented as `dict` in JSON). """

        self.definition = None
        """ Protocol or definition.
        List of `FHIRReference` items referencing `['PlanDefinition'], ['Questionnaire']` (represented as `dict` in JSON). """

        self.description = None
        """ Summary of nature of plan.
        Type `str`. """

        self.goal = None
        """ Desired outcome of plan.
        List of `FHIRReference` items referencing `['Goal']` (represented as `dict` in JSON). """

        self.identifier = None
        """ External Ids for this plan.
        List of `Identifier` items (represented as `dict` in JSON). """

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
        """ draft | active | suspended | completed | entered-in-error |
        cancelled | unknown.
        Type `str`. """

        self.subject = None
        """ Who care plan is for.
        Type `FHIRReference` referencing `['Patient'], ['Group']` (represented as `dict` in JSON). """

        self.supportingInfo = None
        """ Information considered as part of plan.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.title = None
        """ Human-friendly name for the CarePlan.
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
                    True,
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
                    "context",
                    "context",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "definition",
                    "definition",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
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
        Type `FHIRReference` referencing `['Appointment'], ['CommunicationRequest'], ['DeviceRequest'], ['MedicationRequest'], ['NutritionOrder'], ['Task'], ['ProcedureRequest'], ['ReferralRequest'], ['VisionPrescription'], ['RequestGroup']` (represented as `dict` in JSON). """

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

        self.category = None
        """ diet | drug | encounter | observation | procedure | supply | other.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.code = None
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.dailyAmount = None
        """ How to consume/day?.
        Type `Quantity` (represented as `dict` in JSON). """

        self.definition = None
        """ Protocol or definition.
        Type `FHIRReference` referencing `['PlanDefinition'], ['ActivityDefinition'], ['Questionnaire']` (represented as `dict` in JSON). """

        self.description = None
        """ Extra info describing activity to perform.
        Type `str`. """

        self.goal = None
        """ Goals this activity relates to.
        List of `FHIRReference` items referencing `['Goal']` (represented as `dict` in JSON). """

        self.location = None
        """ Where it should happen.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.performer = None
        """ Who will be responsible?.
        List of `FHIRReference` items referencing `['Practitioner'], ['Organization'], ['RelatedPerson'], ['Patient'], ['CareTeam']` (represented as `dict` in JSON). """

        self.productCodeableConcept = None
        """ What is to be administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.productReference = None
        """ What is to be administered/supplied.
        Type `FHIRReference` referencing `['Medication'], ['Substance']` (represented as `dict` in JSON). """

        self.prohibited = None
        """ Do NOT do.
        Type `bool`. """

        self.quantity = None
        """ How much to administer/supply/consume.
        Type `Quantity` (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Why activity should be done or why activity was prohibited.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Condition triggering need for activity.
        List of `FHIRReference` items referencing `['Condition']` (represented as `dict` in JSON). """

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
        cancelled | unknown.
        Type `str`. """

        self.statusReason = None
        """ Reason for current status.
        Type `str`. """

        super(CarePlanActivityDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CarePlanActivityDetail, self).elementProperties()
        js.extend(
            [
                (
                    "category",
                    "category",
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
                    "dailyAmount",
                    "dailyAmount",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "definition",
                    "definition",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
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
                ("prohibited", "prohibited", bool, "boolean", False, None, False),
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
                ("statusReason", "statusReason", str, "string", False, None, False),
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
