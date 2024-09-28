# Generated by Django 5.1.1 on 2024-09-27 17:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0001_initial"),
        ("instructors", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CreditCard",
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
                ("crated_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("card_number", models.CharField(max_length=16, unique=True)),
                ("expired_date", models.DateField()),
                ("cvv", models.CharField(max_length=3)),
            ],
            options={
                "verbose_name": "Credit Card",
                "verbose_name_plural": "Credit Cards",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="BillingAddress",
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
                ("crated_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("country", models.CharField(max_length=30)),
                ("address", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billing_addresses",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "credit_cards",
                    models.ManyToManyField(
                        related_name="billing_addresses", to="transactions.creditcard"
                    ),
                ),
            ],
            options={
                "verbose_name": "Billing Address",
                "verbose_name_plural": "Billing Addresses",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Earnings",
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
                ("crated_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("gross_revenue", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "instructor",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="earnings",
                        to="instructors.instructor",
                    ),
                ),
            ],
            options={
                "verbose_name": "Earnings",
                "verbose_name_plural": "Earnings",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Invoice",
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
                ("crated_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("paid_status", models.BooleanField(default=False)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "billing_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoices",
                        to="transactions.billingaddress",
                    ),
                ),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoices",
                        to="courses.course",
                    ),
                ),
                (
                    "credit_card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoices",
                        to="transactions.creditcard",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoices",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Invoice",
                "verbose_name_plural": "Invoices",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Transactions",
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
                ("crated_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("paid_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="transactions.invoice",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Transactions",
                "verbose_name_plural": "Transactions",
                "ordering": ["id"],
            },
        ),
    ]
