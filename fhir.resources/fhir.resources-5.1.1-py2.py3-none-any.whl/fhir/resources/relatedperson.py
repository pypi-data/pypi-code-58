# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedPerson
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class RelatedPerson(domainresource.DomainResource):
    """ A person that is related to a patient, but who is not a direct target of
    care.

    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """

    resource_type = "RelatedPerson"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.active = None
        """ Whether this related person's record is in active use.
        Type `bool`. """

        self.address = None
        """ Address where the related person can be contacted or visited.
        List of `Address` items (represented as `dict` in JSON). """

        self.birthDate = None
        """ The date on which the related person was born.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.communication = None
        """ A language which may be used to communicate with about the
        patient's health.
        List of `RelatedPersonCommunication` items (represented as `dict` in JSON). """

        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """

        self.identifier = None
        """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.name = None
        """ A name associated with the person.
        List of `HumanName` items (represented as `dict` in JSON). """

        self.patient = None
        """ The patient this person is related to.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.period = None
        """ Period of time that this relationship is considered valid.
        Type `Period` (represented as `dict` in JSON). """

        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """

        self.relationship = None
        """ The nature of the relationship.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        super(RelatedPerson, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RelatedPerson, self).elementProperties()
        js.extend(
            [
                ("active", "active", bool, "boolean", False, None, False),
                ("address", "address", address.Address, "Address", True, None, False),
                (
                    "birthDate",
                    "birthDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    None,
                    False,
                ),
                (
                    "communication",
                    "communication",
                    RelatedPersonCommunication,
                    "RelatedPersonCommunication",
                    True,
                    None,
                    False,
                ),
                ("gender", "gender", str, "code", False, None, False),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                ("name", "name", humanname.HumanName, "HumanName", True, None, False),
                (
                    "patient",
                    "patient",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                (
                    "photo",
                    "photo",
                    attachment.Attachment,
                    "Attachment",
                    True,
                    None,
                    False,
                ),
                (
                    "relationship",
                    "relationship",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "telecom",
                    "telecom",
                    contactpoint.ContactPoint,
                    "ContactPoint",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class RelatedPersonCommunication(backboneelement.BackboneElement):
    """ A language which may be used to communicate with about the patient's health.
    """

    resource_type = "RelatedPersonCommunication"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.language = None
        """ The language which can be used to communicate with the patient
        about his or her health.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.preferred = None
        """ Language preference indicator.
        Type `bool`. """

        super(RelatedPersonCommunication, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(RelatedPersonCommunication, self).elementProperties()
        js.extend(
            [
                (
                    "language",
                    "language",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                ("preferred", "preferred", bool, "boolean", False, None, False),
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
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + ".contactpoint"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + ".humanname"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
