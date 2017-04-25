# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
        ('geography', '0001_initial'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeployEvent',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('planting_record', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.TextField(null=True, blank=True)),
                ('count', models.PositiveIntegerField(null=True, blank=True)),
                ('life_form', models.ForeignKey(to='taxonomy.LifeForm')),
                ('location_detail', models.ForeignKey(null=True, to='geography.Location', blank=True)),
                ('project', models.ForeignKey(null=True, to='core.Project', blank=True)),
                ('site', models.ForeignKey(to='core.Site')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
