# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-04-01 19:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0044_auto_20200331_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statut_contrat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='N-A', max_length=100)),
                ('code_couleur', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name': 'Contrat statut',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Statut_journee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='N-A', max_length=100)),
                ('code_couleur', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name': 'Journée statut',
                'ordering': ['nom'],
            },
        ),
        migrations.AlterModelOptions(
            name='statut_mission',
            options={'ordering': ['nom'], 'verbose_name': 'Mission statut'},
        ),
        migrations.AlterField(
            model_name='competence',
            name='note',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='statut_mission',
            name='nom',
            field=models.CharField(default='N-A', max_length=100),
        ),
    ]
