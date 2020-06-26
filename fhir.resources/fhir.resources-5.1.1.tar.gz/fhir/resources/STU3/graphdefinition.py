# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GraphDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class GraphDefinition(domainresource.DomainResource):
    """ Definition of an graph of resources.

    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """

    resource_type = "GraphDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the graph definition.
        Type `str`. """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.jurisdiction = None
        """ Intended jurisdiction for graph definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.link = None
        """ Links this graph makes rules about.
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """

        self.name = None
        """ Name for this graph definition (computer friendly).
        Type `str`. """

        self.profile = None
        """ Profile on base resource.
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this graph definition is defined.
        Type `str`. """

        self.start = None
        """ Type of resource at which the graph starts.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.url = None
        """ Logical URI to reference this graph definition (globally unique).
        Type `str`. """

        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the graph definition.
        Type `str`. """

        super(GraphDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GraphDefinition, self).elementProperties()
        js.extend(
            [
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
                (
                    "jurisdiction",
                    "jurisdiction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "link",
                    "link",
                    GraphDefinitionLink,
                    "GraphDefinitionLink",
                    True,
                    None,
                    False,
                ),
                ("name", "name", str, "string", False, None, True),
                ("profile", "profile", str, "uri", False, None, False),
                ("publisher", "publisher", str, "string", False, None, False),
                ("purpose", "purpose", str, "markdown", False, None, False),
                ("start", "start", str, "code", False, None, True),
                ("status", "status", str, "code", False, None, True),
                ("url", "url", str, "uri", False, None, False),
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


class GraphDefinitionLink(backboneelement.BackboneElement):
    """ Links this graph makes rules about.
    """

    resource_type = "GraphDefinitionLink"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Why this link is specified.
        Type `str`. """

        self.max = None
        """ Maximum occurrences for this link.
        Type `str`. """

        self.min = None
        """ Minimum occurrences for this link.
        Type `int`. """

        self.path = None
        """ Path in the resource that contains the link.
        Type `str`. """

        self.sliceName = None
        """ Which slice (if profiled).
        Type `str`. """

        self.target = None
        """ Potential target for the link.
        List of `GraphDefinitionLinkTarget` items (represented as `dict` in JSON). """

        super(GraphDefinitionLink, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GraphDefinitionLink, self).elementProperties()
        js.extend(
            [
                ("description", "description", str, "string", False, None, False),
                ("max", "max", str, "string", False, None, False),
                ("min", "min", int, "integer", False, None, False),
                ("path", "path", str, "string", False, None, True),
                ("sliceName", "sliceName", str, "string", False, None, False),
                (
                    "target",
                    "target",
                    GraphDefinitionLinkTarget,
                    "GraphDefinitionLinkTarget",
                    True,
                    None,
                    True,
                ),
            ]
        )
        return js


class GraphDefinitionLinkTarget(backboneelement.BackboneElement):
    """ Potential target for the link.
    """

    resource_type = "GraphDefinitionLinkTarget"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.compartment = None
        """ Compartment Consistency Rules.
        List of `GraphDefinitionLinkTargetCompartment` items (represented as `dict` in JSON). """

        self.link = None
        """ Additional links from target resource.
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """

        self.profile = None
        """ Profile for the target resource.
        Type `str`. """

        self.type = None
        """ Type of resource this link refers to.
        Type `str`. """

        super(GraphDefinitionLinkTarget, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(GraphDefinitionLinkTarget, self).elementProperties()
        js.extend(
            [
                (
                    "compartment",
                    "compartment",
                    GraphDefinitionLinkTargetCompartment,
                    "GraphDefinitionLinkTargetCompartment",
                    True,
                    None,
                    False,
                ),
                (
                    "link",
                    "link",
                    GraphDefinitionLink,
                    "GraphDefinitionLink",
                    True,
                    None,
                    False,
                ),
                ("profile", "profile", str, "uri", False, None, False),
                ("type", "type", str, "code", False, None, True),
            ]
        )
        return js


class GraphDefinitionLinkTargetCompartment(backboneelement.BackboneElement):
    """ Compartment Consistency Rules.
    """

    resource_type = "GraphDefinitionLinkTargetCompartment"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Identifies the compartment.
        Type `str`. """

        self.description = None
        """ Documentation for FHIRPath expression.
        Type `str`. """

        self.expression = None
        """ Custom rule, as a FHIRPath expression.
        Type `str`. """

        self.rule = None
        """ identical | matching | different | custom.
        Type `str`. """

        super(GraphDefinitionLinkTargetCompartment, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(GraphDefinitionLinkTargetCompartment, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                ("description", "description", str, "string", False, None, False),
                ("expression", "expression", str, "string", False, None, False),
                ("rule", "rule", str, "code", False, None, True),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
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
