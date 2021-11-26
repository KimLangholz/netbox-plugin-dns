# Generated by Django 3.2.9 on 2021-11-26 16:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_dns", "0005_update_ns_records"),
    ]

    operations = [
        migrations.AddField(
            model_name="zone",
            name="soa_serial_auto",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="zone",
            name="soa_serial",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(4294967295),
                ],
            ),
        ),
    ]
