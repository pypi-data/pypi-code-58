# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationAdministration
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class MedicationAdministration(domainresource.DomainResource):
    """ Administration of medication to a patient.

    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """

    resource_type = "MedicationAdministration"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.category = None
        """ Type of medication usage.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.context = None
        """ Encounter or Episode of Care administered as part of.
        Type `FHIRReference` referencing `['Encounter', 'EpisodeOfCare']` (represented as `dict` in JSON). """

        self.device = None
        """ Device used to administer.
        List of `FHIRReference` items referencing `['Device']` (represented as `dict` in JSON). """

        self.dosage = None
        """ Details of how medication was taken.
        Type `MedicationAdministrationDosage` (represented as `dict` in JSON). """

        self.effectiveDateTime = None
        """ Start and end time of administration.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.effectivePeriod = None
        """ Start and end time of administration.
        Type `Period` (represented as `dict` in JSON). """

        self.eventHistory = None
        """ A list of events of interest in the lifecycle.
        List of `FHIRReference` items referencing `['Provenance']` (represented as `dict` in JSON). """

        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.instantiates = None
        """ Instantiates protocol or definition.
        List of `str` items. """

        self.medicationCodeableConcept = None
        """ What was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.medicationReference = None
        """ What was administered.
        Type `FHIRReference` referencing `['Medication']` (represented as `dict` in JSON). """

        self.note = None
        """ Information about the administration.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items referencing `['MedicationAdministration', 'Procedure']` (represented as `dict` in JSON). """

        self.performer = None
        """ Who performed the medication administration and what they did.
        List of `MedicationAdministrationPerformer` items (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Reason administration performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Condition or observation that supports why the medication was
        administered.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'DiagnosticReport']` (represented as `dict` in JSON). """

        self.request = None
        """ Request administration performed against.
        Type `FHIRReference` referencing `['MedicationRequest']` (represented as `dict` in JSON). """

        self.status = None
        """ in-progress | not-done | on-hold | completed | entered-in-error |
        stopped | unknown.
        Type `str`. """

        self.statusReason = None
        """ Reason administration not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.subject = None
        """ Who received medication.
        Type `FHIRReference` referencing `['Patient', 'Group']` (represented as `dict` in JSON). """

        self.supportingInformation = None
        """ Additional information to support administration.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        super(MedicationAdministration, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicationAdministration, self).elementProperties()
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
                    "context",
                    "context",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "device",
                    "device",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "dosage",
                    "dosage",
                    MedicationAdministrationDosage,
                    "MedicationAdministrationDosage",
                    False,
                    None,
                    False,
                ),
                (
                    "effectiveDateTime",
                    "effectiveDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "effective",
                    True,
                ),
                (
                    "effectivePeriod",
                    "effectivePeriod",
                    period.Period,
                    "Period",
                    False,
                    "effective",
                    True,
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
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                ("instantiates", "instantiates", str, "uri", True, None, False),
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
                    "partOf",
                    "partOf",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "performer",
                    "performer",
                    MedicationAdministrationPerformer,
                    "MedicationAdministrationPerformer",
                    True,
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
                    "request",
                    "request",
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
                    True,
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


class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.

    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """

    resource_type = "MedicationAdministrationDosage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.dose = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """

        self.method = None
        """ How drug was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.rateQuantity = None
        """ Dose quantity per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """

        self.rateRatio = None
        """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """

        self.route = None
        """ Path of substance into body.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.site = None
        """ Body site administered to.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.text = None
        """ Free text dosage instructions e.g. SIG.
        Type `str`. """

        super(MedicationAdministrationDosage, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicationAdministrationDosage, self).elementProperties()
        js.extend(
            [
                ("dose", "dose", quantity.Quantity, "Quantity", False, None, False),
                (
                    "method",
                    "method",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "rateQuantity",
                    "rateQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "rate",
                    False,
                ),
                ("rateRatio", "rateRatio", ratio.Ratio, "Ratio", False, "rate", False),
                (
                    "route",
                    "route",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "site",
                    "site",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("text", "text", str, "string", False, None, False),
            ]
        )
        return js


class MedicationAdministrationPerformer(backboneelement.BackboneElement):
    """ Who performed the medication administration and what they did.

    Indicates who or what performed the medication administration and how they
    were involved.
    """

    resource_type = "MedicationAdministrationPerformer"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.actor = None
        """ Who performed the medication administration.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Patient', 'RelatedPerson', 'Device']` (represented as `dict` in JSON). """

        self.function = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MedicationAdministrationPerformer, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicationAdministrationPerformer, self).elementProperties()
        js.extend(
            [
                (
                    "actor",
                    "actor",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "function",
                    "function",
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
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + ".ratio"]
