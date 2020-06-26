# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class DeviceRequest(domainresource.DomainResource):
    """ Medical device request.

    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """

    resource_type = "DeviceRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authoredOn = None
        """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.codeCodeableConcept = None
        """ Device requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.codeReference = None
        """ Device requested.
        Type `FHIRReference` referencing `['Device']` (represented as `dict` in JSON). """

        self.context = None
        """ Encounter or Episode motivating request.
        Type `FHIRReference` referencing `['Encounter'], ['EpisodeOfCare']` (represented as `dict` in JSON). """

        self.definition = None
        """ Protocol or definition.
        List of `FHIRReference` items referencing `['ActivityDefinition'], ['PlanDefinition']` (represented as `dict` in JSON). """

        self.groupIdentifier = None
        """ Identifier of composite request.
        Type `Identifier` (represented as `dict` in JSON). """

        self.identifier = None
        """ External Request identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.intent = None
        """ proposal | plan | original-order | encoded | reflex-order.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.note = None
        """ Notes or comments.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.occurrenceDateTime = None
        """ Desired time or schedule for use.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.occurrencePeriod = None
        """ Desired time or schedule for use.
        Type `Period` (represented as `dict` in JSON). """

        self.occurrenceTiming = None
        """ Desired time or schedule for use.
        Type `Timing` (represented as `dict` in JSON). """

        self.performer = None
        """ Requested Filler.
        Type `FHIRReference` referencing `['Practitioner'], ['Organization'], ['Patient'], ['Device'], ['RelatedPerson'], ['HealthcareService']` (represented as `dict` in JSON). """

        self.performerType = None
        """ Fille role.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.priorRequest = None
        """ What request replaces.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.priority = None
        """ Indicates how quickly the {{title}} should be addressed with
        respect to other requests.
        Type `str`. """

        self.reasonCode = None
        """ Coded Reason for request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Linked Reason for request.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.relevantHistory = None
        """ Request provenance.
        List of `FHIRReference` items referencing `['Provenance']` (represented as `dict` in JSON). """

        self.requester = None
        """ Who/what is requesting diagnostics.
        Type `DeviceRequestRequester` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | suspended | completed | entered-in-error |
        cancelled.
        Type `str`. """

        self.subject = None
        """ Focus of request.
        Type `FHIRReference` referencing `['Patient'], ['Group'], ['Location'], ['Device']` (represented as `dict` in JSON). """

        self.supportingInfo = None
        """ Additional clinical information.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        super(DeviceRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceRequest, self).elementProperties()
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
                    "codeCodeableConcept",
                    "codeCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "code",
                    True,
                ),
                (
                    "codeReference",
                    "codeReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "code",
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
                    "intent",
                    "intent",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
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
                (
                    "priorRequest",
                    "priorRequest",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
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
                    "requester",
                    "requester",
                    DeviceRequestRequester,
                    "DeviceRequestRequester",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, False),
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


class DeviceRequestRequester(backboneelement.BackboneElement):
    """ Who/what is requesting diagnostics.

    The individual who initiated the request and has responsibility for its
    activation.
    """

    resource_type = "DeviceRequestRequester"

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

        super(DeviceRequestRequester, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceRequestRequester, self).elementProperties()
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
