# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AllergyIntolerance
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

from .. import allergyintolerance
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class AllergyIntoleranceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("AllergyIntolerance", js["resourceType"])
        return allergyintolerance.AllergyIntolerance(js)

    def testAllergyIntolerance1(self):
        inst = self.instantiate_from("allergyintolerance-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a AllergyIntolerance instance"
        )
        self.implAllergyIntolerance1(inst)

        js = inst.as_json()
        self.assertEqual("AllergyIntolerance", js["resourceType"])
        inst2 = allergyintolerance.AllergyIntolerance(js)
        self.implAllergyIntolerance1(inst2)

    def implAllergyIntolerance1(self, inst):
        self.assertEqual(
            inst.assertedDate.date, FHIRDate("2014-10-09T14:58:00+11:00").date
        )
        self.assertEqual(inst.assertedDate.as_json(), "2014-10-09T14:58:00+11:00")
        self.assertEqual(force_bytes(inst.category[0]), force_bytes("food"))
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("227493005")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display), force_bytes("Cashew nuts")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.criticality), force_bytes("high"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://acme.com/ids/patients/risks"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("49476534"))
        self.assertEqual(inst.lastOccurrence.date, FHIRDate("2012-06").date)
        self.assertEqual(inst.lastOccurrence.as_json(), "2012-06")
        self.assertEqual(
            force_bytes(inst.note[0].text),
            force_bytes(
                "The criticality is high becasue of the observed anaphylactic reaction when challenged with cashew extract."
            ),
        )
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2004").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2004")
        self.assertEqual(
            force_bytes(inst.reaction[0].description),
            force_bytes(
                "Challenge Protocol. Severe reaction to subcutaneous cashew extract. Epinephrine administered"
            ),
        )
        self.assertEqual(
            force_bytes(inst.reaction[0].exposureRoute.coding[0].code),
            force_bytes("34206005"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[0].exposureRoute.coding[0].display),
            force_bytes("Subcutaneous route"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[0].exposureRoute.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[0].manifestation[0].coding[0].code),
            force_bytes("39579001"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[0].manifestation[0].coding[0].display),
            force_bytes("Anaphylactic reaction"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[0].manifestation[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.reaction[0].onset.date, FHIRDate("2012-06-12").date)
        self.assertEqual(inst.reaction[0].onset.as_json(), "2012-06-12")
        self.assertEqual(force_bytes(inst.reaction[0].severity), force_bytes("severe"))
        self.assertEqual(
            force_bytes(inst.reaction[0].substance.coding[0].code),
            force_bytes("1160593"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[0].substance.coding[0].display),
            force_bytes("cashew nut allergenic extract Injectable Product"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[0].substance.coding[0].system),
            force_bytes("http://www.nlm.nih.gov/research/umls/rxnorm"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[1].manifestation[0].coding[0].code),
            force_bytes("64305001"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[1].manifestation[0].coding[0].display),
            force_bytes("Urticaria"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[1].manifestation[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[1].note[0].text),
            force_bytes(
                "The patient reports that the onset of urticaria was within 15 minutes of eating cashews."
            ),
        )
        self.assertEqual(inst.reaction[1].onset.date, FHIRDate("2004").date)
        self.assertEqual(inst.reaction[1].onset.as_json(), "2004")
        self.assertEqual(
            force_bytes(inst.reaction[1].severity), force_bytes("moderate")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("allergy"))
        self.assertEqual(force_bytes(inst.verificationStatus), force_bytes("confirmed"))

    def testAllergyIntolerance2(self):
        inst = self.instantiate_from("allergyintolerance-medication.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a AllergyIntolerance instance"
        )
        self.implAllergyIntolerance2(inst)

        js = inst.as_json()
        self.assertEqual("AllergyIntolerance", js["resourceType"])
        inst2 = allergyintolerance.AllergyIntolerance(js)
        self.implAllergyIntolerance2(inst2)

    def implAllergyIntolerance2(self, inst):
        self.assertEqual(inst.assertedDate.date, FHIRDate("2010-03-01").date)
        self.assertEqual(inst.assertedDate.as_json(), "2010-03-01")
        self.assertEqual(force_bytes(inst.category[0]), force_bytes("medication"))
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("active"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("7980"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display), force_bytes("Penicillin G")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://www.nlm.nih.gov/research/umls/rxnorm"),
        )
        self.assertEqual(force_bytes(inst.criticality), force_bytes("high"))
        self.assertEqual(force_bytes(inst.id), force_bytes("medication"))
        self.assertEqual(
            force_bytes(inst.reaction[0].manifestation[0].coding[0].code),
            force_bytes("247472004"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[0].manifestation[0].coding[0].display),
            force_bytes("Hives"),
        )
        self.assertEqual(
            force_bytes(inst.reaction[0].manifestation[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.verificationStatus), force_bytes("unconfirmed")
        )

    def testAllergyIntolerance3(self):
        inst = self.instantiate_from("allergyintolerance-fishallergy.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a AllergyIntolerance instance"
        )
        self.implAllergyIntolerance3(inst)

        js = inst.as_json()
        self.assertEqual("AllergyIntolerance", js["resourceType"])
        inst2 = allergyintolerance.AllergyIntolerance(js)
        self.implAllergyIntolerance3(inst2)

    def implAllergyIntolerance3(self, inst):
        self.assertEqual(
            inst.assertedDate.date, FHIRDate("2015-08-06T15:37:31-06:00").date
        )
        self.assertEqual(inst.assertedDate.as_json(), "2015-08-06T15:37:31-06:00")
        self.assertEqual(force_bytes(inst.category[0]), force_bytes("food"))
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("227037002")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Fish - dietary (substance)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.code.text),
            force_bytes("Allergic to fresh fish. Tolerates canned fish"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("fishallergy"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://acme.com/ids/patients/risks"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("49476535"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
        self.assertEqual(force_bytes(inst.verificationStatus), force_bytes("confirmed"))
