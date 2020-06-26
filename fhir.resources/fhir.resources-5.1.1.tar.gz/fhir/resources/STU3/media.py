# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Media
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import domainresource


class Media(domainresource.DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """

    resource_type = "Media"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.basedOn = None
        """ Procedure that caused this media to be created.
        List of `FHIRReference` items referencing `['ProcedureRequest']` (represented as `dict` in JSON). """

        self.bodySite = None
        """ Body part in media.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.content = None
        """ Actual Media - reference or data.
        Type `Attachment` (represented as `dict` in JSON). """

        self.context = None
        """ Encounter / Episode associated with media.
        Type `FHIRReference` referencing `['Encounter'], ['EpisodeOfCare']` (represented as `dict` in JSON). """

        self.device = None
        """ Observing Device.
        Type `FHIRReference` referencing `['Device'], ['DeviceMetric']` (represented as `dict` in JSON). """

        self.duration = None
        """ Length in seconds (audio / video).
        Type `int`. """

        self.frames = None
        """ Number of frames if > 1 (photo).
        Type `int`. """

        self.height = None
        """ Height of the image in pixels (photo/video).
        Type `int`. """

        self.identifier = None
        """ Identifier(s) for the image.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.note = None
        """ Comments made about the media.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.occurrenceDateTime = None
        """ When Media was collected.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.occurrencePeriod = None
        """ When Media was collected.
        Type `Period` (represented as `dict` in JSON). """

        self.operator = None
        """ The person who generated the image.
        Type `FHIRReference` referencing `['Practitioner']` (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Why was event performed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.subject = None
        """ Who/What this Media is a record of.
        Type `FHIRReference` referencing `['Patient'], ['Practitioner'], ['Group'], ['Device'], ['Specimen']` (represented as `dict` in JSON). """

        self.subtype = None
        """ The type of acquisition equipment/process.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.type = None
        """ photo | video | audio.
        Type `str`. """

        self.view = None
        """ Imaging view, e.g. Lateral or Antero-posterior.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.width = None
        """ Width of the image in pixels (photo/video).
        Type `int`. """

        super(Media, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Media, self).elementProperties()
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
                (
                    "bodySite",
                    "bodySite",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "content",
                    "content",
                    attachment.Attachment,
                    "Attachment",
                    False,
                    None,
                    True,
                ),
                (
                    "context",
                    "context",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
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
                ("duration", "duration", int, "unsignedInt", False, None, False),
                ("frames", "frames", int, "positiveInt", False, None, False),
                ("height", "height", int, "positiveInt", False, None, False),
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
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                (
                    "occurrenceDateTime",
                    "occurrenceDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "occurrence",
                    False,
                ),
                (
                    "occurrencePeriod",
                    "occurrencePeriod",
                    period.Period,
                    "Period",
                    False,
                    "occurrence",
                    False,
                ),
                (
                    "operator",
                    "operator",
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
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "subtype",
                    "subtype",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("type", "type", str, "code", False, None, True),
                (
                    "view",
                    "view",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("width", "width", int, "positiveInt", False, None, False),
            ]
        )
        return js


try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + ".annotation"]
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + ".attachment"]
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
