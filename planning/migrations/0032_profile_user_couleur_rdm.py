# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-03-31 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0031_profile_user_dernier_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_user',
            name='couleur_rdm',
            field=models.CharField(blank=True, default='#ff8f00', max_length=20),
        ),
    ]