# Generated by Django 5.1 on 2024-08-09 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Inspection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("truck_serial_number", models.CharField(max_length=50)),
                ("truck_model", models.CharField(max_length=50)),
                (
                    "inspector_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "inspection_employee_id",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("date_time", models.DateTimeField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "geo_coordinates",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("service_meter_hours", models.FloatField(blank=True, null=True)),
                (
                    "customer_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "cat_customer_id",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("overall_summary", models.TextField(blank=True, null=True)),
                ("voice_of_customer", models.TextField(blank=True, null=True)),
                ("report_generated", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Exterior",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rust_dent_damage", models.BooleanField(default=False)),
                ("oil_leak", models.BooleanField(default=False)),
                ("image_path", models.CharField(blank=True, max_length=200, null=True)),
                ("summary", models.TextField(blank=True, null=True)),
                (
                    "inspection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inspections.inspection",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Engine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rust_dent_damage", models.BooleanField(default=False)),
                ("oil_condition", models.CharField(max_length=50)),
                ("oil_color", models.CharField(max_length=50)),
                ("brake_fluid_condition", models.CharField(max_length=50)),
                ("brake_fluid_color", models.CharField(max_length=50)),
                ("oil_leak", models.BooleanField(default=False)),
                ("image_path", models.CharField(blank=True, max_length=200, null=True)),
                ("summary", models.TextField(blank=True, null=True)),
                (
                    "inspection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inspections.inspection",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Brake",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fluid_level", models.CharField(max_length=50)),
                ("front_condition", models.CharField(max_length=50)),
                ("rear_condition", models.CharField(max_length=50)),
                ("emergency_brake_condition", models.CharField(max_length=50)),
                ("image_path", models.CharField(blank=True, max_length=200, null=True)),
                ("summary", models.TextField(blank=True, null=True)),
                (
                    "inspection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inspections.inspection",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Battery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("make", models.CharField(max_length=50)),
                ("replacement_date", models.DateTimeField(blank=True, null=True)),
                ("voltage", models.FloatField()),
                ("water_level", models.CharField(max_length=50)),
                ("condition", models.CharField(max_length=50)),
                ("leak_rust", models.BooleanField(default=False)),
                ("image_path", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "inspection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inspections.inspection",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tire",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.CharField(max_length=20)),
                ("pressure", models.FloatField()),
                ("condition", models.CharField(max_length=50)),
                ("image_path", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "inspection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inspections.inspection",
                    ),
                ),
            ],
        ),
    ]
