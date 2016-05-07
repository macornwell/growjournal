# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0007_auto_20160507_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherreading',
            old_name='value',
            new_name='temperature',
        ),
    ]
