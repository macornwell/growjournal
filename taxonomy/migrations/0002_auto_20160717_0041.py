# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graftedlifeform',
            name='rootstock',
            field=models.ForeignKey(to='taxonomy.Rootstock'),
        ),
    ]
