# Generated by Django 5.1 on 2024-08-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inspections", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="InspectionResult",
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
                ("section", models.CharField(max_length=100)),
                ("text_result", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
