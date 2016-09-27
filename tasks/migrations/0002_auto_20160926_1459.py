# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskoutput',
            name='unit',
            field=models.ForeignKey(to='core.Unit'),
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
