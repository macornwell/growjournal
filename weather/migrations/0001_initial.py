# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


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
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('unit', models.CharField(choices=[('f', 'Fahrenheit'), ('c', 'Celsius')], max_length=1, default='f')),
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
                ('temperature', models.DecimalField(decimal_places=2, max_digits=8)),
                ('unit', models.CharField(choices=[('f', 'Fahrenheit'), ('c', 'Celsius')], max_length=1, default='f')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
