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
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_started', models.DateField(null=True, default=django.utils.timezone.now, blank=True)),
                ('date_ended', models.DateField(null=True, blank=True)),
                ('is_perpetual', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True, blank=True)),
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
                ('site_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('is_public_viewable', models.BooleanField(default=True)),
                ('is_public_joinable', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('site_users', models.ManyToManyField(related_name='user_group', to=settings.AUTH_USER_MODEL, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserCoreSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_site', models.ForeignKey(null=True, to='core.Site', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
                ('website_feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('closed_date', models.DateTimeField(null=True, blank=True)),
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
    ]
