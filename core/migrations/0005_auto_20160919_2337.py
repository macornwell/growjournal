# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160919_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='site_users',
            field=models.ManyToManyField(blank=True, related_name='user_group', to=settings.AUTH_USER_MODEL),
        ),
    ]
