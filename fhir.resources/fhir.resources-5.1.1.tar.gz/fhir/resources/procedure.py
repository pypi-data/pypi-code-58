# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Procedure
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.

    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """

    resource_type = "Procedure"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.asserter = None
        """ Person who asserts this procedure.
        Type `FHIRReference` referencing `['Patient', 'RelatedPerson', 'Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.basedOn = None
        """ A request for this procedure.
        List of `FHIRReference` items referencing `['CarePlan', 'ServiceRequest']` (represented as `dict` in JSON). """

        self.bodySite = None
        """ Target body sites.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.category = None
        """ Classification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.code = None
        """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.complication = None
        """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.complicationDetail = None
        """ A condition that is a result of the procedure.
        List of `FHIRReference` items referencing `['Condition']` (represented as `dict` in JSON). """

        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.focalDevice = None
        """ Manipulated, implanted, or removed device.
        List of `ProcedureFocalDevice` items (represented as `dict` in JSON). """

        self.followUp = None
        """ Instructions for follow up.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.identifier = None
        """ External Identifiers for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items referencing `['PlanDefinition', 'ActivityDefinition', 'Measure', 'OperationDefinition', 'Questionnaire']`. """

        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """

        self.location = None
        """ Where the procedure happened.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.note = None
        """ Additional information about the procedure.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.outcome = None
        """ The result of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items referencing `['Procedure', 'Observation', 'MedicationAdministration']` (represented as `dict` in JSON). """

        self.performedAge = None
        """ When the procedure was performed.
        Type `Age` (represented as `dict` in JSON). """

        self.performedDateTime = None
        """ When the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.performedPeriod = None
        """ When the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """

        self.performedRange = None
        """ When the procedure was performed.
        Type `Range` (represented as `dict` in JSON). """

        self.performedString = None
        """ When the procedure was performed.
        Type `str`. """

        self.performer = None
        """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Coded reason procedure performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ The justification that the procedure was performed.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'Procedure', 'DiagnosticReport', 'DocumentReference']` (represented as `dict` in JSON). """

        self.recorder = None
        """ Who recorded the procedure.
        Type `FHIRReference` referencing `['Patient', 'RelatedPerson', 'Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.report = None
        """ Any report resulting from the procedure.
        List of `FHIRReference` items referencing `['DiagnosticReport', 'DocumentReference', 'Composition']` (represented as `dict` in JSON). """

        self.status = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `str`. """

        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subject = None
        """ Who the procedure was performed on.
        Type `FHIRReference` referencing `['Patient', 'Group']` (represented as `dict` in JSON). """

        self.usedCode = None
        """ Coded items used during the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.usedReference = None
        """ Items used during procedure.
        List of `FHIRReference` items referencing `['Device', 'Medication', 'Substance']` (represented as `dict` in JSON). """

        super(Procedure, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Procedure, self).elementProperties()
        js.extend(
            [
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
                    "basedOn",
                    "basedOn",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
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
                    "complication",
                    "complication",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "complicationDetail",
                    "complicationDetail",
                    fhirreference.FHIRReference,
                    "Reference",
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
                    "focalDevice",
                    "focalDevice",
                    ProcedureFocalDevice,
                    "ProcedureFocalDevice",
                    True,
                    None,
                    False,
                ),
                (
                    "followUp",
                    "followUp",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
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
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
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
                    "performedAge",
                    "performedAge",
                    age.Age,
                    "Age",
                    False,
                    "performed",
                    False,
                ),
                (
                    "performedDateTime",
                    "performedDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "performed",
                    False,
                ),
                (
                    "performedPeriod",
                    "performedPeriod",
                    period.Period,
                    "Period",
                    False,
                    "performed",
                    False,
                ),
                (
                    "performedRange",
                    "performedRange",
                    range.Range,
                    "Range",
                    False,
                    "performed",
                    False,
                ),
                (
                    "performedString",
                    "performedString",
                    str,
                    "string",
                    False,
                    "performed",
                    False,
                ),
                (
                    "performer",
                    "performer",
                    ProcedurePerformer,
                    "ProcedurePerformer",
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
                    "recorder",
                    "recorder",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "report",
                    "report",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
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
                    "usedCode",
                    "usedCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "usedReference",
                    "usedReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ Manipulated, implanted, or removed device.

    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """

    resource_type = "ProcedureFocalDevice"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ Kind of change to device.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.manipulated = None
        """ Device that was changed.
        Type `FHIRReference` referencing `['Device']` (represented as `dict` in JSON). """

        super(ProcedureFocalDevice, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProcedureFocalDevice, self).elementProperties()
        js.extend(
            [
                (
                    "action",
                    "action",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "manipulated",
                    "manipulated",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class ProcedurePerformer(backboneelement.BackboneElement):
    """ The people who performed the procedure.

    Limited to "real" people rather than equipment.
    """

    resource_type = "ProcedurePerformer"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.actor = None
        """ The reference to the practitioner.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization', 'Patient', 'RelatedPerson', 'Device']` (represented as `dict` in JSON). """

        self.function = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.onBehalfOf = None
        """ Organization the device or practitioner was acting for.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        super(ProcedurePerformer, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProcedurePerformer, self).elementProperties()
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
                (
                    "onBehalfOf",
                    "onBehalfOf",
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
