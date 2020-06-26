# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class CoverageEligibilityRequest(domainresource.DomainResource):
    """ CoverageEligibilityRequest resource.

    The CoverageEligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    CoverageEligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """

    resource_type = "CoverageEligibilityRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.enterer = None
        """ Author.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.facility = None
        """ Servicing facility.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business Identifier for coverage eligiblity request.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.insurance = None
        """ Patient insurance information.
        List of `CoverageEligibilityRequestInsurance` items (represented as `dict` in JSON). """

        self.insurer = None
        """ Coverage issuer.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.item = None
        """ Item to be evaluated for eligibiity.
        List of `CoverageEligibilityRequestItem` items (represented as `dict` in JSON). """

        self.patient = None
        """ Intended recipient of products and services.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.priority = None
        """ Desired processing priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.provider = None
        """ Party responsible for the request.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.purpose = None
        """ auth-requirements | benefits | discovery | validation.
        List of `str` items. """

        self.servicedDate = None
        """ Estimated date or dates of service.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.servicedPeriod = None
        """ Estimated date or dates of service.
        Type `Period` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        self.supportingInfo = None
        """ Supporting information.
        List of `CoverageEligibilityRequestSupportingInfo` items (represented as `dict` in JSON). """

        super(CoverageEligibilityRequest, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CoverageEligibilityRequest, self).elementProperties()
        js.extend(
            [
                (
                    "created",
                    "created",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    True,
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
                    "facility",
                    "facility",
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
                    "insurance",
                    "insurance",
                    CoverageEligibilityRequestInsurance,
                    "CoverageEligibilityRequestInsurance",
                    True,
                    None,
                    False,
                ),
                (
                    "insurer",
                    "insurer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "item",
                    "item",
                    CoverageEligibilityRequestItem,
                    "CoverageEligibilityRequestItem",
                    True,
                    None,
                    False,
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
                    "priority",
                    "priority",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "provider",
                    "provider",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("purpose", "purpose", str, "code", True, None, True),
                (
                    "servicedDate",
                    "servicedDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    "serviced",
                    False,
                ),
                (
                    "servicedPeriod",
                    "servicedPeriod",
                    period.Period,
                    "Period",
                    False,
                    "serviced",
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "supportingInfo",
                    "supportingInfo",
                    CoverageEligibilityRequestSupportingInfo,
                    "CoverageEligibilityRequestSupportingInfo",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class CoverageEligibilityRequestInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services.
    """

    resource_type = "CoverageEligibilityRequestInsurance"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.businessArrangement = None
        """ Additional provider contract number.
        Type `str`. """

        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` referencing `['Coverage']` (represented as `dict` in JSON). """

        self.focal = None
        """ Applicable coverage.
        Type `bool`. """

        super(CoverageEligibilityRequestInsurance, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CoverageEligibilityRequestInsurance, self).elementProperties()
        js.extend(
            [
                (
                    "businessArrangement",
                    "businessArrangement",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "coverage",
                    "coverage",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("focal", "focal", bool, "boolean", False, None, False),
            ]
        )
        return js


class CoverageEligibilityRequestItem(backboneelement.BackboneElement):
    """ Item to be evaluated for eligibiity.

    Service categories or billable services for which benefit details and/or an
    authorization prior to service delivery may be required by the payor.
    """

    resource_type = "CoverageEligibilityRequestItem"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.detail = None
        """ Product or service details.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.diagnosis = None
        """ Applicable diagnosis.
        List of `CoverageEligibilityRequestItemDiagnosis` items (represented as `dict` in JSON). """

        self.facility = None
        """ Servicing facility.
        Type `FHIRReference` referencing `['Location', 'Organization']` (represented as `dict` in JSON). """

        self.modifier = None
        """ Product or service billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.provider = None
        """ Perfoming practitioner.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """

        self.supportingInfoSequence = None
        """ Applicable exception or supporting information.
        List of `int` items. """

        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """

        super(CoverageEligibilityRequestItem, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CoverageEligibilityRequestItem, self).elementProperties()
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
                    "detail",
                    "detail",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "diagnosis",
                    "diagnosis",
                    CoverageEligibilityRequestItemDiagnosis,
                    "CoverageEligibilityRequestItemDiagnosis",
                    True,
                    None,
                    False,
                ),
                (
                    "facility",
                    "facility",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "modifier",
                    "modifier",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "productOrService",
                    "productOrService",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "provider",
                    "provider",
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
                    "supportingInfoSequence",
                    "supportingInfoSequence",
                    int,
                    "positiveInt",
                    True,
                    None,
                    False,
                ),
                ("unitPrice", "unitPrice", money.Money, "Money", False, None, False),
            ]
        )
        return js


class CoverageEligibilityRequestItemDiagnosis(backboneelement.BackboneElement):
    """ Applicable diagnosis.

    Patient diagnosis for which care is sought.
    """

    resource_type = "CoverageEligibilityRequestItemDiagnosis"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.diagnosisCodeableConcept = None
        """ Nature of illness or problem.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.diagnosisReference = None
        """ Nature of illness or problem.
        Type `FHIRReference` referencing `['Condition']` (represented as `dict` in JSON). """

        super(CoverageEligibilityRequestItemDiagnosis, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CoverageEligibilityRequestItemDiagnosis, self).elementProperties()
        js.extend(
            [
                (
                    "diagnosisCodeableConcept",
                    "diagnosisCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "diagnosis",
                    False,
                ),
                (
                    "diagnosisReference",
                    "diagnosisReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "diagnosis",
                    False,
                ),
            ]
        )
        return js


class CoverageEligibilityRequestSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """

    resource_type = "CoverageEligibilityRequestSupportingInfo"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.appliesToAll = None
        """ Applies to all items.
        Type `bool`. """

        self.information = None
        """ Data to be provided.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.sequence = None
        """ Information instance identifier.
        Type `int`. """

        super(CoverageEligibilityRequestSupportingInfo, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CoverageEligibilityRequestSupportingInfo, self).elementProperties()
        js.extend(
            [
                ("appliesToAll", "appliesToAll", bool, "boolean", False, None, False),
                (
                    "information",
                    "information",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("sequence", "sequence", int, "positiveInt", False, None, True),
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
    from . import money
except ImportError:
    money = sys.modules[__package__ + ".money"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
