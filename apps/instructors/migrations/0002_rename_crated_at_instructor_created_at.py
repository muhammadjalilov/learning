# Generated by Django 5.1.1 on 2024-09-29 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("instructors", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="instructor",
            old_name="crated_at",
            new_name="created_at",
        ),
    ]
