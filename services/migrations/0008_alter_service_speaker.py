# Generated by Django 4.1.7 on 2023-04-03 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0007_alter_service_speaker"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="speaker",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="services.speaker"
            ),
        ),
    ]
