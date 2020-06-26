# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Patient(domainresource.DomainResource):
    """ Information about an individual or animal receiving health care services.

    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    resource_type = "Patient"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.active = None
        """ Whether this patient's record is in active use.
        Type `bool`. """

        self.address = None
        """ An address for the individual.
        List of `Address` items (represented as `dict` in JSON). """

        self.birthDate = None
        """ The date of birth for the individual.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.communication = None
        """ A language which may be used to communicate with the patient about
        his or her health.
        List of `PatientCommunication` items (represented as `dict` in JSON). """

        self.contact = None
        """ A contact party (e.g. guardian, partner, friend) for the patient.
        List of `PatientContact` items (represented as `dict` in JSON). """

        self.deceasedBoolean = None
        """ Indicates if the individual is deceased or not.
        Type `bool`. """

        self.deceasedDateTime = None
        """ Indicates if the individual is deceased or not.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """

        self.generalPractitioner = None
        """ Patient's nominated primary care provider.
        List of `FHIRReference` items referencing `['Organization', 'Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.identifier = None
        """ An identifier for this patient.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.link = None
        """ Link to another patient resource that concerns the same actual
        person.
        List of `PatientLink` items (represented as `dict` in JSON). """

        self.managingOrganization = None
        """ Organization that is the custodian of the patient record.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.maritalStatus = None
        """ Marital (civil) status of a patient.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.multipleBirthBoolean = None
        """ Whether patient is part of a multiple birth.
        Type `bool`. """

        self.multipleBirthInteger = None
        """ Whether patient is part of a multiple birth.
        Type `int`. """

        self.name = None
        """ A name associated with the patient.
        List of `HumanName` items (represented as `dict` in JSON). """

        self.photo = None
        """ Image of the patient.
        List of `Attachment` items (represented as `dict` in JSON). """

        self.telecom = None
        """ A contact detail for the individual.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        super(Patient, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Patient, self).elementProperties()
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
                    PatientCommunication,
                    "PatientCommunication",
                    True,
                    None,
                    False,
                ),
                (
                    "contact",
                    "contact",
                    PatientContact,
                    "PatientContact",
                    True,
                    None,
                    False,
                ),
                (
                    "deceasedBoolean",
                    "deceasedBoolean",
                    bool,
                    "boolean",
                    False,
                    "deceased",
                    False,
                ),
                (
                    "deceasedDateTime",
                    "deceasedDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "deceased",
                    False,
                ),
                ("gender", "gender", str, "code", False, None, False),
                (
                    "generalPractitioner",
                    "generalPractitioner",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
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
                ("link", "link", PatientLink, "PatientLink", True, None, False),
                (
                    "managingOrganization",
                    "managingOrganization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "maritalStatus",
                    "maritalStatus",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "multipleBirthBoolean",
                    "multipleBirthBoolean",
                    bool,
                    "boolean",
                    False,
                    "multipleBirth",
                    False,
                ),
                (
                    "multipleBirthInteger",
                    "multipleBirthInteger",
                    int,
                    "integer",
                    False,
                    "multipleBirth",
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


class PatientCommunication(backboneelement.BackboneElement):
    """ A language which may be used to communicate with the patient about his or
    her health.
    """

    resource_type = "PatientCommunication"

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

        super(PatientCommunication, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PatientCommunication, self).elementProperties()
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


class PatientContact(backboneelement.BackboneElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """

    resource_type = "PatientContact"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.address = None
        """ Address for the contact person.
        Type `Address` (represented as `dict` in JSON). """

        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """

        self.name = None
        """ A name associated with the contact person.
        Type `HumanName` (represented as `dict` in JSON). """

        self.organization = None
        """ Organization that is associated with the contact.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.period = None
        """ The period during which this contact person or organization is
        valid to be contacted relating to this patient.
        Type `Period` (represented as `dict` in JSON). """

        self.relationship = None
        """ The kind of relationship.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        super(PatientContact, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PatientContact, self).elementProperties()
        js.extend(
            [
                ("address", "address", address.Address, "Address", False, None, False),
                ("gender", "gender", str, "code", False, None, False),
                ("name", "name", humanname.HumanName, "HumanName", False, None, False),
                (
                    "organization",
                    "organization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
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


class PatientLink(backboneelement.BackboneElement):
    """ Link to another patient resource that concerns the same actual person.

    Link to another patient resource that concerns the same actual patient.
    """

    resource_type = "PatientLink"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.other = None
        """ The other patient or related person resource that the link refers
        to.
        Type `FHIRReference` referencing `['Patient', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.type = None
        """ replaced-by | replaces | refer | seealso.
        Type `str`. """

        super(PatientLink, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PatientLink, self).elementProperties()
        js.extend(
            [
                (
                    "other",
                    "other",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("type", "type", str, "code", False, None, True),
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
