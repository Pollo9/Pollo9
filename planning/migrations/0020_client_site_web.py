# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-03-28 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0019_auto_20200328_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='site_web',
            field=models.CharField(default='N-A', max_length=100),
        ),
    ]
