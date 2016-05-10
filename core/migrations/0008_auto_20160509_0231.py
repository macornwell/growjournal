# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20160509_0217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='notes_id',
            new_name='feedback_id',
        ),
    ]
