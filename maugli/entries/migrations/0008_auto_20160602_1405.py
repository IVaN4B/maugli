# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_remove_menulink_entry'),
        ('entries', '0007_entry_links'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='links',
        ),
        migrations.AddField(
            model_name='entry',
            name='links',
            field=models.ManyToManyField(blank=True, null=True, related_name='entry', to='menu.MenuLink'),
        ),
    ]
