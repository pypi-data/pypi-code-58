# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction
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

from .. import medicinalproductinteraction
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MedicinalProductInteractionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductInteraction", js["resourceType"])
        return medicinalproductinteraction.MedicinalProductInteraction(js)

    def testMedicinalProductInteraction1(self):
        inst = self.instantiate_from("medicinalproductinteraction-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicinalProductInteraction instance"
        )
        self.implMedicinalProductInteraction1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductInteraction", js["resourceType"])
        inst2 = medicinalproductinteraction.MedicinalProductInteraction(js)
        self.implMedicinalProductInteraction1(inst2)

    def implMedicinalProductInteraction1(self, inst):
        self.assertEqual(
            force_bytes(inst.effect.coding[0].code),
            force_bytes("Increasedplasmaconcentrations"),
        )
        self.assertEqual(
            force_bytes(inst.effect.coding[0].system),
            force_bytes("http://ema.europa.eu/example/interactionseffect"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.interactant[0].itemCodeableConcept.coding[0].code),
            force_bytes("ketoconazole"),
        )
        self.assertEqual(
            force_bytes(inst.interactant[0].itemCodeableConcept.coding[0].system),
            force_bytes("http://ema.europa.eu/example/interactant"),
        )
        self.assertEqual(
            force_bytes(inst.interactant[1].itemCodeableConcept.coding[0].code),
            force_bytes("itraconazole"),
        )
        self.assertEqual(
            force_bytes(inst.interactant[1].itemCodeableConcept.coding[0].system),
            force_bytes("http://ema.europa.eu/example/interactant"),
        )
        self.assertEqual(
            force_bytes(inst.management.text),
            force_bytes(
                "Coadministration not recommended in patients receiving concomitant systemic treatment strong inhibitors of both CYP3A4 and P-gp"
            ),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].code),
            force_bytes("StrongInhibitorofCYP3A4"),
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://ema.europa.eu/example/interactionsType"),
        )
