# Generated by Django 5.1.1 on 2024-09-30 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_rename_crated_at_account_created_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="card",
        ),
    ]
