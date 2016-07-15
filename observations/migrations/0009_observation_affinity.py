# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0008_auto_20160507_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='affinity',
            field=models.CharField(max_length=3, default='neu', choices=[('pos', 'Positive'), ('neu', 'Neutral'), ('neg', 'Negative')]),
        ),
    ]
