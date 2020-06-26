# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class CodeSystem(domainresource.DomainResource):
    """ A set of codes drawn from one or more code systems.

    A code system resource specifies a set of codes drawn from one or more code
    systems.
    """

    resource_type = "CodeSystem"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.caseSensitive = None
        """ If code comparison is case sensitive.
        Type `bool`. """

        self.compositional = None
        """ If code system defines a post-composition grammar.
        Type `bool`. """

        self.concept = None
        """ Concepts in the code system.
        List of `CodeSystemConcept` items (represented as `dict` in JSON). """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.content = None
        """ not-present | example | fragment | complete.
        Type `str`. """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.count = None
        """ Total concepts in the code system.
        Type `int`. """

        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the code system.
        Type `str`. """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.filter = None
        """ Filter that can be used in a value set.
        List of `CodeSystemFilter` items (represented as `dict` in JSON). """

        self.hierarchyMeaning = None
        """ grouped-by | is-a | part-of | classified-with.
        Type `str`. """

        self.identifier = None
        """ Additional identifier for the code system.
        Type `Identifier` (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for code system (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.name = None
        """ Name for this code system (computer friendly).
        Type `str`. """

        self.property = None
        """ Additional information supplied about each concept.
        List of `CodeSystemProperty` items (represented as `dict` in JSON). """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this code system is defined.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.title = None
        """ Name for this code system (human friendly).
        Type `str`. """

        self.url = None
        """ Logical URI to reference this code system (globally unique)
        (Coding.system).
        Type `str`. """

        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.valueSet = None
        """ Canonical URL for value set with entire code system.
        Type `str`. """

        self.version = None
        """ Business version of the code system (Coding.version).
        Type `str`. """

        self.versionNeeded = None
        """ If definitions are not stable.
        Type `bool`. """

        super(CodeSystem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CodeSystem, self).elementProperties()
        js.extend(
            [
                ("caseSensitive", "caseSensitive", bool, "boolean", False, None, False),
                ("compositional", "compositional", bool, "boolean", False, None, False),
                (
                    "concept",
                    "concept",
                    CodeSystemConcept,
                    "CodeSystemConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "contact",
                    "contact",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("content", "content", str, "code", False, None, True),
                ("copyright", "copyright", str, "markdown", False, None, False),
                ("count", "count", int, "unsignedInt", False, None, False),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                ("description", "description", str, "markdown", False, None, False),
                ("experimental", "experimental", bool, "boolean", False, None, False),
                (
                    "filter",
                    "filter",
                    CodeSystemFilter,
                    "CodeSystemFilter",
                    True,
                    None,
                    False,
                ),
                (
                    "hierarchyMeaning",
                    "hierarchyMeaning",
                    str,
                    "code",
                    False,
                    None,
                    False,
                ),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                (
                    "jurisdiction",
                    "jurisdiction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("name", "name", str, "string", False, None, False),
                (
                    "property",
                    "property",
                    CodeSystemProperty,
                    "CodeSystemProperty",
                    True,
                    None,
                    False,
                ),
                ("publisher", "publisher", str, "string", False, None, False),
                ("purpose", "purpose", str, "markdown", False, None, False),
                ("status", "status", str, "code", False, None, True),
                ("title", "title", str, "string", False, None, False),
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
                ("valueSet", "valueSet", str, "uri", False, None, False),
                ("version", "version", str, "string", False, None, False),
                ("versionNeeded", "versionNeeded", bool, "boolean", False, None, False),
            ]
        )
        return js


class CodeSystemConcept(backboneelement.BackboneElement):
    """ Concepts in the code system.

    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meaning of the hierarchical relationships are.
    """

    resource_type = "CodeSystemConcept"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Code that identifies concept.
        Type `str`. """

        self.concept = None
        """ Child Concepts (is-a/contains/categorizes).
        List of `CodeSystemConcept` items (represented as `dict` in JSON). """

        self.definition = None
        """ Formal definition.
        Type `str`. """

        self.designation = None
        """ Additional representations for the concept.
        List of `CodeSystemConceptDesignation` items (represented as `dict` in JSON). """

        self.display = None
        """ Text to display to the user.
        Type `str`. """

        self.property = None
        """ Property value for the concept.
        List of `CodeSystemConceptProperty` items (represented as `dict` in JSON). """

        super(CodeSystemConcept, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CodeSystemConcept, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                (
                    "concept",
                    "concept",
                    CodeSystemConcept,
                    "CodeSystemConcept",
                    True,
                    None,
                    False,
                ),
                ("definition", "definition", str, "string", False, None, False),
                (
                    "designation",
                    "designation",
                    CodeSystemConceptDesignation,
                    "CodeSystemConceptDesignation",
                    True,
                    None,
                    False,
                ),
                ("display", "display", str, "string", False, None, False),
                (
                    "property",
                    "property",
                    CodeSystemConceptProperty,
                    "CodeSystemConceptProperty",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class CodeSystemConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for the concept.

    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """

    resource_type = "CodeSystemConceptDesignation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.language = None
        """ Human language of the designation.
        Type `str`. """

        self.use = None
        """ Details how this designation would be used.
        Type `Coding` (represented as `dict` in JSON). """

        self.value = None
        """ The text value for this designation.
        Type `str`. """

        super(CodeSystemConceptDesignation, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CodeSystemConceptDesignation, self).elementProperties()
        js.extend(
            [
                ("language", "language", str, "code", False, None, False),
                ("use", "use", coding.Coding, "Coding", False, None, False),
                ("value", "value", str, "string", False, None, True),
            ]
        )
        return js


class CodeSystemConceptProperty(backboneelement.BackboneElement):
    """ Property value for the concept.

    A property value for this concept.
    """

    resource_type = "CodeSystemConceptProperty"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Reference to CodeSystem.property.code.
        Type `str`. """

        self.valueBoolean = None
        """ Value of the property for this concept.
        Type `bool`. """

        self.valueCode = None
        """ Value of the property for this concept.
        Type `str`. """

        self.valueCoding = None
        """ Value of the property for this concept.
        Type `Coding` (represented as `dict` in JSON). """

        self.valueDateTime = None
        """ Value of the property for this concept.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueInteger = None
        """ Value of the property for this concept.
        Type `int`. """

        self.valueString = None
        """ Value of the property for this concept.
        Type `str`. """

        super(CodeSystemConceptProperty, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CodeSystemConceptProperty, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                ("valueBoolean", "valueBoolean", bool, "boolean", False, "value", True),
                ("valueCode", "valueCode", str, "code", False, "value", True),
                (
                    "valueCoding",
                    "valueCoding",
                    coding.Coding,
                    "Coding",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueDateTime",
                    "valueDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "value",
                    True,
                ),
                ("valueInteger", "valueInteger", int, "integer", False, "value", True),
                ("valueString", "valueString", str, "string", False, "value", True),
            ]
        )
        return js


class CodeSystemFilter(backboneelement.BackboneElement):
    """ Filter that can be used in a value set.

    A filter that can be used in a value set compose statement when selecting
    concepts using a filter.
    """

    resource_type = "CodeSystemFilter"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Code that identifies the filter.
        Type `str`. """

        self.description = None
        """ How or why the filter is used.
        Type `str`. """

        self.operator = None
        """ Operators that can be used with filter.
        List of `str` items. """

        self.value = None
        """ What to use for the value.
        Type `str`. """

        super(CodeSystemFilter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CodeSystemFilter, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                ("description", "description", str, "string", False, None, False),
                ("operator", "operator", str, "code", True, None, True),
                ("value", "value", str, "string", False, None, True),
            ]
        )
        return js


class CodeSystemProperty(backboneelement.BackboneElement):
    """ Additional information supplied about each concept.

    A property defines an additional slot through which additional information
    can be provided about a concept.
    """

    resource_type = "CodeSystemProperty"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Identifies the property on the concepts, and when referred to in
        operations.
        Type `str`. """

        self.description = None
        """ Why the property is defined, and/or what it conveys.
        Type `str`. """

        self.type = None
        """ code | Coding | string | integer | boolean | dateTime.
        Type `str`. """

        self.uri = None
        """ Formal identifier for the property.
        Type `str`. """

        super(CodeSystemProperty, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CodeSystemProperty, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                ("description", "description", str, "string", False, None, False),
                ("type", "type", str, "code", False, None, True),
                ("uri", "uri", str, "uri", False, None, False),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + ".coding"]
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + ".contactdetail"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + ".usagecontext"]
