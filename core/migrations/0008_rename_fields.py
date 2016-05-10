# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20160509_0217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Feedback',
            new_name='feedback_id',
            old_name='note_id',
        ),
        migrations.RenameField(
            model_name='Feedback',
            new_name='feedback',
            old_name='notes',
        ),
    ]
