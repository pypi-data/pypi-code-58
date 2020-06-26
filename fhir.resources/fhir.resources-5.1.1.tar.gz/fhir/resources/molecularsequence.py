# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MolecularSequence
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class MolecularSequence(domainresource.DomainResource):
    """ Information about a biological sequence.

    Raw data describing a biological sequence.
    """

    resource_type = "MolecularSequence"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.coordinateSystem = None
        """ Base number of coordinate system (0 for 0-based numbering or
        coordinates, inclusive start, exclusive end, 1 for 1-based
        numbering, inclusive start, inclusive end).
        Type `int`. """

        self.device = None
        """ The method for sequencing.
        Type `FHIRReference` referencing `['Device']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Unique ID for this particular sequence. This is a FHIR-defined id.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.observedSeq = None
        """ Sequence that was observed.
        Type `str`. """

        self.patient = None
        """ Who and/or what this is about.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.performer = None
        """ Who should be responsible for test result.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.pointer = None
        """ Pointer to next atomic sequence.
        List of `FHIRReference` items referencing `['MolecularSequence']` (represented as `dict` in JSON). """

        self.quality = None
        """ An set of value as quality of sequence.
        List of `MolecularSequenceQuality` items (represented as `dict` in JSON). """

        self.quantity = None
        """ The number of copies of the sequence of interest.  (RNASeq).
        Type `Quantity` (represented as `dict` in JSON). """

        self.readCoverage = None
        """ Average number of reads representing a given nucleotide in the
        reconstructed sequence.
        Type `int`. """

        self.referenceSeq = None
        """ A sequence used as reference.
        Type `MolecularSequenceReferenceSeq` (represented as `dict` in JSON). """

        self.repository = None
        """ External repository which contains detailed report related with
        observedSeq in this resource.
        List of `MolecularSequenceRepository` items (represented as `dict` in JSON). """

        self.specimen = None
        """ Specimen used for sequencing.
        Type `FHIRReference` referencing `['Specimen']` (represented as `dict` in JSON). """

        self.structureVariant = None
        """ Structural variant.
        List of `MolecularSequenceStructureVariant` items (represented as `dict` in JSON). """

        self.type = None
        """ aa | dna | rna.
        Type `str`. """

        self.variant = None
        """ Variant in sequence.
        List of `MolecularSequenceVariant` items (represented as `dict` in JSON). """

        super(MolecularSequence, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequence, self).elementProperties()
        js.extend(
            [
                (
                    "coordinateSystem",
                    "coordinateSystem",
                    int,
                    "integer",
                    False,
                    None,
                    True,
                ),
                (
                    "device",
                    "device",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                ("observedSeq", "observedSeq", str, "string", False, None, False),
                (
                    "patient",
                    "patient",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "performer",
                    "performer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "pointer",
                    "pointer",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "quality",
                    "quality",
                    MolecularSequenceQuality,
                    "MolecularSequenceQuality",
                    True,
                    None,
                    False,
                ),
                (
                    "quantity",
                    "quantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                ("readCoverage", "readCoverage", int, "integer", False, None, False),
                (
                    "referenceSeq",
                    "referenceSeq",
                    MolecularSequenceReferenceSeq,
                    "MolecularSequenceReferenceSeq",
                    False,
                    None,
                    False,
                ),
                (
                    "repository",
                    "repository",
                    MolecularSequenceRepository,
                    "MolecularSequenceRepository",
                    True,
                    None,
                    False,
                ),
                (
                    "specimen",
                    "specimen",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "structureVariant",
                    "structureVariant",
                    MolecularSequenceStructureVariant,
                    "MolecularSequenceStructureVariant",
                    True,
                    None,
                    False,
                ),
                ("type", "type", str, "code", False, None, False),
                (
                    "variant",
                    "variant",
                    MolecularSequenceVariant,
                    "MolecularSequenceVariant",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class MolecularSequenceQuality(backboneelement.BackboneElement):
    """ An set of value as quality of sequence.

    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """

    resource_type = "MolecularSequenceQuality"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.end = None
        """ End position of the sequence.
        Type `int`. """

        self.fScore = None
        """ F-score.
        Type `float`. """

        self.gtFP = None
        """ False positives where the non-REF alleles in the Truth and Query
        Call Sets match.
        Type `float`. """

        self.method = None
        """ Method to get quality.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.precision = None
        """ Precision of comparison.
        Type `float`. """

        self.queryFP = None
        """ False positives.
        Type `float`. """

        self.queryTP = None
        """ True positives from the perspective of the query data.
        Type `float`. """

        self.recall = None
        """ Recall of comparison.
        Type `float`. """

        self.roc = None
        """ Receiver Operator Characteristic (ROC) Curve.
        Type `MolecularSequenceQualityRoc` (represented as `dict` in JSON). """

        self.score = None
        """ Quality score for the comparison.
        Type `Quantity` (represented as `dict` in JSON). """

        self.standardSequence = None
        """ Standard sequence for comparison.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.start = None
        """ Start position of the sequence.
        Type `int`. """

        self.truthFN = None
        """ False negatives.
        Type `float`. """

        self.truthTP = None
        """ True positives from the perspective of the truth data.
        Type `float`. """

        self.type = None
        """ indel | snp | unknown.
        Type `str`. """

        super(MolecularSequenceQuality, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequenceQuality, self).elementProperties()
        js.extend(
            [
                ("end", "end", int, "integer", False, None, False),
                ("fScore", "fScore", float, "decimal", False, None, False),
                ("gtFP", "gtFP", float, "decimal", False, None, False),
                (
                    "method",
                    "method",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("precision", "precision", float, "decimal", False, None, False),
                ("queryFP", "queryFP", float, "decimal", False, None, False),
                ("queryTP", "queryTP", float, "decimal", False, None, False),
                ("recall", "recall", float, "decimal", False, None, False),
                (
                    "roc",
                    "roc",
                    MolecularSequenceQualityRoc,
                    "MolecularSequenceQualityRoc",
                    False,
                    None,
                    False,
                ),
                ("score", "score", quantity.Quantity, "Quantity", False, None, False),
                (
                    "standardSequence",
                    "standardSequence",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("start", "start", int, "integer", False, None, False),
                ("truthFN", "truthFN", float, "decimal", False, None, False),
                ("truthTP", "truthTP", float, "decimal", False, None, False),
                ("type", "type", str, "code", False, None, True),
            ]
        )
        return js


class MolecularSequenceQualityRoc(backboneelement.BackboneElement):
    """ Receiver Operator Characteristic (ROC) Curve.

    Receiver Operator Characteristic (ROC) Curve  to give
    sensitivity/specificity tradeoff.
    """

    resource_type = "MolecularSequenceQualityRoc"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.fMeasure = None
        """ FScore of the GQ score.
        List of `float` items. """

        self.numFN = None
        """ Roc score false negative numbers.
        List of `int` items. """

        self.numFP = None
        """ Roc score false positive numbers.
        List of `int` items. """

        self.numTP = None
        """ Roc score true positive numbers.
        List of `int` items. """

        self.precision = None
        """ Precision of the GQ score.
        List of `float` items. """

        self.score = None
        """ Genotype quality score.
        List of `int` items. """

        self.sensitivity = None
        """ Sensitivity of the GQ score.
        List of `float` items. """

        super(MolecularSequenceQualityRoc, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MolecularSequenceQualityRoc, self).elementProperties()
        js.extend(
            [
                ("fMeasure", "fMeasure", float, "decimal", True, None, False),
                ("numFN", "numFN", int, "integer", True, None, False),
                ("numFP", "numFP", int, "integer", True, None, False),
                ("numTP", "numTP", int, "integer", True, None, False),
                ("precision", "precision", float, "decimal", True, None, False),
                ("score", "score", int, "integer", True, None, False),
                ("sensitivity", "sensitivity", float, "decimal", True, None, False),
            ]
        )
        return js


class MolecularSequenceReferenceSeq(backboneelement.BackboneElement):
    """ A sequence used as reference.

    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """

    resource_type = "MolecularSequenceReferenceSeq"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.chromosome = None
        """ Chromosome containing genetic finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.genomeBuild = None
        """ The Genome Build used for reference, following GRCh build versions
        e.g. 'GRCh 37'.
        Type `str`. """

        self.orientation = None
        """ sense | antisense.
        Type `str`. """

        self.referenceSeqId = None
        """ Reference identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.referenceSeqPointer = None
        """ A pointer to another MolecularSequence entity as reference sequence.
        Type `FHIRReference` referencing `['MolecularSequence']` (represented as `dict` in JSON). """

        self.referenceSeqString = None
        """ A string to represent reference sequence.
        Type `str`. """

        self.strand = None
        """ watson | crick.
        Type `str`. """

        self.windowEnd = None
        """ End position of the window on the reference sequence.
        Type `int`. """

        self.windowStart = None
        """ Start position of the window on the  reference sequence.
        Type `int`. """

        super(MolecularSequenceReferenceSeq, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MolecularSequenceReferenceSeq, self).elementProperties()
        js.extend(
            [
                (
                    "chromosome",
                    "chromosome",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("genomeBuild", "genomeBuild", str, "string", False, None, False),
                ("orientation", "orientation", str, "code", False, None, False),
                (
                    "referenceSeqId",
                    "referenceSeqId",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "referenceSeqPointer",
                    "referenceSeqPointer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "referenceSeqString",
                    "referenceSeqString",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                ("strand", "strand", str, "code", False, None, False),
                ("windowEnd", "windowEnd", int, "integer", False, None, False),
                ("windowStart", "windowStart", int, "integer", False, None, False),
            ]
        )
        return js


class MolecularSequenceRepository(backboneelement.BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.

    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """

    resource_type = "MolecularSequenceRepository"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.datasetId = None
        """ Id of the dataset that used to call for dataset in repository.
        Type `str`. """

        self.name = None
        """ Repository's name.
        Type `str`. """

        self.readsetId = None
        """ Id of the read.
        Type `str`. """

        self.type = None
        """ directlink | openapi | login | oauth | other.
        Type `str`. """

        self.url = None
        """ URI of the repository.
        Type `str`. """

        self.variantsetId = None
        """ Id of the variantset that used to call for variantset in repository.
        Type `str`. """

        super(MolecularSequenceRepository, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MolecularSequenceRepository, self).elementProperties()
        js.extend(
            [
                ("datasetId", "datasetId", str, "string", False, None, False),
                ("name", "name", str, "string", False, None, False),
                ("readsetId", "readsetId", str, "string", False, None, False),
                ("type", "type", str, "code", False, None, True),
                ("url", "url", str, "uri", False, None, False),
                ("variantsetId", "variantsetId", str, "string", False, None, False),
            ]
        )
        return js


class MolecularSequenceStructureVariant(backboneelement.BackboneElement):
    """ Structural variant.

    Information about chromosome structure variation.
    """

    resource_type = "MolecularSequenceStructureVariant"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.exact = None
        """ Does the structural variant have base pair resolution breakpoints?.
        Type `bool`. """

        self.inner = None
        """ Structural variant inner.
        Type `MolecularSequenceStructureVariantInner` (represented as `dict` in JSON). """

        self.length = None
        """ Structural variant length.
        Type `int`. """

        self.outer = None
        """ Structural variant outer.
        Type `MolecularSequenceStructureVariantOuter` (represented as `dict` in JSON). """

        self.variantType = None
        """ Structural variant change type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MolecularSequenceStructureVariant, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariant, self).elementProperties()
        js.extend(
            [
                ("exact", "exact", bool, "boolean", False, None, False),
                (
                    "inner",
                    "inner",
                    MolecularSequenceStructureVariantInner,
                    "MolecularSequenceStructureVariantInner",
                    False,
                    None,
                    False,
                ),
                ("length", "length", int, "integer", False, None, False),
                (
                    "outer",
                    "outer",
                    MolecularSequenceStructureVariantOuter,
                    "MolecularSequenceStructureVariantOuter",
                    False,
                    None,
                    False,
                ),
                (
                    "variantType",
                    "variantType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class MolecularSequenceStructureVariantInner(backboneelement.BackboneElement):
    """ Structural variant inner.
    """

    resource_type = "MolecularSequenceStructureVariantInner"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.end = None
        """ Structural variant inner end.
        Type `int`. """

        self.start = None
        """ Structural variant inner start.
        Type `int`. """

        super(MolecularSequenceStructureVariantInner, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantInner, self).elementProperties()
        js.extend(
            [
                ("end", "end", int, "integer", False, None, False),
                ("start", "start", int, "integer", False, None, False),
            ]
        )
        return js


class MolecularSequenceStructureVariantOuter(backboneelement.BackboneElement):
    """ Structural variant outer.
    """

    resource_type = "MolecularSequenceStructureVariantOuter"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.end = None
        """ Structural variant outer end.
        Type `int`. """

        self.start = None
        """ Structural variant outer start.
        Type `int`. """

        super(MolecularSequenceStructureVariantOuter, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantOuter, self).elementProperties()
        js.extend(
            [
                ("end", "end", int, "integer", False, None, False),
                ("start", "start", int, "integer", False, None, False),
            ]
        )
        return js


class MolecularSequenceVariant(backboneelement.BackboneElement):
    """ Variant in sequence.

    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """

    resource_type = "MolecularSequenceVariant"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.cigar = None
        """ Extended CIGAR string for aligning the sequence with reference
        bases.
        Type `str`. """

        self.end = None
        """ End position of the variant on the reference sequence.
        Type `int`. """

        self.observedAllele = None
        """ Allele that was observed.
        Type `str`. """

        self.referenceAllele = None
        """ Allele in the reference sequence.
        Type `str`. """

        self.start = None
        """ Start position of the variant on the  reference sequence.
        Type `int`. """

        self.variantPointer = None
        """ Pointer to observed variant information.
        Type `FHIRReference` referencing `['Observation']` (represented as `dict` in JSON). """

        super(MolecularSequenceVariant, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequenceVariant, self).elementProperties()
        js.extend(
            [
                ("cigar", "cigar", str, "string", False, None, False),
                ("end", "end", int, "integer", False, None, False),
                ("observedAllele", "observedAllele", str, "string", False, None, False),
                (
                    "referenceAllele",
                    "referenceAllele",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                ("start", "start", int, "integer", False, None, False),
                (
                    "variantPointer",
                    "variantPointer",
                    fhirreference.FHIRReference,
                    "Reference",
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
