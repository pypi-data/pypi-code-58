# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class CoverageEligibilityResponse(domainresource.DomainResource):
    """ CoverageEligibilityResponse resource.

    This resource provides eligibility and plan details from the processing of
    an CoverageEligibilityRequest resource.
    """

    resource_type = "CoverageEligibilityResponse"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.created = None
        """ Response creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.disposition = None
        """ Disposition Message.
        Type `str`. """

        self.error = None
        """ Processing errors.
        List of `CoverageEligibilityResponseError` items (represented as `dict` in JSON). """

        self.form = None
        """ Printed form identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business Identifier for coverage eligiblity request.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.insurance = None
        """ Patient insurance information.
        List of `CoverageEligibilityResponseInsurance` items (represented as `dict` in JSON). """

        self.insurer = None
        """ Coverage issuer.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.outcome = None
        """ queued | complete | error | partial.
        Type `str`. """

        self.patient = None
        """ Intended recipient of products and services.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.preAuthRef = None
        """ Preauthorization reference.
        Type `str`. """

        self.purpose = None
        """ auth-requirements | benefits | discovery | validation.
        List of `str` items. """

        self.request = None
        """ Eligibility request reference.
        Type `FHIRReference` referencing `['CoverageEligibilityRequest']` (represented as `dict` in JSON). """

        self.requestor = None
        """ Party responsible for the request.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.servicedDate = None
        """ Estimated date or dates of service.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.servicedPeriod = None
        """ Estimated date or dates of service.
        Type `Period` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        super(CoverageEligibilityResponse, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CoverageEligibilityResponse, self).elementProperties()
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
                ("disposition", "disposition", str, "string", False, None, False),
                (
                    "error",
                    "error",
                    CoverageEligibilityResponseError,
                    "CoverageEligibilityResponseError",
                    True,
                    None,
                    False,
                ),
                (
                    "form",
                    "form",
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
                (
                    "insurance",
                    "insurance",
                    CoverageEligibilityResponseInsurance,
                    "CoverageEligibilityResponseInsurance",
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
                ("outcome", "outcome", str, "code", False, None, True),
                (
                    "patient",
                    "patient",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("preAuthRef", "preAuthRef", str, "string", False, None, False),
                ("purpose", "purpose", str, "code", True, None, True),
                (
                    "request",
                    "request",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "requestor",
                    "requestor",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
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
            ]
        )
        return js


class CoverageEligibilityResponseError(backboneelement.BackboneElement):
    """ Processing errors.

    Errors encountered during the processing of the request.
    """

    resource_type = "CoverageEligibilityResponseError"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Error code detailing processing issues.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(CoverageEligibilityResponseError, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CoverageEligibilityResponseError, self).elementProperties()
        js.extend(
            [
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class CoverageEligibilityResponseInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services.
    """

    resource_type = "CoverageEligibilityResponseInsurance"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.benefitPeriod = None
        """ When the benefits are applicable.
        Type `Period` (represented as `dict` in JSON). """

        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` referencing `['Coverage']` (represented as `dict` in JSON). """

        self.inforce = None
        """ Coverage inforce indicator.
        Type `bool`. """

        self.item = None
        """ Benefits and authorization details.
        List of `CoverageEligibilityResponseInsuranceItem` items (represented as `dict` in JSON). """

        super(CoverageEligibilityResponseInsurance, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsurance, self).elementProperties()
        js.extend(
            [
                (
                    "benefitPeriod",
                    "benefitPeriod",
                    period.Period,
                    "Period",
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
                ("inforce", "inforce", bool, "boolean", False, None, False),
                (
                    "item",
                    "item",
                    CoverageEligibilityResponseInsuranceItem,
                    "CoverageEligibilityResponseInsuranceItem",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class CoverageEligibilityResponseInsuranceItem(backboneelement.BackboneElement):
    """ Benefits and authorization details.

    Benefits and optionally current balances, and authorization details by
    category or service.
    """

    resource_type = "CoverageEligibilityResponseInsuranceItem"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authorizationRequired = None
        """ Authorization required flag.
        Type `bool`. """

        self.authorizationSupporting = None
        """ Type of required supporting materials.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.authorizationUrl = None
        """ Preauthorization requirements endpoint.
        Type `str`. """

        self.benefit = None
        """ Benefit Summary.
        List of `CoverageEligibilityResponseInsuranceItemBenefit` items (represented as `dict` in JSON). """

        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.description = None
        """ Description of the benefit or services covered.
        Type `str`. """

        self.excluded = None
        """ Excluded from the plan.
        Type `bool`. """

        self.modifier = None
        """ Product or service billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.name = None
        """ Short name for the benefit.
        Type `str`. """

        self.network = None
        """ In or out of network.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.provider = None
        """ Performing practitioner.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.term = None
        """ Annual or lifetime.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.unit = None
        """ Individual or family.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(CoverageEligibilityResponseInsuranceItem, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItem, self).elementProperties()
        js.extend(
            [
                (
                    "authorizationRequired",
                    "authorizationRequired",
                    bool,
                    "boolean",
                    False,
                    None,
                    False,
                ),
                (
                    "authorizationSupporting",
                    "authorizationSupporting",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "authorizationUrl",
                    "authorizationUrl",
                    str,
                    "uri",
                    False,
                    None,
                    False,
                ),
                (
                    "benefit",
                    "benefit",
                    CoverageEligibilityResponseInsuranceItemBenefit,
                    "CoverageEligibilityResponseInsuranceItemBenefit",
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
                ("description", "description", str, "string", False, None, False),
                ("excluded", "excluded", bool, "boolean", False, None, False),
                (
                    "modifier",
                    "modifier",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("name", "name", str, "string", False, None, False),
                (
                    "network",
                    "network",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
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
                    "term",
                    "term",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "unit",
                    "unit",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class CoverageEligibilityResponseInsuranceItemBenefit(backboneelement.BackboneElement):
    """ Benefit Summary.

    Benefits used to date.
    """

    resource_type = "CoverageEligibilityResponseInsuranceItemBenefit"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.allowedMoney = None
        """ Benefits allowed.
        Type `Money` (represented as `dict` in JSON). """

        self.allowedString = None
        """ Benefits allowed.
        Type `str`. """

        self.allowedUnsignedInt = None
        """ Benefits allowed.
        Type `int`. """

        self.type = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.usedMoney = None
        """ Benefits used.
        Type `Money` (represented as `dict` in JSON). """

        self.usedString = None
        """ Benefits used.
        Type `str`. """

        self.usedUnsignedInt = None
        """ Benefits used.
        Type `int`. """

        super(CoverageEligibilityResponseInsuranceItemBenefit, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(
            CoverageEligibilityResponseInsuranceItemBenefit, self
        ).elementProperties()
        js.extend(
            [
                (
                    "allowedMoney",
                    "allowedMoney",
                    money.Money,
                    "Money",
                    False,
                    "allowed",
                    False,
                ),
                (
                    "allowedString",
                    "allowedString",
                    str,
                    "string",
                    False,
                    "allowed",
                    False,
                ),
                (
                    "allowedUnsignedInt",
                    "allowedUnsignedInt",
                    int,
                    "unsignedInt",
                    False,
                    "allowed",
                    False,
                ),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                ("usedMoney", "usedMoney", money.Money, "Money", False, "used", False),
                ("usedString", "usedString", str, "string", False, "used", False),
                (
                    "usedUnsignedInt",
                    "usedUnsignedInt",
                    int,
                    "unsignedInt",
                    False,
                    "used",
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
    from . import money
except ImportError:
    money = sys.modules[__package__ + ".money"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
