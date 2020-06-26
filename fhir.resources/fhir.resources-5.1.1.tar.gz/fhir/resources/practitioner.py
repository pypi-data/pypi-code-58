# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Practitioner
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Practitioner(domainresource.DomainResource):
    """ A person with a  formal responsibility in the provisioning of healthcare or
    related services.

    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """

    resource_type = "Practitioner"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.active = None
        """ Whether this practitioner's record is in active use.
        Type `bool`. """

        self.address = None
        """ Address(es) of the practitioner that are not role specific
        (typically home address).
        List of `Address` items (represented as `dict` in JSON). """

        self.birthDate = None
        """ The date  on which the practitioner was born.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.communication = None
        """ A language the practitioner can use in patient communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """

        self.identifier = None
        """ An identifier for the person as this agent.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.name = None
        """ The name(s) associated with the practitioner.
        List of `HumanName` items (represented as `dict` in JSON). """

        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """

        self.qualification = None
        """ Certification, licenses, or training pertaining to the provision of
        care.
        List of `PractitionerQualification` items (represented as `dict` in JSON). """

        self.telecom = None
        """ A contact detail for the practitioner (that apply to all roles).
        List of `ContactPoint` items (represented as `dict` in JSON). """

        super(Practitioner, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Practitioner, self).elementProperties()
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
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
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
                    "photo",
                    "photo",
                    attachment.Attachment,
                    "Attachment",
                    True,
                    None,
                    False,
                ),
                (
                    "qualification",
                    "qualification",
                    PractitionerQualification,
                    "PractitionerQualification",
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


class PractitionerQualification(backboneelement.BackboneElement):
    """ Certification, licenses, or training pertaining to the provision of care.

    The official certifications, training, and licenses that authorize or
    otherwise pertain to the provision of care by the practitioner.  For
    example, a medical license issued by a medical board authorizing the
    practitioner to practice medicine within a certian locality.
    """

    resource_type = "PractitionerQualification"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Coded representation of the qualification.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ An identifier for this qualification for the practitioner.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.issuer = None
        """ Organization that regulates and issues the qualification.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.period = None
        """ Period during which the qualification is valid.
        Type `Period` (represented as `dict` in JSON). """

        super(PractitionerQualification, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(PractitionerQualification, self).elementProperties()
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
                    "issuer",
                    "issuer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
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
