#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2019-05-14.
#  2019, SMART Health IT.


import io
import json
import os
import unittest

from . import subscription
from .fhirdate import FHIRDate


class SubscriptionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Subscription", js["resourceType"])
        return subscription.Subscription(js)

    def testSubscription1(self):
        inst = self.instantiate_from("subscription-example-error.json")
        self.assertIsNotNone(inst, "Must have instantiated a Subscription instance")
        self.implSubscription1(inst)

        js = inst.as_json()
        self.assertEqual("Subscription", js["resourceType"])
        inst2 = subscription.Subscription(js)
        self.implSubscription1(inst2)

    def implSubscription1(self, inst):
        self.assertEqual(
            inst.channel.endpoint,
            "https://biliwatch.com/customers/mount-auburn-miu/on-result",
        )
        self.assertEqual(
            inst.channel.header, "Authorization: Bearer secret-token-abc-123"
        )
        self.assertEqual(inst.channel.payload, "application/json")
        self.assertEqual(inst.channel.type, "rest-hook")
        self.assertEqual(inst.contact[0].system, "phone")
        self.assertEqual(inst.contact[0].value, "ext 4123")
        self.assertEqual(inst.criteria, "Observation?code=http://loinc.org|1975-2")
        self.assertEqual(inst.end.date, FHIRDate("2021-01-01T00:00:00Z").date)
        self.assertEqual(inst.end.as_json(), "2021-01-01T00:00:00Z")
        self.assertEqual(inst.error, "Socket Error 10060 - can't connect to host")
        self.assertEqual(inst.id, "example-error")
        self.assertEqual(inst.reason, "Monitor new neonatal function")
        self.assertEqual(inst.status, "error")
        self.assertEqual(inst.tag[0].code, "bili-done")
        self.assertEqual(inst.tag[0].system, "http://example.org/fhir/cs/internal")
        self.assertEqual(inst.text.div, "<div>[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

    def testSubscription2(self):
        inst = self.instantiate_from("subscription-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Subscription instance")
        self.implSubscription2(inst)

        js = inst.as_json()
        self.assertEqual("Subscription", js["resourceType"])
        inst2 = subscription.Subscription(js)
        self.implSubscription2(inst2)

    def implSubscription2(self, inst):
        self.assertEqual(
            inst.channel.endpoint,
            "https://biliwatch.com/customers/mount-auburn-miu/on-result",
        )
        self.assertEqual(
            inst.channel.header, "Authorization: Bearer secret-token-abc-123"
        )
        self.assertEqual(inst.channel.payload, "application/json")
        self.assertEqual(inst.channel.type, "rest-hook")
        self.assertEqual(inst.contact[0].system, "phone")
        self.assertEqual(inst.contact[0].value, "ext 4123")
        self.assertEqual(inst.criteria, "Observation?code=http://loinc.org|1975-2")
        self.assertEqual(inst.end.date, FHIRDate("2021-01-01T00:00:00Z").date)
        self.assertEqual(inst.end.as_json(), "2021-01-01T00:00:00Z")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.reason, "Monitor new neonatal function")
        self.assertEqual(inst.status, "requested")
        self.assertEqual(inst.tag[0].code, "bili-done")
        self.assertEqual(inst.tag[0].system, "http://example.org/fhir/cs/internal")
        self.assertEqual(inst.text.div, "<div>[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")
