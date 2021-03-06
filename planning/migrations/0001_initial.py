# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-03-20 08:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse_client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='N-A', max_length=50)),
                ('adresse', models.CharField(default='N-A', max_length=100)),
                ('ville', models.CharField(default='N-A', max_length=100)),
                ('code_postal', models.CharField(default='N-A', max_length=10)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Adresse',
            },
        ),
        migrations.CreateModel(
            name='bdd_messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'envoi")),
                ('lu', models.BooleanField(default=False)),
                ('envoyeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='envoyeur', to=settings.AUTH_USER_MODEL)),
                ('receveur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receveur', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Message',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='N-A', max_length=100)),
                ('code_couleur', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Mission_type_client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='N-A', max_length=50)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planning.Client')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Mission type',
            },
        ),
        migrations.CreateModel(
            name='Piece_jointe_client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='N-A', max_length=50)),
                ('document', models.FileField(blank=True, upload_to='piece_jointe_client/')),
                ('date_upload', models.DateField(auto_now_add=True)),
                ('is_favorite', models.BooleanField(default=False)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planning.Client')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Piece jointe',
            },
        ),
        migrations.CreateModel(
            name='Profile_consultant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diminutif', models.CharField(default='N-A', max_length=10)),
                ('telephone', models.CharField(default='N-A', max_length=20)),
                ('adresse', models.CharField(default='N-A', max_length=100)),
                ('archive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Statut_mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('code_couleur', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Mission statut',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='N-A', max_length=50)),
                ('archive', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['nom'],
                'verbose_name': 'Theme',
            },
        ),
        migrations.AddField(
            model_name='profile_consultant',
            name='theme_confirme',
            field=models.ManyToManyField(blank=True, related_name='theme_confirme', to='planning.Theme'),
        ),
        migrations.AddField(
            model_name='profile_consultant',
            name='theme_junior',
            field=models.ManyToManyField(blank=True, related_name='theme_junior', to='planning.Theme'),
        ),
        migrations.AddField(
            model_name='profile_consultant',
            name='theme_senior',
            field=models.ManyToManyField(blank=True, related_name='theme_senior', to='planning.Theme'),
        ),
        migrations.AddField(
            model_name='profile_consultant',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mission_type_client',
            name='theme',
            field=models.ManyToManyField(blank=True, to='planning.Theme'),
        ),
        migrations.AddField(
            model_name='adresse_client',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planning.Client'),
        ),
    ]
