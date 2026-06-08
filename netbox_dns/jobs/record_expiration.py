from datetime import date, datetime

from django.db.models import F
from django.utils.translation import gettext_lazy as _

from core.choices import JobIntervalChoices
from netbox.jobs import JobRunner, system_job
from netbox_dns.models import Record


@system_job(interval=JobIntervalChoices.INTERVAL_DAILY)
class RecordExpirationJob(JobRunner):
    class Meta:
        name = "Handle expired records"

    def run(self, *args, **kwargs):
        self.logger.info(_("Checking record expiration"))

        expired_records = Record.objects.filter(
            expiration_date__isnull=False,
            expiration_date__lte=date.today(),
            expiration_date__gte=F("last_updated"),
        )

        if not expired_records.exists():
            self.logger.info(_("No expired records found"))
            return

        update_zones = set()

        for record in expired_records:
            self.logger.info(
                _("Updating expired record {record}").format(record=record)
            )

            update_zones.add(record.zone)

            record.last_updated = datetime.now()
            super(Record, record).save()

        for zone in update_zones:
            self.logger.info(_("Updating SOA_SERIAL for zone {zone}").format(zone=zone))

            zone.update_serial()
