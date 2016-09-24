# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0003_siteinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifeform',
            name='latin_name',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='lifeform',
            name='name',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='variety',
            name='latin_name',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='variety',
            name='name_denormalized',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
