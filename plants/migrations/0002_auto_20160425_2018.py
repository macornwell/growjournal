# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantproductivityreport',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='unit',
            field=models.ForeignKey(to='core.Unit'),
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
