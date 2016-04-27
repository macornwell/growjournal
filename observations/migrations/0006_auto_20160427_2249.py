# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0005_auto_20160424_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherreading',
            name='state',
            field=models.CharField(choices=[('s', 'Sunny'), ('p', 'Partly Cloudy'), ('c', 'Cloudy'), ('o', 'Overcast'), ('r', 'Rainy'), ('f', 'Freeze'), ('t', 'Frost'), ('n', 'Snow')], max_length=1),
        ),
    ]
