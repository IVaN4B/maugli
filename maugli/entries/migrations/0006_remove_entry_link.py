# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 13:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0005_remove_entry_alias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='link',
        ),
    ]
