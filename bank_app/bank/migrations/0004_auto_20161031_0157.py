# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20161030_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(),
        ),
    ]
