# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical
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

from .. import medicinalproductpharmaceutical
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MedicinalProductPharmaceuticalTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductPharmaceutical", js["resourceType"])
        return medicinalproductpharmaceutical.MedicinalProductPharmaceutical(js)

    def testMedicinalProductPharmaceutical1(self):
        inst = self.instantiate_from("medicinalproductpharmaceutical-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicinalProductPharmaceutical instance"
        )
        self.implMedicinalProductPharmaceutical1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductPharmaceutical", js["resourceType"])
        inst2 = medicinalproductpharmaceutical.MedicinalProductPharmaceutical(js)
        self.implMedicinalProductPharmaceutical1(inst2)

    def implMedicinalProductPharmaceutical1(self, inst):
        self.assertEqual(
            force_bytes(inst.administrableDoseForm.coding[0].code),
            force_bytes("Film-coatedtablet"),
        )
        self.assertEqual(
            force_bytes(inst.administrableDoseForm.coding[0].system),
            force_bytes("http://ema.europa.eu/example/administrabledoseform"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://ema.europa.eu/example/phpididentifiersets"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("{PhPID}"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.routeOfAdministration[0].code.coding[0].code),
            force_bytes("OralUse"),
        )
        self.assertEqual(
            force_bytes(inst.routeOfAdministration[0].code.coding[0].system),
            force_bytes("http://ema.europa.eu/example/routeofadministration"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.unitOfPresentation.coding[0].code), force_bytes("Tablet")
        )
        self.assertEqual(
            force_bytes(inst.unitOfPresentation.coding[0].system),
            force_bytes("http://ema.europa.eu/example/unitofpresentation"),
        )
