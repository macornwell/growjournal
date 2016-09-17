# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('project_id', models.AutoField(serialize=False, primary_key=True)),
                ('date_started', models.DateField(default=django.utils.timezone.now, blank=True, null=True)),
                ('date_ended', models.DateField(blank=True, null=True)),
                ('is_perpetual', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_public_viewable', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('site_id', models.AutoField(serialize=False, primary_key=True)),
                ('is_public_viewable', models.BooleanField(default=True)),
                ('is_public_joinable', models.BooleanField(default=False)),
                ('site_users', models.ManyToManyField(related_name='user_group', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WebsiteFeedback',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('website_feedback_id', models.AutoField(serialize=False, primary_key=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('closed_date', models.DateTimeField(blank=True, null=True)),
                ('feedback', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='project',
            name='site',
            field=models.ForeignKey(to='core.Site'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
