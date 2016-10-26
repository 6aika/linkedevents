# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-09 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_add_api_keys_for_external_data_sources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='api_key',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
