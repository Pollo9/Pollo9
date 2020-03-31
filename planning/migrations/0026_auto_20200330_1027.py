# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-03-30 08:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0025_auto_20200330_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='consultant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
