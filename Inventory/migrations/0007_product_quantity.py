# Generated by Django 5.0.6 on 2024-06-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Inventory", "0006_remove_product_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
