# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-03-31 13:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0041_profile_user_couleur_rdm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_user',
            name='couleur_rdm',
        ),
    ]
