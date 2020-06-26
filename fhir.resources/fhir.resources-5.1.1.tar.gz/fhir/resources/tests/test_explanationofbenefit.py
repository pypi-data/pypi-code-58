# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit
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

from .. import explanationofbenefit
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ExplanationOfBenefitTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ExplanationOfBenefit", js["resourceType"])
        return explanationofbenefit.ExplanationOfBenefit(js)

    def testExplanationOfBenefit1(self):
        inst = self.instantiate_from("explanationofbenefit-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a ExplanationOfBenefit instance"
        )
        self.implExplanationOfBenefit1(inst)

        js = inst.as_json()
        self.assertEqual("ExplanationOfBenefit", js["resourceType"])
        inst2 = explanationofbenefit.ExplanationOfBenefit(js)
        self.implExplanationOfBenefit1(inst2)

    def implExplanationOfBenefit1(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.disposition), force_bytes("Claim settled as per contract.")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("EB3500"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.BenefitsInc.com/fhir/explanationofbenefit"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("987654321")
        )
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 120.0)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[1].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.item[0].adjudication[1].value, 0.8)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[2].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].adjudication[2].amount.value, 96.0)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[2].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[0].careTeamSequence[0], 1)
        self.assertEqual(force_bytes(inst.item[0].net.currency), force_bytes("USD"))
        self.assertEqual(inst.item[0].net.value, 135.57)
        self.assertEqual(
            force_bytes(inst.item[0].productOrService.coding[0].code),
            force_bytes("1205"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].productOrService.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-USCLS"),
        )
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.item[0].unitPrice.currency), force_bytes("USD")
        )
        self.assertEqual(inst.item[0].unitPrice.value, 135.57)
        self.assertEqual(
            force_bytes(inst.item[1].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[1].adjudication[0].amount.value, 180.0)
        self.assertEqual(
            force_bytes(inst.item[1].adjudication[0].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[1].careTeamSequence[0], 1)
        self.assertEqual(
            force_bytes(inst.item[1].detail[0].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[1].detail[0].adjudication[0].amount.value, 180.0)
        self.assertEqual(
            force_bytes(inst.item[1].detail[0].adjudication[0].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.item[1].detail[0].net.currency), force_bytes("USD")
        )
        self.assertEqual(inst.item[1].detail[0].net.value, 200.0)
        self.assertEqual(
            force_bytes(inst.item[1].detail[0].productOrService.coding[0].code),
            force_bytes("group"),
        )
        self.assertEqual(inst.item[1].detail[0].sequence, 1)
        self.assertEqual(
            force_bytes(
                inst.item[1].detail[0].subDetail[0].adjudication[0].amount.currency
            ),
            force_bytes("USD"),
        )
        self.assertEqual(
            inst.item[1].detail[0].subDetail[0].adjudication[0].amount.value, 200.0
        )
        self.assertEqual(
            force_bytes(
                inst.item[1]
                .detail[0]
                .subDetail[0]
                .adjudication[0]
                .category.coding[0]
                .code
            ),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[1]
                .detail[0]
                .subDetail[0]
                .adjudication[1]
                .category.coding[0]
                .code
            ),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.item[1].detail[0].subDetail[0].adjudication[1].value, 0.9)
        self.assertEqual(
            force_bytes(
                inst.item[1].detail[0].subDetail[0].adjudication[2].amount.currency
            ),
            force_bytes("USD"),
        )
        self.assertEqual(
            inst.item[1].detail[0].subDetail[0].adjudication[2].amount.value, 180.0
        )
        self.assertEqual(
            force_bytes(
                inst.item[1]
                .detail[0]
                .subDetail[0]
                .adjudication[2]
                .category.coding[0]
                .code
            ),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.item[1].detail[0].subDetail[0].net.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[1].detail[0].subDetail[0].net.value, 200.0)
        self.assertEqual(
            force_bytes(
                inst.item[1].detail[0].subDetail[0].productOrService.coding[0].code
            ),
            force_bytes("1205"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[1].detail[0].subDetail[0].productOrService.coding[0].system
            ),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-USCLS"),
        )
        self.assertEqual(inst.item[1].detail[0].subDetail[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[1].detail[0].subDetail[0].unitPrice.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[1].detail[0].subDetail[0].unitPrice.value, 200.0)
        self.assertEqual(force_bytes(inst.item[1].net.currency), force_bytes("USD"))
        self.assertEqual(inst.item[1].net.value, 200.0)
        self.assertEqual(
            force_bytes(inst.item[1].productOrService.coding[0].code),
            force_bytes("group"),
        )
        self.assertEqual(inst.item[1].sequence, 2)
        self.assertEqual(inst.item[1].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[1].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("complete"))
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/payeetype"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the ExplanationOfBenefit</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.total[0].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[0].amount.value, 135.57)
        self.assertEqual(
            force_bytes(inst.total[0].category.coding[0].code), force_bytes("submitted")
        )
        self.assertEqual(force_bytes(inst.total[1].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[1].amount.value, 96.0)
        self.assertEqual(
            force_bytes(inst.total[1].category.coding[0].code), force_bytes("benefit")
        )
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("oral"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/claim-type"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("claim"))

    def testExplanationOfBenefit2(self):
        inst = self.instantiate_from("explanationofbenefit-example-2.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a ExplanationOfBenefit instance"
        )
        self.implExplanationOfBenefit2(inst)

        js = inst.as_json()
        self.assertEqual("ExplanationOfBenefit", js["resourceType"])
        inst2 = explanationofbenefit.ExplanationOfBenefit(js)
        self.implExplanationOfBenefit2(inst2)

    def implExplanationOfBenefit2(self, inst):
        self.assertEqual(inst.accident.date.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.accident.date.as_json(), "2014-02-14")
        self.assertEqual(
            force_bytes(inst.accident.type.coding[0].code), force_bytes("SPT")
        )
        self.assertEqual(
            force_bytes(inst.accident.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(inst.billablePeriod.end.date, FHIRDate("2014-03-01").date)
        self.assertEqual(inst.billablePeriod.end.as_json(), "2014-03-01")
        self.assertEqual(inst.billablePeriod.start.date, FHIRDate("2014-02-01").date)
        self.assertEqual(inst.billablePeriod.start.as_json(), "2014-02-01")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.disposition), force_bytes("Could not process.")
        )
        self.assertEqual(force_bytes(inst.formCode.coding[0].code), force_bytes("2"))
        self.assertEqual(
            force_bytes(inst.formCode.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/forms-codes"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("EB3501"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.BenefitsInc.com/fhir/explanationofbenefit"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("error-1"))
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("error"))
        self.assertEqual(inst.precedence, 2)
        self.assertEqual(inst.procedure[0].date.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.procedure[0].date.as_json(), "2014-02-14")
        self.assertEqual(
            force_bytes(inst.procedure[0].procedureCodeableConcept.coding[0].code),
            force_bytes("123001"),
        )
        self.assertEqual(
            force_bytes(inst.procedure[0].procedureCodeableConcept.coding[0].system),
            force_bytes("http://hl7.org/fhir/sid/ex-icd-10-procedures"),
        )
        self.assertEqual(inst.procedure[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.processNote[0].language.coding[0].code),
            force_bytes("en-CA"),
        )
        self.assertEqual(
            force_bytes(inst.processNote[0].language.coding[0].system),
            force_bytes("urn:ietf:bcp:47"),
        )
        self.assertEqual(inst.processNote[0].number, 1)
        self.assertEqual(
            force_bytes(inst.processNote[0].text), force_bytes("Invalid claim")
        )
        self.assertEqual(force_bytes(inst.processNote[0].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.related[0].reference.system),
            force_bytes("http://www.BenefitsInc.com/case-number"),
        )
        self.assertEqual(
            force_bytes(inst.related[0].reference.value),
            force_bytes("23-56Tu-XX-47-20150M14"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.subType.coding[0].code), force_bytes("emergency")
        )
        self.assertEqual(
            force_bytes(inst.subType.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-claimsubtype"),
        )
        self.assertEqual(
            force_bytes(inst.supportingInfo[0].category.coding[0].code),
            force_bytes("employmentimpacted"),
        )
        self.assertEqual(
            force_bytes(inst.supportingInfo[0].category.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/claiminformationcategory"
            ),
        )
        self.assertEqual(inst.supportingInfo[0].sequence, 1)
        self.assertEqual(
            inst.supportingInfo[0].timingPeriod.end.date, FHIRDate("2014-02-28").date
        )
        self.assertEqual(
            inst.supportingInfo[0].timingPeriod.end.as_json(), "2014-02-28"
        )
        self.assertEqual(
            inst.supportingInfo[0].timingPeriod.start.date, FHIRDate("2014-02-14").date
        )
        self.assertEqual(
            inst.supportingInfo[0].timingPeriod.start.as_json(), "2014-02-14"
        )
        self.assertEqual(
            force_bytes(inst.supportingInfo[1].category.coding[0].code),
            force_bytes("hospitalized"),
        )
        self.assertEqual(
            force_bytes(inst.supportingInfo[1].category.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/claiminformationcategory"
            ),
        )
        self.assertEqual(inst.supportingInfo[1].sequence, 2)
        self.assertEqual(
            inst.supportingInfo[1].timingPeriod.end.date, FHIRDate("2014-02-16").date
        )
        self.assertEqual(
            inst.supportingInfo[1].timingPeriod.end.as_json(), "2014-02-16"
        )
        self.assertEqual(
            inst.supportingInfo[1].timingPeriod.start.date, FHIRDate("2014-02-14").date
        )
        self.assertEqual(
            inst.supportingInfo[1].timingPeriod.start.as_json(), "2014-02-14"
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.total[0].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[0].amount.value, 2478.57)
        self.assertEqual(
            force_bytes(inst.total[0].category.coding[0].code), force_bytes("submitted")
        )
        self.assertEqual(force_bytes(inst.total[1].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[1].amount.value, 0.0)
        self.assertEqual(
            force_bytes(inst.total[1].category.coding[0].code), force_bytes("benefit")
        )
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("oral"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/claim-type"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("claim"))
