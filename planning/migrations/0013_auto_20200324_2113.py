# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-03-24 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0012_competence_date_modification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='date_modification',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
