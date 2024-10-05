# Generated by Django 5.1.1 on 2024-10-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_alter_course_options"),
        ("transactions", "0011_alter_invoice_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="course",
            field=models.ManyToManyField(related_name="invoices", to="courses.course"),
        ),
    ]
