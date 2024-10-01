# Generated by Django 5.1.1 on 2024-10-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0006_remove_billingaddress_credit_cards"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="billingaddress",
            options={
                "verbose_name": "Billing Address",
                "verbose_name_plural": "Billing Addresses",
            },
        ),
        migrations.AddField(
            model_name="billingaddress",
            name="name",
            field=models.CharField(
                default=1, max_length=128, verbose_name="Name on Invoice"
            ),
            preserve_default=False,
        ),
    ]
