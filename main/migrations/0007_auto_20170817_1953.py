# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-17 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170817_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='number',
            field=models.PositiveIntegerField(unique=True, verbose_name='题目编号'),
        ),
    ]