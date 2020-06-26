# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class SupplyRequest(domainresource.DomainResource):
    """ Request for a medication, substance or device.

    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """

    resource_type = "SupplyRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authoredOn = None
        """ When the request was made.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.category = None
        """ The kind of supply (central, non-stock, etc.).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.deliverFrom = None
        """ The origin of the supply.
        Type `FHIRReference` referencing `['Organization'], ['Location']` (represented as `dict` in JSON). """

        self.deliverTo = None
        """ The destination of the supply.
        Type `FHIRReference` referencing `['Organization'], ['Location'], ['Patient']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """

        self.occurrenceDateTime = None
        """ When the request should be fulfilled.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.occurrencePeriod = None
        """ When the request should be fulfilled.
        Type `Period` (represented as `dict` in JSON). """

        self.occurrenceTiming = None
        """ When the request should be fulfilled.
        Type `Timing` (represented as `dict` in JSON). """

        self.orderedItem = None
        """ The item being requested.
        Type `SupplyRequestOrderedItem` (represented as `dict` in JSON). """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.reasonCodeableConcept = None
        """ Why the supply item was requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why the supply item was requested.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.requester = None
        """ Who/what is requesting service.
        Type `SupplyRequestRequester` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | suspended +.
        Type `str`. """

        self.supplier = None
        """ Who is intended to fulfill the request.
        List of `FHIRReference` items referencing `['Organization']` (represented as `dict` in JSON). """

        super(SupplyRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SupplyRequest, self).elementProperties()
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
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "deliverFrom",
                    "deliverFrom",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "deliverTo",
                    "deliverTo",
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
                    "orderedItem",
                    "orderedItem",
                    SupplyRequestOrderedItem,
                    "SupplyRequestOrderedItem",
                    False,
                    None,
                    False,
                ),
                ("priority", "priority", str, "code", False, None, False),
                (
                    "reasonCodeableConcept",
                    "reasonCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "reason",
                    False,
                ),
                (
                    "reasonReference",
                    "reasonReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "reason",
                    False,
                ),
                (
                    "requester",
                    "requester",
                    SupplyRequestRequester,
                    "SupplyRequestRequester",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, False),
                (
                    "supplier",
                    "supplier",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class SupplyRequestOrderedItem(backboneelement.BackboneElement):
    """ The item being requested.
    """

    resource_type = "SupplyRequestOrderedItem"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.itemCodeableConcept = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.itemReference = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `FHIRReference` referencing `['Medication'], ['Substance'], ['Device']` (represented as `dict` in JSON). """

        self.quantity = None
        """ The requested amount of the item indicated.
        Type `Quantity` (represented as `dict` in JSON). """

        super(SupplyRequestOrderedItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SupplyRequestOrderedItem, self).elementProperties()
        js.extend(
            [
                (
                    "itemCodeableConcept",
                    "itemCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "item",
                    False,
                ),
                (
                    "itemReference",
                    "itemReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "item",
                    False,
                ),
                (
                    "quantity",
                    "quantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class SupplyRequestRequester(backboneelement.BackboneElement):
    """ Who/what is requesting service.

    The individual who initiated the request and has responsibility for its
    activation.
    """

    resource_type = "SupplyRequestRequester"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.agent = None
        """ Individual making the request.
        Type `FHIRReference` referencing `['Practitioner'], ['Organization'], ['Patient'], ['RelatedPerson'], ['Device']` (represented as `dict` in JSON). """

        self.onBehalfOf = None
        """ Organization agent is acting for.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        super(SupplyRequestRequester, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SupplyRequestRequester, self).elementProperties()
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
