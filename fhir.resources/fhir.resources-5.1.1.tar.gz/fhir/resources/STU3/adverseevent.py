# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class AdverseEvent(domainresource.DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.

    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """

    resource_type = "AdverseEvent"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.category = None
        """ AE | PAE
        An adverse event is an event that caused harm to a patient,  an
        adverse reaction is a something that is a subject-specific event
        that is a result of an exposure to a medication, food, device or
        environmental substance, a potential adverse event is something
        that occurred and that could have caused harm to a patient but did
        not.
        Type `str`. """

        self.date = None
        """ When the event occurred.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Description of the adverse event.
        Type `str`. """

        self.eventParticipant = None
        """ Who  was involved in the adverse event or the potential adverse
        event.
        Type `FHIRReference` referencing `['Practitioner'], ['Device']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier for the event.
        Type `Identifier` (represented as `dict` in JSON). """

        self.location = None
        """ Location where adverse event occurred.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.outcome = None
        """ resolved | recovering | ongoing | resolvedWithSequelae | fatal |
        unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.reaction = None
        """ Adverse Reaction Events linked to exposure to substance.
        List of `FHIRReference` items referencing `['Condition']` (represented as `dict` in JSON). """

        self.recorder = None
        """ Who recorded the adverse event.
        Type `FHIRReference` referencing `['Patient'], ['Practitioner'], ['RelatedPerson']` (represented as `dict` in JSON). """

        self.referenceDocument = None
        """ AdverseEvent.referenceDocument.
        List of `FHIRReference` items referencing `['DocumentReference']` (represented as `dict` in JSON). """

        self.seriousness = None
        """ Mild | Moderate | Severe.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.study = None
        """ AdverseEvent.study.
        List of `FHIRReference` items referencing `['ResearchStudy']` (represented as `dict` in JSON). """

        self.subject = None
        """ Subject or group impacted by event.
        Type `FHIRReference` referencing `['Patient'], ['ResearchSubject'], ['Medication'], ['Device']` (represented as `dict` in JSON). """

        self.subjectMedicalHistory = None
        """ AdverseEvent.subjectMedicalHistory.
        List of `FHIRReference` items referencing `['Condition'], ['Observation'], ['AllergyIntolerance'], ['FamilyMemberHistory'], ['Immunization'], ['Procedure']` (represented as `dict` in JSON). """

        self.suspectEntity = None
        """ The suspected agent causing the adverse event.
        List of `AdverseEventSuspectEntity` items (represented as `dict` in JSON). """

        self.type = None
        """ actual | potential.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(AdverseEvent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AdverseEvent, self).elementProperties()
        js.extend(
            [
                ("category", "category", str, "code", False, None, False),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                ("description", "description", str, "string", False, None, False),
                (
                    "eventParticipant",
                    "eventParticipant",
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
                    "location",
                    "location",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
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
                    "reaction",
                    "reaction",
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
                    "referenceDocument",
                    "referenceDocument",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "seriousness",
                    "seriousness",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "study",
                    "study",
                    fhirreference.FHIRReference,
                    "Reference",
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
                    False,
                ),
                (
                    "subjectMedicalHistory",
                    "subjectMedicalHistory",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "suspectEntity",
                    "suspectEntity",
                    AdverseEventSuspectEntity,
                    "AdverseEventSuspectEntity",
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


class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """ The suspected agent causing the adverse event.

    Describes the entity that is suspected to have caused the adverse event.
    """

    resource_type = "AdverseEventSuspectEntity"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.causality = None
        """ causality1 | causality2.
        Type `str`. """

        self.causalityAssessment = None
        """ assess1 | assess2.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.causalityAuthor = None
        """ AdverseEvent.suspectEntity.causalityAuthor.
        Type `FHIRReference` referencing `['Practitioner'], ['PractitionerRole']` (represented as `dict` in JSON). """

        self.causalityMethod = None
        """ method1 | method2.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.causalityProductRelatedness = None
        """ AdverseEvent.suspectEntity.causalityProductRelatedness.
        Type `str`. """

        self.causalityResult = None
        """ result1 | result2.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.instance = None
        """ Refers to the specific entity that caused the adverse event.
        Type `FHIRReference` referencing `['Substance'], ['Medication'], ['MedicationAdministration'], ['MedicationStatement'], ['Device']` (represented as `dict` in JSON). """

        super(AdverseEventSuspectEntity, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(AdverseEventSuspectEntity, self).elementProperties()
        js.extend(
            [
                ("causality", "causality", str, "code", False, None, False),
                (
                    "causalityAssessment",
                    "causalityAssessment",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "causalityAuthor",
                    "causalityAuthor",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "causalityMethod",
                    "causalityMethod",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "causalityProductRelatedness",
                    "causalityProductRelatedness",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "causalityResult",
                    "causalityResult",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "instance",
                    "instance",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
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
