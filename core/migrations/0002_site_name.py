# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=50, default=None),
            preserve_default=False,
        ),
    ]
