# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('livestock', '0003_auto_20160427_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalReport',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('animal_report_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('affinity', models.CharField(max_length=3, default='neu', choices=[('pos', 'Positive'), ('neu', 'Neutral'), ('neg', 'Negative')])),
                ('summary', models.CharField(blank=True, null=True, max_length=50)),
                ('report_details', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='animalmovement',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='animalmovement',
            name='user',
        ),
        migrations.DeleteModel(
            name='Animal',
        ),
        migrations.DeleteModel(
            name='AnimalMovement',
        ),
    ]
