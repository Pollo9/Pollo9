# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-03-20 09:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0003_remove_theme_archive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
            ],
            options={
                'verbose_name': 'Competence',
                'ordering': ['nom'],
            },
        ),
        migrations.AlterModelOptions(
            name='mission',
            options={'ordering': ['jour_de_mission'], 'verbose_name': 'Mission'},
        ),
        migrations.AlterModelOptions(
            name='profile_consultant',
            options={'ordering': ['id'], 'verbose_name': 'Profile Consultant'},
        ),
        migrations.RemoveField(
            model_name='profile_consultant',
            name='theme_confirme',
        ),
        migrations.RemoveField(
            model_name='profile_consultant',
            name='theme_junior',
        ),
        migrations.RemoveField(
            model_name='profile_consultant',
            name='theme_senior',
        ),
        migrations.AddField(
            model_name='competence',
            name='consultant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planning.Profile_consultant'),
        ),
        migrations.AddField(
            model_name='competence',
            name='nom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planning.Theme'),
        ),
    ]
