# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Immunization
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Immunization(domainresource.DomainResource):
    """ Immunization event information.

    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """

    resource_type = "Immunization"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.doseQuantity = None
        """ Amount of vaccine administered.
        Type `Quantity` (represented as `dict` in JSON). """

        self.education = None
        """ Educational material presented to patient.
        List of `ImmunizationEducation` items (represented as `dict` in JSON). """

        self.encounter = None
        """ Encounter immunization was part of.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.expirationDate = None
        """ Vaccine expiration date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.fundingSource = None
        """ Funding source for the vaccine.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.isSubpotent = None
        """ Dose potency.
        Type `bool`. """

        self.location = None
        """ Where immunization occurred.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.lotNumber = None
        """ Vaccine lot number.
        Type `str`. """

        self.manufacturer = None
        """ Vaccine manufacturer.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.note = None
        """ Additional immunization notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.occurrenceDateTime = None
        """ Vaccine administration date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.occurrenceString = None
        """ Vaccine administration date.
        Type `str`. """

        self.patient = None
        """ Who was immunized.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.performer = None
        """ Who performed event.
        List of `ImmunizationPerformer` items (represented as `dict` in JSON). """

        self.primarySource = None
        """ Indicates context the data was recorded in.
        Type `bool`. """

        self.programEligibility = None
        """ Patient eligibility for a vaccination program.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.protocolApplied = None
        """ Protocol followed by the provider.
        List of `ImmunizationProtocolApplied` items (represented as `dict` in JSON). """

        self.reaction = None
        """ Details of a reaction that follows immunization.
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Why immunization occurred.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why immunization occurred.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'DiagnosticReport']` (represented as `dict` in JSON). """

        self.recorded = None
        """ When the immunization was first captured in the subject's record.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.reportOrigin = None
        """ Indicates the source of a secondarily reported record.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.route = None
        """ How vaccine entered body.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.site = None
        """ Body site vaccine  was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.status = None
        """ completed | entered-in-error | not-done.
        Type `str`. """

        self.statusReason = None
        """ Reason not done.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subpotentReason = None
        """ Reason for being subpotent.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.vaccineCode = None
        """ Vaccine product administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(Immunization, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Immunization, self).elementProperties()
        js.extend(
            [
                (
                    "doseQuantity",
                    "doseQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "education",
                    "education",
                    ImmunizationEducation,
                    "ImmunizationEducation",
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
                    "expirationDate",
                    "expirationDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    None,
                    False,
                ),
                (
                    "fundingSource",
                    "fundingSource",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
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
                ("isSubpotent", "isSubpotent", bool, "boolean", False, None, False),
                (
                    "location",
                    "location",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("lotNumber", "lotNumber", str, "string", False, None, False),
                (
                    "manufacturer",
                    "manufacturer",
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
                    "occurrenceDateTime",
                    "occurrenceDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "occurrence",
                    True,
                ),
                (
                    "occurrenceString",
                    "occurrenceString",
                    str,
                    "string",
                    False,
                    "occurrence",
                    True,
                ),
                (
                    "patient",
                    "patient",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "performer",
                    "performer",
                    ImmunizationPerformer,
                    "ImmunizationPerformer",
                    True,
                    None,
                    False,
                ),
                ("primarySource", "primarySource", bool, "boolean", False, None, False),
                (
                    "programEligibility",
                    "programEligibility",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "protocolApplied",
                    "protocolApplied",
                    ImmunizationProtocolApplied,
                    "ImmunizationProtocolApplied",
                    True,
                    None,
                    False,
                ),
                (
                    "reaction",
                    "reaction",
                    ImmunizationReaction,
                    "ImmunizationReaction",
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
                    "recorded",
                    "recorded",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "reportOrigin",
                    "reportOrigin",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
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
                    "subpotentReason",
                    "subpotentReason",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "vaccineCode",
                    "vaccineCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class ImmunizationEducation(backboneelement.BackboneElement):
    """ Educational material presented to patient.

    Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
    """

    resource_type = "ImmunizationEducation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.documentType = None
        """ Educational material document identifier.
        Type `str`. """

        self.presentationDate = None
        """ Educational material presentation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.publicationDate = None
        """ Educational material publication date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.reference = None
        """ Educational material reference pointer.
        Type `str`. """

        super(ImmunizationEducation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationEducation, self).elementProperties()
        js.extend(
            [
                ("documentType", "documentType", str, "string", False, None, False),
                (
                    "presentationDate",
                    "presentationDate",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "publicationDate",
                    "publicationDate",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                ("reference", "reference", str, "uri", False, None, False),
            ]
        )
        return js


class ImmunizationPerformer(backboneelement.BackboneElement):
    """ Who performed event.

    Indicates who performed the immunization event.
    """

    resource_type = "ImmunizationPerformer"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.actor = None
        """ Individual or organization who was performing.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.function = None
        """ What type of performance was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ImmunizationPerformer, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationPerformer, self).elementProperties()
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


class ImmunizationProtocolApplied(backboneelement.BackboneElement):
    """ Protocol followed by the provider.

    The protocol (set of recommendations) being followed by the provider who
    administered the dose.
    """

    resource_type = "ImmunizationProtocolApplied"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authority = None
        """ Who is responsible for publishing the recommendations.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.doseNumberPositiveInt = None
        """ Dose number within series.
        Type `int`. """

        self.doseNumberString = None
        """ Dose number within series.
        Type `str`. """

        self.series = None
        """ Name of vaccine series.
        Type `str`. """

        self.seriesDosesPositiveInt = None
        """ Recommended number of doses for immunity.
        Type `int`. """

        self.seriesDosesString = None
        """ Recommended number of doses for immunity.
        Type `str`. """

        self.targetDisease = None
        """ Vaccine preventatable disease being targetted.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(ImmunizationProtocolApplied, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImmunizationProtocolApplied, self).elementProperties()
        js.extend(
            [
                (
                    "authority",
                    "authority",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "doseNumberPositiveInt",
                    "doseNumberPositiveInt",
                    int,
                    "positiveInt",
                    False,
                    "doseNumber",
                    True,
                ),
                (
                    "doseNumberString",
                    "doseNumberString",
                    str,
                    "string",
                    False,
                    "doseNumber",
                    True,
                ),
                ("series", "series", str, "string", False, None, False),
                (
                    "seriesDosesPositiveInt",
                    "seriesDosesPositiveInt",
                    int,
                    "positiveInt",
                    False,
                    "seriesDoses",
                    False,
                ),
                (
                    "seriesDosesString",
                    "seriesDosesString",
                    str,
                    "string",
                    False,
                    "seriesDoses",
                    False,
                ),
                (
                    "targetDisease",
                    "targetDisease",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class ImmunizationReaction(backboneelement.BackboneElement):
    """ Details of a reaction that follows immunization.

    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """

    resource_type = "ImmunizationReaction"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.date = None
        """ When reaction started.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.detail = None
        """ Additional information on reaction.
        Type `FHIRReference` referencing `['Observation']` (represented as `dict` in JSON). """

        self.reported = None
        """ Indicates self-reported reaction.
        Type `bool`. """

        super(ImmunizationReaction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationReaction, self).elementProperties()
        js.extend(
            [
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                (
                    "detail",
                    "detail",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("reported", "reported", bool, "boolean", False, None, False),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
