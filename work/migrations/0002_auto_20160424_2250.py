# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160424_1435'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkCompleted',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('work_completed_id', models.AutoField(serialize=False, primary_key=True)),
                ('datetime', models.DateTimeField()),
                ('summary', models.CharField(max_length=50, null=True, blank=True)),
                ('work', models.TextField()),
                ('project', models.ForeignKey(to='core.Project', blank=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='work',
            name='project',
        ),
        migrations.RemoveField(
            model_name='work',
            name='user',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]
