from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_rename_crated_at_category_created_at_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={"ordering": ["-id"]},
        ),
    ]
