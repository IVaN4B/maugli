# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20160606_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlist',
            name='column',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='columns',
        ),
        migrations.AddField(
            model_name='column',
            name='value',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='ProductList',
        ),
    ]
