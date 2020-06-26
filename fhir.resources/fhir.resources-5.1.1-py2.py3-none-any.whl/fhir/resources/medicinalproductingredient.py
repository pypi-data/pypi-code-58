# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class MedicinalProductIngredient(domainresource.DomainResource):
    """ An ingredient of a manufactured item or pharmaceutical product.
    """

    resource_type = "MedicinalProductIngredient"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.allergenicIndicator = None
        """ If the ingredient is a known or suspected allergen.
        Type `bool`. """

        self.identifier = None
        """ Identifier for the ingredient.
        Type `Identifier` (represented as `dict` in JSON). """

        self.manufacturer = None
        """ Manufacturer of this Ingredient.
        List of `FHIRReference` items referencing `['Organization']` (represented as `dict` in JSON). """

        self.role = None
        """ Ingredient role e.g. Active ingredient, excipient.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.specifiedSubstance = None
        """ A specified substance that comprises this ingredient.
        List of `MedicinalProductIngredientSpecifiedSubstance` items (represented as `dict` in JSON). """

        self.substance = None
        """ The ingredient substance.
        Type `MedicinalProductIngredientSubstance` (represented as `dict` in JSON). """

        super(MedicinalProductIngredient, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicinalProductIngredient, self).elementProperties()
        js.extend(
            [
                (
                    "allergenicIndicator",
                    "allergenicIndicator",
                    bool,
                    "boolean",
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
                    "manufacturer",
                    "manufacturer",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "role",
                    "role",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "specifiedSubstance",
                    "specifiedSubstance",
                    MedicinalProductIngredientSpecifiedSubstance,
                    "MedicinalProductIngredientSpecifiedSubstance",
                    True,
                    None,
                    False,
                ),
                (
                    "substance",
                    "substance",
                    MedicinalProductIngredientSubstance,
                    "MedicinalProductIngredientSubstance",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class MedicinalProductIngredientSpecifiedSubstance(backboneelement.BackboneElement):
    """ A specified substance that comprises this ingredient.
    """

    resource_type = "MedicinalProductIngredientSpecifiedSubstance"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ The specified substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.confidentiality = None
        """ Confidentiality level of the specified substance as the ingredient.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.group = None
        """ The group of specified substance, e.g. group 1 to 4.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.strength = None
        """ Quantity of the substance or specified substance present in the
        manufactured item or pharmaceutical product.
        List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items (represented as `dict` in JSON). """

        super(MedicinalProductIngredientSpecifiedSubstance, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(
            MedicinalProductIngredientSpecifiedSubstance, self
        ).elementProperties()
        js.extend(
            [
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "confidentiality",
                    "confidentiality",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "group",
                    "group",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "strength",
                    "strength",
                    MedicinalProductIngredientSpecifiedSubstanceStrength,
                    "MedicinalProductIngredientSpecifiedSubstanceStrength",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class MedicinalProductIngredientSpecifiedSubstanceStrength(
    backboneelement.BackboneElement
):
    """ Quantity of the substance or specified substance present in the
    manufactured item or pharmaceutical product.
    """

    resource_type = "MedicinalProductIngredientSpecifiedSubstanceStrength"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.concentration = None
        """ The strength per unitary volume (or mass).
        Type `Ratio` (represented as `dict` in JSON). """

        self.concentrationLowLimit = None
        """ A lower limit for the strength per unitary volume (or mass), for
        when there is a range. The concentration attribute then becomes the
        upper limit.
        Type `Ratio` (represented as `dict` in JSON). """

        self.country = None
        """ The country or countries for which the strength range applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.measurementPoint = None
        """ For when strength is measured at a particular point or distance.
        Type `str`. """

        self.presentation = None
        """ The quantity of substance in the unit of presentation, or in the
        volume (or mass) of the single pharmaceutical product or
        manufactured item.
        Type `Ratio` (represented as `dict` in JSON). """

        self.presentationLowLimit = None
        """ A lower limit for the quantity of substance in the unit of
        presentation. For use when there is a range of strengths, this is
        the lower limit, with the presentation attribute becoming the upper
        limit.
        Type `Ratio` (represented as `dict` in JSON). """

        self.referenceStrength = None
        """ Strength expressed in terms of a reference substance.
        List of `MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength` items (represented as `dict` in JSON). """

        super(MedicinalProductIngredientSpecifiedSubstanceStrength, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(
            MedicinalProductIngredientSpecifiedSubstanceStrength, self
        ).elementProperties()
        js.extend(
            [
                (
                    "concentration",
                    "concentration",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    None,
                    False,
                ),
                (
                    "concentrationLowLimit",
                    "concentrationLowLimit",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    None,
                    False,
                ),
                (
                    "country",
                    "country",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "measurementPoint",
                    "measurementPoint",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "presentation",
                    "presentation",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    None,
                    True,
                ),
                (
                    "presentationLowLimit",
                    "presentationLowLimit",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    None,
                    False,
                ),
                (
                    "referenceStrength",
                    "referenceStrength",
                    MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength,
                    "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(
    backboneelement.BackboneElement
):
    """ Strength expressed in terms of a reference substance.
    """

    resource_type = (
        "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength"
    )

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.country = None
        """ The country or countries for which the strength range applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.measurementPoint = None
        """ For when strength is measured at a particular point or distance.
        Type `str`. """

        self.strength = None
        """ Strength expressed in terms of a reference substance.
        Type `Ratio` (represented as `dict` in JSON). """

        self.strengthLowLimit = None
        """ Strength expressed in terms of a reference substance.
        Type `Ratio` (represented as `dict` in JSON). """

        self.substance = None
        """ Relevant reference substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(
            MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self
        ).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(
            MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self
        ).elementProperties()
        js.extend(
            [
                (
                    "country",
                    "country",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "measurementPoint",
                    "measurementPoint",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                ("strength", "strength", ratio.Ratio, "Ratio", False, None, True),
                (
                    "strengthLowLimit",
                    "strengthLowLimit",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    None,
                    False,
                ),
                (
                    "substance",
                    "substance",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class MedicinalProductIngredientSubstance(backboneelement.BackboneElement):
    """ The ingredient substance.
    """

    resource_type = "MedicinalProductIngredientSubstance"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ The ingredient substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.strength = None
        """ Quantity of the substance or specified substance present in the
        manufactured item or pharmaceutical product.
        List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items (represented as `dict` in JSON). """

        super(MedicinalProductIngredientSubstance, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicinalProductIngredientSubstance, self).elementProperties()
        js.extend(
            [
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "strength",
                    "strength",
                    MedicinalProductIngredientSpecifiedSubstanceStrength,
                    "MedicinalProductIngredientSpecifiedSubstanceStrength",
                    True,
                    None,
                    False,
                ),
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + ".ratio"]
