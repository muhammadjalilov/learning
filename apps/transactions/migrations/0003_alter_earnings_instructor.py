# Generated by Django 5.1.1 on 2024-09-30 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructors", "0002_rename_crated_at_instructor_created_at"),
        ("transactions", "0002_rename_crated_at_billingaddress_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="earnings",
            name="instructor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="earnings",
                to="instructors.instructor",
            ),
        ),
    ]
