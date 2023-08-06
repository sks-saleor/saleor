# Generated by Django 3.2.18 on 2023-05-29 11:25

import django.contrib.postgres.indexes
from django.db import migrations
from django.contrib.postgres.operations import AddIndexConcurrently


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0183_calculate_discounted_prices"),
    ]

    atomic = False

    operations = [
        AddIndexConcurrently(
            model_name="product",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["name", "slug"],
                name="product_gin",
                opclasses=["gin_trgm_ops", "gin_trgm_ops"],
            ),
        ),
    ]