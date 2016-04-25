# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0003_temperaturereading_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='observation',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='observation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='temperaturereading',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='weatherreading',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='weatherreading',
            name='state',
            field=models.CharField(choices=[('s', 'Sunny'), ('p', 'Partly Cloudy'), ('c', 'Cloudy'), ('o', 'Overcast'), ('r', 'Rainy'), ('f', 'Freeze'), ('r', 'Frost'), ('n', 'Snow')], max_length=1),
        ),
    ]
