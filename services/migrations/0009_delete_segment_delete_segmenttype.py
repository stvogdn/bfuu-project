# Generated by Django 4.1.7 on 2023-04-05 23:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0008_alter_service_speaker"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Segment",
        ),
        migrations.DeleteModel(
            name="SegmentType",
        ),
    ]