# Generated by Django 4.1.5 on 2023-01-27 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
        ("type", "0001_initial"),
        ("docs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doc",
            name="card",
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name="doc",
            name="store",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.store",
            ),
        ),
        migrations.AlterField(
            model_name="doc",
            name="type",
            field=models.ForeignKey(
                blank=True, on_delete=django.db.models.deletion.CASCADE, to="type.type"
            ),
        ),
    ]
