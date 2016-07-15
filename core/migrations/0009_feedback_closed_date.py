# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='closed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
