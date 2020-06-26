# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Condition
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

from .. import condition
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ConditionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Condition", js["resourceType"])
        return condition.Condition(js)

    def testCondition1(self):
        inst = self.instantiate_from("condition-example-f003-abscess.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition1(inst)

        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition1(inst2)

    def implCondition1(self, inst):
        self.assertEqual(inst.assertedDate.date, FHIRDate("2012-02-20").date)
        self.assertEqual(inst.assertedDate.as_json(), "2012-02-20")
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].code), force_bytes("280193007")
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].display),
            force_bytes("Entire retropharyngeal area"),
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("439401001")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display), force_bytes("diagnosis")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("active"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("18099001"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Retropharyngeal abscess"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.evidence[0].code[0].coding[0].code),
            force_bytes("169068008"),
        )
        self.assertEqual(
            force_bytes(inst.evidence[0].code[0].coding[0].display),
            force_bytes("CT of neck"),
        )
        self.assertEqual(
            force_bytes(inst.evidence[0].code[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f003"))
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2012-02-27").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2012-02-27")
        self.assertEqual(
            force_bytes(inst.severity.coding[0].code), force_bytes("371923003")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].display),
            force_bytes("Mild to moderate"),
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.verificationStatus), force_bytes("confirmed"))

    def testCondition2(self):
        inst = self.instantiate_from("condition-example-f203-sepsis.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition2(inst)

        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition2(inst2)

    def implCondition2(self, inst):
        self.assertEqual(inst.assertedDate.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.assertedDate.as_json(), "2013-03-11")
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].code), force_bytes("281158006")
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].display),
            force_bytes("Pulmonary vascular structure"),
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("55607006")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display), force_bytes("Problem")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[1].code),
            force_bytes("problem-list-item"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[1].system),
            force_bytes("http://hl7.org/fhir/condition-category"),
        )
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("active"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("10001005"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display), force_bytes("Bacterial sepsis")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f203"))
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2013-03-08").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2013-03-08")
        self.assertEqual(
            force_bytes(inst.severity.coding[0].code), force_bytes("371924009")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].display),
            force_bytes("Moderate to severe"),
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.verificationStatus), force_bytes("confirmed"))

    def testCondition3(self):
        inst = self.instantiate_from("condition-example-stroke.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition3(inst)

        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition3(inst2)

    def implCondition3(self, inst):
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code),
            force_bytes("encounter-diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display),
            force_bytes("Encounter Diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/condition-category"),
        )
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("422504002")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Ischemic stroke (disorder)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Stroke"))
        self.assertEqual(force_bytes(inst.id), force_bytes("stroke"))
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2010-07-18").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2010-07-18")
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Ischemic stroke, July 18, 2010</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.verificationStatus), force_bytes("confirmed"))

    def testCondition4(self):
        inst = self.instantiate_from("condition-example-family-history.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition4(inst)

        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition4(inst2)

    def implCondition4(self, inst):
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code),
            force_bytes("problem-list-item"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display),
            force_bytes("Problem List Item"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/condition-category"),
        )
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("312824007")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Family history of cancer of colon"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("family-history"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Family history of cancer of colon</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCondition5(self):
        inst = self.instantiate_from("condition-example-f002-lung.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition5(inst)

        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition5(inst2)

    def implCondition5(self, inst):
        self.assertEqual(inst.assertedDate.date, FHIRDate("2012-06-03").date)
        self.assertEqual(inst.assertedDate.as_json(), "2012-06-03")
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].code), force_bytes("51185008")
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].display), force_bytes("Thorax")
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("439401001")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display), force_bytes("diagnosis")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("254637007")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("NSCLC - Non-small cell lung cancer"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.evidence[0].code[0].coding[0].code),
            force_bytes("169069000"),
        )
        self.assertEqual(
            force_bytes(inst.evidence[0].code[0].coding[0].display),
            force_bytes("CT of thorax"),
        )
        self.assertEqual(
            force_bytes(inst.evidence[0].code[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f002"))
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2011-05-05").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2011-05-05")
        self.assertEqual(
            force_bytes(inst.severity.coding[0].code), force_bytes("24484000")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].display), force_bytes("Severe")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.stage.summary.coding[0].code), force_bytes("258219007")
        )
        self.assertEqual(
            force_bytes(inst.stage.summary.coding[0].display), force_bytes("stage II")
        )
        self.assertEqual(
            force_bytes(inst.stage.summary.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.verificationStatus), force_bytes("confirmed"))

    def testCondition6(self):
        inst = self.instantiate_from("condition-example-f205-infection.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition6(inst)

        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition6(inst2)

    def implCondition6(self, inst):
        self.assertEqual(inst.assertedDate.date, FHIRDate("2013-04-04").date)
        self.assertEqual(inst.assertedDate.as_json(), "2013-04-04")
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("active"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("87628006"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Bacterial infectious disease"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f205"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.verificationStatus), force_bytes("differential")
        )

    def testCondition7(self):
        inst = self.instantiate_from("condition-example-f204-renal.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition7(inst)

        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition7(inst2)

    def implCondition7(self, inst):
        self.assertEqual(inst.abatementDateTime.date, FHIRDate("2013-03-20").date)
        self.assertEqual(inst.abatementDateTime.as_json(), "2013-03-20")
        self.assertEqual(inst.assertedDate.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.assertedDate.as_json(), "2013-03-11")
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].code), force_bytes("181414000")
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].display), force_bytes("Kidney")
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("55607006")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display), force_bytes("Problem")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[1].code),
            force_bytes("problem-list-item"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[1].system),
            force_bytes("http://hl7.org/fhir/condition-category"),
        )
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("active"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("36225005"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Acute renal insufficiency specified as due to procedure"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f204"))
        self.assertEqual(
            force_bytes(inst.note[0].text), force_bytes("The patient is anuric.")
        )
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2013-03-11")
        self.assertEqual(
            force_bytes(inst.severity.coding[0].code), force_bytes("24484000")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].display), force_bytes("Severe")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.stage.summary.coding[0].code), force_bytes("14803004")
        )
        self.assertEqual(
            force_bytes(inst.stage.summary.coding[0].display), force_bytes("Temporary")
        )
        self.assertEqual(
            force_bytes(inst.stage.summary.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.verificationStatus), force_bytes("differential")
        )

    def testCondition8(self):
        inst = self.instantiate_from("condition-example2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition8(inst)

        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition8(inst2)

    def implCondition8(self, inst):
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code),
            force_bytes("problem-list-item"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display),
            force_bytes("Problem List Item"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/condition-category"),
        )
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("active"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Asthma"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example2"))
        self.assertEqual(
            force_bytes(inst.onsetString), force_bytes("approximately November 2012")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].code), force_bytes("255604002")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].display), force_bytes("Mild")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Mild Asthma (Date: 12-Nov 2012)</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.verificationStatus), force_bytes("confirmed"))

    def testCondition9(self):
        inst = self.instantiate_from("condition-example-f202-malignancy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition9(inst)

        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition9(inst2)

    def implCondition9(self, inst):
        self.assertEqual(force_bytes(inst.abatementAge.code), force_bytes("a"))
        self.assertEqual(
            force_bytes(inst.abatementAge.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.abatementAge.unit), force_bytes("years"))
        self.assertEqual(inst.abatementAge.value, 54)
        self.assertEqual(inst.assertedDate.date, FHIRDate("2012-12-01").date)
        self.assertEqual(inst.assertedDate.as_json(), "2012-12-01")
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].code), force_bytes("361355005")
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].display),
            force_bytes("Entire head and neck"),
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code),
            force_bytes("encounter-diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/condition-category"),
        )
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("resolved"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("363346000")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Malignant neoplastic disease"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f202"))
        self.assertEqual(force_bytes(inst.meta.security[0].code), force_bytes("TBOO"))
        self.assertEqual(
            force_bytes(inst.meta.security[0].display), force_bytes("taboo")
        )
        self.assertEqual(
            force_bytes(inst.meta.security[0].system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(force_bytes(inst.onsetAge.code), force_bytes("a"))
        self.assertEqual(
            force_bytes(inst.onsetAge.system), force_bytes("http://unitsofmeasure.org")
        )
        self.assertEqual(force_bytes(inst.onsetAge.unit), force_bytes("years"))
        self.assertEqual(inst.onsetAge.value, 52)
        self.assertEqual(
            force_bytes(inst.severity.coding[0].code), force_bytes("24484000")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].display), force_bytes("Severe")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.verificationStatus), force_bytes("confirmed"))

    def testCondition10(self):
        inst = self.instantiate_from("condition-example-f201-fever.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition10(inst)

        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition10(inst2)

    def implCondition10(self, inst):
        self.assertEqual(
            force_bytes(inst.abatementString), force_bytes("around April 9, 2013")
        )
        self.assertEqual(inst.assertedDate.date, FHIRDate("2013-04-04").date)
        self.assertEqual(inst.assertedDate.as_json(), "2013-04-04")
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].code), force_bytes("38266002")
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].display),
            force_bytes("Entire body as a whole"),
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("55607006")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display), force_bytes("Problem")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[1].code),
            force_bytes("problem-list-item"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[1].system),
            force_bytes("http://hl7.org/fhir/condition-category"),
        )
        self.assertEqual(force_bytes(inst.clinicalStatus), force_bytes("resolved"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("386661006")
        )
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Fever"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.evidence[0].code[0].coding[0].code),
            force_bytes("258710007"),
        )
        self.assertEqual(
            force_bytes(inst.evidence[0].code[0].coding[0].display),
            force_bytes("degrees C"),
        )
        self.assertEqual(
            force_bytes(inst.evidence[0].code[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f201"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2013-04-02").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2013-04-02")
        self.assertEqual(
            force_bytes(inst.severity.coding[0].code), force_bytes("255604002")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].display), force_bytes("Mild")
        )
        self.assertEqual(
            force_bytes(inst.severity.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.verificationStatus), force_bytes("confirmed"))
