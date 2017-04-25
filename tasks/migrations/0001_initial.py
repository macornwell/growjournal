# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('ended', models.DateTimeField(null=True, blank=True)),
                ('summary', models.CharField(null=True, max_length=100, blank=True)),
                ('details', models.TextField()),
                ('project', models.ForeignKey(to='core.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskOutput',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('task_output_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('details', models.TextField(null=True, blank=True)),
                ('life_form', models.ForeignKey(null=True, to='taxonomy.LifeForm', blank=True)),
                ('task', models.ForeignKey(to='tasks.Task')),
                ('unit', models.ForeignKey(to='core.Unit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('task_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.ForeignKey(to='tasks.TaskType'),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
