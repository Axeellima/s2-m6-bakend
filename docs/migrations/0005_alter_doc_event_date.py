# Generated by Django 4.1.5 on 2023-01-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("docs", "0004_alter_doc_hour"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doc",
            name="event_date",
            field=models.DateField(null=True),
        ),
    ]