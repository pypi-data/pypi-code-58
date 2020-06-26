# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIndication
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

from .. import medicinalproductindication
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MedicinalProductIndicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductIndication", js["resourceType"])
        return medicinalproductindication.MedicinalProductIndication(js)

    def testMedicinalProductIndication1(self):
        inst = self.instantiate_from("medicinalproductindication-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicinalProductIndication instance"
        )
        self.implMedicinalProductIndication1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductIndication", js["resourceType"])
        inst2 = medicinalproductindication.MedicinalProductIndication(js)
        self.implMedicinalProductIndication1(inst2)

    def implMedicinalProductIndication1(self, inst):
        self.assertEqual(
            force_bytes(inst.comorbidity[0].coding[0].code), force_bytes("Hipsurgery")
        )
        self.assertEqual(
            force_bytes(inst.comorbidity[0].coding[0].system),
            force_bytes("http://ema.europa.eu/example/comorbidity"),
        )
        self.assertEqual(
            force_bytes(inst.diseaseSymptomProcedure.coding[0].code),
            force_bytes("Venousthromboembolismprophylaxis"),
        )
        self.assertEqual(
            force_bytes(inst.diseaseSymptomProcedure.coding[0].system),
            force_bytes(
                "http://ema.europa.eu/example/indicationasdisease-symptom-procedure"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.intendedEffect.coding[0].code), force_bytes("PRYLX")
        )
        self.assertEqual(
            force_bytes(inst.intendedEffect.coding[0].system),
            force_bytes("http://ema.europa.eu/example/intendedeffect"),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.population[0].ageRange.low.unit), force_bytes("a")
        )
        self.assertEqual(inst.population[0].ageRange.low.value, 18)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
