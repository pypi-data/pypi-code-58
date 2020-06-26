# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcedureRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class ProcedureRequest(domainresource.DomainResource):
    """ A request for a procedure or diagnostic to be performed.

    A record of a request for diagnostic investigations, treatments, or
    operations to be performed.
    """

    resource_type = "ProcedureRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.asNeededBoolean = None
        """ Preconditions for procedure or diagnostic.
        Type `bool`. """

        self.asNeededCodeableConcept = None
        """ Preconditions for procedure or diagnostic.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.authoredOn = None
        """ Date request signed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.bodySite = None
        """ Location on Body.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.category = None
        """ Classification of procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.code = None
        """ What is being requested/ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.context = None
        """ Encounter or Episode during which request was created.
        Type `FHIRReference` referencing `['Encounter'], ['EpisodeOfCare']` (represented as `dict` in JSON). """

        self.definition = None
        """ Protocol or definition.
        List of `FHIRReference` items referencing `['ActivityDefinition'], ['PlanDefinition']` (represented as `dict` in JSON). """

        self.doNotPerform = None
        """ True if procedure should not be performed.
        Type `bool`. """

        self.identifier = None
        """ Identifiers assigned to this order.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.intent = None
        """ proposal | plan | order +.
        Type `str`. """

        self.note = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.occurrenceDateTime = None
        """ When procedure should occur.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.occurrencePeriod = None
        """ When procedure should occur.
        Type `Period` (represented as `dict` in JSON). """

        self.occurrenceTiming = None
        """ When procedure should occur.
        Type `Timing` (represented as `dict` in JSON). """

        self.performer = None
        """ Requested perfomer.
        Type `FHIRReference` referencing `['Practitioner'], ['Organization'], ['Patient'], ['Device'], ['RelatedPerson'], ['HealthcareService']` (represented as `dict` in JSON). """

        self.performerType = None
        """ Performer role.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.reasonCode = None
        """ Explanation/Justification for test.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Explanation/Justification for test.
        List of `FHIRReference` items referencing `['Condition'], ['Observation']` (represented as `dict` in JSON). """

        self.relevantHistory = None
        """ Request provenance.
        List of `FHIRReference` items referencing `['Provenance']` (represented as `dict` in JSON). """

        self.replaces = None
        """ What request replaces.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.requester = None
        """ Who/what is requesting procedure or diagnostic.
        Type `ProcedureRequestRequester` (represented as `dict` in JSON). """

        self.requisition = None
        """ Composite Request ID.
        Type `Identifier` (represented as `dict` in JSON). """

        self.specimen = None
        """ Procedure Samples.
        List of `FHIRReference` items referencing `['Specimen']` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | suspended | completed | entered-in-error |
        cancelled.
        Type `str`. """

        self.subject = None
        """ Individual the service is ordered for.
        Type `FHIRReference` referencing `['Patient'], ['Group'], ['Location'], ['Device']` (represented as `dict` in JSON). """

        self.supportingInfo = None
        """ Additional clinical information.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        super(ProcedureRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProcedureRequest, self).elementProperties()
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
                    True,
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
                ("doNotPerform", "doNotPerform", bool, "boolean", False, None, False),
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
                    ProcedureRequestRequester,
                    "ProcedureRequestRequester",
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


class ProcedureRequestRequester(backboneelement.BackboneElement):
    """ Who/what is requesting procedure or diagnostic.

    The individual who initiated the request and has responsibility for its
    activation.
    """

    resource_type = "ProcedureRequestRequester"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.agent = None
        """ Individual making the request.
        Type `FHIRReference` referencing `['Device'], ['Practitioner'], ['Organization']` (represented as `dict` in JSON). """

        self.onBehalfOf = None
        """ Organization agent is acting for.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        super(ProcedureRequestRequester, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ProcedureRequestRequester, self).elementProperties()
        js.extend(
            [
                (
                    "agent",
                    "agent",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
