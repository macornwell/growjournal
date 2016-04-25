# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0004_auto_20160424_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='observation',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
