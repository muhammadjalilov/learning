# Generated by Django 5.1.1 on 2024-10-05 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0003_student_period"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="period",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 10, 5, 5, 5, 45, 586117, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
