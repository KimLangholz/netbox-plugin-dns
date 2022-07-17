# Generated by Django 4.0.3 on 2022-07-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_dns", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="nameserver",
            name="description",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="record",
            name="description",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="zone",
            name="description",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
