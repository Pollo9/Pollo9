# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-03-20 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0002_mission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='archive',
        ),
    ]
