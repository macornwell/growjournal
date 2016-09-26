# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0005_auto_20160925_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteinventory',
            name='user',
        ),
    ]
