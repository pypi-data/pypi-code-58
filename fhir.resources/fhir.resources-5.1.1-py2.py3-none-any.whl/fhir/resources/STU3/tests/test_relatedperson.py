# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedPerson
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

from .. import relatedperson
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class RelatedPersonTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("RelatedPerson", js["resourceType"])
        return relatedperson.RelatedPerson(js)

    def testRelatedPerson1(self):
        inst = self.instantiate_from("relatedperson-example-peter.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson1(inst)

        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson1(inst2)

    def implRelatedPerson1(self, inst):
        self.assertEqual(
            force_bytes(inst.address[0].city), force_bytes("PleasantVille")
        )
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("534 Erewhon St")
        )
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("3999"))
        self.assertEqual(force_bytes(inst.address[0].state), force_bytes("Vic"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("home"))
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("peter"))
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Chalmers"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Peter"))
        self.assertEqual(force_bytes(inst.name[0].given[1]), force_bytes("James"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(inst.period.start.date, FHIRDate("2012-03-11").date)
        self.assertEqual(inst.period.start.as_json(), "2012-03-11")
        self.assertEqual(
            force_bytes(inst.photo[0].contentType), force_bytes("image/jpeg")
        )
        self.assertEqual(force_bytes(inst.photo[0].url), force_bytes("Binary/f012"))
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].code), force_bytes("C")
        )
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].system),
            force_bytes("http://hl7.org/fhir/v2/0131"),
        )
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value), force_bytes("(03) 5555 6473")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testRelatedPerson2(self):
        inst = self.instantiate_from("relatedperson-example-f001-sarah.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson2(inst)

        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson2(inst2)

    def implRelatedPerson2(self, inst):
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f001"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:2.16.840.1.113883.2.4.6.3"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].type.text), force_bytes("BSN"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Abels"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Sarah"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("usual"))
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].code), force_bytes("SIGOTHR")
        )
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/RoleCode"),
        )
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("mobile"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("0690383372"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("home"))
        self.assertEqual(
            force_bytes(inst.telecom[1].value), force_bytes("s.abels@kpn.nl")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testRelatedPerson3(self):
        inst = self.instantiate_from("relatedperson-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson3(inst)

        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson3(inst2)

    def implRelatedPerson3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Paris"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("FRA"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]),
            force_bytes("43, Place du Marché Sainte Catherine"),
        )
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("75004"))
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("benedicte"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:oid:1.2.250.1.61")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.text), force_bytes("INSEE")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("272117510400399")
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("du Marché"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Bénédicte"))
        self.assertEqual(
            force_bytes(inst.photo[0].contentType), force_bytes("image/jpeg")
        )
        self.assertEqual(force_bytes(inst.photo[0].url), force_bytes("Binary/f016"))
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].code), force_bytes("N")
        )
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].system),
            force_bytes("http://hl7.org/fhir/v2/0131"),
        )
        self.assertEqual(
            force_bytes(inst.relationship.coding[1].code), force_bytes("WIFE")
        )
        self.assertEqual(
            force_bytes(inst.relationship.coding[1].system),
            force_bytes("http://hl7.org/fhir/v3/RoleCode"),
        )
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value), force_bytes("+33 (237) 998327")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testRelatedPerson4(self):
        inst = self.instantiate_from("relatedperson-example-f002-ariadne.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson4(inst)

        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson4(inst2)

    def implRelatedPerson4(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("1963").date)
        self.assertEqual(inst.birthDate.as_json(), "1963")
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f002"))
        self.assertEqual(
            force_bytes(inst.name[0].text), force_bytes("Ariadne Bor-Jansma")
        )
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("usual"))
        self.assertEqual(inst.period.start.date, FHIRDate("1975").date)
        self.assertEqual(inst.period.start.as_json(), "1975")
        self.assertEqual(
            force_bytes(inst.photo[0].contentType), force_bytes("image/jpeg")
        )
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].code), force_bytes("SIGOTHR")
        )
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/RoleCode"),
        )
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("home"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value), force_bytes("+31201234567")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
