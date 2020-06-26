# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Organization
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Organization(domainresource.DomainResource):
    """ A grouping of people or organizations with a common purpose.

    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, payer/insurer, etc.
    """

    resource_type = "Organization"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.active = None
        """ Whether the organization's record is still in active use.
        Type `bool`. """

        self.address = None
        """ An address for the organization.
        List of `Address` items (represented as `dict` in JSON). """

        self.alias = None
        """ A list of alternate names that the organization is known as, or was
        known as in the past.
        List of `str` items. """

        self.contact = None
        """ Contact for the organization for a certain purpose.
        List of `OrganizationContact` items (represented as `dict` in JSON). """

        self.endpoint = None
        """ Technical endpoints providing access to services operated for the
        organization.
        List of `FHIRReference` items referencing `['Endpoint']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Identifies this organization  across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.name = None
        """ Name used for the organization.
        Type `str`. """

        self.partOf = None
        """ The organization of which this organization forms a part.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.telecom = None
        """ A contact detail for the organization.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        self.type = None
        """ Kind of organization.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(Organization, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Organization, self).elementProperties()
        js.extend(
            [
                ("active", "active", bool, "boolean", False, None, False),
                ("address", "address", address.Address, "Address", True, None, False),
                ("alias", "alias", str, "string", True, None, False),
                (
                    "contact",
                    "contact",
                    OrganizationContact,
                    "OrganizationContact",
                    True,
                    None,
                    False,
                ),
                (
                    "endpoint",
                    "endpoint",
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
                ("name", "name", str, "string", False, None, False),
                (
                    "partOf",
                    "partOf",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
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


class OrganizationContact(backboneelement.BackboneElement):
    """ Contact for the organization for a certain purpose.
    """

    resource_type = "OrganizationContact"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.address = None
        """ Visiting or postal addresses for the contact.
        Type `Address` (represented as `dict` in JSON). """

        self.name = None
        """ A name associated with the contact.
        Type `HumanName` (represented as `dict` in JSON). """

        self.purpose = None
        """ The type of contact.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.telecom = None
        """ Contact details (telephone, email, etc.)  for a contact.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        super(OrganizationContact, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(OrganizationContact, self).elementProperties()
        js.extend(
            [
                ("address", "address", address.Address, "Address", False, None, False),
                ("name", "name", humanname.HumanName, "HumanName", False, None, False),
                (
                    "purpose",
                    "purpose",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
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


try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + ".address"]
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + ".contactpoint"]
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
