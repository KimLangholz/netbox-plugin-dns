from datetime import date

from django.test import TestCase

from netbox_dns.choices import RecordStatusChoices, RecordTypeChoices
from netbox_dns.models import NameServer, Record, Zone


class RecordExpirationTestSet(TestCase):
    @classmethod
    def setUpTestData(cls):
        zone = Zone.objects.create(
            name="zone1.example.com",
            soa_mname=NameServer.objects.create(name="ns1.example.com"),
            soa_rname="hostmaster.example.com",
        )

        cls.record_data = {
            "name": "name1",
            "zone": zone,
            "type": RecordTypeChoices.AAAA,
            "value": "2001:db8::1",
        }

    def test_expired(self):
        record = Record.objects.create(
            expiration_date="2026-06-02",
            **self.record_data,
        )

        self.assertTrue(record.is_expired)
        self.assertFalse(record.is_active)
        self.assertEqual(record.status, RecordStatusChoices.STATUS_EXPIRED)

    def test_expiration_date_in_future(self):
        record = Record.objects.create(
            expiration_date="2126-01-07",
            **self.record_data,
        )

        self.assertFalse(record.is_expired)
        self.assertTrue(record.is_active)
        self.assertNotEqual(record.status, RecordStatusChoices.STATUS_EXPIRED)

    def test_no_expiration(self):
        record = Record.objects.create(
            **self.record_data,
        )

        self.assertFalse(record.is_expired)
        self.assertTrue(record.is_active)
        self.assertNotEqual(record.status, RecordStatusChoices.STATUS_EXPIRED)

    def test_remove_expiration(self):
        record = Record.objects.create(
            expiration_date="2026-06-02",
            **self.record_data,
        )

        self.assertTrue(record.is_expired)
        self.assertFalse(record.is_active)
        self.assertEqual(record.status, RecordStatusChoices.STATUS_EXPIRED)

        record.expiration_date = None
        record.save()

        self.assertFalse(record.is_expired)
        self.assertFalse(record.is_active)
        self.assertEqual(record.status, RecordStatusChoices.STATUS_EXPIRED)

    def test_postpone_expiration_expired(self):
        record = Record.objects.create(
            expiration_date="2026-06-02",
            **self.record_data,
        )

        self.assertTrue(record.is_expired)
        self.assertFalse(record.is_active)
        self.assertEqual(record.status, RecordStatusChoices.STATUS_EXPIRED)

        record.expiration_date = date(2126, 1, 7)
        record.save()

        self.assertFalse(record.is_expired)
        self.assertFalse(record.is_active)
        self.assertEqual(record.status, RecordStatusChoices.STATUS_EXPIRED)
