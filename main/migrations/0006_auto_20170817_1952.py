# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-17 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170817_1943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['number'], 'verbose_name': '题目', 'verbose_name_plural': '题目'},
        ),
        migrations.RenameField(
            model_name='problem',
            old_name='order',
            new_name='number',
        ),
    ]
