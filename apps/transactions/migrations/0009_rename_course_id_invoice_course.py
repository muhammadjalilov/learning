# Generated by Django 5.1.1 on 2024-10-02 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0008_alter_billingaddress_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="invoice",
            old_name="course_id",
            new_name="course",
        ),
    ]
