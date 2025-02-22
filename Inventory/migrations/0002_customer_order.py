# Generated by Django 5.0.6 on 2024-06-05 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Inventory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=12, null=True),
                ),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=6
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Processing", "Processing"),
                            ("Shipped", "Shipped"),
                            ("Delivered", "Delivered"),
                            ("Cancelled", "Cancelled"),
                        ],
                        default="Pending",
                        max_length=20,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="Inventory.customer",
                    ),
                ),
            ],
        ),
    ]
