# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import plants.mixins
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_project_completed'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloom',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('bloom_id', models.AutoField(primary_key=True, serialize=False)),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, plants.mixins.SpeciesOrCultivarMixin),
        ),
        migrations.CreateModel(
            name='Cultivar',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('plant_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('genus_id', models.AutoField(primary_key=True, serialize=False)),
                ('latin_name', models.CharField(unique=True, max_length=30, blank=True)),
                ('name', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('harvest_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlantProductivityReport',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('plant_productivity_report_id', models.AutoField(primary_key=True, serialize=False)),
                ('productivity', models.CharField(choices=[('0', 'None'), ('1', 'Very-Low'), ('2', 'Low'), ('3', 'Medium'), ('4', 'High'), ('5', 'Excessive')], max_length=1)),
                ('cultivar', models.ForeignKey(null=True, blank=True, to='plants.Cultivar')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, plants.mixins.SpeciesOrCultivarMixin),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('resource_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('description', models.TextField(null=True, blank=True)),
                ('cultivar', models.ForeignKey(null=True, blank=True, to='plants.Cultivar')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, plants.mixins.SpeciesOrCultivarMixin),
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('species_id', models.AutoField(primary_key=True, serialize=False)),
                ('latin_name', models.CharField(null=True, max_length=30, blank=True)),
                ('name', models.CharField(max_length=30)),
                ('genus', models.ForeignKey(to='plants.Genus', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Watering',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('watering_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('target', models.CharField(max_length=50)),
                ('project', models.ForeignKey(null=True, blank=True, to='core.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='resource',
            name='species',
            field=models.ForeignKey(null=True, blank=True, to='plants.Species'),
        ),
        migrations.AddField(
            model_name='plantproductivityreport',
            name='species',
            field=models.ForeignKey(null=True, blank=True, to='plants.Species'),
        ),
        migrations.AddField(
            model_name='plantproductivityreport',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='harvest',
            name='resource',
            field=models.ForeignKey(to='plants.Resource'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='unit',
            field=models.ForeignKey(to='plants.Unit'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cultivar',
            name='species',
            field=models.ForeignKey(to='plants.Species', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bloom',
            name='cultivar',
            field=models.ForeignKey(null=True, blank=True, to='plants.Cultivar'),
        ),
        migrations.AddField(
            model_name='bloom',
            name='species',
            field=models.ForeignKey(null=True, blank=True, to='plants.Species'),
        ),
        migrations.AddField(
            model_name='bloom',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='species',
            unique_together=set([('genus', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='cultivar',
            unique_together=set([('species', 'name')]),
        ),
    ]
