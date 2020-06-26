# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Expression
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


from . import element


class Expression(element.Element):
    """ An expression that can be used to generate a value.

    A expression that is evaluated in a specified context and returns a value.
    The context of use of the expression must specify the context in which the
    expression is evaluated, and how the result of the expression is used.
    """

    resource_type = "Expression"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Natural language description of the condition.
        Type `str`. """

        self.expression = None
        """ Expression in specified language.
        Type `str`. """

        self.language = None
        """ text/cql | text/fhirpath | application/x-fhir-query | etc..
        Type `str`. """

        self.name = None
        """ Short name assigned to expression for reuse.
        Type `str`. """

        self.reference = None
        """ Where the expression is found.
        Type `str`. """

        super(Expression, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Expression, self).elementProperties()
        js.extend(
            [
                ("description", "description", str, "string", False, None, False),
                ("expression", "expression", str, "string", False, None, False),
                ("language", "language", str, "code", False, None, True),
                ("name", "name", str, "id", False, None, False),
                ("reference", "reference", str, "uri", False, None, False),
            ]
        )
        return js
