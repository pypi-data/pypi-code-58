# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Goal
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Goal(domainresource.DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization.

    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """

    resource_type = "Goal"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.achievementStatus = None
        """ in-progress | improving | worsening | no-change | achieved |
        sustaining | not-achieved | no-progress | not-attainable.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.addresses = None
        """ Issues addressed by this goal.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'MedicationStatement', 'NutritionOrder', 'ServiceRequest', 'RiskAssessment']` (represented as `dict` in JSON). """

        self.category = None
        """ E.g. Treatment, dietary, behavioral, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.description = None
        """ Code or text describing goal.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.expressedBy = None
        """ Who's responsible for creating Goal?.
        Type `FHIRReference` referencing `['Patient', 'Practitioner', 'PractitionerRole', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.identifier = None
        """ External Ids for this goal.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.lifecycleStatus = None
        """ proposed | planned | accepted | active | on-hold | completed |
        cancelled | entered-in-error | rejected.
        Type `str`. """

        self.note = None
        """ Comments about the goal.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.outcomeCode = None
        """ What result was achieved regarding the goal?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.outcomeReference = None
        """ Observation that resulted from goal.
        List of `FHIRReference` items referencing `['Observation']` (represented as `dict` in JSON). """

        self.priority = None
        """ high-priority | medium-priority | low-priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.startCodeableConcept = None
        """ When goal pursuit begins.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.startDate = None
        """ When goal pursuit begins.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.statusDate = None
        """ When goal status took effect.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.statusReason = None
        """ Reason for current status.
        Type `str`. """

        self.subject = None
        """ Who this goal is intended for.
        Type `FHIRReference` referencing `['Patient', 'Group', 'Organization']` (represented as `dict` in JSON). """

        self.target = None
        """ Target outcome for the goal.
        List of `GoalTarget` items (represented as `dict` in JSON). """

        super(Goal, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Goal, self).elementProperties()
        js.extend(
            [
                (
                    "achievementStatus",
                    "achievementStatus",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
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
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "description",
                    "description",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "expressedBy",
                    "expressedBy",
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
                ("lifecycleStatus", "lifecycleStatus", str, "code", False, None, True),
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
                    "outcomeCode",
                    "outcomeCode",
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
                    "priority",
                    "priority",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "startCodeableConcept",
                    "startCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "start",
                    False,
                ),
                (
                    "startDate",
                    "startDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    "start",
                    False,
                ),
                (
                    "statusDate",
                    "statusDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    None,
                    False,
                ),
                ("statusReason", "statusReason", str, "string", False, None, False),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("target", "target", GoalTarget, "GoalTarget", True, None, False),
            ]
        )
        return js


class GoalTarget(backboneelement.BackboneElement):
    """ Target outcome for the goal.

    Indicates what should be done by when.
    """

    resource_type = "GoalTarget"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.detailBoolean = None
        """ The target value to be achieved.
        Type `bool`. """

        self.detailCodeableConcept = None
        """ The target value to be achieved.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.detailInteger = None
        """ The target value to be achieved.
        Type `int`. """

        self.detailQuantity = None
        """ The target value to be achieved.
        Type `Quantity` (represented as `dict` in JSON). """

        self.detailRange = None
        """ The target value to be achieved.
        Type `Range` (represented as `dict` in JSON). """

        self.detailRatio = None
        """ The target value to be achieved.
        Type `Ratio` (represented as `dict` in JSON). """

        self.detailString = None
        """ The target value to be achieved.
        Type `str`. """

        self.dueDate = None
        """ Reach goal on or before.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.dueDuration = None
        """ Reach goal on or before.
        Type `Duration` (represented as `dict` in JSON). """

        self.measure = None
        """ The parameter whose value is being tracked.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(GoalTarget, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GoalTarget, self).elementProperties()
        js.extend(
            [
                (
                    "detailBoolean",
                    "detailBoolean",
                    bool,
                    "boolean",
                    False,
                    "detail",
                    False,
                ),
                (
                    "detailCodeableConcept",
                    "detailCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "detail",
                    False,
                ),
                (
                    "detailInteger",
                    "detailInteger",
                    int,
                    "integer",
                    False,
                    "detail",
                    False,
                ),
                (
                    "detailQuantity",
                    "detailQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "detail",
                    False,
                ),
                (
                    "detailRange",
                    "detailRange",
                    range.Range,
                    "Range",
                    False,
                    "detail",
                    False,
                ),
                (
                    "detailRatio",
                    "detailRatio",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    "detail",
                    False,
                ),
                ("detailString", "detailString", str, "string", False, "detail", False),
                ("dueDate", "dueDate", fhirdate.FHIRDate, "date", False, "due", False),
                (
                    "dueDuration",
                    "dueDuration",
                    duration.Duration,
                    "Duration",
                    False,
                    "due",
                    False,
                ),
                (
                    "measure",
                    "measure",
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
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + ".duration"]
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + ".ratio"]
