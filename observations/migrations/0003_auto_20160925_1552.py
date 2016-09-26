# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0002_auto_20160717_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observation',
            name='grafted_life_form',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='grafted_life_form',
        ),
    ]
