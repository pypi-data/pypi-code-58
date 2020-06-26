# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Encounter
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

from .. import encounter
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class EncounterTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Encounter", js["resourceType"])
        return encounter.Encounter(js)

    def testEncounter1(self):
        inst = self.instantiate_from("encounter-example-home.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter1(inst)

        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter1(inst2)

    def implEncounter1(self, inst):
        self.assertEqual(force_bytes(inst.class_fhir.code), force_bytes("HH"))
        self.assertEqual(
            force_bytes(inst.class_fhir.display), force_bytes("home health")
        )
        self.assertEqual(
            force_bytes(inst.class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("home"))
        self.assertEqual(force_bytes(inst.id), force_bytes("home"))
        self.assertEqual(
            inst.location[0].period.end.date, FHIRDate("2015-01-17T16:30:00+10:00").date
        )
        self.assertEqual(
            inst.location[0].period.end.as_json(), "2015-01-17T16:30:00+10:00"
        )
        self.assertEqual(
            inst.location[0].period.start.date,
            FHIRDate("2015-01-17T16:00:00+10:00").date,
        )
        self.assertEqual(
            inst.location[0].period.start.as_json(), "2015-01-17T16:00:00+10:00"
        )
        self.assertEqual(force_bytes(inst.location[0].status), force_bytes("completed"))
        self.assertEqual(
            inst.participant[0].period.end.date,
            FHIRDate("2015-01-17T16:30:00+10:00").date,
        )
        self.assertEqual(
            inst.participant[0].period.end.as_json(), "2015-01-17T16:30:00+10:00"
        )
        self.assertEqual(
            inst.participant[0].period.start.date,
            FHIRDate("2015-01-17T16:00:00+10:00").date,
        )
        self.assertEqual(
            inst.participant[0].period.start.as_json(), "2015-01-17T16:00:00+10:00"
        )
        self.assertEqual(
            inst.period.end.date, FHIRDate("2015-01-17T16:30:00+10:00").date
        )
        self.assertEqual(inst.period.end.as_json(), "2015-01-17T16:30:00+10:00")
        self.assertEqual(
            inst.period.start.date, FHIRDate("2015-01-17T16:00:00+10:00").date
        )
        self.assertEqual(inst.period.start.as_json(), "2015-01-17T16:00:00+10:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("finished"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Encounter with patient @example who is at home</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testEncounter2(self):
        inst = self.instantiate_from("encounter-example-f201-20130404.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter2(inst)

        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter2(inst2)

    def implEncounter2(self, inst):
        self.assertEqual(force_bytes(inst.class_fhir.code), force_bytes("AMB"))
        self.assertEqual(
            force_bytes(inst.class_fhir.display), force_bytes("ambulatory")
        )
        self.assertEqual(
            force_bytes(inst.class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f201"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("temp"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("Encounter_Roel_20130404"),
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("17621005")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].display), force_bytes("Normal")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.reason[0].text),
            force_bytes(
                "The patient had fever peaks over the last couple of days. He is worried about these peaks."
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("finished"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].code), force_bytes("11429006")
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].display), force_bytes("Consultation")
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )

    def testEncounter3(self):
        inst = self.instantiate_from("encounter-example-f003-abscess.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter3(inst)

        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter3(inst2)

    def implEncounter3(self, inst):
        self.assertEqual(force_bytes(inst.class_fhir.code), force_bytes("AMB"))
        self.assertEqual(
            force_bytes(inst.class_fhir.display), force_bytes("ambulatory")
        )
        self.assertEqual(
            force_bytes(inst.class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].code),
            force_bytes("305956004"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].display),
            force_bytes("Referral by physician"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dischargeDisposition.coding[0].code),
            force_bytes("306689006"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dischargeDisposition.coding[0].display),
            force_bytes("Discharge to home"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dischargeDisposition.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.preAdmissionIdentifier.system),
            force_bytes("http://www.bmc.nl/zorgportal/identifiers/pre-admissions"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.preAdmissionIdentifier.use),
            force_bytes("official"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.preAdmissionIdentifier.value),
            force_bytes("93042"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f003"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/zorgportal/identifiers/encounters"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("v6751"))
        self.assertEqual(force_bytes(inst.length.code), force_bytes("min"))
        self.assertEqual(
            force_bytes(inst.length.system), force_bytes("http://unitsofmeasure.org")
        )
        self.assertEqual(force_bytes(inst.length.unit), force_bytes("min"))
        self.assertEqual(inst.length.value, 90)
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("103391001")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].display),
            force_bytes("Non-urgent ear, nose and throat admission"),
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].code), force_bytes("18099001")
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].display),
            force_bytes("Retropharyngeal abscess"),
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.reason[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/encounter-primaryDiagnosis"
            ),
        )
        self.assertEqual(inst.reason[0].extension[0].valuePositiveInt, 1)
        self.assertEqual(force_bytes(inst.status), force_bytes("finished"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].code), force_bytes("270427003")
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].display),
            force_bytes("Patient-initiated encounter"),
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )

    def testEncounter4(self):
        inst = self.instantiate_from("encounter-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter4(inst)

        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter4(inst2)

    def implEncounter4(self, inst):
        self.assertEqual(force_bytes(inst.class_fhir.code), force_bytes("IMP"))
        self.assertEqual(
            force_bytes(inst.class_fhir.display), force_bytes("inpatient encounter")
        )
        self.assertEqual(
            force_bytes(inst.class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.status), force_bytes("in-progress"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Encounter with patient @example</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testEncounter5(self):
        inst = self.instantiate_from("encounter-example-f002-lung.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter5(inst)

        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter5(inst2)

    def implEncounter5(self, inst):
        self.assertEqual(force_bytes(inst.class_fhir.code), force_bytes("AMB"))
        self.assertEqual(
            force_bytes(inst.class_fhir.display), force_bytes("ambulatory")
        )
        self.assertEqual(
            force_bytes(inst.class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].code),
            force_bytes("305997006"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].display),
            force_bytes("Referral by radiologist"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dischargeDisposition.coding[0].code),
            force_bytes("306689006"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dischargeDisposition.coding[0].display),
            force_bytes("Discharge to home"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dischargeDisposition.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.preAdmissionIdentifier.system),
            force_bytes("http://www.bmc.nl/zorgportal/identifiers/pre-admissions"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.preAdmissionIdentifier.use),
            force_bytes("official"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.preAdmissionIdentifier.value),
            force_bytes("98682"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f002"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/zorgportal/identifiers/encounters"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("v3251"))
        self.assertEqual(force_bytes(inst.length.code), force_bytes("min"))
        self.assertEqual(
            force_bytes(inst.length.system), force_bytes("http://unitsofmeasure.org")
        )
        self.assertEqual(force_bytes(inst.length.unit), force_bytes("min"))
        self.assertEqual(inst.length.value, 140)
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("103391001")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].display), force_bytes("Urgent")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].code), force_bytes("34068001")
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].display),
            force_bytes("Partial lobectomy of lung"),
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("finished"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].code), force_bytes("270427003")
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].display),
            force_bytes("Patient-initiated encounter"),
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )

    def testEncounter6(self):
        inst = self.instantiate_from("encounter-example-f203-20130311.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter6(inst)

        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter6(inst2)

    def implEncounter6(self, inst):
        self.assertEqual(force_bytes(inst.class_fhir.code), force_bytes("IMP"))
        self.assertEqual(
            force_bytes(inst.class_fhir.display), force_bytes("inpatient encounter")
        )
        self.assertEqual(
            force_bytes(inst.class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(inst.diagnosis[0].rank, 1)
        self.assertEqual(
            force_bytes(inst.diagnosis[0].role.coding[0].code), force_bytes("AD")
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[0].role.coding[0].display),
            force_bytes("Admission diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[0].role.coding[0].system),
            force_bytes("http://hl7.org/fhir/diagnosis-role"),
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[1].role.coding[0].code), force_bytes("DD")
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[1].role.coding[0].display),
            force_bytes("Discharge diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[1].role.coding[0].system),
            force_bytes("http://hl7.org/fhir/diagnosis-role"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].code),
            force_bytes("309902002"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].display),
            force_bytes("Clinical Oncology Department"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dietPreference[0].coding[0].code),
            force_bytes("276026009"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dietPreference[0].coding[0].display),
            force_bytes("Fluid balance regulation"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dietPreference[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.reAdmission.coding[0].display),
            force_bytes("readmitted"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.specialArrangement[0].coding[0].code),
            force_bytes("wheel"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.specialArrangement[0].coding[0].display),
            force_bytes("Wheelchair"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.specialArrangement[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/encounter-special-arrangements"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.specialCourtesy[0].coding[0].code),
            force_bytes("NRM"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.specialCourtesy[0].coding[0].display),
            force_bytes("normal courtesy"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.specialCourtesy[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/EncounterSpecialCourtesy"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f203"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("temp"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("Encounter_Roel_20130311"),
        )
        self.assertEqual(
            force_bytes(inst.participant[0].type[0].coding[0].code), force_bytes("PART")
        )
        self.assertEqual(
            force_bytes(inst.participant[0].type[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/ParticipationType"),
        )
        self.assertEqual(inst.period.end.date, FHIRDate("2013-03-20").date)
        self.assertEqual(inst.period.end.as_json(), "2013-03-20")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.period.start.as_json(), "2013-03-11")
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("394849002")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].display), force_bytes("High priority")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.reason[0].text),
            force_bytes(
                "The patient seems to suffer from bilateral pneumonia and renal insufficiency, most likely due to chemotherapy."
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("finished"))
        self.assertEqual(
            inst.statusHistory[0].period.start.date, FHIRDate("2013-03-08").date
        )
        self.assertEqual(inst.statusHistory[0].period.start.as_json(), "2013-03-08")
        self.assertEqual(
            force_bytes(inst.statusHistory[0].status), force_bytes("arrived")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].code), force_bytes("183807002")
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].display),
            force_bytes("Inpatient stay for nine days"),
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )

    def testEncounter7(self):
        inst = self.instantiate_from("encounter-example-xcda.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter7(inst)

        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter7(inst2)

    def implEncounter7(self, inst):
        self.assertEqual(force_bytes(inst.class_fhir.code), force_bytes("AMB"))
        self.assertEqual(
            force_bytes(inst.class_fhir.display), force_bytes("ambulatory")
        )
        self.assertEqual(
            force_bytes(inst.class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("xcda"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://healthcare.example.org/identifiers/enocunter"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("1234213.52345873")
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].code), force_bytes("T-D8200")
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].display), force_bytes("Arm")
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].system),
            force_bytes("http://ihe.net/xds/connectathon/eventCodes"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("finished"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testEncounter8(self):
        inst = self.instantiate_from("encounter-example-f202-20130128.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter8(inst)

        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter8(inst2)

    def implEncounter8(self, inst):
        self.assertEqual(force_bytes(inst.class_fhir.code), force_bytes("AMB"))
        self.assertEqual(
            force_bytes(inst.class_fhir.display), force_bytes("ambulatory")
        )
        self.assertEqual(
            force_bytes(inst.class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(inst.diagnosis[0].rank, 1)
        self.assertEqual(
            force_bytes(inst.diagnosis[0].role.coding[0].code), force_bytes("AD")
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[0].role.coding[0].display),
            force_bytes("Admission diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[0].role.coding[0].system),
            force_bytes("http://hl7.org/fhir/diagnosis-role"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f202"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("temp"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("Encounter_Roel_20130128"),
        )
        self.assertEqual(force_bytes(inst.length.code), force_bytes("min"))
        self.assertEqual(
            force_bytes(inst.length.system), force_bytes("http://unitsofmeasure.org")
        )
        self.assertEqual(force_bytes(inst.length.unit), force_bytes("minutes"))
        self.assertEqual(inst.length.value, 56)
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("103391001")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].display), force_bytes("Urgent")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.reason[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/encounter-primaryDiagnosis"
            ),
        )
        self.assertEqual(inst.reason[0].extension[0].valuePositiveInt, 2)
        self.assertEqual(
            force_bytes(inst.reason[0].text),
            force_bytes("The patient is treated for a tumor."),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("finished"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].code), force_bytes("367336001")
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].display), force_bytes("Chemotherapy")
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )

    def testEncounter9(self):
        inst = self.instantiate_from("encounter-example-emerg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter9(inst)

        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter9(inst2)

    def implEncounter9(self, inst):
        self.assertEqual(
            force_bytes(inst.classHistory[0].class_fhir.code), force_bytes("EMER")
        )
        self.assertEqual(
            force_bytes(inst.classHistory[0].class_fhir.display),
            force_bytes("emergency"),
        )
        self.assertEqual(
            force_bytes(inst.classHistory[0].class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(
            inst.classHistory[0].period.end.date,
            FHIRDate("2017-02-01T09:27:00+10:00").date,
        )
        self.assertEqual(
            inst.classHistory[0].period.end.as_json(), "2017-02-01T09:27:00+10:00"
        )
        self.assertEqual(
            inst.classHistory[0].period.start.date,
            FHIRDate("2017-02-01T07:15:00+10:00").date,
        )
        self.assertEqual(
            inst.classHistory[0].period.start.as_json(), "2017-02-01T07:15:00+10:00"
        )
        self.assertEqual(
            force_bytes(inst.classHistory[1].class_fhir.code), force_bytes("IMP")
        )
        self.assertEqual(
            force_bytes(inst.classHistory[1].class_fhir.display),
            force_bytes("inpatient encounter"),
        )
        self.assertEqual(
            force_bytes(inst.classHistory[1].class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(
            inst.classHistory[1].period.start.date,
            FHIRDate("2017-02-01T09:27:00+10:00").date,
        )
        self.assertEqual(
            inst.classHistory[1].period.start.as_json(), "2017-02-01T09:27:00+10:00"
        )
        self.assertEqual(force_bytes(inst.class_fhir.code), force_bytes("IMP"))
        self.assertEqual(
            force_bytes(inst.class_fhir.display), force_bytes("inpatient encounter")
        )
        self.assertEqual(
            force_bytes(inst.class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].code),
            force_bytes("emd"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].display),
            force_bytes("From accident/emergency department"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].system),
            force_bytes("http://hl7.org/fhir/admit-source"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("emerg"))
        self.assertEqual(
            inst.location[0].period.end.date, FHIRDate("2017-02-01T08:45:00+10:00").date
        )
        self.assertEqual(
            inst.location[0].period.end.as_json(), "2017-02-01T08:45:00+10:00"
        )
        self.assertEqual(
            inst.location[0].period.start.date,
            FHIRDate("2017-02-01T07:15:00+10:00").date,
        )
        self.assertEqual(
            inst.location[0].period.start.as_json(), "2017-02-01T07:15:00+10:00"
        )
        self.assertEqual(force_bytes(inst.location[0].status), force_bytes("active"))
        self.assertEqual(
            inst.location[1].period.end.date, FHIRDate("2017-02-01T09:27:00+10:00").date
        )
        self.assertEqual(
            inst.location[1].period.end.as_json(), "2017-02-01T09:27:00+10:00"
        )
        self.assertEqual(
            inst.location[1].period.start.date,
            FHIRDate("2017-02-01T08:45:00+10:00").date,
        )
        self.assertEqual(
            inst.location[1].period.start.as_json(), "2017-02-01T08:45:00+10:00"
        )
        self.assertEqual(force_bytes(inst.location[1].status), force_bytes("active"))
        self.assertEqual(
            inst.location[2].period.end.date, FHIRDate("2017-02-01T12:15:00+10:00").date
        )
        self.assertEqual(
            inst.location[2].period.end.as_json(), "2017-02-01T12:15:00+10:00"
        )
        self.assertEqual(
            inst.location[2].period.start.date,
            FHIRDate("2017-02-01T09:27:00+10:00").date,
        )
        self.assertEqual(
            inst.location[2].period.start.as_json(), "2017-02-01T09:27:00+10:00"
        )
        self.assertEqual(force_bytes(inst.location[2].status), force_bytes("active"))
        self.assertEqual(
            inst.location[3].period.end.date, FHIRDate("2017-02-01T12:45:00+10:00").date
        )
        self.assertEqual(
            inst.location[3].period.end.as_json(), "2017-02-01T12:45:00+10:00"
        )
        self.assertEqual(
            inst.location[3].period.start.date,
            FHIRDate("2017-02-01T12:15:00+10:00").date,
        )
        self.assertEqual(
            inst.location[3].period.start.as_json(), "2017-02-01T12:15:00+10:00"
        )
        self.assertEqual(force_bytes(inst.location[3].status), force_bytes("reserved"))
        self.assertEqual(
            inst.location[4].period.start.date,
            FHIRDate("2017-02-01T12:45:00+10:00").date,
        )
        self.assertEqual(
            inst.location[4].period.start.as_json(), "2017-02-01T12:45:00+10:00"
        )
        self.assertEqual(force_bytes(inst.location[4].status), force_bytes("active"))
        self.assertEqual(
            inst.period.start.date, FHIRDate("2017-02-01T07:15:00+10:00").date
        )
        self.assertEqual(inst.period.start.as_json(), "2017-02-01T07:15:00+10:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("in-progress"))
        self.assertEqual(
            inst.statusHistory[0].period.end.date,
            FHIRDate("2017-02-01T07:35:00+10:00").date,
        )
        self.assertEqual(
            inst.statusHistory[0].period.end.as_json(), "2017-02-01T07:35:00+10:00"
        )
        self.assertEqual(
            inst.statusHistory[0].period.start.date,
            FHIRDate("2017-02-01T07:15:00+10:00").date,
        )
        self.assertEqual(
            inst.statusHistory[0].period.start.as_json(), "2017-02-01T07:15:00+10:00"
        )
        self.assertEqual(
            force_bytes(inst.statusHistory[0].status), force_bytes("arrived")
        )
        self.assertEqual(
            inst.statusHistory[1].period.end.date,
            FHIRDate("2017-02-01T08:45:00+10:00").date,
        )
        self.assertEqual(
            inst.statusHistory[1].period.end.as_json(), "2017-02-01T08:45:00+10:00"
        )
        self.assertEqual(
            inst.statusHistory[1].period.start.date,
            FHIRDate("2017-02-01T07:35:00+10:00").date,
        )
        self.assertEqual(
            inst.statusHistory[1].period.start.as_json(), "2017-02-01T07:35:00+10:00"
        )
        self.assertEqual(
            force_bytes(inst.statusHistory[1].status), force_bytes("triaged")
        )
        self.assertEqual(
            inst.statusHistory[2].period.end.date,
            FHIRDate("2017-02-01T12:15:00+10:00").date,
        )
        self.assertEqual(
            inst.statusHistory[2].period.end.as_json(), "2017-02-01T12:15:00+10:00"
        )
        self.assertEqual(
            inst.statusHistory[2].period.start.date,
            FHIRDate("2017-02-01T08:45:00+10:00").date,
        )
        self.assertEqual(
            inst.statusHistory[2].period.start.as_json(), "2017-02-01T08:45:00+10:00"
        )
        self.assertEqual(
            force_bytes(inst.statusHistory[2].status), force_bytes("in-progress")
        )
        self.assertEqual(
            inst.statusHistory[3].period.end.date,
            FHIRDate("2017-02-01T12:45:00+10:00").date,
        )
        self.assertEqual(
            inst.statusHistory[3].period.end.as_json(), "2017-02-01T12:45:00+10:00"
        )
        self.assertEqual(
            inst.statusHistory[3].period.start.date,
            FHIRDate("2017-02-01T12:15:00+10:00").date,
        )
        self.assertEqual(
            inst.statusHistory[3].period.start.as_json(), "2017-02-01T12:15:00+10:00"
        )
        self.assertEqual(
            force_bytes(inst.statusHistory[3].status), force_bytes("onleave")
        )
        self.assertEqual(
            inst.statusHistory[4].period.start.date,
            FHIRDate("2017-02-01T12:45:00+10:00").date,
        )
        self.assertEqual(
            inst.statusHistory[4].period.start.as_json(), "2017-02-01T12:45:00+10:00"
        )
        self.assertEqual(
            force_bytes(inst.statusHistory[4].status), force_bytes("in-progress")
        )
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Emergency visit that escalated into inpatient patient @example</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testEncounter10(self):
        inst = self.instantiate_from("encounter-example-f001-heart.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter10(inst)

        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter10(inst2)

    def implEncounter10(self, inst):
        self.assertEqual(force_bytes(inst.class_fhir.code), force_bytes("AMB"))
        self.assertEqual(
            force_bytes(inst.class_fhir.display), force_bytes("ambulatory")
        )
        self.assertEqual(
            force_bytes(inst.class_fhir.system),
            force_bytes("http://hl7.org/fhir/v3/ActCode"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].code),
            force_bytes("305956004"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].display),
            force_bytes("Referral by physician"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.admitSource.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dischargeDisposition.coding[0].code),
            force_bytes("306689006"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dischargeDisposition.coding[0].display),
            force_bytes("Discharge to home"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.dischargeDisposition.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.preAdmissionIdentifier.system),
            force_bytes("http://www.amc.nl/zorgportal/identifiers/pre-admissions"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.preAdmissionIdentifier.use),
            force_bytes("official"),
        )
        self.assertEqual(
            force_bytes(inst.hospitalization.preAdmissionIdentifier.value),
            force_bytes("93042"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("f001"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.amc.nl/zorgportal/identifiers/visits"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("v1451"))
        self.assertEqual(force_bytes(inst.length.code), force_bytes("min"))
        self.assertEqual(
            force_bytes(inst.length.system), force_bytes("http://unitsofmeasure.org")
        )
        self.assertEqual(force_bytes(inst.length.unit), force_bytes("min"))
        self.assertEqual(inst.length.value, 140)
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("310361003")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].display),
            force_bytes("Non-urgent cardiological admission"),
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].code), force_bytes("34068001")
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].display),
            force_bytes("Heart valve replacement"),
        )
        self.assertEqual(
            force_bytes(inst.reason[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("finished"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].code), force_bytes("270427003")
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].display),
            force_bytes("Patient-initiated encounter"),
        )
        self.assertEqual(
            force_bytes(inst.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
