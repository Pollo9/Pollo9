# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-03-27 11:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0016_auto_20200324_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_consultant',
            name='is_online',
        ),
    ]