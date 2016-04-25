# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20160424_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workcompleted',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
