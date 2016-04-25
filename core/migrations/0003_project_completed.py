# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160424_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
