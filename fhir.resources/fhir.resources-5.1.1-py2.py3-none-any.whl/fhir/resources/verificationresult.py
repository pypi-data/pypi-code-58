# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VerificationResult
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class VerificationResult(domainresource.DomainResource):
    """ Describes validation requirements, source(s), status and dates for one or
    more elements.
    """

    resource_type = "VerificationResult"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.attestation = None
        """ Information about the entity attesting to information.
        Type `VerificationResultAttestation` (represented as `dict` in JSON). """

        self.failureAction = None
        """ fatal | warn | rec-only | none.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.frequency = None
        """ Frequency of revalidation.
        Type `Timing` (represented as `dict` in JSON). """

        self.lastPerformed = None
        """ The date/time validation was last completed (including failed
        validations).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.need = None
        """ none | initial | periodic.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.nextScheduled = None
        """ The date when target is next validated, if appropriate.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.primarySource = None
        """ Information about the primary source(s) involved in validation.
        List of `VerificationResultPrimarySource` items (represented as `dict` in JSON). """

        self.status = None
        """ attested | validated | in-process | req-revalid | val-fail | reval-
        fail.
        Type `str`. """

        self.statusDate = None
        """ When the validation status was updated.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.target = None
        """ A resource that was validated.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.targetLocation = None
        """ The fhirpath location(s) within the resource that was validated.
        List of `str` items. """

        self.validationProcess = None
        """ The primary process by which the target is validated (edit check;
        value set; primary source; multiple sources; standalone; in
        context).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.validationType = None
        """ nothing | primary | multiple.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.validator = None
        """ Information about the entity validating information.
        List of `VerificationResultValidator` items (represented as `dict` in JSON). """

        super(VerificationResult, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(VerificationResult, self).elementProperties()
        js.extend(
            [
                (
                    "attestation",
                    "attestation",
                    VerificationResultAttestation,
                    "VerificationResultAttestation",
                    False,
                    None,
                    False,
                ),
                (
                    "failureAction",
                    "failureAction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("frequency", "frequency", timing.Timing, "Timing", False, None, False),
                (
                    "lastPerformed",
                    "lastPerformed",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "need",
                    "need",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "nextScheduled",
                    "nextScheduled",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    None,
                    False,
                ),
                (
                    "primarySource",
                    "primarySource",
                    VerificationResultPrimarySource,
                    "VerificationResultPrimarySource",
                    True,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "statusDate",
                    "statusDate",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "target",
                    "target",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("targetLocation", "targetLocation", str, "string", True, None, False),
                (
                    "validationProcess",
                    "validationProcess",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "validationType",
                    "validationType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "validator",
                    "validator",
                    VerificationResultValidator,
                    "VerificationResultValidator",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class VerificationResultAttestation(backboneelement.BackboneElement):
    """ Information about the entity attesting to information.
    """

    resource_type = "VerificationResultAttestation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.communicationMethod = None
        """ The method by which attested information was submitted/retrieved.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.date = None
        """ The date the information was attested to.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.onBehalfOf = None
        """ When the who is asserting on behalf of another (organization or
        individual).
        Type `FHIRReference` referencing `['Organization', 'Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.proxyIdentityCertificate = None
        """ A digital identity certificate associated with the proxy entity
        submitting attested information on behalf of the attestation source.
        Type `str`. """

        self.proxySignature = None
        """ Proxy signature.
        Type `Signature` (represented as `dict` in JSON). """

        self.sourceIdentityCertificate = None
        """ A digital identity certificate associated with the attestation
        source.
        Type `str`. """

        self.sourceSignature = None
        """ Attester signature.
        Type `Signature` (represented as `dict` in JSON). """

        self.who = None
        """ The individual or organization attesting to information.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        super(VerificationResultAttestation, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(VerificationResultAttestation, self).elementProperties()
        js.extend(
            [
                (
                    "communicationMethod",
                    "communicationMethod",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("date", "date", fhirdate.FHIRDate, "date", False, None, False),
                (
                    "onBehalfOf",
                    "onBehalfOf",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "proxyIdentityCertificate",
                    "proxyIdentityCertificate",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "proxySignature",
                    "proxySignature",
                    signature.Signature,
                    "Signature",
                    False,
                    None,
                    False,
                ),
                (
                    "sourceIdentityCertificate",
                    "sourceIdentityCertificate",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "sourceSignature",
                    "sourceSignature",
                    signature.Signature,
                    "Signature",
                    False,
                    None,
                    False,
                ),
                (
                    "who",
                    "who",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class VerificationResultPrimarySource(backboneelement.BackboneElement):
    """ Information about the primary source(s) involved in validation.
    """

    resource_type = "VerificationResultPrimarySource"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.canPushUpdates = None
        """ yes | no | undetermined.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.communicationMethod = None
        """ Method for exchanging information with the primary source.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.pushTypeAvailable = None
        """ specific | any | source.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.type = None
        """ Type of primary source (License Board; Primary Education;
        Continuing Education; Postal Service; Relationship owner;
        Registration Authority; legal source; issuing source; authoritative
        source).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.validationDate = None
        """ When the target was validated against the primary source.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.validationStatus = None
        """ successful | failed | unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.who = None
        """ Reference to the primary source.
        Type `FHIRReference` referencing `['Organization', 'Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        super(VerificationResultPrimarySource, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(VerificationResultPrimarySource, self).elementProperties()
        js.extend(
            [
                (
                    "canPushUpdates",
                    "canPushUpdates",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "communicationMethod",
                    "communicationMethod",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "pushTypeAvailable",
                    "pushTypeAvailable",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "validationDate",
                    "validationDate",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "validationStatus",
                    "validationStatus",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "who",
                    "who",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class VerificationResultValidator(backboneelement.BackboneElement):
    """ Information about the entity validating information.
    """

    resource_type = "VerificationResultValidator"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.attestationSignature = None
        """ Validator signature.
        Type `Signature` (represented as `dict` in JSON). """

        self.identityCertificate = None
        """ A digital identity certificate associated with the validator.
        Type `str`. """

        self.organization = None
        """ Reference to the organization validating information.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        super(VerificationResultValidator, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(VerificationResultValidator, self).elementProperties()
        js.extend(
            [
                (
                    "attestationSignature",
                    "attestationSignature",
                    signature.Signature,
                    "Signature",
                    False,
                    None,
                    False,
                ),
                (
                    "identityCertificate",
                    "identityCertificate",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "organization",
                    "organization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


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
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + ".signature"]
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
