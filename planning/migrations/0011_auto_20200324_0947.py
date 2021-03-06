# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-03-24 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0010_auto_20200322_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='avatar',
            field=models.ImageField(default='avatar/default.png', upload_to='avatar'),
        ),
        migrations.AddField(
            model_name='client',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
