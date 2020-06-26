# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class MedicationRequest(domainresource.DomainResource):
    """ Ordering of medication for patient or group.

    An order or request for both supply of the medication and the instructions
    for administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or
    "MedicationOrder" to generalize the use across inpatient and outpatient
    settings, including care plans, etc., and to harmonize with workflow
    patterns.
    """

    resource_type = "MedicationRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authoredOn = None
        """ When request was initially authored.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items referencing `['CarePlan', 'MedicationRequest', 'ServiceRequest', 'ImmunizationRecommendation']` (represented as `dict` in JSON). """

        self.category = None
        """ Type of medication usage.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.courseOfTherapyType = None
        """ Overall pattern of medication administration.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.detectedIssue = None
        """ Clinical Issue with action.
        List of `FHIRReference` items referencing `['DetectedIssue']` (represented as `dict` in JSON). """

        self.dispenseRequest = None
        """ Medication supply authorization.
        Type `MedicationRequestDispenseRequest` (represented as `dict` in JSON). """

        self.doNotPerform = None
        """ True if request is prohibiting action.
        Type `bool`. """

        self.dosageInstruction = None
        """ How the medication should be taken.
        List of `Dosage` items (represented as `dict` in JSON). """

        self.encounter = None
        """ Encounter created as part of encounter/admission/stay.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.eventHistory = None
        """ A list of events of interest in the lifecycle.
        List of `FHIRReference` items referencing `['Provenance']` (represented as `dict` in JSON). """

        self.groupIdentifier = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """

        self.identifier = None
        """ External ids for this request.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """

        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """

        self.insurance = None
        """ Associated insurance coverage.
        List of `FHIRReference` items referencing `['Coverage', 'ClaimResponse']` (represented as `dict` in JSON). """

        self.intent = None
        """ proposal | plan | order | original-order | reflex-order | filler-
        order | instance-order | option.
        Type `str`. """

        self.medicationCodeableConcept = None
        """ Medication to be taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.medicationReference = None
        """ Medication to be taken.
        Type `FHIRReference` referencing `['Medication']` (represented as `dict` in JSON). """

        self.note = None
        """ Information about the prescription.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.performer = None
        """ Intended performer of administration.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization', 'Patient', 'Device', 'RelatedPerson', 'CareTeam']` (represented as `dict` in JSON). """

        self.performerType = None
        """ Desired kind of performer of the medication administration.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.priorPrescription = None
        """ An order/prescription that is being replaced.
        Type `FHIRReference` referencing `['MedicationRequest']` (represented as `dict` in JSON). """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.reasonCode = None
        """ Reason or indication for ordering or not ordering the medication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Condition or observation that supports why the prescription is
        being written.
        List of `FHIRReference` items referencing `['Condition', 'Observation']` (represented as `dict` in JSON). """

        self.recorder = None
        """ Person who entered the request.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.reportedBoolean = None
        """ Reported rather than primary record.
        Type `bool`. """

        self.reportedReference = None
        """ Reported rather than primary record.
        Type `FHIRReference` referencing `['Patient', 'Practitioner', 'PractitionerRole', 'RelatedPerson', 'Organization']` (represented as `dict` in JSON). """

        self.requester = None
        """ Who/What requested the Request.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization', 'Patient', 'RelatedPerson', 'Device']` (represented as `dict` in JSON). """

        self.status = None
        """ active | on-hold | cancelled | completed | entered-in-error |
        stopped | draft | unknown.
        Type `str`. """

        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subject = None
        """ Who or group medication request is for.
        Type `FHIRReference` referencing `['Patient', 'Group']` (represented as `dict` in JSON). """

        self.substitution = None
        """ Any restrictions on medication substitution.
        Type `MedicationRequestSubstitution` (represented as `dict` in JSON). """

        self.supportingInformation = None
        """ Information to support ordering of the medication.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        super(MedicationRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicationRequest, self).elementProperties()
        js.extend(
            [
                (
                    "authoredOn",
                    "authoredOn",
                    fhirdate.FHIRDate,
                    "dateTime",
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
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "courseOfTherapyType",
                    "courseOfTherapyType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "detectedIssue",
                    "detectedIssue",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "dispenseRequest",
                    "dispenseRequest",
                    MedicationRequestDispenseRequest,
                    "MedicationRequestDispenseRequest",
                    False,
                    None,
                    False,
                ),
                ("doNotPerform", "doNotPerform", bool, "boolean", False, None, False),
                (
                    "dosageInstruction",
                    "dosageInstruction",
                    dosage.Dosage,
                    "Dosage",
                    True,
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
                    "eventHistory",
                    "eventHistory",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "groupIdentifier",
                    "groupIdentifier",
                    identifier.Identifier,
                    "Identifier",
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
                    "instantiatesCanonical",
                    "instantiatesCanonical",
                    str,
                    "canonical",
                    True,
                    None,
                    False,
                ),
                ("instantiatesUri", "instantiatesUri", str, "uri", True, None, False),
                (
                    "insurance",
                    "insurance",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("intent", "intent", str, "code", False, None, True),
                (
                    "medicationCodeableConcept",
                    "medicationCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "medication",
                    True,
                ),
                (
                    "medicationReference",
                    "medicationReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "medication",
                    True,
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
                    "performer",
                    "performer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "performerType",
                    "performerType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "priorPrescription",
                    "priorPrescription",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("priority", "priority", str, "code", False, None, False),
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
                    "recorder",
                    "recorder",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "reportedBoolean",
                    "reportedBoolean",
                    bool,
                    "boolean",
                    False,
                    "reported",
                    False,
                ),
                (
                    "reportedReference",
                    "reportedReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "reported",
                    False,
                ),
                (
                    "requester",
                    "requester",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
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
                    "substitution",
                    "substitution",
                    MedicationRequestSubstitution,
                    "MedicationRequestSubstitution",
                    False,
                    None,
                    False,
                ),
                (
                    "supportingInformation",
                    "supportingInformation",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class MedicationRequestDispenseRequest(backboneelement.BackboneElement):
    """ Medication supply authorization.

    Indicates the specific details for the dispense or medication supply part
    of a medication request (also known as a Medication Prescription or
    Medication Order).  Note that this information is not always sent with the
    order.  There may be in some settings (e.g. hospitals) institutional or
    system support for completing the dispense details in the pharmacy
    department.
    """

    resource_type = "MedicationRequestDispenseRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.dispenseInterval = None
        """ Minimum period of time between dispenses.
        Type `Duration` (represented as `dict` in JSON). """

        self.expectedSupplyDuration = None
        """ Number of days supply per dispense.
        Type `Duration` (represented as `dict` in JSON). """

        self.initialFill = None
        """ First fill details.
        Type `MedicationRequestDispenseRequestInitialFill` (represented as `dict` in JSON). """

        self.numberOfRepeatsAllowed = None
        """ Number of refills authorized.
        Type `int`. """

        self.performer = None
        """ Intended dispenser.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.quantity = None
        """ Amount of medication to supply per dispense.
        Type `Quantity` (represented as `dict` in JSON). """

        self.validityPeriod = None
        """ Time period supply is authorized for.
        Type `Period` (represented as `dict` in JSON). """

        super(MedicationRequestDispenseRequest, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicationRequestDispenseRequest, self).elementProperties()
        js.extend(
            [
                (
                    "dispenseInterval",
                    "dispenseInterval",
                    duration.Duration,
                    "Duration",
                    False,
                    None,
                    False,
                ),
                (
                    "expectedSupplyDuration",
                    "expectedSupplyDuration",
                    duration.Duration,
                    "Duration",
                    False,
                    None,
                    False,
                ),
                (
                    "initialFill",
                    "initialFill",
                    MedicationRequestDispenseRequestInitialFill,
                    "MedicationRequestDispenseRequestInitialFill",
                    False,
                    None,
                    False,
                ),
                (
                    "numberOfRepeatsAllowed",
                    "numberOfRepeatsAllowed",
                    int,
                    "unsignedInt",
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
                    "quantity",
                    "quantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "validityPeriod",
                    "validityPeriod",
                    period.Period,
                    "Period",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class MedicationRequestDispenseRequestInitialFill(backboneelement.BackboneElement):
    """ First fill details.

    Indicates the quantity or duration for the first dispense of the
    medication.
    """

    resource_type = "MedicationRequestDispenseRequestInitialFill"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.duration = None
        """ First fill duration.
        Type `Duration` (represented as `dict` in JSON). """

        self.quantity = None
        """ First fill quantity.
        Type `Quantity` (represented as `dict` in JSON). """

        super(MedicationRequestDispenseRequestInitialFill, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(
            MedicationRequestDispenseRequestInitialFill, self
        ).elementProperties()
        js.extend(
            [
                (
                    "duration",
                    "duration",
                    duration.Duration,
                    "Duration",
                    False,
                    None,
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
            ]
        )
        return js


class MedicationRequestSubstitution(backboneelement.BackboneElement):
    """ Any restrictions on medication substitution.

    Indicates whether or not substitution can or should be part of the
    dispense. In some cases, substitution must happen, in other cases
    substitution must not happen. This block explains the prescriber's intent.
    If nothing is specified substitution may be done.
    """

    resource_type = "MedicationRequestSubstitution"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.allowedBoolean = None
        """ Whether substitution is allowed or not.
        Type `bool`. """

        self.allowedCodeableConcept = None
        """ Whether substitution is allowed or not.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.reason = None
        """ Why should (not) substitution be made.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MedicationRequestSubstitution, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicationRequestSubstitution, self).elementProperties()
        js.extend(
            [
                (
                    "allowedBoolean",
                    "allowedBoolean",
                    bool,
                    "boolean",
                    False,
                    "allowed",
                    True,
                ),
                (
                    "allowedCodeableConcept",
                    "allowedCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "allowed",
                    True,
                ),
                (
                    "reason",
                    "reason",
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
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + ".dosage"]
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
