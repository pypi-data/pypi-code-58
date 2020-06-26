# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Parameters
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

from .. import parameters
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ParametersTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Parameters", js["resourceType"])
        return parameters.Parameters(js)

    def testParameters1(self):
        inst = self.instantiate_from("parameters-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Parameters instance")
        self.implParameters1(inst)

        js = inst.as_json()
        self.assertEqual("Parameters", js["resourceType"])
        inst2 = parameters.Parameters(js)
        self.implParameters1(inst2)

    def implParameters1(self, inst):
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.parameter[0].name), force_bytes("exact"))
        self.assertTrue(inst.parameter[0].valueBoolean)
        self.assertEqual(force_bytes(inst.parameter[1].name), force_bytes("property"))
        self.assertEqual(
            force_bytes(inst.parameter[1].part[0].name), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].part[0].valueCode), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].part[1].name), force_bytes("value")
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].part[1].valueCode), force_bytes("top")
        )
        self.assertEqual(force_bytes(inst.parameter[2].name), force_bytes("patient"))
        self.assertEqual(
            force_bytes(inst.parameter[2].resource.id), force_bytes("example")
        )
