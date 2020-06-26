#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Person) on 2019-05-14.
#  2019, SMART Health IT.


from . import (address, attachment, backboneelement, contactpoint,
               domainresource, fhirdate, fhirreference, humanname, identifier)


class Person(domainresource.DomainResource):
    """ A generic person record.
    
    Demographics and administrative information about a person independent of a
    specific health-related context.
    """

    resource_name = "Person"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.active = None
        """ This person's record is in active use.
        Type `bool`. """

        self.address = None
        """ One or more addresses for the person.
        List of `Address` items (represented as `dict` in JSON). """

        self.birthDate = None
        """ The date on which the person was born.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """

        self.identifier = None
        """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.link = None
        """ Link to a resource that concerns the same actual person.
        List of `PersonLink` items (represented as `dict` in JSON). """

        self.managingOrganization = None
        """ The organization that is the custodian of the person record.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

        self.name = None
        """ A name associated with the person.
        List of `HumanName` items (represented as `dict` in JSON). """

        self.photo = None
        """ Image of the person.
        Type `Attachment` (represented as `dict` in JSON). """

        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        super(Person, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Person, self).elementProperties()
        js.extend(
            [
                ("active", "active", bool, False, None, False),
                ("address", "address", address.Address, True, None, False),
                ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
                ("gender", "gender", str, False, None, False),
                ("identifier", "identifier", identifier.Identifier, True, None, False),
                ("link", "link", PersonLink, True, None, False),
                (
                    "managingOrganization",
                    "managingOrganization",
                    fhirreference.FHIRReference,
                    False,
                    None,
                    False,
                ),
                ("name", "name", humanname.HumanName, True, None, False),
                ("photo", "photo", attachment.Attachment, False, None, False),
                ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ]
        )
        return js


class PersonLink(backboneelement.BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """

    resource_name = "PersonLink"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.assurance = None
        """ level1 | level2 | level3 | level4.
        Type `str`. """

        self.target = None
        """ The resource to which this actual person is associated.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson, Person` (represented as `dict` in JSON). """

        super(PersonLink, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PersonLink, self).elementProperties()
        js.extend(
            [
                ("assurance", "assurance", str, False, None, False),
                ("target", "target", fhirreference.FHIRReference, False, None, True),
            ]
        )
        return js
