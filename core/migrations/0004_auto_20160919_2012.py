# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_usercoresettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_users',
            field=models.ManyToManyField(related_name='user_group', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
