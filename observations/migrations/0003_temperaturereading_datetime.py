# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0002_auto_20160423_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperaturereading',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
