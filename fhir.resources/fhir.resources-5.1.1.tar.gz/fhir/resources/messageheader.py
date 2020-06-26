# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageHeader
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class MessageHeader(domainresource.DomainResource):
    """ A resource that describes a message that is exchanged between systems.

    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """

    resource_type = "MessageHeader"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.author = None
        """ The source of the decision.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.definition = None
        """ Link to the definition for this message.
        Type `str` referencing `['MessageDefinition']`. """

        self.destination = None
        """ Message destination application(s).
        List of `MessageHeaderDestination` items (represented as `dict` in JSON). """

        self.enterer = None
        """ The source of the data entry.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.eventCoding = None
        """ Code for the event this message represents or link to event
        definition.
        Type `Coding` (represented as `dict` in JSON). """

        self.eventUri = None
        """ Code for the event this message represents or link to event
        definition.
        Type `str`. """

        self.focus = None
        """ The actual content of the message.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.reason = None
        """ Cause of event.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.response = None
        """ If this is a reply to prior message.
        Type `MessageHeaderResponse` (represented as `dict` in JSON). """

        self.responsible = None
        """ Final responsibility for event.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.sender = None
        """ Real world sender of the message.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.source = None
        """ Message source application.
        Type `MessageHeaderSource` (represented as `dict` in JSON). """

        super(MessageHeader, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeader, self).elementProperties()
        js.extend(
            [
                (
                    "author",
                    "author",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("definition", "definition", str, "canonical", False, None, False),
                (
                    "destination",
                    "destination",
                    MessageHeaderDestination,
                    "MessageHeaderDestination",
                    True,
                    None,
                    False,
                ),
                (
                    "enterer",
                    "enterer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "eventCoding",
                    "eventCoding",
                    coding.Coding,
                    "Coding",
                    False,
                    "event",
                    True,
                ),
                ("eventUri", "eventUri", str, "uri", False, "event", True),
                (
                    "focus",
                    "focus",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
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
                (
                    "response",
                    "response",
                    MessageHeaderResponse,
                    "MessageHeaderResponse",
                    False,
                    None,
                    False,
                ),
                (
                    "responsible",
                    "responsible",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "sender",
                    "sender",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "source",
                    "source",
                    MessageHeaderSource,
                    "MessageHeaderSource",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class MessageHeaderDestination(backboneelement.BackboneElement):
    """ Message destination application(s).

    The destination application which the message is intended for.
    """

    resource_type = "MessageHeaderDestination"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.endpoint = None
        """ Actual destination address or id.
        Type `str`. """

        self.name = None
        """ Name of system.
        Type `str`. """

        self.receiver = None
        """ Intended "real-world" recipient for the data.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.target = None
        """ Particular delivery destination within the destination.
        Type `FHIRReference` referencing `['Device']` (represented as `dict` in JSON). """

        super(MessageHeaderDestination, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeaderDestination, self).elementProperties()
        js.extend(
            [
                ("endpoint", "endpoint", str, "url", False, None, True),
                ("name", "name", str, "string", False, None, False),
                (
                    "receiver",
                    "receiver",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "target",
                    "target",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class MessageHeaderResponse(backboneelement.BackboneElement):
    """ If this is a reply to prior message.

    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """

    resource_type = "MessageHeaderResponse"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ ok | transient-error | fatal-error.
        Type `str`. """

        self.details = None
        """ Specific list of hints/warnings/errors.
        Type `FHIRReference` referencing `['OperationOutcome']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Id of original message.
        Type `str`. """

        super(MessageHeaderResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeaderResponse, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                (
                    "details",
                    "details",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("identifier", "identifier", str, "id", False, None, True),
            ]
        )
        return js


class MessageHeaderSource(backboneelement.BackboneElement):
    """ Message source application.

    The source application from which this message originated.
    """

    resource_type = "MessageHeaderSource"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contact = None
        """ Human contact for problems.
        Type `ContactPoint` (represented as `dict` in JSON). """

        self.endpoint = None
        """ Actual message source address or id.
        Type `str`. """

        self.name = None
        """ Name of system.
        Type `str`. """

        self.software = None
        """ Name of software running the system.
        Type `str`. """

        self.version = None
        """ Version of software running.
        Type `str`. """

        super(MessageHeaderSource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeaderSource, self).elementProperties()
        js.extend(
            [
                (
                    "contact",
                    "contact",
                    contactpoint.ContactPoint,
                    "ContactPoint",
                    False,
                    None,
                    False,
                ),
                ("endpoint", "endpoint", str, "url", False, None, True),
                ("name", "name", str, "string", False, None, False),
                ("software", "software", str, "string", False, None, False),
                ("version", "version", str, "string", False, None, False),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + ".coding"]
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + ".contactpoint"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
