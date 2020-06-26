# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SpecimenDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class SpecimenDefinition(domainresource.DomainResource):
    """ Kind of specimen.

    A kind of specimen with associated set of requirements.
    """

    resource_type = "SpecimenDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.collection = None
        """ Specimen collection procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier of a kind of specimen.
        Type `Identifier` (represented as `dict` in JSON). """

        self.patientPreparation = None
        """ Patient preparation for collection.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.timeAspect = None
        """ Time aspect for collection.
        Type `str`. """

        self.typeCollected = None
        """ Kind of material to collect.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.typeTested = None
        """ Specimen in container intended for testing by lab.
        List of `SpecimenDefinitionTypeTested` items (represented as `dict` in JSON). """

        super(SpecimenDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SpecimenDefinition, self).elementProperties()
        js.extend(
            [
                (
                    "collection",
                    "collection",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
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
                    "patientPreparation",
                    "patientPreparation",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("timeAspect", "timeAspect", str, "string", False, None, False),
                (
                    "typeCollected",
                    "typeCollected",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "typeTested",
                    "typeTested",
                    SpecimenDefinitionTypeTested,
                    "SpecimenDefinitionTypeTested",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    """ Specimen in container intended for testing by lab.

    Specimen conditioned in a container as expected by the testing laboratory.
    """

    resource_type = "SpecimenDefinitionTypeTested"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.container = None
        """ The specimen's container.
        Type `SpecimenDefinitionTypeTestedContainer` (represented as `dict` in JSON). """

        self.handling = None
        """ Specimen handling before testing.
        List of `SpecimenDefinitionTypeTestedHandling` items (represented as `dict` in JSON). """

        self.isDerived = None
        """ Primary or secondary specimen.
        Type `bool`. """

        self.preference = None
        """ preferred | alternate.
        Type `str`. """

        self.rejectionCriterion = None
        """ Rejection criterion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.requirement = None
        """ Specimen requirements.
        Type `str`. """

        self.retentionTime = None
        """ Specimen retention time.
        Type `Duration` (represented as `dict` in JSON). """

        self.type = None
        """ Type of intended specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(SpecimenDefinitionTypeTested, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTested, self).elementProperties()
        js.extend(
            [
                (
                    "container",
                    "container",
                    SpecimenDefinitionTypeTestedContainer,
                    "SpecimenDefinitionTypeTestedContainer",
                    False,
                    None,
                    False,
                ),
                (
                    "handling",
                    "handling",
                    SpecimenDefinitionTypeTestedHandling,
                    "SpecimenDefinitionTypeTestedHandling",
                    True,
                    None,
                    False,
                ),
                ("isDerived", "isDerived", bool, "boolean", False, None, False),
                ("preference", "preference", str, "code", False, None, True),
                (
                    "rejectionCriterion",
                    "rejectionCriterion",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("requirement", "requirement", str, "string", False, None, False),
                (
                    "retentionTime",
                    "retentionTime",
                    duration.Duration,
                    "Duration",
                    False,
                    None,
                    False,
                ),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    """ The specimen's container.
    """

    resource_type = "SpecimenDefinitionTypeTestedContainer"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.additive = None
        """ Additive associated with container.
        List of `SpecimenDefinitionTypeTestedContainerAdditive` items (represented as `dict` in JSON). """

        self.cap = None
        """ Color of container cap.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.capacity = None
        """ Container capacity.
        Type `Quantity` (represented as `dict` in JSON). """

        self.description = None
        """ Container description.
        Type `str`. """

        self.material = None
        """ Container material.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.minimumVolumeQuantity = None
        """ Minimum volume.
        Type `Quantity` (represented as `dict` in JSON). """

        self.minimumVolumeString = None
        """ Minimum volume.
        Type `str`. """

        self.preparation = None
        """ Specimen container preparation.
        Type `str`. """

        self.type = None
        """ Kind of container associated with the kind of specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(SpecimenDefinitionTypeTestedContainer, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainer, self).elementProperties()
        js.extend(
            [
                (
                    "additive",
                    "additive",
                    SpecimenDefinitionTypeTestedContainerAdditive,
                    "SpecimenDefinitionTypeTestedContainerAdditive",
                    True,
                    None,
                    False,
                ),
                (
                    "cap",
                    "cap",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "capacity",
                    "capacity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
                (
                    "material",
                    "material",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "minimumVolumeQuantity",
                    "minimumVolumeQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "minimumVolume",
                    False,
                ),
                (
                    "minimumVolumeString",
                    "minimumVolumeString",
                    str,
                    "string",
                    False,
                    "minimumVolume",
                    False,
                ),
                ("preparation", "preparation", str, "string", False, None, False),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    """ Additive associated with container.

    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """

    resource_type = "SpecimenDefinitionTypeTestedContainerAdditive"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.additiveCodeableConcept = None
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.additiveReference = None
        """ Additive associated with container.
        Type `FHIRReference` referencing `['Substance']` (represented as `dict` in JSON). """

        super(SpecimenDefinitionTypeTestedContainerAdditive, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(
            SpecimenDefinitionTypeTestedContainerAdditive, self
        ).elementProperties()
        js.extend(
            [
                (
                    "additiveCodeableConcept",
                    "additiveCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "additive",
                    True,
                ),
                (
                    "additiveReference",
                    "additiveReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "additive",
                    True,
                ),
            ]
        )
        return js


class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    """ Specimen handling before testing.

    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """

    resource_type = "SpecimenDefinitionTypeTestedHandling"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.instruction = None
        """ Preservation instruction.
        Type `str`. """

        self.maxDuration = None
        """ Maximum preservation time.
        Type `Duration` (represented as `dict` in JSON). """

        self.temperatureQualifier = None
        """ Temperature qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.temperatureRange = None
        """ Temperature range.
        Type `Range` (represented as `dict` in JSON). """

        super(SpecimenDefinitionTypeTestedHandling, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedHandling, self).elementProperties()
        js.extend(
            [
                ("instruction", "instruction", str, "string", False, None, False),
                (
                    "maxDuration",
                    "maxDuration",
                    duration.Duration,
                    "Duration",
                    False,
                    None,
                    False,
                ),
                (
                    "temperatureQualifier",
                    "temperatureQualifier",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "temperatureRange",
                    "temperatureRange",
                    range.Range,
                    "Range",
                    False,
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
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + ".duration"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
