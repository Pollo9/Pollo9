# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-04-01 22:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0046_jour_bloque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='N-A', max_length=100)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planning.Client')),
                ('statut', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planning.Statut_contrat')),
            ],
            options={
                'verbose_name': 'Contrat',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Jour_annee_bloque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True)),
                ('est_recurrent', models.BooleanField(default=False)),
                ('est_bloque', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Jours année bloqué',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Jour_mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour_de_mission', models.DateField(blank=True)),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('mission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planning.Mission')),
            ],
            options={
                'verbose_name': 'Missions jour',
                'ordering': ['jour_de_mission'],
            },
        ),
        migrations.CreateModel(
            name='Jour_semaine_bloque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('numero_jour', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('est_recurrent', models.BooleanField(default=False)),
                ('est_bloque', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Jours semaine bloqué',
                'ordering': ['nom'],
            },
        ),
    ]