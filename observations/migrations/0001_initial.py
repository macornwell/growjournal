# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('observation_id', models.AutoField(serialize=False, primary_key=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('affinity', models.CharField(default='neu', choices=[('pos', 'Positive'), ('neu', 'Neutral'), ('neg', 'Negative')], max_length=3)),
                ('summary', models.CharField(null=True, blank=True, max_length=100)),
                ('observation', models.TextField()),
                ('grafted_life_form', models.ForeignKey(to='taxonomy.GraftedLifeForm', blank=True, null=True)),
                ('life_form', models.ForeignKey(to='taxonomy.LifeForm', blank=True, null=True)),
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
                ('observation_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('kingdom_specific', models.ForeignKey(to='taxonomy.Kingdom', blank=True, null=True)),
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
                ('prediction_id', models.AutoField(serialize=False, primary_key=True)),
                ('datetime', models.DateTimeField()),
                ('affinity', models.CharField(default='neu', choices=[('pos', 'Positive'), ('neu', 'Neutral'), ('neg', 'Negative')], max_length=3)),
                ('summary', models.CharField(null=True, blank=True, max_length=100)),
                ('details', models.TextField()),
                ('grafted_life_form', models.ForeignKey(to='taxonomy.GraftedLifeForm', blank=True, null=True)),
                ('life_form', models.ForeignKey(to='taxonomy.LifeForm', blank=True, null=True)),
                ('observation', models.ForeignKey(to='observations.Observation', blank=True, null=True)),
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
