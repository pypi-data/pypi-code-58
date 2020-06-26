# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DataElement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class DataElement(domainresource.DomainResource):
    """ Resource data element.

    The formal description of a single piece of information that can be
    gathered and reported.
    """

    resource_type = "DataElement"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.element = None
        """ Definition of element.
        List of `ElementDefinition` items (represented as `dict` in JSON). """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.identifier = None
        """ Additional identifier for the data element.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for data element (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.mapping = None
        """ External specification mapped to.
        List of `DataElementMapping` items (represented as `dict` in JSON). """

        self.name = None
        """ Name for this data element (computer friendly).
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.stringency = None
        """ comparable | fully-specified | equivalent | convertable | scaleable
        | flexible.
        Type `str`. """

        self.title = None
        """ Name for this data element (human friendly).
        Type `str`. """

        self.url = None
        """ Logical URI to reference this data element (globally unique).
        Type `str`. """

        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the data element.
        Type `str`. """

        super(DataElement, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DataElement, self).elementProperties()
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
                ("copyright", "copyright", str, "markdown", False, None, False),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                (
                    "element",
                    "element",
                    elementdefinition.ElementDefinition,
                    "ElementDefinition",
                    True,
                    None,
                    True,
                ),
                ("experimental", "experimental", bool, "boolean", False, None, False),
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
                    "jurisdiction",
                    "jurisdiction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "mapping",
                    "mapping",
                    DataElementMapping,
                    "DataElementMapping",
                    True,
                    None,
                    False,
                ),
                ("name", "name", str, "string", False, None, False),
                ("publisher", "publisher", str, "string", False, None, False),
                ("status", "status", str, "code", False, None, True),
                ("stringency", "stringency", str, "code", False, None, False),
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
                ("version", "version", str, "string", False, None, False),
            ]
        )
        return js


class DataElementMapping(backboneelement.BackboneElement):
    """ External specification mapped to.

    Identifies a specification (other than a terminology) that the elements
    which make up the DataElement have some correspondence with.
    """

    resource_type = "DataElementMapping"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.comment = None
        """ Versions, issues, scope limitations, etc..
        Type `str`. """

        self.identity = None
        """ Internal id when this mapping is used.
        Type `str`. """

        self.name = None
        """ Names what this mapping refers to.
        Type `str`. """

        self.uri = None
        """ Identifies what this mapping refers to.
        Type `str`. """

        super(DataElementMapping, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DataElementMapping, self).elementProperties()
        js.extend(
            [
                ("comment", "comment", str, "string", False, None, False),
                ("identity", "identity", str, "id", False, None, True),
                ("name", "name", str, "string", False, None, False),
                ("uri", "uri", str, "uri", False, None, False),
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
    from . import elementdefinition
except ImportError:
    elementdefinition = sys.modules[__package__ + ".elementdefinition"]
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
