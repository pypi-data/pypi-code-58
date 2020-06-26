# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeableConcept
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import element


class CodeableConcept(element.Element):
    """ Concept - reference to a terminology or just  text.

    A concept that may be defined by a formal reference to a terminology or
    ontology or may be provided by text.
    """

    resource_type = "CodeableConcept"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.coding = None
        """ Code defined by a terminology system.
        List of `Coding` items (represented as `dict` in JSON). """

        self.text = None
        """ Plain text representation of the concept.
        Type `str`. """

        super(CodeableConcept, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CodeableConcept, self).elementProperties()
        js.extend(
            [
                ("coding", "coding", coding.Coding, "Coding", True, None, False),
                ("text", "text", str, "string", False, None, False),
            ]
        )
        return js


try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + ".coding"]
