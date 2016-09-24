# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160919_2337'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxonomy', '0002_auto_20160717_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInventory',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('site_inventory_id', models.AutoField(serialize=False, primary_key=True)),
                ('count', models.PositiveIntegerField(default=0)),
                ('life_form', models.ForeignKey(to='taxonomy.LifeForm')),
                ('site', models.ForeignKey(to='core.Site')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
