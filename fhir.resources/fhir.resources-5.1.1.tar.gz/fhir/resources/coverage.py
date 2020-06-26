# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coverage
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan or a payment agreement.

    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """

    resource_type = "Coverage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.beneficiary = None
        """ Plan beneficiary.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.class_fhir = None
        """ Additional coverage classifications.
        List of `CoverageClass` items (represented as `dict` in JSON). """

        self.contract = None
        """ Contract details.
        List of `FHIRReference` items referencing `['Contract']` (represented as `dict` in JSON). """

        self.costToBeneficiary = None
        """ Patient payments for services/products.
        List of `CoverageCostToBeneficiary` items (represented as `dict` in JSON). """

        self.dependent = None
        """ Dependent number.
        Type `str`. """

        self.identifier = None
        """ Business Identifier for the coverage.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.network = None
        """ Insurer network.
        Type `str`. """

        self.order = None
        """ Relative order of the coverage.
        Type `int`. """

        self.payor = None
        """ Issuer of the policy.
        List of `FHIRReference` items referencing `['Organization', 'Patient', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.period = None
        """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """

        self.policyHolder = None
        """ Owner of the policy.
        Type `FHIRReference` referencing `['Patient', 'RelatedPerson', 'Organization']` (represented as `dict` in JSON). """

        self.relationship = None
        """ Beneficiary relationship to the subscriber.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        self.subrogation = None
        """ Reimbursement to insurer.
        Type `bool`. """

        self.subscriber = None
        """ Subscriber to the policy.
        Type `FHIRReference` referencing `['Patient', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.subscriberId = None
        """ ID assigned to the subscriber.
        Type `str`. """

        self.type = None
        """ Coverage category such as medical or accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(Coverage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend(
            [
                (
                    "beneficiary",
                    "beneficiary",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "class_fhir",
                    "class",
                    CoverageClass,
                    "CoverageClass",
                    True,
                    None,
                    False,
                ),
                (
                    "contract",
                    "contract",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "costToBeneficiary",
                    "costToBeneficiary",
                    CoverageCostToBeneficiary,
                    "CoverageCostToBeneficiary",
                    True,
                    None,
                    False,
                ),
                ("dependent", "dependent", str, "string", False, None, False),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                ("network", "network", str, "string", False, None, False),
                ("order", "order", int, "positiveInt", False, None, False),
                (
                    "payor",
                    "payor",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    True,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                (
                    "policyHolder",
                    "policyHolder",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "relationship",
                    "relationship",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                ("subrogation", "subrogation", bool, "boolean", False, None, False),
                (
                    "subscriber",
                    "subscriber",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("subscriberId", "subscriberId", str, "string", False, None, False),
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


class CoverageClass(backboneelement.BackboneElement):
    """ Additional coverage classifications.

    A suite of underwriter specific classifiers.
    """

    resource_type = "CoverageClass"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ Human readable description of the type and value.
        Type `str`. """

        self.type = None
        """ Type of class such as 'group' or 'plan'.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.value = None
        """ Value associated with the type.
        Type `str`. """

        super(CoverageClass, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageClass, self).elementProperties()
        js.extend(
            [
                ("name", "name", str, "string", False, None, False),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                ("value", "value", str, "string", False, None, True),
            ]
        )
        return js


class CoverageCostToBeneficiary(backboneelement.BackboneElement):
    """ Patient payments for services/products.

    A suite of codes indicating the cost category and associated amount which
    have been detailed in the policy and may have been  included on the health
    card.
    """

    resource_type = "CoverageCostToBeneficiary"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.exception = None
        """ Exceptions for patient payments.
        List of `CoverageCostToBeneficiaryException` items (represented as `dict` in JSON). """

        self.type = None
        """ Cost category.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueMoney = None
        """ The amount or percentage due from the beneficiary.
        Type `Money` (represented as `dict` in JSON). """

        self.valueQuantity = None
        """ The amount or percentage due from the beneficiary.
        Type `Quantity` (represented as `dict` in JSON). """

        super(CoverageCostToBeneficiary, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CoverageCostToBeneficiary, self).elementProperties()
        js.extend(
            [
                (
                    "exception",
                    "exception",
                    CoverageCostToBeneficiaryException,
                    "CoverageCostToBeneficiaryException",
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
                (
                    "valueMoney",
                    "valueMoney",
                    money.Money,
                    "Money",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueQuantity",
                    "valueQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "value",
                    True,
                ),
            ]
        )
        return js


class CoverageCostToBeneficiaryException(backboneelement.BackboneElement):
    """ Exceptions for patient payments.

    A suite of codes indicating exceptions or reductions to patient costs and
    their effective periods.
    """

    resource_type = "CoverageCostToBeneficiaryException"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.period = None
        """ The effective period of the exception.
        Type `Period` (represented as `dict` in JSON). """

        self.type = None
        """ Exception category.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(CoverageCostToBeneficiaryException, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CoverageCostToBeneficiaryException, self).elementProperties()
        js.extend(
            [
                ("period", "period", period.Period, "Period", False, None, False),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
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
