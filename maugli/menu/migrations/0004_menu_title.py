# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20160601_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
