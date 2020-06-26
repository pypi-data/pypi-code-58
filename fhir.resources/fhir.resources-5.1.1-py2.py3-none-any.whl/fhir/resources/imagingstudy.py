# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingStudy
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class ImagingStudy(domainresource.DomainResource):
    """ A set of images produced in single study (one or more series of references
    images).

    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """

    resource_type = "ImagingStudy"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.basedOn = None
        """ Request fulfilled.
        List of `FHIRReference` items referencing `['CarePlan', 'ServiceRequest', 'Appointment', 'AppointmentResponse', 'Task']` (represented as `dict` in JSON). """

        self.description = None
        """ Institution-generated description.
        Type `str`. """

        self.encounter = None
        """ Encounter with which this imaging study is associated.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.endpoint = None
        """ Study access endpoint.
        List of `FHIRReference` items referencing `['Endpoint']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Identifiers for the whole study.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.interpreter = None
        """ Who interpreted images.
        List of `FHIRReference` items referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.location = None
        """ Where ImagingStudy occurred.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.modality = None
        """ All series modality if actual acquisition modalities.
        List of `Coding` items (represented as `dict` in JSON). """

        self.note = None
        """ User-defined comments.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.numberOfInstances = None
        """ Number of Study Related Instances.
        Type `int`. """

        self.numberOfSeries = None
        """ Number of Study Related Series.
        Type `int`. """

        self.procedureCode = None
        """ The performed procedure code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.procedureReference = None
        """ The performed Procedure reference.
        Type `FHIRReference` referencing `['Procedure']` (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Why the study was requested.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why was study performed.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'Media', 'DiagnosticReport', 'DocumentReference']` (represented as `dict` in JSON). """

        self.referrer = None
        """ Referring physician.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.series = None
        """ Each study has one or more series of instances.
        List of `ImagingStudySeries` items (represented as `dict` in JSON). """

        self.started = None
        """ When the study was started.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.status = None
        """ registered | available | cancelled | entered-in-error | unknown.
        Type `str`. """

        self.subject = None
        """ Who or what is the subject of the study.
        Type `FHIRReference` referencing `['Patient', 'Device', 'Group']` (represented as `dict` in JSON). """

        super(ImagingStudy, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImagingStudy, self).elementProperties()
        js.extend(
            [
                (
                    "basedOn",
                    "basedOn",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
                (
                    "encounter",
                    "encounter",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "endpoint",
                    "endpoint",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
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
                (
                    "interpreter",
                    "interpreter",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "location",
                    "location",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("modality", "modality", coding.Coding, "Coding", True, None, False),
                (
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                (
                    "numberOfInstances",
                    "numberOfInstances",
                    int,
                    "unsignedInt",
                    False,
                    None,
                    False,
                ),
                (
                    "numberOfSeries",
                    "numberOfSeries",
                    int,
                    "unsignedInt",
                    False,
                    None,
                    False,
                ),
                (
                    "procedureCode",
                    "procedureCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "procedureReference",
                    "procedureReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "reasonCode",
                    "reasonCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "reasonReference",
                    "reasonReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "referrer",
                    "referrer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "series",
                    "series",
                    ImagingStudySeries,
                    "ImagingStudySeries",
                    True,
                    None,
                    False,
                ),
                (
                    "started",
                    "started",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class ImagingStudySeries(backboneelement.BackboneElement):
    """ Each study has one or more series of instances.

    Each study has one or more series of images or other content.
    """

    resource_type = "ImagingStudySeries"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.bodySite = None
        """ Body part examined.
        Type `Coding` (represented as `dict` in JSON). """

        self.description = None
        """ A short human readable summary of the series.
        Type `str`. """

        self.endpoint = None
        """ Series access endpoint.
        List of `FHIRReference` items referencing `['Endpoint']` (represented as `dict` in JSON). """

        self.instance = None
        """ A single SOP instance from the series.
        List of `ImagingStudySeriesInstance` items (represented as `dict` in JSON). """

        self.laterality = None
        """ Body part laterality.
        Type `Coding` (represented as `dict` in JSON). """

        self.modality = None
        """ The modality of the instances in the series.
        Type `Coding` (represented as `dict` in JSON). """

        self.number = None
        """ Numeric identifier of this series.
        Type `int`. """

        self.numberOfInstances = None
        """ Number of Series Related Instances.
        Type `int`. """

        self.performer = None
        """ Who performed the series.
        List of `ImagingStudySeriesPerformer` items (represented as `dict` in JSON). """

        self.specimen = None
        """ Specimen imaged.
        List of `FHIRReference` items referencing `['Specimen']` (represented as `dict` in JSON). """

        self.started = None
        """ When the series started.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.uid = None
        """ DICOM Series Instance UID for the series.
        Type `str`. """

        super(ImagingStudySeries, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImagingStudySeries, self).elementProperties()
        js.extend(
            [
                ("bodySite", "bodySite", coding.Coding, "Coding", False, None, False),
                ("description", "description", str, "string", False, None, False),
                (
                    "endpoint",
                    "endpoint",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "instance",
                    "instance",
                    ImagingStudySeriesInstance,
                    "ImagingStudySeriesInstance",
                    True,
                    None,
                    False,
                ),
                (
                    "laterality",
                    "laterality",
                    coding.Coding,
                    "Coding",
                    False,
                    None,
                    False,
                ),
                ("modality", "modality", coding.Coding, "Coding", False, None, True),
                ("number", "number", int, "unsignedInt", False, None, False),
                (
                    "numberOfInstances",
                    "numberOfInstances",
                    int,
                    "unsignedInt",
                    False,
                    None,
                    False,
                ),
                (
                    "performer",
                    "performer",
                    ImagingStudySeriesPerformer,
                    "ImagingStudySeriesPerformer",
                    True,
                    None,
                    False,
                ),
                (
                    "specimen",
                    "specimen",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "started",
                    "started",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                ("uid", "uid", str, "id", False, None, True),
            ]
        )
        return js


class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """ A single SOP instance from the series.

    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """

    resource_type = "ImagingStudySeriesInstance"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.number = None
        """ The number of this instance in the series.
        Type `int`. """

        self.sopClass = None
        """ DICOM class type.
        Type `Coding` (represented as `dict` in JSON). """

        self.title = None
        """ Description of instance.
        Type `str`. """

        self.uid = None
        """ DICOM SOP Instance UID.
        Type `str`. """

        super(ImagingStudySeriesInstance, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImagingStudySeriesInstance, self).elementProperties()
        js.extend(
            [
                ("number", "number", int, "unsignedInt", False, None, False),
                ("sopClass", "sopClass", coding.Coding, "Coding", False, None, True),
                ("title", "title", str, "string", False, None, False),
                ("uid", "uid", str, "id", False, None, True),
            ]
        )
        return js


class ImagingStudySeriesPerformer(backboneelement.BackboneElement):
    """ Who performed the series.

    Indicates who or what performed the series and how they were involved.
    """

    resource_type = "ImagingStudySeriesPerformer"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.actor = None
        """ Who performed the series.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization', 'CareTeam', 'Patient', 'Device', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.function = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ImagingStudySeriesPerformer, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImagingStudySeriesPerformer, self).elementProperties()
        js.extend(
            [
                (
                    "actor",
                    "actor",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "function",
                    "function",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + ".annotation"]
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + ".coding"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
