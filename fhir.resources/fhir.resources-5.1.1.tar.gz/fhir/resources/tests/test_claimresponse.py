# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse
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

from .. import claimresponse
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ClaimResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ClaimResponse", js["resourceType"])
        return claimresponse.ClaimResponse(js)

    def testClaimResponse1(self):
        inst = self.instantiate_from("claimresponse-example-unsolicited-preauth.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse1(inst)

        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse1(inst2)

    def implClaimResponse1(self, inst):
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[0].adjudication[0].amount.value, 250.0)
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[1].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[0].adjudication[1].amount.value, 10.0)
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[1].category.coding[0].code),
            force_bytes("copay"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[2].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.addItem[0].adjudication[2].value, 100.0)
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[3].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[0].adjudication[3].amount.value, 240.0)
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[3].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.addItem[0].itemSequence[0], 1)
        self.assertEqual(
            force_bytes(inst.addItem[0].modifier[0].coding[0].code), force_bytes("x")
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].modifier[0].coding[0].display),
            force_bytes("None"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].modifier[0].coding[0].system),
            force_bytes("http://example.org/fhir/modifiers"),
        )
        self.assertEqual(force_bytes(inst.addItem[0].net.currency), force_bytes("USD"))
        self.assertEqual(inst.addItem[0].net.value, 250.0)
        self.assertEqual(inst.addItem[0].noteNumber[0], 101)
        self.assertEqual(
            force_bytes(inst.addItem[0].productOrService.coding[0].code),
            force_bytes("1101"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].productOrService.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[1].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[1].adjudication[0].amount.value, 800.0)
        self.assertEqual(
            force_bytes(inst.addItem[1].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[1].adjudication[1].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.addItem[1].adjudication[1].value, 100.0)
        self.assertEqual(
            force_bytes(inst.addItem[1].adjudication[2].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[1].adjudication[2].amount.value, 800.0)
        self.assertEqual(
            force_bytes(inst.addItem[1].adjudication[2].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.addItem[1].itemSequence[0], 1)
        self.assertEqual(force_bytes(inst.addItem[1].net.currency), force_bytes("USD"))
        self.assertEqual(inst.addItem[1].net.value, 800.0)
        self.assertEqual(
            force_bytes(inst.addItem[1].productOrService.coding[0].code),
            force_bytes("2101"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[1].productOrService.coding[0].display),
            force_bytes("Radiograph, series (12)"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[1].productOrService.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.disposition),
            force_bytes(
                "The enclosed services are authorized for your provision within 30 days of this notice."
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("UR3503"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.SocialBenefitsInc.com/fhir/ClaimResponse"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("UR3503"))
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.insurance[0].sequence, 1)
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
            force_bytes(inst.payeeType.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.payeeType.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/payeetype"),
        )
        self.assertEqual(force_bytes(inst.preAuthRef), force_bytes("18SS12345"))
        self.assertEqual(
            force_bytes(inst.processNote[0].language.coding[0].code),
            force_bytes("en-CA"),
        )
        self.assertEqual(
            force_bytes(inst.processNote[0].language.coding[0].system),
            force_bytes("urn:ietf:bcp:47"),
        )
        self.assertEqual(inst.processNote[0].number, 101)
        self.assertEqual(
            force_bytes(inst.processNote[0].text),
            force_bytes(
                "Please submit a Pre-Authorization request if a more extensive examination or urgent services are required."
            ),
        )
        self.assertEqual(force_bytes(inst.processNote[0].type), force_bytes("print"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A sample unsolicited pre-authorization response which authorizes basic dental services to be performed for a patient.</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.total[0].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[0].amount.value, 1050.0)
        self.assertEqual(
            force_bytes(inst.total[0].category.coding[0].code), force_bytes("submitted")
        )
        self.assertEqual(force_bytes(inst.total[1].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[1].amount.value, 1040.0)
        self.assertEqual(
            force_bytes(inst.total[1].category.coding[0].code), force_bytes("benefit")
        )
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("oral"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/claim-type"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("preauthorization"))

    def testClaimResponse2(self):
        inst = self.instantiate_from("claimresponse-example-additem.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse2(inst)

        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse2(inst2)

    def implClaimResponse2(self, inst):
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[0].adjudication[0].amount.value, 100.0)
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[1].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[0].adjudication[1].amount.value, 10.0)
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[1].category.coding[0].code),
            force_bytes("copay"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[2].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.addItem[0].adjudication[2].value, 80.0)
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[3].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[0].adjudication[3].amount.value, 72.0)
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[3].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[3].reason.coding[0].code),
            force_bytes("ar002"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[3].reason.coding[0].display),
            force_bytes("Plan Limit Reached"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].adjudication[3].reason.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/adjudication-reason"),
        )
        self.assertEqual(inst.addItem[0].itemSequence[0], 1)
        self.assertEqual(
            force_bytes(inst.addItem[0].modifier[0].coding[0].code), force_bytes("x")
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].modifier[0].coding[0].display),
            force_bytes("None"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].modifier[0].coding[0].system),
            force_bytes("http://example.org/fhir/modifiers"),
        )
        self.assertEqual(force_bytes(inst.addItem[0].net.currency), force_bytes("USD"))
        self.assertEqual(inst.addItem[0].net.value, 135.57)
        self.assertEqual(inst.addItem[0].noteNumber[0], 101)
        self.assertEqual(
            force_bytes(inst.addItem[0].productOrService.coding[0].code),
            force_bytes("1101"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[0].productOrService.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[1].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[1].adjudication[0].amount.value, 35.57)
        self.assertEqual(
            force_bytes(inst.addItem[1].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[1].adjudication[1].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.addItem[1].adjudication[1].value, 80.0)
        self.assertEqual(
            force_bytes(inst.addItem[1].adjudication[2].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[1].adjudication[2].amount.value, 28.47)
        self.assertEqual(
            force_bytes(inst.addItem[1].adjudication[2].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.addItem[1].itemSequence[0], 1)
        self.assertEqual(force_bytes(inst.addItem[1].net.currency), force_bytes("USD"))
        self.assertEqual(inst.addItem[1].net.value, 35.57)
        self.assertEqual(
            force_bytes(inst.addItem[1].productOrService.coding[0].code),
            force_bytes("2141"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[1].productOrService.coding[0].display),
            force_bytes("Radiograph, bytewing"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[1].productOrService.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[2].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[2].adjudication[0].amount.value, 350.0)
        self.assertEqual(
            force_bytes(inst.addItem[2].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[2].adjudication[1].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.addItem[2].adjudication[1].value, 80.0)
        self.assertEqual(
            force_bytes(inst.addItem[2].adjudication[2].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.addItem[2].adjudication[2].amount.value, 270.0)
        self.assertEqual(
            force_bytes(inst.addItem[2].adjudication[2].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.addItem[2].detailSequence[0], 2)
        self.assertEqual(inst.addItem[2].itemSequence[0], 3)
        self.assertEqual(
            force_bytes(inst.addItem[2].modifier[0].coding[0].code), force_bytes("x")
        )
        self.assertEqual(
            force_bytes(inst.addItem[2].modifier[0].coding[0].display),
            force_bytes("None"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[2].modifier[0].coding[0].system),
            force_bytes("http://example.org/fhir/modifiers"),
        )
        self.assertEqual(force_bytes(inst.addItem[2].net.currency), force_bytes("USD"))
        self.assertEqual(inst.addItem[2].net.value, 350.0)
        self.assertEqual(inst.addItem[2].noteNumber[0], 101)
        self.assertEqual(
            force_bytes(inst.addItem[2].productOrService.coding[0].code),
            force_bytes("expense"),
        )
        self.assertEqual(
            force_bytes(inst.addItem[2].productOrService.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.disposition), force_bytes("Claim settled as per contract.")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("R3503"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.BenefitsInc.com/fhir/remittance"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("R3503"))
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 0.0)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[1].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].adjudication[1].amount.value, 0.0)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[1].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[0].itemSequence, 1)
        self.assertEqual(
            force_bytes(inst.item[1].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[1].adjudication[0].amount.value, 105.0)
        self.assertEqual(
            force_bytes(inst.item[1].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.item[1].adjudication[1].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.item[1].adjudication[1].value, 80.0)
        self.assertEqual(
            force_bytes(inst.item[1].adjudication[2].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[1].adjudication[2].amount.value, 84.0)
        self.assertEqual(
            force_bytes(inst.item[1].adjudication[2].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[1].itemSequence, 2)
        self.assertEqual(
            force_bytes(inst.item[2].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[2].adjudication[0].amount.value, 750.0)
        self.assertEqual(
            force_bytes(inst.item[2].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].adjudication[1].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.item[2].adjudication[1].value, 80.0)
        self.assertEqual(
            force_bytes(inst.item[2].adjudication[2].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[2].adjudication[2].amount.value, 600.0)
        self.assertEqual(
            force_bytes(inst.item[2].adjudication[2].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[2].detail[0].adjudication[0].amount.value, 750.0)
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].adjudication[1].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.item[2].detail[0].adjudication[1].value, 80.0)
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].adjudication[2].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[2].detail[0].adjudication[2].amount.value, 600.0)
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].adjudication[2].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[2].detail[0].detailSequence, 1)
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[2].detail[1].adjudication[0].amount.value, 0.0)
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].adjudication[1].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[2].detail[1].adjudication[1].amount.value, 0.0)
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].adjudication[1].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[2].detail[1].detailSequence, 2)
        self.assertEqual(inst.item[2].itemSequence, 3)
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
            force_bytes(inst.payeeType.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.payeeType.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/payeetype"),
        )
        self.assertEqual(force_bytes(inst.payment.amount.currency), force_bytes("USD"))
        self.assertEqual(inst.payment.amount.value, 100.47)
        self.assertEqual(inst.payment.date.date, FHIRDate("2014-08-31").date)
        self.assertEqual(inst.payment.date.as_json(), "2014-08-31")
        self.assertEqual(
            force_bytes(inst.payment.identifier.system),
            force_bytes("http://www.BenefitsInc.com/fhir/paymentidentifier"),
        )
        self.assertEqual(
            force_bytes(inst.payment.identifier.value), force_bytes("201408-2-15507")
        )
        self.assertEqual(
            force_bytes(inst.payment.type.coding[0].code), force_bytes("complete")
        )
        self.assertEqual(
            force_bytes(inst.payment.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-paymenttype"),
        )
        self.assertEqual(
            force_bytes(inst.processNote[0].language.coding[0].code),
            force_bytes("en-CA"),
        )
        self.assertEqual(
            force_bytes(inst.processNote[0].language.coding[0].system),
            force_bytes("urn:ietf:bcp:47"),
        )
        self.assertEqual(inst.processNote[0].number, 101)
        self.assertEqual(
            force_bytes(inst.processNote[0].text),
            force_bytes("Package codes are not permitted. Codes replaced by Insurer."),
        )
        self.assertEqual(force_bytes(inst.processNote[0].type), force_bytes("print"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the ClaimResponse to Claim Oral Average with additional items</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.total[0].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[0].amount.value, 1340.57)
        self.assertEqual(
            force_bytes(inst.total[0].category.coding[0].code), force_bytes("submitted")
        )
        self.assertEqual(force_bytes(inst.total[1].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[1].amount.value, 1054.47)
        self.assertEqual(
            force_bytes(inst.total[1].category.coding[0].code), force_bytes("benefit")
        )
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("oral"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/claim-type"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("claim"))

    def testClaimResponse3(self):
        inst = self.instantiate_from("claimresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse3(inst)

        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse3(inst2)

    def implClaimResponse3(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.disposition), force_bytes("Claim settled as per contract.")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("R3500"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.BenefitsInc.com/fhir/remittance"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("R3500"))
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 135.57)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[1].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].adjudication[1].amount.value, 10.0)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[1].category.coding[0].code),
            force_bytes("copay"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[2].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.item[0].adjudication[2].value, 80.0)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[3].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].adjudication[3].amount.value, 90.47)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[3].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[3].reason.coding[0].code),
            force_bytes("ar002"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[3].reason.coding[0].display),
            force_bytes("Plan Limit Reached"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[3].reason.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/adjudication-reason"),
        )
        self.assertEqual(inst.item[0].itemSequence, 1)
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
            force_bytes(inst.payeeType.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.payeeType.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/payeetype"),
        )
        self.assertEqual(force_bytes(inst.payment.amount.currency), force_bytes("USD"))
        self.assertEqual(inst.payment.amount.value, 100.47)
        self.assertEqual(inst.payment.date.date, FHIRDate("2014-08-31").date)
        self.assertEqual(inst.payment.date.as_json(), "2014-08-31")
        self.assertEqual(
            force_bytes(inst.payment.identifier.system),
            force_bytes("http://www.BenefitsInc.com/fhir/paymentidentifier"),
        )
        self.assertEqual(
            force_bytes(inst.payment.identifier.value), force_bytes("201408-2-1569478")
        )
        self.assertEqual(
            force_bytes(inst.payment.type.coding[0].code), force_bytes("complete")
        )
        self.assertEqual(
            force_bytes(inst.payment.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-paymenttype"),
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
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the ClaimResponse</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.total[0].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[0].amount.value, 135.57)
        self.assertEqual(
            force_bytes(inst.total[0].category.coding[0].code), force_bytes("submitted")
        )
        self.assertEqual(force_bytes(inst.total[1].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[1].amount.value, 90.47)
        self.assertEqual(
            force_bytes(inst.total[1].category.coding[0].code), force_bytes("benefit")
        )
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("oral"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/claim-type"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("claim"))

    def testClaimResponse4(self):
        inst = self.instantiate_from("claimresponse-example-vision-3tier.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse4(inst)

        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse4(inst2)

    def implClaimResponse4(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.disposition), force_bytes("Claim settled as per contract.")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("R3502"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://thebenefitcompany.com/claimresponse"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("CR6532875367")
        )
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 235.4)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[1].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].adjudication[1].amount.value, 20.0)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[1].category.coding[0].code),
            force_bytes("copay"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[2].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.item[0].adjudication[2].value, 80.0)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[3].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].adjudication[3].amount.value, 172.32)
        self.assertEqual(
            force_bytes(inst.item[0].adjudication[3].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].detail[0].adjudication[0].amount.value, 100.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].adjudication[1].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].detail[0].adjudication[1].amount.value, 20.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].adjudication[1].category.coding[0].code),
            force_bytes("copay"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].adjudication[2].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.item[0].detail[0].adjudication[2].value, 80.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].adjudication[3].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].detail[0].adjudication[3].amount.value, 80.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].adjudication[3].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[0].detail[0].detailSequence, 1)
        self.assertEqual(inst.item[0].detail[0].noteNumber[0], 1)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].detail[1].adjudication[0].amount.value, 110.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].adjudication[1].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.item[0].detail[1].adjudication[1].value, 80.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].adjudication[2].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].detail[1].adjudication[2].amount.value, 88.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].adjudication[2].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[0].detail[1].detailSequence, 2)
        self.assertEqual(inst.item[0].detail[1].noteNumber[0], 1)
        self.assertEqual(
            force_bytes(
                inst.item[0].detail[1].subDetail[0].adjudication[0].amount.currency
            ),
            force_bytes("USD"),
        )
        self.assertEqual(
            inst.item[0].detail[1].subDetail[0].adjudication[0].amount.value, 60.0
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .detail[1]
                .subDetail[0]
                .adjudication[0]
                .category.coding[0]
                .code
            ),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .detail[1]
                .subDetail[0]
                .adjudication[1]
                .category.coding[0]
                .code
            ),
            force_bytes("eligpercent"),
        )
        self.assertEqual(
            inst.item[0].detail[1].subDetail[0].adjudication[1].value, 80.0
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].detail[1].subDetail[0].adjudication[2].amount.currency
            ),
            force_bytes("USD"),
        )
        self.assertEqual(
            inst.item[0].detail[1].subDetail[0].adjudication[2].amount.value, 48.0
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .detail[1]
                .subDetail[0]
                .adjudication[2]
                .category.coding[0]
                .code
            ),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[0].noteNumber[0], 1)
        self.assertEqual(inst.item[0].detail[1].subDetail[0].subDetailSequence, 1)
        self.assertEqual(
            force_bytes(
                inst.item[0].detail[1].subDetail[1].adjudication[0].amount.currency
            ),
            force_bytes("USD"),
        )
        self.assertEqual(
            inst.item[0].detail[1].subDetail[1].adjudication[0].amount.value, 30.0
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .detail[1]
                .subDetail[1]
                .adjudication[0]
                .category.coding[0]
                .code
            ),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .detail[1]
                .subDetail[1]
                .adjudication[1]
                .category.coding[0]
                .code
            ),
            force_bytes("eligpercent"),
        )
        self.assertEqual(
            inst.item[0].detail[1].subDetail[1].adjudication[1].value, 80.0
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].detail[1].subDetail[1].adjudication[2].amount.currency
            ),
            force_bytes("USD"),
        )
        self.assertEqual(
            inst.item[0].detail[1].subDetail[1].adjudication[2].amount.value, 24.0
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .detail[1]
                .subDetail[1]
                .adjudication[2]
                .category.coding[0]
                .code
            ),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[1].subDetailSequence, 2)
        self.assertEqual(
            force_bytes(
                inst.item[0].detail[1].subDetail[2].adjudication[0].amount.currency
            ),
            force_bytes("USD"),
        )
        self.assertEqual(
            inst.item[0].detail[1].subDetail[2].adjudication[0].amount.value, 10.0
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .detail[1]
                .subDetail[2]
                .adjudication[0]
                .category.coding[0]
                .code
            ),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .detail[1]
                .subDetail[2]
                .adjudication[1]
                .category.coding[0]
                .code
            ),
            force_bytes("eligpercent"),
        )
        self.assertEqual(
            inst.item[0].detail[1].subDetail[2].adjudication[1].value, 80.0
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].detail[1].subDetail[2].adjudication[2].amount.currency
            ),
            force_bytes("USD"),
        )
        self.assertEqual(
            inst.item[0].detail[1].subDetail[2].adjudication[2].amount.value, 8.0
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .detail[1]
                .subDetail[2]
                .adjudication[2]
                .category.coding[0]
                .code
            ),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[2].noteNumber[0], 1)
        self.assertEqual(inst.item[0].detail[1].subDetail[2].subDetailSequence, 3)
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].adjudication[0].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].detail[2].adjudication[0].amount.value, 200.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].adjudication[0].category.coding[0].code),
            force_bytes("eligible"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].adjudication[1].category.coding[0].code),
            force_bytes("eligpercent"),
        )
        self.assertEqual(inst.item[0].detail[2].adjudication[1].value, 80.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].adjudication[2].amount.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.item[0].detail[2].adjudication[2].amount.value, 14.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].adjudication[2].category.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(inst.item[0].detail[2].detailSequence, 3)
        self.assertEqual(inst.item[0].detail[2].noteNumber[0], 1)
        self.assertEqual(inst.item[0].itemSequence, 1)
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
            force_bytes(inst.payeeType.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.payeeType.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/payeetype"),
        )
        self.assertEqual(
            force_bytes(inst.payment.adjustment.currency), force_bytes("USD")
        )
        self.assertEqual(inst.payment.adjustment.value, 75.0)
        self.assertEqual(
            force_bytes(inst.payment.adjustmentReason.coding[0].code),
            force_bytes("a002"),
        )
        self.assertEqual(
            force_bytes(inst.payment.adjustmentReason.coding[0].display),
            force_bytes("Prior Overpayment"),
        )
        self.assertEqual(
            force_bytes(inst.payment.adjustmentReason.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/payment-adjustment-reason"
            ),
        )
        self.assertEqual(force_bytes(inst.payment.amount.currency), force_bytes("USD"))
        self.assertEqual(inst.payment.amount.value, 107.0)
        self.assertEqual(inst.payment.date.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.payment.date.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.payment.identifier.system),
            force_bytes("http://thebenefitcompany.com/paymentidentifier"),
        )
        self.assertEqual(
            force_bytes(inst.payment.identifier.value), force_bytes("201416-123456")
        )
        self.assertEqual(
            force_bytes(inst.payment.type.coding[0].code), force_bytes("complete")
        )
        self.assertEqual(
            force_bytes(inst.payment.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-paymenttype"),
        )
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
            force_bytes(inst.processNote[0].text),
            force_bytes("After hours surcharge declined"),
        )
        self.assertEqual(force_bytes(inst.processNote[0].type), force_bytes("display"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the ClaimResponse</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.total[0].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[0].amount.value, 235.4)
        self.assertEqual(
            force_bytes(inst.total[0].category.coding[0].code), force_bytes("submitted")
        )
        self.assertEqual(force_bytes(inst.total[1].amount.currency), force_bytes("USD"))
        self.assertEqual(inst.total[1].amount.value, 182.0)
        self.assertEqual(
            force_bytes(inst.total[1].category.coding[0].code), force_bytes("benefit")
        )
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("vision"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/claim-type"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("claim"))

    def testClaimResponse5(self):
        inst = self.instantiate_from("claimresponse-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse5(inst)

        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse5(inst2)

    def implClaimResponse5(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.disposition), force_bytes("Claim could not be processed")
        )
        self.assertEqual(
            force_bytes(inst.error[0].code.coding[0].code), force_bytes("a002")
        )
        self.assertEqual(
            force_bytes(inst.error[0].code.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/adjudication-error"),
        )
        self.assertEqual(inst.error[0].detailSequence, 2)
        self.assertEqual(inst.error[0].itemSequence, 3)
        self.assertEqual(force_bytes(inst.formCode.coding[0].code), force_bytes("2"))
        self.assertEqual(
            force_bytes(inst.formCode.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/forms-codes"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("R3501"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.BenefitsInc.com/fhir/remittance"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("R3501"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("error"))
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
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the ClaimResponse that demonstrates returning errors</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("oral"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/claim-type"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("claim"))
