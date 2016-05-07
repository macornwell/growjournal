# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0006_auto_20160427_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherreading',
            name='unit',
            field=models.CharField(default='f', max_length=1, choices=[('f', 'Fahrenheit'), ('c', 'Celsius')]),
        ),
        migrations.AddField(
            model_name='weatherreading',
            name='value',
            field=models.DecimalField(decimal_places=2, default=-1, max_digits=8),
            preserve_default=False,
        ),
    ]
