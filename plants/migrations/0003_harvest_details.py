# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20160425_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvest',
            name='details',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
    ]
