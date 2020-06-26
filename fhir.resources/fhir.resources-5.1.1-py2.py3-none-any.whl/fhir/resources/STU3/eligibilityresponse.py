# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EligibilityResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class EligibilityResponse(domainresource.DomainResource):
    """ EligibilityResponse resource.

    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """

    resource_type = "EligibilityResponse"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.disposition = None
        """ Disposition Message.
        Type `str`. """

        self.error = None
        """ Processing errors.
        List of `EligibilityResponseError` items (represented as `dict` in JSON). """

        self.form = None
        """ Printed Form Identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.inforce = None
        """ Coverage inforce indicator.
        Type `bool`. """

        self.insurance = None
        """ Details by insurance coverage.
        List of `EligibilityResponseInsurance` items (represented as `dict` in JSON). """

        self.insurer = None
        """ Insurer issuing the coverage.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.outcome = None
        """ complete | error | partial.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.request = None
        """ Eligibility reference.
        Type `FHIRReference` referencing `['EligibilityRequest']` (represented as `dict` in JSON). """

        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `['Practitioner']` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        super(EligibilityResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EligibilityResponse, self).elementProperties()
        js.extend(
            [
                (
                    "created",
                    "created",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                ("disposition", "disposition", str, "string", False, None, False),
                (
                    "error",
                    "error",
                    EligibilityResponseError,
                    "EligibilityResponseError",
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
                ("inforce", "inforce", bool, "boolean", False, None, False),
                (
                    "insurance",
                    "insurance",
                    EligibilityResponseInsurance,
                    "EligibilityResponseInsurance",
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
                    "request",
                    "request",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "requestOrganization",
                    "requestOrganization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "requestProvider",
                    "requestProvider",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, False),
            ]
        )
        return js


class EligibilityResponseError(backboneelement.BackboneElement):
    """ Processing errors.

    Mutually exclusive with Services Provided (Item).
    """

    resource_type = "EligibilityResponseError"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Error code detailing processing issues.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(EligibilityResponseError, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EligibilityResponseError, self).elementProperties()
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


class EligibilityResponseInsurance(backboneelement.BackboneElement):
    """ Details by insurance coverage.

    The insurer may provide both the details for the requested coverage as well
    as details for additional coverages known to the insurer.
    """

    resource_type = "EligibilityResponseInsurance"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.benefitBalance = None
        """ Benefits by Category.
        List of `EligibilityResponseInsuranceBenefitBalance` items (represented as `dict` in JSON). """

        self.contract = None
        """ Contract details.
        Type `FHIRReference` referencing `['Contract']` (represented as `dict` in JSON). """

        self.coverage = None
        """ Updated Coverage details.
        Type `FHIRReference` referencing `['Coverage']` (represented as `dict` in JSON). """

        super(EligibilityResponseInsurance, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(EligibilityResponseInsurance, self).elementProperties()
        js.extend(
            [
                (
                    "benefitBalance",
                    "benefitBalance",
                    EligibilityResponseInsuranceBenefitBalance,
                    "EligibilityResponseInsuranceBenefitBalance",
                    True,
                    None,
                    False,
                ),
                (
                    "contract",
                    "contract",
                    fhirreference.FHIRReference,
                    "Reference",
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
                    False,
                ),
            ]
        )
        return js


class EligibilityResponseInsuranceBenefitBalance(backboneelement.BackboneElement):
    """ Benefits by Category.

    Benefits and optionally current balances by Category.
    """

    resource_type = "EligibilityResponseInsuranceBenefitBalance"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.category = None
        """ Type of services covered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.description = None
        """ Description of the benefit or services covered.
        Type `str`. """

        self.excluded = None
        """ Excluded from the plan.
        Type `bool`. """

        self.financial = None
        """ Benefit Summary.
        List of `EligibilityResponseInsuranceBenefitBalanceFinancial` items (represented as `dict` in JSON). """

        self.name = None
        """ Short name for the benefit.
        Type `str`. """

        self.network = None
        """ In or out of network.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subCategory = None
        """ Detailed services covered within the type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.term = None
        """ Annual or lifetime.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.unit = None
        """ Individual or family.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(EligibilityResponseInsuranceBenefitBalance, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(EligibilityResponseInsuranceBenefitBalance, self).elementProperties()
        js.extend(
            [
                (
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                ("description", "description", str, "string", False, None, False),
                ("excluded", "excluded", bool, "boolean", False, None, False),
                (
                    "financial",
                    "financial",
                    EligibilityResponseInsuranceBenefitBalanceFinancial,
                    "EligibilityResponseInsuranceBenefitBalanceFinancial",
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
                    "subCategory",
                    "subCategory",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
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


class EligibilityResponseInsuranceBenefitBalanceFinancial(
    backboneelement.BackboneElement
):
    """ Benefit Summary.

    Benefits Used to date.
    """

    resource_type = "EligibilityResponseInsuranceBenefitBalanceFinancial"

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
        """ Deductable, visits, benefit amount.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.usedMoney = None
        """ Benefits used.
        Type `Money` (represented as `dict` in JSON). """

        self.usedUnsignedInt = None
        """ Benefits used.
        Type `int`. """

        super(EligibilityResponseInsuranceBenefitBalanceFinancial, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(
            EligibilityResponseInsuranceBenefitBalanceFinancial, self
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
