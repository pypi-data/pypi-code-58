# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AuditEvent
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

from .. import auditevent
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class AuditEventTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("AuditEvent", js["resourceType"])
        return auditevent.AuditEvent(js)

    def testAuditEvent1(self):
        inst = self.instantiate_from("audit-event-example-search.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent1(inst)

        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent1(inst2)

    def implAuditEvent1(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("E"))
        self.assertEqual(force_bytes(inst.agent[0].altId), force_bytes("601847123"))
        self.assertEqual(force_bytes(inst.agent[0].name), force_bytes("Grahame Grieve"))
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].code), force_bytes("humanuser")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].display), force_bytes("human user")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/extra-security-role-type"
            ),
        )
        self.assertEqual(force_bytes(inst.agent[1].altId), force_bytes("6580"))
        self.assertEqual(
            force_bytes(inst.agent[1].network.address),
            force_bytes("Workstation1.ehr.familyclinic.com"),
        )
        self.assertEqual(force_bytes(inst.agent[1].network.type), force_bytes("1"))
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].code), force_bytes("110153")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].display),
            force_bytes("Source Role ID"),
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(
            force_bytes(inst.entity[0].query),
            force_bytes(
                "aHR0cDovL2ZoaXItZGV2LmhlYWx0aGludGVyc2VjdGlvbnMuY29tLmF1L29wZW4vRW5jb3VudGVyP3BhcnRpY2lwYW50PTEz"
            ),
        )
        self.assertEqual(force_bytes(inst.entity[0].role.code), force_bytes("24"))
        self.assertEqual(force_bytes(inst.entity[0].role.display), force_bytes("Query"))
        self.assertEqual(
            force_bytes(inst.entity[0].role.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/object-role"),
        )
        self.assertEqual(force_bytes(inst.entity[0].type.code), force_bytes("2"))
        self.assertEqual(
            force_bytes(inst.entity[0].type.display), force_bytes("System Object")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-entity-type"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-search"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("0"))
        self.assertEqual(inst.recorded.date, FHIRDate("2015-08-22T23:42:24Z").date)
        self.assertEqual(inst.recorded.as_json(), "2015-08-22T23:42:24Z")
        self.assertEqual(force_bytes(inst.source.site), force_bytes("Cloud"))
        self.assertEqual(force_bytes(inst.source.type[0].code), force_bytes("3"))
        self.assertEqual(
            force_bytes(inst.source.type[0].display), force_bytes("Web Server")
        )
        self.assertEqual(
            force_bytes(inst.source.type[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/security-source-type"),
        )
        self.assertEqual(force_bytes(inst.subtype[0].code), force_bytes("search"))
        self.assertEqual(force_bytes(inst.subtype[0].display), force_bytes("search"))
        self.assertEqual(
            force_bytes(inst.subtype[0].system),
            force_bytes("http://hl7.org/fhir/restful-interaction"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.code), force_bytes("rest"))
        self.assertEqual(
            force_bytes(inst.type.display), force_bytes("Restful Operation")
        )
        self.assertEqual(
            force_bytes(inst.type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-event-type"),
        )

    def testAuditEvent2(self):
        inst = self.instantiate_from("audit-event-example-logout.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent2(inst)

        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent2(inst2)

    def implAuditEvent2(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("E"))
        self.assertEqual(force_bytes(inst.agent[0].altId), force_bytes("601847123"))
        self.assertEqual(force_bytes(inst.agent[0].name), force_bytes("Grahame Grieve"))
        self.assertEqual(
            force_bytes(inst.agent[0].network.address), force_bytes("127.0.0.1")
        )
        self.assertEqual(force_bytes(inst.agent[0].network.type), force_bytes("2"))
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].code), force_bytes("humanuser")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].display), force_bytes("human user")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/extra-security-role-type"
            ),
        )
        self.assertEqual(force_bytes(inst.agent[1].altId), force_bytes("6580"))
        self.assertEqual(
            force_bytes(inst.agent[1].network.address),
            force_bytes("Workstation1.ehr.familyclinic.com"),
        )
        self.assertEqual(force_bytes(inst.agent[1].network.type), force_bytes("1"))
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].code), force_bytes("110153")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].display),
            force_bytes("Source Role ID"),
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-logout"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("0"))
        self.assertEqual(inst.recorded.date, FHIRDate("2013-06-20T23:46:41Z").date)
        self.assertEqual(inst.recorded.as_json(), "2013-06-20T23:46:41Z")
        self.assertEqual(force_bytes(inst.source.site), force_bytes("Cloud"))
        self.assertEqual(force_bytes(inst.source.type[0].code), force_bytes("3"))
        self.assertEqual(
            force_bytes(inst.source.type[0].display), force_bytes("Web Server")
        )
        self.assertEqual(
            force_bytes(inst.source.type[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/security-source-type"),
        )
        self.assertEqual(force_bytes(inst.subtype[0].code), force_bytes("110123"))
        self.assertEqual(force_bytes(inst.subtype[0].display), force_bytes("Logout"))
        self.assertEqual(
            force_bytes(inst.subtype[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.code), force_bytes("110114"))
        self.assertEqual(
            force_bytes(inst.type.display), force_bytes("User Authentication")
        )
        self.assertEqual(
            force_bytes(inst.type.system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )

    def testAuditEvent3(self):
        inst = self.instantiate_from("audit-event-example-vread.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent3(inst)

        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent3(inst2)

    def implAuditEvent3(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("R"))
        self.assertEqual(force_bytes(inst.agent[0].altId), force_bytes("601847123"))
        self.assertEqual(force_bytes(inst.agent[0].name), force_bytes("Grahame Grieve"))
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].code), force_bytes("humanuser")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].display), force_bytes("human user")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/extra-security-role-type"
            ),
        )
        self.assertEqual(force_bytes(inst.agent[1].altId), force_bytes("6580"))
        self.assertEqual(
            force_bytes(inst.agent[1].network.address),
            force_bytes("Workstation1.ehr.familyclinic.com"),
        )
        self.assertEqual(force_bytes(inst.agent[1].network.type), force_bytes("1"))
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].code), force_bytes("110153")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].display),
            force_bytes("Source Role ID"),
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.entity[0].lifecycle.code), force_bytes("6"))
        self.assertEqual(
            force_bytes(inst.entity[0].lifecycle.display), force_bytes("Access / Use")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].lifecycle.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dicom-audit-lifecycle"),
        )
        self.assertEqual(force_bytes(inst.entity[0].type.code), force_bytes("2"))
        self.assertEqual(
            force_bytes(inst.entity[0].type.display), force_bytes("System Object")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-entity-type"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-rest"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("0"))
        self.assertEqual(inst.recorded.date, FHIRDate("2013-06-20T23:42:24Z").date)
        self.assertEqual(inst.recorded.as_json(), "2013-06-20T23:42:24Z")
        self.assertEqual(force_bytes(inst.source.site), force_bytes("Cloud"))
        self.assertEqual(force_bytes(inst.source.type[0].code), force_bytes("3"))
        self.assertEqual(
            force_bytes(inst.source.type[0].display), force_bytes("Web Server")
        )
        self.assertEqual(
            force_bytes(inst.source.type[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/security-source-type"),
        )
        self.assertEqual(force_bytes(inst.subtype[0].code), force_bytes("vread"))
        self.assertEqual(force_bytes(inst.subtype[0].display), force_bytes("vread"))
        self.assertEqual(
            force_bytes(inst.subtype[0].system),
            force_bytes("http://hl7.org/fhir/restful-interaction"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.code), force_bytes("rest"))
        self.assertEqual(
            force_bytes(inst.type.display), force_bytes("Restful Operation")
        )
        self.assertEqual(
            force_bytes(inst.type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-event-type"),
        )

    def testAuditEvent4(self):
        inst = self.instantiate_from("audit-event-example-media.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent4(inst)

        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent4(inst2)

    def implAuditEvent4(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("R"))
        self.assertFalse(inst.agent[0].requestor)
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].code), force_bytes("110153")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].display),
            force_bytes("Source Role ID"),
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.agent[1].altId), force_bytes("601847123"))
        self.assertEqual(force_bytes(inst.agent[1].name), force_bytes("Grahame Grieve"))
        self.assertTrue(inst.agent[1].requestor)
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].code), force_bytes("humanuser")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].display), force_bytes("human user")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/extra-security-role-type"
            ),
        )
        self.assertEqual(force_bytes(inst.agent[2].media.code), force_bytes("110033"))
        self.assertEqual(force_bytes(inst.agent[2].media.display), force_bytes("DVD"))
        self.assertEqual(
            force_bytes(inst.agent[2].media.system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(
            force_bytes(inst.agent[2].name), force_bytes("Media title: Hello World")
        )
        self.assertFalse(inst.agent[2].requestor)
        self.assertEqual(
            force_bytes(inst.agent[2].type.coding[0].code), force_bytes("110154")
        )
        self.assertEqual(
            force_bytes(inst.agent[2].type.coding[0].display),
            force_bytes("Destination Media"),
        )
        self.assertEqual(
            force_bytes(inst.agent[2].type.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.entity[0].role.code), force_bytes("1"))
        self.assertEqual(
            force_bytes(inst.entity[0].role.display), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].role.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/object-role"),
        )
        self.assertEqual(force_bytes(inst.entity[0].type.code), force_bytes("1"))
        self.assertEqual(
            force_bytes(inst.entity[0].type.display), force_bytes("Person")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-entity-type"),
        )
        self.assertEqual(force_bytes(inst.entity[1].role.code), force_bytes("20"))
        self.assertEqual(force_bytes(inst.entity[1].role.display), force_bytes("Job"))
        self.assertEqual(
            force_bytes(inst.entity[1].role.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/object-role"),
        )
        self.assertEqual(force_bytes(inst.entity[1].type.code), force_bytes("2"))
        self.assertEqual(
            force_bytes(inst.entity[1].type.display), force_bytes("System Object")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-entity-type"),
        )
        self.assertEqual(force_bytes(inst.entity[2].type.code), force_bytes("2"))
        self.assertEqual(
            force_bytes(inst.entity[2].type.display), force_bytes("System Object")
        )
        self.assertEqual(
            force_bytes(inst.entity[2].type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-entity-type"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-media"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("0"))
        self.assertEqual(inst.recorded.date, FHIRDate("2015-08-27T23:42:24Z").date)
        self.assertEqual(inst.recorded.as_json(), "2015-08-27T23:42:24Z")
        self.assertEqual(force_bytes(inst.subtype[0].code), force_bytes("ITI-32"))
        self.assertEqual(
            force_bytes(inst.subtype[0].display),
            force_bytes("Distribute Document Set on Media"),
        )
        self.assertEqual(
            force_bytes(inst.subtype[0].system),
            force_bytes("urn:oid:1.3.6.1.4.1.19376.1.2"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.code), force_bytes("110106"))
        self.assertEqual(force_bytes(inst.type.display), force_bytes("Export"))
        self.assertEqual(
            force_bytes(inst.type.system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )

    def testAuditEvent5(self):
        inst = self.instantiate_from("audit-event-example-login.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent5(inst)

        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent5(inst2)

    def implAuditEvent5(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("E"))
        self.assertEqual(force_bytes(inst.agent[0].altId), force_bytes("601847123"))
        self.assertEqual(force_bytes(inst.agent[0].name), force_bytes("Grahame Grieve"))
        self.assertEqual(
            force_bytes(inst.agent[0].network.address), force_bytes("127.0.0.1")
        )
        self.assertEqual(force_bytes(inst.agent[0].network.type), force_bytes("2"))
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].code), force_bytes("humanuser")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].display), force_bytes("human user")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/extra-security-role-type"
            ),
        )
        self.assertEqual(force_bytes(inst.agent[1].altId), force_bytes("6580"))
        self.assertEqual(
            force_bytes(inst.agent[1].network.address),
            force_bytes("Workstation1.ehr.familyclinic.com"),
        )
        self.assertEqual(force_bytes(inst.agent[1].network.type), force_bytes("1"))
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].code), force_bytes("110153")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].display),
            force_bytes("Source Role ID"),
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-login"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("0"))
        self.assertEqual(inst.recorded.date, FHIRDate("2013-06-20T23:41:23Z").date)
        self.assertEqual(inst.recorded.as_json(), "2013-06-20T23:41:23Z")
        self.assertEqual(force_bytes(inst.source.site), force_bytes("Cloud"))
        self.assertEqual(force_bytes(inst.source.type[0].code), force_bytes("3"))
        self.assertEqual(
            force_bytes(inst.source.type[0].display), force_bytes("Web Server")
        )
        self.assertEqual(
            force_bytes(inst.source.type[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/security-source-type"),
        )
        self.assertEqual(force_bytes(inst.subtype[0].code), force_bytes("110122"))
        self.assertEqual(force_bytes(inst.subtype[0].display), force_bytes("Login"))
        self.assertEqual(
            force_bytes(inst.subtype[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.code), force_bytes("110114"))
        self.assertEqual(
            force_bytes(inst.type.display), force_bytes("User Authentication")
        )
        self.assertEqual(
            force_bytes(inst.type.system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )

    def testAuditEvent6(self):
        inst = self.instantiate_from("audit-event-example-pixQuery.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent6(inst)

        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent6(inst2)

    def implAuditEvent6(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("E"))
        self.assertEqual(force_bytes(inst.agent[0].altId), force_bytes("6580"))
        self.assertEqual(
            force_bytes(inst.agent[0].network.address),
            force_bytes("Workstation1.ehr.familyclinic.com"),
        )
        self.assertEqual(force_bytes(inst.agent[0].network.type), force_bytes("1"))
        self.assertFalse(inst.agent[0].requestor)
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].code), force_bytes("110153")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].display),
            force_bytes("Source Role ID"),
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.agent[1].altId), force_bytes("601847123"))
        self.assertEqual(force_bytes(inst.agent[1].name), force_bytes("Grahame Grieve"))
        self.assertTrue(inst.agent[1].requestor)
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].code), force_bytes("humanuser")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].display), force_bytes("human user")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/extra-security-role-type"
            ),
        )
        self.assertEqual(force_bytes(inst.entity[0].role.code), force_bytes("1"))
        self.assertEqual(
            force_bytes(inst.entity[0].role.display), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].role.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/object-role"),
        )
        self.assertEqual(force_bytes(inst.entity[0].type.code), force_bytes("1"))
        self.assertEqual(
            force_bytes(inst.entity[0].type.display), force_bytes("Person")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-entity-type"),
        )
        self.assertEqual(
            force_bytes(inst.entity[1].detail[0].type), force_bytes("MSH-10")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].detail[0].valueBase64Binary),
            force_bytes("MS4yLjg0MC4xMTQzNTAuMS4xMy4wLjEuNy4xLjE="),
        )
        self.assertEqual(force_bytes(inst.entity[1].role.code), force_bytes("24"))
        self.assertEqual(force_bytes(inst.entity[1].role.display), force_bytes("Query"))
        self.assertEqual(
            force_bytes(inst.entity[1].role.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/object-role"),
        )
        self.assertEqual(force_bytes(inst.entity[1].type.code), force_bytes("2"))
        self.assertEqual(
            force_bytes(inst.entity[1].type.display), force_bytes("System Object")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-entity-type"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-pixQuery"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("0"))
        self.assertEqual(inst.recorded.date, FHIRDate("2015-08-26T23:42:24Z").date)
        self.assertEqual(inst.recorded.as_json(), "2015-08-26T23:42:24Z")
        self.assertEqual(force_bytes(inst.subtype[0].code), force_bytes("ITI-9"))
        self.assertEqual(force_bytes(inst.subtype[0].display), force_bytes("PIX Query"))
        self.assertEqual(
            force_bytes(inst.subtype[0].system),
            force_bytes("urn:oid:1.3.6.1.4.1.19376.1.2"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.code), force_bytes("110112"))
        self.assertEqual(force_bytes(inst.type.display), force_bytes("Query"))
        self.assertEqual(
            force_bytes(inst.type.system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )

    def testAuditEvent7(self):
        inst = self.instantiate_from("auditevent-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent7(inst)

        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent7(inst2)

    def implAuditEvent7(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("E"))
        self.assertEqual(
            force_bytes(inst.agent[0].network.address), force_bytes("127.0.0.1")
        )
        self.assertEqual(force_bytes(inst.agent[0].network.type), force_bytes("2"))
        self.assertFalse(inst.agent[0].requestor)
        self.assertEqual(
            force_bytes(inst.agent[0].role[0].text), force_bytes("Service User (Logon)")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].code), force_bytes("humanuser")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].display), force_bytes("human user")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/extra-security-role-type"
            ),
        )
        self.assertEqual(force_bytes(inst.agent[1].altId), force_bytes("6580"))
        self.assertEqual(
            force_bytes(inst.agent[1].network.address),
            force_bytes("Workstation1.ehr.familyclinic.com"),
        )
        self.assertEqual(force_bytes(inst.agent[1].network.type), force_bytes("1"))
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].code), force_bytes("110153")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].display),
            force_bytes("Source Role ID"),
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.entity[0].lifecycle.code), force_bytes("6"))
        self.assertEqual(
            force_bytes(inst.entity[0].lifecycle.display), force_bytes("Access / Use")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].lifecycle.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dicom-audit-lifecycle"),
        )
        self.assertEqual(
            force_bytes(inst.entity[0].name), force_bytes("Grahame's Laptop")
        )
        self.assertEqual(force_bytes(inst.entity[0].role.code), force_bytes("4"))
        self.assertEqual(
            force_bytes(inst.entity[0].role.display), force_bytes("Domain Resource")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].role.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/object-role"),
        )
        self.assertEqual(force_bytes(inst.entity[0].type.code), force_bytes("4"))
        self.assertEqual(force_bytes(inst.entity[0].type.display), force_bytes("Other"))
        self.assertEqual(
            force_bytes(inst.entity[0].type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-entity-type"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("0"))
        self.assertEqual(inst.recorded.date, FHIRDate("2012-10-25T22:04:27+11:00").date)
        self.assertEqual(inst.recorded.as_json(), "2012-10-25T22:04:27+11:00")
        self.assertEqual(force_bytes(inst.source.site), force_bytes("Development"))
        self.assertEqual(force_bytes(inst.source.type[0].code), force_bytes("110122"))
        self.assertEqual(force_bytes(inst.source.type[0].display), force_bytes("Login"))
        self.assertEqual(
            force_bytes(inst.source.type[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.subtype[0].code), force_bytes("110120"))
        self.assertEqual(
            force_bytes(inst.subtype[0].display), force_bytes("Application Start")
        )
        self.assertEqual(
            force_bytes(inst.subtype[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Application Start for under service login &quot;Grahame&quot; (id: Grahame\'s Test HL7Connect)</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.code), force_bytes("110100"))
        self.assertEqual(
            force_bytes(inst.type.display), force_bytes("Application Activity")
        )
        self.assertEqual(
            force_bytes(inst.type.system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )

    def testAuditEvent8(self):
        inst = self.instantiate_from("auditevent-example-disclosure.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent8(inst)

        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent8(inst2)

    def implAuditEvent8(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("R"))
        self.assertEqual(force_bytes(inst.agent[0].altId), force_bytes("notMe"))
        self.assertEqual(
            force_bytes(inst.agent[0].name),
            force_bytes("That guy everyone wishes would be caught"),
        )
        self.assertEqual(
            force_bytes(inst.agent[0].network.address), force_bytes("custodian.net")
        )
        self.assertEqual(force_bytes(inst.agent[0].network.type), force_bytes("1"))
        self.assertEqual(
            force_bytes(inst.agent[0].policy[0]), force_bytes("http://consent.com/yes")
        )
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].code), force_bytes("110153")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].display),
            force_bytes("Source Role ID"),
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(
            force_bytes(inst.agent[1].network.address), force_bytes("marketing.land")
        )
        self.assertEqual(force_bytes(inst.agent[1].network.type), force_bytes("1"))
        self.assertEqual(
            force_bytes(inst.agent[1].purposeOfUse[0].coding[0].code),
            force_bytes("HMARKT"),
        )
        self.assertEqual(
            force_bytes(inst.agent[1].purposeOfUse[0].coding[0].display),
            force_bytes("healthcare marketing"),
        )
        self.assertEqual(
            force_bytes(inst.agent[1].purposeOfUse[0].coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].code), force_bytes("110152")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].display),
            force_bytes("Destination Role ID"),
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.entity[0].role.code), force_bytes("1"))
        self.assertEqual(
            force_bytes(inst.entity[0].role.display), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].role.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/object-role"),
        )
        self.assertEqual(force_bytes(inst.entity[0].type.code), force_bytes("1"))
        self.assertEqual(
            force_bytes(inst.entity[0].type.display), force_bytes("Person")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-entity-type"),
        )
        self.assertEqual(
            force_bytes(inst.entity[1].description),
            force_bytes("data about Everthing important"),
        )
        self.assertEqual(force_bytes(inst.entity[1].lifecycle.code), force_bytes("11"))
        self.assertEqual(
            force_bytes(inst.entity[1].lifecycle.display), force_bytes("Disclosure")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].lifecycle.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dicom-audit-lifecycle"),
        )
        self.assertEqual(force_bytes(inst.entity[1].name), force_bytes("Namne of What"))
        self.assertEqual(force_bytes(inst.entity[1].role.code), force_bytes("4"))
        self.assertEqual(
            force_bytes(inst.entity[1].role.display), force_bytes("Domain Resource")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].role.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/object-role"),
        )
        self.assertEqual(
            force_bytes(inst.entity[1].securityLabel[0].code), force_bytes("V")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].securityLabel[0].display),
            force_bytes("very restricted"),
        )
        self.assertEqual(
            force_bytes(inst.entity[1].securityLabel[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-Confidentiality"),
        )
        self.assertEqual(
            force_bytes(inst.entity[1].securityLabel[1].code), force_bytes("STD")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].securityLabel[1].display),
            force_bytes("sexually transmitted disease information sensitivity"),
        )
        self.assertEqual(
            force_bytes(inst.entity[1].securityLabel[1].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(
            force_bytes(inst.entity[1].securityLabel[2].code), force_bytes("DELAU")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].securityLabel[2].display),
            force_bytes("delete after use"),
        )
        self.assertEqual(
            force_bytes(inst.entity[1].securityLabel[2].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(force_bytes(inst.entity[1].type.code), force_bytes("2"))
        self.assertEqual(
            force_bytes(inst.entity[1].type.display), force_bytes("System Object")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-entity-type"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-disclosure"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("0"))
        self.assertEqual(
            force_bytes(inst.outcomeDesc), force_bytes("Successful  Disclosure")
        )
        self.assertEqual(
            force_bytes(inst.purposeOfEvent[0].coding[0].code), force_bytes("HMARKT")
        )
        self.assertEqual(
            force_bytes(inst.purposeOfEvent[0].coding[0].display),
            force_bytes("healthcare marketing"),
        )
        self.assertEqual(
            force_bytes(inst.purposeOfEvent[0].coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.recorded.date, FHIRDate("2013-09-22T00:08:00Z").date)
        self.assertEqual(inst.recorded.as_json(), "2013-09-22T00:08:00Z")
        self.assertEqual(force_bytes(inst.source.site), force_bytes("Watcher"))
        self.assertEqual(force_bytes(inst.source.type[0].code), force_bytes("4"))
        self.assertEqual(
            force_bytes(inst.source.type[0].display), force_bytes("Application Server")
        )
        self.assertEqual(
            force_bytes(inst.source.type[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/security-source-type"),
        )
        self.assertEqual(force_bytes(inst.subtype[0].code), force_bytes("Disclosure"))
        self.assertEqual(
            force_bytes(inst.subtype[0].display), force_bytes("HIPAA disclosure")
        )
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Disclosure by some idiot, for marketing reasons, to places unknown, of a Poor Sap, data about Everthing important.</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.code), force_bytes("110106"))
        self.assertEqual(force_bytes(inst.type.display), force_bytes("Export"))
        self.assertEqual(
            force_bytes(inst.type.system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )

    def testAuditEvent9(self):
        inst = self.instantiate_from("auditevent-example-error.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent9(inst)

        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent9(inst2)

    def implAuditEvent9(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("C"))
        self.assertEqual(force_bytes(inst.agent[0].altId), force_bytes("601847123"))
        self.assertEqual(force_bytes(inst.agent[0].name), force_bytes("Grahame Grieve"))
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].code), force_bytes("humanuser")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].display), force_bytes("human user")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].type.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/extra-security-role-type"
            ),
        )
        self.assertEqual(force_bytes(inst.agent[1].altId), force_bytes("6580"))
        self.assertEqual(
            force_bytes(inst.agent[1].network.address),
            force_bytes("Workstation1.ehr.familyclinic.com"),
        )
        self.assertEqual(force_bytes(inst.agent[1].network.type), force_bytes("1"))
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].code), force_bytes("110153")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].display),
            force_bytes("Source Role ID"),
        )
        self.assertEqual(
            force_bytes(inst.agent[1].type.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("o1"))
        self.assertEqual(
            force_bytes(inst.entity[0].detail[0].type),
            force_bytes("requested transaction"),
        )
        self.assertEqual(
            force_bytes(inst.entity[0].detail[0].valueString),
            force_bytes("http POST ..... "),
        )
        self.assertEqual(force_bytes(inst.entity[0].type.code), force_bytes("2"))
        self.assertEqual(
            force_bytes(inst.entity[0].type.display), force_bytes("System Object")
        )
        self.assertEqual(
            force_bytes(inst.entity[0].type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-entity-type"),
        )
        self.assertEqual(
            force_bytes(inst.entity[1].description), force_bytes("transaction failed")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].type.code), force_bytes("OperationOutcome")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].type.display), force_bytes("OperationOutcome")
        )
        self.assertEqual(
            force_bytes(inst.entity[1].type.system),
            force_bytes("http://hl7.org/fhir/resource-types"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-error"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("8"))
        self.assertEqual(
            force_bytes(inst.outcomeDesc),
            force_bytes(
                "Invalid request to create an Operation resource on the Patient endpoint."
            ),
        )
        self.assertEqual(inst.recorded.date, FHIRDate("2017-09-07T23:42:24Z").date)
        self.assertEqual(inst.recorded.as_json(), "2017-09-07T23:42:24Z")
        self.assertEqual(force_bytes(inst.source.site), force_bytes("Cloud"))
        self.assertEqual(force_bytes(inst.source.type[0].code), force_bytes("3"))
        self.assertEqual(
            force_bytes(inst.source.type[0].display), force_bytes("Web Server")
        )
        self.assertEqual(
            force_bytes(inst.source.type[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/security-source-type"),
        )
        self.assertEqual(force_bytes(inst.subtype[0].code), force_bytes("create"))
        self.assertEqual(force_bytes(inst.subtype[0].display), force_bytes("create"))
        self.assertEqual(
            force_bytes(inst.subtype[0].system),
            force_bytes("http://hl7.org/fhir/restful-interaction"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.code), force_bytes("rest"))
        self.assertEqual(
            force_bytes(inst.type.display), force_bytes("Restful Operation")
        )
        self.assertEqual(
            force_bytes(inst.type.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/audit-event-type"),
        )
