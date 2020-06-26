# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Signature
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import element


class Signature(element.Element):
    """ A Signature - XML DigSig, JWS, Graphical image of signature, etc..

    A signature along with supporting context. The signature may be a digital
    signature that is cryptographic in nature, or some other signature
    acceptable to the domain. This other signature may be as simple as a
    graphical image representing a hand-written signature, or a signature
    ceremony Different signature approaches have different utilities.
    """

    resource_type = "Signature"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.data = None
        """ The actual signature content (XML DigSig. JWS, picture, etc.).
        Type `str`. """

        self.onBehalfOf = None
        """ The party represented.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'RelatedPerson', 'Patient', 'Device', 'Organization']` (represented as `dict` in JSON). """

        self.sigFormat = None
        """ The technical format of the signature.
        Type `str`. """

        self.targetFormat = None
        """ The technical format of the signed resources.
        Type `str`. """

        self.type = None
        """ Indication of the reason the entity signed the object(s).
        List of `Coding` items (represented as `dict` in JSON). """

        self.when = None
        """ When the signature was created.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.who = None
        """ Who signed.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'RelatedPerson', 'Patient', 'Device', 'Organization']` (represented as `dict` in JSON). """

        super(Signature, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend(
            [
                ("data", "data", str, "base64Binary", False, None, False),
                (
                    "onBehalfOf",
                    "onBehalfOf",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("sigFormat", "sigFormat", str, "code", False, None, False),
                ("targetFormat", "targetFormat", str, "code", False, None, False),
                ("type", "type", coding.Coding, "Coding", True, None, True),
                ("when", "when", fhirdate.FHIRDate, "instant", False, None, True),
                (
                    "who",
                    "who",
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
