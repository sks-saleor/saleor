# Generated by Django 3.2.20 on 2023-07-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0059_merge_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='language_code',
            field=models.CharField(choices=[('en', 'English'), ('en-us', 'English (United States)'), ('km', 'Khmer'), ('km-kh', 'Khmer (Cambodia)')], default='en', max_length=35),
        ),
    ]