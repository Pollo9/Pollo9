# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-04-02 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0049_delete_jour_bloque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jour_semaine_bloque',
            name='est_recurrent',
        ),
    ]
