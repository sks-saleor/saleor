# Generated by Django 1.10.3 on 2016-12-12 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("product", "0016_auto_20161204_0311")]

    operations = [
        migrations.AddField(
            model_name="attributechoicevalue",
            name="slug",
            field=models.SlugField(default=""),
            preserve_default=False,
        )
    ]
