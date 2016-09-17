# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TemperatureReading',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('temperature_reading_id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(max_digits=8, decimal_places=2)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('unit', models.CharField(default='f', choices=[('f', 'Fahrenheit'), ('c', 'Celsius')], max_length=1)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeatherReading',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('weather_reading_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('state', models.CharField(choices=[('s', 'Sunny'), ('p', 'Partly Cloudy'), ('c', 'Cloudy'), ('o', 'Overcast'), ('r', 'Rainy'), ('f', 'Freeze'), ('t', 'Frost'), ('n', 'Snow')], max_length=1)),
                ('temperature', models.DecimalField(max_digits=8, decimal_places=2)),
                ('unit', models.CharField(default='f', choices=[('f', 'Fahrenheit'), ('c', 'Celsius')], max_length=1)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
