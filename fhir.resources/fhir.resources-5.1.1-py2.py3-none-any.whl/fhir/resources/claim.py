# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Claim
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.

    A provider issued list of professional services and products which have
    been provided, or are to be provided, to a patient which is sent to an
    insurer for reimbursement.
    """

    resource_type = "Claim"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.accident = None
        """ Details of the event.
        Type `ClaimAccident` (represented as `dict` in JSON). """

        self.billablePeriod = None
        """ Relevant time frame for the claim.
        Type `Period` (represented as `dict` in JSON). """

        self.careTeam = None
        """ Members of the care team.
        List of `ClaimCareTeam` items (represented as `dict` in JSON). """

        self.created = None
        """ Resource creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.diagnosis = None
        """ Pertinent diagnosis information.
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """

        self.enterer = None
        """ Author of the claim.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.facility = None
        """ Servicing facility.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.fundsReserve = None
        """ For whom to reserve funds.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business Identifier for claim.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.insurance = None
        """ Patient insurance information.
        List of `ClaimInsurance` items (represented as `dict` in JSON). """

        self.insurer = None
        """ Target.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.item = None
        """ Product or service provided.
        List of `ClaimItem` items (represented as `dict` in JSON). """

        self.originalPrescription = None
        """ Original prescription if superseded by fulfiller.
        Type `FHIRReference` referencing `['DeviceRequest', 'MedicationRequest', 'VisionPrescription']` (represented as `dict` in JSON). """

        self.patient = None
        """ The recipient of the products and services.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.payee = None
        """ Recipient of benefits payable.
        Type `ClaimPayee` (represented as `dict` in JSON). """

        self.prescription = None
        """ Prescription authorizing services and products.
        Type `FHIRReference` referencing `['DeviceRequest', 'MedicationRequest', 'VisionPrescription']` (represented as `dict` in JSON). """

        self.priority = None
        """ Desired processing ugency.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.procedure = None
        """ Clinical procedures performed.
        List of `ClaimProcedure` items (represented as `dict` in JSON). """

        self.provider = None
        """ Party responsible for the claim.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.referral = None
        """ Treatment referral.
        Type `FHIRReference` referencing `['ServiceRequest']` (represented as `dict` in JSON). """

        self.related = None
        """ Prior or corollary claims.
        List of `ClaimRelated` items (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        self.subType = None
        """ More granular claim type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.supportingInfo = None
        """ Supporting information.
        List of `ClaimSupportingInfo` items (represented as `dict` in JSON). """

        self.total = None
        """ Total claim cost.
        Type `Money` (represented as `dict` in JSON). """

        self.type = None
        """ Category or discipline.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.use = None
        """ claim | preauthorization | predetermination.
        Type `str`. """

        super(Claim, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend(
            [
                (
                    "accident",
                    "accident",
                    ClaimAccident,
                    "ClaimAccident",
                    False,
                    None,
                    False,
                ),
                (
                    "billablePeriod",
                    "billablePeriod",
                    period.Period,
                    "Period",
                    False,
                    None,
                    False,
                ),
                (
                    "careTeam",
                    "careTeam",
                    ClaimCareTeam,
                    "ClaimCareTeam",
                    True,
                    None,
                    False,
                ),
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
                    "diagnosis",
                    "diagnosis",
                    ClaimDiagnosis,
                    "ClaimDiagnosis",
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
                    "facility",
                    "facility",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "fundsReserve",
                    "fundsReserve",
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
                    ClaimInsurance,
                    "ClaimInsurance",
                    True,
                    None,
                    True,
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
                ("item", "item", ClaimItem, "ClaimItem", True, None, False),
                (
                    "originalPrescription",
                    "originalPrescription",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
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
                ("payee", "payee", ClaimPayee, "ClaimPayee", False, None, False),
                (
                    "prescription",
                    "prescription",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "priority",
                    "priority",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "procedure",
                    "procedure",
                    ClaimProcedure,
                    "ClaimProcedure",
                    True,
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
                    True,
                ),
                (
                    "referral",
                    "referral",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("related", "related", ClaimRelated, "ClaimRelated", True, None, False),
                ("status", "status", str, "code", False, None, True),
                (
                    "subType",
                    "subType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "supportingInfo",
                    "supportingInfo",
                    ClaimSupportingInfo,
                    "ClaimSupportingInfo",
                    True,
                    None,
                    False,
                ),
                ("total", "total", money.Money, "Money", False, None, False),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                ("use", "use", str, "code", False, None, True),
            ]
        )
        return js


class ClaimAccident(backboneelement.BackboneElement):
    """ Details of the event.

    Details of an accident which resulted in injuries which required the
    products and services listed in the claim.
    """

    resource_type = "ClaimAccident"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.date = None
        """ When the incident occurred.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.locationAddress = None
        """ Where the event occurred.
        Type `Address` (represented as `dict` in JSON). """

        self.locationReference = None
        """ Where the event occurred.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.type = None
        """ The nature of the accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ClaimAccident, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimAccident, self).elementProperties()
        js.extend(
            [
                ("date", "date", fhirdate.FHIRDate, "date", False, None, True),
                (
                    "locationAddress",
                    "locationAddress",
                    address.Address,
                    "Address",
                    False,
                    "location",
                    False,
                ),
                (
                    "locationReference",
                    "locationReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "location",
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
            ]
        )
        return js


class ClaimCareTeam(backboneelement.BackboneElement):
    """ Members of the care team.

    The members of the team who provided the products and services.
    """

    resource_type = "ClaimCareTeam"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.provider = None
        """ Practitioner or organization.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.qualification = None
        """ Practitioner credential or specialization.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.responsible = None
        """ Indicator of the lead practitioner.
        Type `bool`. """

        self.role = None
        """ Function within the team.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sequence = None
        """ Order of care team.
        Type `int`. """

        super(ClaimCareTeam, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimCareTeam, self).elementProperties()
        js.extend(
            [
                (
                    "provider",
                    "provider",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "qualification",
                    "qualification",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("responsible", "responsible", bool, "boolean", False, None, False),
                (
                    "role",
                    "role",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("sequence", "sequence", int, "positiveInt", False, None, True),
            ]
        )
        return js


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ Pertinent diagnosis information.

    Information about diagnoses relevant to the claim items.
    """

    resource_type = "ClaimDiagnosis"

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

        self.onAdmission = None
        """ Present on admission.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.packageCode = None
        """ Package billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sequence = None
        """ Diagnosis instance identifier.
        Type `int`. """

        self.type = None
        """ Timing or nature of the diagnosis.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(ClaimDiagnosis, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend(
            [
                (
                    "diagnosisCodeableConcept",
                    "diagnosisCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "diagnosis",
                    True,
                ),
                (
                    "diagnosisReference",
                    "diagnosisReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "diagnosis",
                    True,
                ),
                (
                    "onAdmission",
                    "onAdmission",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "packageCode",
                    "packageCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("sequence", "sequence", int, "positiveInt", False, None, True),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class ClaimInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """

    resource_type = "ClaimInsurance"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.businessArrangement = None
        """ Additional provider contract number.
        Type `str`. """

        self.claimResponse = None
        """ Adjudication results.
        Type `FHIRReference` referencing `['ClaimResponse']` (represented as `dict` in JSON). """

        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` referencing `['Coverage']` (represented as `dict` in JSON). """

        self.focal = None
        """ Coverage to be used for adjudication.
        Type `bool`. """

        self.identifier = None
        """ Pre-assigned Claim number.
        Type `Identifier` (represented as `dict` in JSON). """

        self.preAuthRef = None
        """ Prior authorization reference number.
        List of `str` items. """

        self.sequence = None
        """ Insurance instance identifier.
        Type `int`. """

        super(ClaimInsurance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimInsurance, self).elementProperties()
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
                    "claimResponse",
                    "claimResponse",
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
                    True,
                ),
                ("focal", "focal", bool, "boolean", False, None, True),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                ("preAuthRef", "preAuthRef", str, "string", True, None, False),
                ("sequence", "sequence", int, "positiveInt", False, None, True),
            ]
        )
        return js


class ClaimItem(backboneelement.BackboneElement):
    """ Product or service provided.

    A claim line. Either a simple  product or service or a 'group' of details
    which can each be a simple items or groups of sub-details.
    """

    resource_type = "ClaimItem"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.bodySite = None
        """ Anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.careTeamSequence = None
        """ Applicable careTeam members.
        List of `int` items. """

        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.detail = None
        """ Product or service provided.
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """

        self.diagnosisSequence = None
        """ Applicable diagnoses.
        List of `int` items. """

        self.encounter = None
        """ Encounters related to this billed item.
        List of `FHIRReference` items referencing `['Encounter']` (represented as `dict` in JSON). """

        self.factor = None
        """ Price scaling factor.
        Type `float`. """

        self.informationSequence = None
        """ Applicable exception and supporting information.
        List of `int` items. """

        self.locationAddress = None
        """ Place of service or where product was supplied.
        Type `Address` (represented as `dict` in JSON). """

        self.locationCodeableConcept = None
        """ Place of service or where product was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.locationReference = None
        """ Place of service or where product was supplied.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.modifier = None
        """ Product or service billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """

        self.procedureSequence = None
        """ Applicable procedures.
        List of `int` items. """

        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.programCode = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """

        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sequence = None
        """ Item instance identifier.
        Type `int`. """

        self.servicedDate = None
        """ Date or dates of service or product delivery.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.servicedPeriod = None
        """ Date or dates of service or product delivery.
        Type `Period` (represented as `dict` in JSON). """

        self.subSite = None
        """ Anatomical sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items referencing `['Device']` (represented as `dict` in JSON). """

        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """

        super(ClaimItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend(
            [
                (
                    "bodySite",
                    "bodySite",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "careTeamSequence",
                    "careTeamSequence",
                    int,
                    "positiveInt",
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
                (
                    "detail",
                    "detail",
                    ClaimItemDetail,
                    "ClaimItemDetail",
                    True,
                    None,
                    False,
                ),
                (
                    "diagnosisSequence",
                    "diagnosisSequence",
                    int,
                    "positiveInt",
                    True,
                    None,
                    False,
                ),
                (
                    "encounter",
                    "encounter",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("factor", "factor", float, "decimal", False, None, False),
                (
                    "informationSequence",
                    "informationSequence",
                    int,
                    "positiveInt",
                    True,
                    None,
                    False,
                ),
                (
                    "locationAddress",
                    "locationAddress",
                    address.Address,
                    "Address",
                    False,
                    "location",
                    False,
                ),
                (
                    "locationCodeableConcept",
                    "locationCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "location",
                    False,
                ),
                (
                    "locationReference",
                    "locationReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "location",
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
                ("net", "net", money.Money, "Money", False, None, False),
                (
                    "procedureSequence",
                    "procedureSequence",
                    int,
                    "positiveInt",
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
                    True,
                ),
                (
                    "programCode",
                    "programCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
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
                    "revenue",
                    "revenue",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("sequence", "sequence", int, "positiveInt", False, None, True),
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
                (
                    "subSite",
                    "subSite",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "udi",
                    "udi",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("unitPrice", "unitPrice", money.Money, "Money", False, None, False),
            ]
        )
        return js


class ClaimItemDetail(backboneelement.BackboneElement):
    """ Product or service provided.

    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """

    resource_type = "ClaimItemDetail"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.factor = None
        """ Price scaling factor.
        Type `float`. """

        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """

        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.programCode = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """

        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sequence = None
        """ Item instance identifier.
        Type `int`. """

        self.subDetail = None
        """ Product or service provided.
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """

        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items referencing `['Device']` (represented as `dict` in JSON). """

        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """

        super(ClaimItemDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
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
                ("factor", "factor", float, "decimal", False, None, False),
                (
                    "modifier",
                    "modifier",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("net", "net", money.Money, "Money", False, None, False),
                (
                    "productOrService",
                    "productOrService",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "programCode",
                    "programCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
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
                    "revenue",
                    "revenue",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("sequence", "sequence", int, "positiveInt", False, None, True),
                (
                    "subDetail",
                    "subDetail",
                    ClaimItemDetailSubDetail,
                    "ClaimItemDetailSubDetail",
                    True,
                    None,
                    False,
                ),
                (
                    "udi",
                    "udi",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("unitPrice", "unitPrice", money.Money, "Money", False, None, False),
            ]
        )
        return js


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Product or service provided.

    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """

    resource_type = "ClaimItemDetailSubDetail"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.factor = None
        """ Price scaling factor.
        Type `float`. """

        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """

        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.programCode = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """

        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sequence = None
        """ Item instance identifier.
        Type `int`. """

        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items referencing `['Device']` (represented as `dict` in JSON). """

        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """

        super(ClaimItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
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
                ("factor", "factor", float, "decimal", False, None, False),
                (
                    "modifier",
                    "modifier",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("net", "net", money.Money, "Money", False, None, False),
                (
                    "productOrService",
                    "productOrService",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "programCode",
                    "programCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
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
                    "revenue",
                    "revenue",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("sequence", "sequence", int, "positiveInt", False, None, True),
                (
                    "udi",
                    "udi",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("unitPrice", "unitPrice", money.Money, "Money", False, None, False),
            ]
        )
        return js


class ClaimPayee(backboneelement.BackboneElement):
    """ Recipient of benefits payable.

    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """

    resource_type = "ClaimPayee"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.party = None
        """ Recipient reference.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization', 'Patient', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.type = None
        """ Category of recipient.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ClaimPayee, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend(
            [
                (
                    "party",
                    "party",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
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
                    True,
                ),
            ]
        )
        return js


class ClaimProcedure(backboneelement.BackboneElement):
    """ Clinical procedures performed.

    Procedures performed on the patient relevant to the billing items with the
    claim.
    """

    resource_type = "ClaimProcedure"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.date = None
        """ When the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.procedureCodeableConcept = None
        """ Specific clinical procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.procedureReference = None
        """ Specific clinical procedure.
        Type `FHIRReference` referencing `['Procedure']` (represented as `dict` in JSON). """

        self.sequence = None
        """ Procedure instance identifier.
        Type `int`. """

        self.type = None
        """ Category of Procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items referencing `['Device']` (represented as `dict` in JSON). """

        super(ClaimProcedure, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimProcedure, self).elementProperties()
        js.extend(
            [
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                (
                    "procedureCodeableConcept",
                    "procedureCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "procedure",
                    True,
                ),
                (
                    "procedureReference",
                    "procedureReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "procedure",
                    True,
                ),
                ("sequence", "sequence", int, "positiveInt", False, None, True),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "udi",
                    "udi",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class ClaimRelated(backboneelement.BackboneElement):
    """ Prior or corollary claims.

    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """

    resource_type = "ClaimRelated"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.claim = None
        """ Reference to the related claim.
        Type `FHIRReference` referencing `['Claim']` (represented as `dict` in JSON). """

        self.reference = None
        """ File or case reference.
        Type `Identifier` (represented as `dict` in JSON). """

        self.relationship = None
        """ How the reference claim is related.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ClaimRelated, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimRelated, self).elementProperties()
        js.extend(
            [
                (
                    "claim",
                    "claim",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "reference",
                    "reference",
                    identifier.Identifier,
                    "Identifier",
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
            ]
        )
        return js


class ClaimSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """

    resource_type = "ClaimSupportingInfo"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.category = None
        """ Classification of the supplied information.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.code = None
        """ Type of information.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.reason = None
        """ Explanation for the information.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sequence = None
        """ Information instance identifier.
        Type `int`. """

        self.timingDate = None
        """ When it occurred.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.timingPeriod = None
        """ When it occurred.
        Type `Period` (represented as `dict` in JSON). """

        self.valueAttachment = None
        """ Data to be provided.
        Type `Attachment` (represented as `dict` in JSON). """

        self.valueBoolean = None
        """ Data to be provided.
        Type `bool`. """

        self.valueQuantity = None
        """ Data to be provided.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueReference = None
        """ Data to be provided.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.valueString = None
        """ Data to be provided.
        Type `str`. """

        super(ClaimSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimSupportingInfo, self).elementProperties()
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
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
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
                ("sequence", "sequence", int, "positiveInt", False, None, True),
                (
                    "timingDate",
                    "timingDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    "timing",
                    False,
                ),
                (
                    "timingPeriod",
                    "timingPeriod",
                    period.Period,
                    "Period",
                    False,
                    "timing",
                    False,
                ),
                (
                    "valueAttachment",
                    "valueAttachment",
                    attachment.Attachment,
                    "Attachment",
                    False,
                    "value",
                    False,
                ),
                (
                    "valueBoolean",
                    "valueBoolean",
                    bool,
                    "boolean",
                    False,
                    "value",
                    False,
                ),
                (
                    "valueQuantity",
                    "valueQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "value",
                    False,
                ),
                (
                    "valueReference",
                    "valueReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "value",
                    False,
                ),
                ("valueString", "valueString", str, "string", False, "value", False),
            ]
        )
        return js


try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + ".address"]
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + ".attachment"]
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
