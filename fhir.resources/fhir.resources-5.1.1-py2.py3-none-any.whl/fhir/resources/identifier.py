# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Identifier
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import element


class Identifier(element.Element):
    """ An identifier intended for computation.

    An identifier - identifies some entity uniquely and unambiguously.
    Typically this is used for business identifiers.
    """

    resource_type = "Identifier"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.assigner = None
        """ Organization that issued id (may be just text).
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.period = None
        """ Time period when id is/was valid for use.
        Type `Period` (represented as `dict` in JSON). """

        self.system = None
        """ The namespace for the identifier value.
        Type `str`. """

        self.type = None
        """ Description of identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.use = None
        """ usual | official | temp | secondary | old (If known).
        Type `str`. """

        self.value = None
        """ The value that is unique.
        Type `str`. """

        super(Identifier, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Identifier, self).elementProperties()
        js.extend(
            [
                (
                    "assigner",
                    "assigner",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                ("system", "system", str, "uri", False, None, False),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("use", "use", str, "code", False, None, False),
                ("value", "value", str, "string", False, None, False),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
