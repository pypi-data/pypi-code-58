# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItem
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import chargeitem
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ChargeItemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ChargeItem", js["resourceType"])
        return chargeitem.ChargeItem(js)

    def testChargeItem1(self):
        inst = self.instantiate_from("chargeitem-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ChargeItem instance")
        self.implChargeItem1(inst)

        js = inst.as_json()
        self.assertEqual("ChargeItem", js["resourceType"])
        inst2 = chargeitem.ChargeItem(js)
        self.implChargeItem1(inst2)

    def implChargeItem1(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("01510"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes(
                "Zusatzpauschale für Beobachtung nach diagnostischer Koronarangiografie"
            ),
        )
        self.assertEqual(
            force_bytes(inst.definition[0]),
            force_bytes(
                "http://www.kbv.de/tools/ebm/html/01520_2904360860826220813632.html"
            ),
        )
        self.assertEqual(
            inst.enteredDate.date, FHIRDate("2017-01-25T23:55:04+01:00").date
        )
        self.assertEqual(inst.enteredDate.as_json(), "2017-01-25T23:55:04+01:00")
        self.assertEqual(inst.factorOverride, 0.8)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.identifier.system),
            force_bytes("http://myHospital.org/ChargeItems"),
        )
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("654321"))
        self.assertEqual(
            force_bytes(inst.note[0].text),
            force_bytes("The code is only applicable for periods longer than 4h"),
        )
        self.assertEqual(
            inst.note[0].time.date, FHIRDate("2017-01-25T23:55:04+01:00").date
        )
        self.assertEqual(inst.note[0].time.as_json(), "2017-01-25T23:55:04+01:00")
        self.assertEqual(
            inst.occurrencePeriod.end.date, FHIRDate("2017-01-25T12:35:00+01:00").date
        )
        self.assertEqual(
            inst.occurrencePeriod.end.as_json(), "2017-01-25T12:35:00+01:00"
        )
        self.assertEqual(
            inst.occurrencePeriod.start.date, FHIRDate("2017-01-25T08:00:00+01:00").date
        )
        self.assertEqual(
            inst.occurrencePeriod.start.as_json(), "2017-01-25T08:00:00+01:00"
        )
        self.assertEqual(
            force_bytes(inst.overrideReason),
            force_bytes(
                "Patient is Cardiologist's golf buddy, so he gets a 20% discount!"
            ),
        )
        self.assertEqual(
            force_bytes(inst.participant[0].role.coding[0].code),
            force_bytes("17561000"),
        )
        self.assertEqual(
            force_bytes(inst.participant[0].role.coding[0].display),
            force_bytes("Cardiologist"),
        )
        self.assertEqual(
            force_bytes(inst.participant[0].role.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.participant[1].role.coding[0].code),
            force_bytes("224542009"),
        )
        self.assertEqual(
            force_bytes(inst.participant[1].role.coding[0].display),
            force_bytes("Coronary Care Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.participant[1].role.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.priceOverride.code), force_bytes("EUR"))
        self.assertEqual(
            force_bytes(inst.priceOverride.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(force_bytes(inst.priceOverride.unit), force_bytes("EUR"))
        self.assertEqual(inst.priceOverride.value, 40)
        self.assertEqual(inst.quantity.value, 1)
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].code), force_bytes("123456")
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].display), force_bytes("DIAG-1")
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/sid/icd-10"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("billable"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Example of ChargeItem Usage in Context of the German EBM Billing code system</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
