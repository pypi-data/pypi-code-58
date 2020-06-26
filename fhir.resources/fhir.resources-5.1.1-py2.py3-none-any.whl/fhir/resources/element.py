# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


from . import fhirabstractbase


class Element(fhirabstractbase.FHIRAbstractBase):
    """ Base for all elements.

    Base definition for all elements in a resource.
    """

    resource_type = "Element"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.extension = None
        """ Additional content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """

        self.id = None
        """ Unique id for inter-element referencing.
        Type `str`. """

        super(Element, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Element, self).elementProperties()
        from . import extension

        js.extend(
            [
                (
                    "extension",
                    "extension",
                    extension.Extension,
                    "Extension",
                    True,
                    None,
                    False,
                ),
                ("id", "id", str, "string", False, None, False),
            ]
        )
        return js
