# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GuidanceResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import domainresource


class GuidanceResponse(domainresource.DomainResource):
    """ The formal response to a guidance request.

    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """

    resource_type = "GuidanceResponse"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.context = None
        """ Encounter or Episode during which the response was returned.
        Type `FHIRReference` referencing `['Encounter'], ['EpisodeOfCare']` (represented as `dict` in JSON). """

        self.dataRequirement = None
        """ Additional required data.
        List of `DataRequirement` items (represented as `dict` in JSON). """

        self.evaluationMessage = None
        """ Messages resulting from the evaluation of the artifact or artifacts.
        List of `FHIRReference` items referencing `['OperationOutcome']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier.
        Type `Identifier` (represented as `dict` in JSON). """

        self.module = None
        """ A reference to a knowledge module.
        Type `FHIRReference` referencing `['ServiceDefinition']` (represented as `dict` in JSON). """

        self.note = None
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.occurrenceDateTime = None
        """ When the guidance response was processed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.outputParameters = None
        """ The output parameters of the evaluation, if any.
        Type `FHIRReference` referencing `['Parameters']` (represented as `dict` in JSON). """

        self.performer = None
        """ Device returning the guidance.
        Type `FHIRReference` referencing `['Device']` (represented as `dict` in JSON). """

        self.reasonCodeableConcept = None
        """ Reason for the response.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Reason for the response.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.requestId = None
        """ The id of the request associated with this response, if any.
        Type `str`. """

        self.result = None
        """ Proposed actions, if any.
        Type `FHIRReference` referencing `['CarePlan'], ['RequestGroup']` (represented as `dict` in JSON). """

        self.status = None
        """ success | data-requested | data-required | in-progress | failure |
        entered-in-error.
        Type `str`. """

        self.subject = None
        """ Patient the request was performed for.
        Type `FHIRReference` referencing `['Patient'], ['Group']` (represented as `dict` in JSON). """

        super(GuidanceResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend(
            [
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
                    "dataRequirement",
                    "dataRequirement",
                    datarequirement.DataRequirement,
                    "DataRequirement",
                    True,
                    None,
                    False,
                ),
                (
                    "evaluationMessage",
                    "evaluationMessage",
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
                    False,
                    None,
                    False,
                ),
                (
                    "module",
                    "module",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
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
                    None,
                    False,
                ),
                (
                    "outputParameters",
                    "outputParameters",
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
                    "reasonCodeableConcept",
                    "reasonCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "reason",
                    False,
                ),
                (
                    "reasonReference",
                    "reasonReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "reason",
                    False,
                ),
                ("requestId", "requestId", str, "id", False, None, False),
                (
                    "result",
                    "result",
                    fhirreference.FHIRReference,
                    "Reference",
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
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + ".datarequirement"]
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
