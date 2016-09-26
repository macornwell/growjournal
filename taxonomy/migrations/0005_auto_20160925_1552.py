# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0003_auto_20160925_1552'),
        ('taxonomy', '0004_auto_20160921_1547'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='graftedlifeform',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='graftedlifeform',
            name='rootstock',
        ),
        migrations.RemoveField(
            model_name='graftedlifeform',
            name='scion',
        ),
        migrations.DeleteModel(
            name='GraftedLifeForm',
        ),
    ]
