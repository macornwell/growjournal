# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_auto_20160926_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='location',
        ),
    ]
