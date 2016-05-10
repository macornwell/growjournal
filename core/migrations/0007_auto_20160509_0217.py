# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_auto_20160427_2249'),
    ]

    operations = [
        migrations.RenameModel(
            new_name='Feedback',
            old_name='note'

        ),
    ]
