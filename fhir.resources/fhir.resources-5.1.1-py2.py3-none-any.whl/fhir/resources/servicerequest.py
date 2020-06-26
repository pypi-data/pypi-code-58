# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ServiceRequest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import domainresource


class ServiceRequest(domainresource.DomainResource):
    """ A request for a service to be performed.

    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """

    resource_type = "ServiceRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.asNeededBoolean = None
        """ Preconditions for service.
        Type `bool`. """

        self.asNeededCodeableConcept = None
        """ Preconditions for service.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.authoredOn = None
        """ Date request signed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items referencing `['CarePlan', 'ServiceRequest', 'MedicationRequest']` (represented as `dict` in JSON). """

        self.bodySite = None
        """ Location on Body.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.category = None
        """ Classification of service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.code = None
        """ What is being requested/ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.doNotPerform = None
        """ True if service/procedure should not be performed.
        Type `bool`. """

        self.encounter = None
        """ Encounter in which the request was created.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Identifiers assigned to this order.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items referencing `['ActivityDefinition', 'PlanDefinition']`. """

        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """

        self.insurance = None
        """ Associated insurance coverage.
        List of `FHIRReference` items referencing `['Coverage', 'ClaimResponse']` (represented as `dict` in JSON). """

        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `str`. """

        self.locationCode = None
        """ Requested location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.locationReference = None
        """ Requested location.
        List of `FHIRReference` items referencing `['Location']` (represented as `dict` in JSON). """

        self.note = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.occurrenceDateTime = None
        """ When service should occur.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.occurrencePeriod = None
        """ When service should occur.
        Type `Period` (represented as `dict` in JSON). """

        self.occurrenceTiming = None
        """ When service should occur.
        Type `Timing` (represented as `dict` in JSON). """

        self.orderDetail = None
        """ Additional order information.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.patientInstruction = None
        """ Patient or consumer-oriented instructions.
        Type `str`. """

        self.performer = None
        """ Requested performer.
        List of `FHIRReference` items referencing `['Practitioner', 'PractitionerRole', 'Organization', 'CareTeam', 'HealthcareService', 'Patient', 'Device', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.performerType = None
        """ Performer role.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.quantityQuantity = None
        """ Service amount.
        Type `Quantity` (represented as `dict` in JSON). """

        self.quantityRange = None
        """ Service amount.
        Type `Range` (represented as `dict` in JSON). """

        self.quantityRatio = None
        """ Service amount.
        Type `Ratio` (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Explanation/Justification for procedure or service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Explanation/Justification for service or service.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'DiagnosticReport', 'DocumentReference']` (represented as `dict` in JSON). """

        self.relevantHistory = None
        """ Request provenance.
        List of `FHIRReference` items referencing `['Provenance']` (represented as `dict` in JSON). """

        self.replaces = None
        """ What request replaces.
        List of `FHIRReference` items referencing `['ServiceRequest']` (represented as `dict` in JSON). """

        self.requester = None
        """ Who/what is requesting service.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization', 'Patient', 'RelatedPerson', 'Device']` (represented as `dict` in JSON). """

        self.requisition = None
        """ Composite Request ID.
        Type `Identifier` (represented as `dict` in JSON). """

        self.specimen = None
        """ Procedure Samples.
        List of `FHIRReference` items referencing `['Specimen']` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """

        self.subject = None
        """ Individual or Entity the service is ordered for.
        Type `FHIRReference` referencing `['Patient', 'Group', 'Location', 'Device']` (represented as `dict` in JSON). """

        self.supportingInfo = None
        """ Additional clinical information.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        super(ServiceRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ServiceRequest, self).elementProperties()
        js.extend(
            [
                (
                    "asNeededBoolean",
                    "asNeededBoolean",
                    bool,
                    "boolean",
                    False,
                    "asNeeded",
                    False,
                ),
                (
                    "asNeededCodeableConcept",
                    "asNeededCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "asNeeded",
                    False,
                ),
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
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("doNotPerform", "doNotPerform", bool, "boolean", False, None, False),
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
                    "locationCode",
                    "locationCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "locationReference",
                    "locationReference",
                    fhirreference.FHIRReference,
                    "Reference",
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
                    "occurrenceTiming",
                    "occurrenceTiming",
                    timing.Timing,
                    "Timing",
                    False,
                    "occurrence",
                    False,
                ),
                (
                    "orderDetail",
                    "orderDetail",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "patientInstruction",
                    "patientInstruction",
                    str,
                    "string",
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
                    "performerType",
                    "performerType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("priority", "priority", str, "code", False, None, False),
                (
                    "quantityQuantity",
                    "quantityQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "quantity",
                    False,
                ),
                (
                    "quantityRange",
                    "quantityRange",
                    range.Range,
                    "Range",
                    False,
                    "quantity",
                    False,
                ),
                (
                    "quantityRatio",
                    "quantityRatio",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    "quantity",
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
                    "relevantHistory",
                    "relevantHistory",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "replaces",
                    "replaces",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
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
                (
                    "requisition",
                    "requisition",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                (
                    "specimen",
                    "specimen",
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
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + ".ratio"]
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
