# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CompartmentDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class CompartmentDefinition(domainresource.DomainResource):
    """ Compartment Definition for a resource.

    A compartment definition that defines how resources are accessed on a
    server.
    """

    resource_type = "CompartmentDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Patient | Encounter | RelatedPerson | Practitioner | Device.
        Type `str`. """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the compartment definition.
        Type `str`. """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.name = None
        """ Name for this compartment definition (computer friendly).
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this compartment definition is defined.
        Type `str`. """

        self.resource = None
        """ How a resource is related to the compartment.
        List of `CompartmentDefinitionResource` items (represented as `dict` in JSON). """

        self.search = None
        """ Whether the search syntax is supported.
        Type `bool`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.url = None
        """ Canonical identifier for this compartment definition, represented
        as a URI (globally unique).
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the compartment definition.
        Type `str`. """

        super(CompartmentDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompartmentDefinition, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                (
                    "contact",
                    "contact",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                ("description", "description", str, "markdown", False, None, False),
                ("experimental", "experimental", bool, "boolean", False, None, False),
                ("name", "name", str, "string", False, None, True),
                ("publisher", "publisher", str, "string", False, None, False),
                ("purpose", "purpose", str, "markdown", False, None, False),
                (
                    "resource",
                    "resource",
                    CompartmentDefinitionResource,
                    "CompartmentDefinitionResource",
                    True,
                    None,
                    False,
                ),
                ("search", "search", bool, "boolean", False, None, True),
                ("status", "status", str, "code", False, None, True),
                ("url", "url", str, "uri", False, None, True),
                (
                    "useContext",
                    "useContext",
                    usagecontext.UsageContext,
                    "UsageContext",
                    True,
                    None,
                    False,
                ),
                ("version", "version", str, "string", False, None, False),
            ]
        )
        return js


class CompartmentDefinitionResource(backboneelement.BackboneElement):
    """ How a resource is related to the compartment.

    Information about how a resource is related to the compartment.
    """

    resource_type = "CompartmentDefinitionResource"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Name of resource type.
        Type `str`. """

        self.documentation = None
        """ Additional documentation about the resource and compartment.
        Type `str`. """

        self.param = None
        """ Search Parameter Name, or chained parameters.
        List of `str` items. """

        super(CompartmentDefinitionResource, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CompartmentDefinitionResource, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                ("documentation", "documentation", str, "string", False, None, False),
                ("param", "param", str, "string", True, None, False),
            ]
        )
        return js


try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + ".contactdetail"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + ".usagecontext"]
