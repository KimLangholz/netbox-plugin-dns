from datetime import date

from django.utils.translation import gettext_lazy as _

from core.choices import JobIntervalChoices
from netbox.jobs import JobRunner, system_job
from netbox_dns.choices import RecordStatusChoices
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
        ).exclude(status=RecordStatusChoices.STATUS_EXPIRED)

        if not expired_records.exists():
            self.logger.info(_("No expired records found"))
            return

        for record in expired_records:
            self.logger.info(
                _("Setting record {record} status to {status}").format(
                    record=record, status=RecordStatusChoices.STATUS_EXPIRED
                )
            )

            record.status = RecordStatusChoices.STATUS_EXPIRED
            record.save()
