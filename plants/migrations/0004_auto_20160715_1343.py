# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import plants.mixins
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plants', '0003_harvest_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantReport',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('plant_report_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('affinity', models.CharField(max_length=3, default='neu', choices=[('pos', 'Positive'), ('neu', 'Neutral'), ('neg', 'Negative')])),
                ('summary', models.CharField(blank=True, null=True, max_length=50)),
                ('report_details', models.TextField()),
                ('cultivar', models.ForeignKey(to='plants.Cultivar', blank=True, null=True)),
                ('species', models.ForeignKey(to='plants.Species', blank=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, plants.mixins.SpeciesOrCultivarMixin),
        ),
        migrations.AddField(
            model_name='harvest',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plantproductivityreport',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
