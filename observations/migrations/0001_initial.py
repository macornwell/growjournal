# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('observation_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('affinity', models.CharField(choices=[('pos', 'Positive'), ('neu', 'Neutral'), ('neg', 'Negative')], max_length=3, default='neu')),
                ('summary', models.CharField(null=True, max_length=100, blank=True)),
                ('observation', models.TextField()),
                ('life_form', models.ForeignKey(null=True, to='taxonomy.LifeForm', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ObservationType',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('observation_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('kingdom_specific', models.ForeignKey(null=True, to='taxonomy.Kingdom', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('prediction_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('affinity', models.CharField(choices=[('pos', 'Positive'), ('neu', 'Neutral'), ('neg', 'Negative')], max_length=3, default='neu')),
                ('summary', models.CharField(null=True, max_length=100, blank=True)),
                ('details', models.TextField()),
                ('life_form', models.ForeignKey(null=True, to='taxonomy.LifeForm', blank=True)),
                ('observation', models.ForeignKey(null=True, to='observations.Observation', blank=True)),
                ('site', models.ForeignKey(to='core.Site')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='observation',
            name='observation_type',
            field=models.ForeignKey(to='observations.ObservationType'),
        ),
        migrations.AddField(
            model_name='observation',
            name='site',
            field=models.ForeignKey(to='core.Site'),
        ),
        migrations.AddField(
            model_name='observation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
