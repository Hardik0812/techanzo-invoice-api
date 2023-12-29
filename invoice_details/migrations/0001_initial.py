# Generated by Django 5.0 on 2023-12-29 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("currency", "0002_alter_currency_symbol"),
        ("customer", "0001_initial"),
    ]

    operations = [
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
                ("invoice_number", models.CharField(max_length=150)),
                ("date", models.DateField()),
                ("note", models.TextField(max_length=1000)),
                (
                    "currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="currency.currency",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="customer.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InvoiceDetails",
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
                ("sr_no", models.IntegerField()),
                ("description", models.TextField(max_length=1000)),
                ("rate", models.FloatField()),
                ("quantity", models.IntegerField()),
                ("price", models.FloatField()),
                ("sgst", models.FloatField()),
                ("cgst", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoice_details.invoice",
                    ),
                ),
            ],
        ),
    ]
