# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_menulink_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menulink',
            name='weight',
        ),
    ]
