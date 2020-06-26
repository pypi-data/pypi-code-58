# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentResponse
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import enrollmentresponse
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class EnrollmentResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("EnrollmentResponse", js["resourceType"])
        return enrollmentresponse.EnrollmentResponse(js)

    def testEnrollmentResponse1(self):
        inst = self.instantiate_from("enrollmentresponse-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a EnrollmentResponse instance"
        )
        self.implEnrollmentResponse1(inst)

        js = inst.as_json()
        self.assertEqual("EnrollmentResponse", js["resourceType"])
        inst2 = enrollmentresponse.EnrollmentResponse(js)
        self.implEnrollmentResponse1(inst2)

    def implEnrollmentResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.disposition), force_bytes("Dependant added to policy.")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("ER2500"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.BenefitsInc.com/fhir/enrollmentresponse"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("781234"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the EnrollmentResponse</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
