#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/CodeableConcept) on 2019-05-14.
#  2019, SMART Health IT.


from . import coding, element


class CodeableConcept(element.Element):
    """ Concept - reference to a terminology or just  text.
    
    A concept that may be defined by a formal reference to a terminology or
    ontology or may be provided by text.
    """

    resource_name = "CodeableConcept"

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
                ("coding", "coding", coding.Coding, True, None, False),
                ("text", "text", str, False, None, False),
            ]
        )
        return js
