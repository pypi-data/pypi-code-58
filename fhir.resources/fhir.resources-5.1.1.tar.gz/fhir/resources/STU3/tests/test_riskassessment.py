# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RiskAssessment
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

from .. import riskassessment
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class RiskAssessmentTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("RiskAssessment", js["resourceType"])
        return riskassessment.RiskAssessment(js)

    def testRiskAssessment1(self):
        inst = self.instantiate_from("riskassessment-example-population.json")
        self.assertIsNotNone(inst, "Must have instantiated a RiskAssessment instance")
        self.implRiskAssessment1(inst)

        js = inst.as_json()
        self.assertEqual("RiskAssessment", js["resourceType"])
        inst2 = riskassessment.RiskAssessment(js)
        self.implRiskAssessment1(inst2)

    def implRiskAssessment1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("population"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testRiskAssessment2(self):
        inst = self.instantiate_from("riskassessment-example-cardiac.json")
        self.assertIsNotNone(inst, "Must have instantiated a RiskAssessment instance")
        self.implRiskAssessment2(inst)

        js = inst.as_json()
        self.assertEqual("RiskAssessment", js["resourceType"])
        inst2 = riskassessment.RiskAssessment(js)
        self.implRiskAssessment2(inst2)

    def implRiskAssessment2(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("cardiac"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("http://example.org")
        )
        self.assertEqual(force_bytes(inst.identifier.use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier.value), force_bytes("risk-assessment-cardiac")
        )
        self.assertEqual(
            inst.occurrenceDateTime.date, FHIRDate("2014-07-19T16:04:00Z").date
        )
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-07-19T16:04:00Z")
        self.assertEqual(
            force_bytes(inst.prediction[0].outcome.text), force_bytes("Heart Attack")
        )
        self.assertEqual(inst.prediction[0].probabilityDecimal, 0.02)
        self.assertEqual(
            force_bytes(inst.prediction[0].whenRange.high.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[0].whenRange.high.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[0].whenRange.high.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[0].whenRange.high.value, 49)
        self.assertEqual(
            force_bytes(inst.prediction[0].whenRange.low.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[0].whenRange.low.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[0].whenRange.low.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[0].whenRange.low.value, 39)
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))

    def testRiskAssessment3(self):
        inst = self.instantiate_from("riskassessment-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a RiskAssessment instance")
        self.implRiskAssessment3(inst)

        js = inst.as_json()
        self.assertEqual("RiskAssessment", js["resourceType"])
        inst2 = riskassessment.RiskAssessment(js)
        self.implRiskAssessment3(inst2)

    def implRiskAssessment3(self, inst):
        self.assertEqual(
            force_bytes(inst.comment), force_bytes("High degree of certainty")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("genetic"))
        self.assertEqual(
            force_bytes(inst.method.coding[0].code), force_bytes("BRCAPRO")
        )
        self.assertEqual(
            inst.occurrenceDateTime.date, FHIRDate("2006-01-13T23:01:00Z").date
        )
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2006-01-13T23:01:00Z")
        self.assertEqual(
            force_bytes(inst.prediction[0].outcome.text), force_bytes("Breast Cancer")
        )
        self.assertEqual(inst.prediction[0].probabilityDecimal, 0.000168)
        self.assertEqual(
            force_bytes(inst.prediction[0].whenRange.high.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[0].whenRange.high.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[0].whenRange.high.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[0].whenRange.high.value, 53)
        self.assertEqual(
            force_bytes(inst.prediction[1].outcome.text), force_bytes("Breast Cancer")
        )
        self.assertEqual(inst.prediction[1].probabilityDecimal, 0.000368)
        self.assertEqual(
            force_bytes(inst.prediction[1].whenRange.high.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[1].whenRange.high.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[1].whenRange.high.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[1].whenRange.high.value, 57)
        self.assertEqual(
            force_bytes(inst.prediction[1].whenRange.low.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[1].whenRange.low.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[1].whenRange.low.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[1].whenRange.low.value, 54)
        self.assertEqual(
            force_bytes(inst.prediction[2].outcome.text), force_bytes("Breast Cancer")
        )
        self.assertEqual(inst.prediction[2].probabilityDecimal, 0.000594)
        self.assertEqual(
            force_bytes(inst.prediction[2].whenRange.high.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[2].whenRange.high.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[2].whenRange.high.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[2].whenRange.high.value, 62)
        self.assertEqual(
            force_bytes(inst.prediction[2].whenRange.low.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[2].whenRange.low.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[2].whenRange.low.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[2].whenRange.low.value, 58)
        self.assertEqual(
            force_bytes(inst.prediction[3].outcome.text), force_bytes("Breast Cancer")
        )
        self.assertEqual(inst.prediction[3].probabilityDecimal, 0.000838)
        self.assertEqual(
            force_bytes(inst.prediction[3].whenRange.high.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[3].whenRange.high.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[3].whenRange.high.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[3].whenRange.high.value, 67)
        self.assertEqual(
            force_bytes(inst.prediction[3].whenRange.low.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[3].whenRange.low.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[3].whenRange.low.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[3].whenRange.low.value, 63)
        self.assertEqual(
            force_bytes(inst.prediction[4].outcome.text), force_bytes("Breast Cancer")
        )
        self.assertEqual(inst.prediction[4].probabilityDecimal, 0.001089)
        self.assertEqual(
            force_bytes(inst.prediction[4].whenRange.high.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[4].whenRange.high.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[4].whenRange.high.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[4].whenRange.high.value, 72)
        self.assertEqual(
            force_bytes(inst.prediction[4].whenRange.low.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[4].whenRange.low.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[4].whenRange.low.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[4].whenRange.low.value, 68)
        self.assertEqual(
            force_bytes(inst.prediction[5].outcome.text), force_bytes("Breast Cancer")
        )
        self.assertEqual(inst.prediction[5].probabilityDecimal, 0.001327)
        self.assertEqual(
            force_bytes(inst.prediction[5].whenRange.high.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[5].whenRange.high.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[5].whenRange.high.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[5].whenRange.high.value, 77)
        self.assertEqual(
            force_bytes(inst.prediction[5].whenRange.low.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[5].whenRange.low.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[5].whenRange.low.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[5].whenRange.low.value, 73)
        self.assertEqual(
            force_bytes(inst.prediction[6].outcome.text), force_bytes("Breast Cancer")
        )
        self.assertEqual(inst.prediction[6].probabilityDecimal, 0.00153)
        self.assertEqual(
            force_bytes(inst.prediction[6].whenRange.high.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[6].whenRange.high.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[6].whenRange.high.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[6].whenRange.high.value, 82)
        self.assertEqual(
            force_bytes(inst.prediction[6].whenRange.low.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[6].whenRange.low.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[6].whenRange.low.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[6].whenRange.low.value, 78)
        self.assertEqual(
            force_bytes(inst.prediction[7].outcome.text), force_bytes("Breast Cancer")
        )
        self.assertEqual(inst.prediction[7].probabilityDecimal, 0.001663)
        self.assertEqual(
            force_bytes(inst.prediction[7].whenRange.high.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[7].whenRange.high.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[7].whenRange.high.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[7].whenRange.high.value, 88)
        self.assertEqual(
            force_bytes(inst.prediction[7].whenRange.low.code), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.prediction[7].whenRange.low.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[7].whenRange.low.unit), force_bytes("years")
        )
        self.assertEqual(inst.prediction[7].whenRange.low.value, 83)
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testRiskAssessment4(self):
        inst = self.instantiate_from("riskassessment-example-prognosis.json")
        self.assertIsNotNone(inst, "Must have instantiated a RiskAssessment instance")
        self.implRiskAssessment4(inst)

        js = inst.as_json()
        self.assertEqual("RiskAssessment", js["resourceType"])
        inst2 = riskassessment.RiskAssessment(js)
        self.implRiskAssessment4(inst2)

    def implRiskAssessment4(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("prognosis"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2010-11-22").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2010-11-22")
        self.assertEqual(
            force_bytes(inst.prediction[0].outcome.coding[0].code),
            force_bytes("249943000:363698007=72098002,260868000=6934004"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[0].outcome.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[0].outcome.text),
            force_bytes("permanent weakness of the left arm"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[0].qualitativeRisk.coding[0].code),
            force_bytes("moderate"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[0].qualitativeRisk.coding[0].display),
            force_bytes("moderate likelihood"),
        )
        self.assertEqual(
            force_bytes(inst.prediction[0].qualitativeRisk.coding[0].system),
            force_bytes("http://hl7.org/fhir/risk-probability"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
