# Generated by Django 5.1.1 on 2024-09-29 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="billingaddress",
            old_name="crated_at",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="creditcard",
            old_name="crated_at",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="earnings",
            old_name="crated_at",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="invoice",
            old_name="crated_at",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="transactions",
            old_name="crated_at",
            new_name="created_at",
        ),
    ]
