# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taxonomy.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('genus_id', models.AutoField(serialize=False, primary_key=True)),
                ('latin_name', models.CharField(unique=True, max_length=30)),
                ('name', models.CharField(null=True, blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GraftedLifeForm',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('grafted_life_form_id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kingdom',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('kingdom_id', models.AutoField(serialize=False, primary_key=True)),
                ('latin_name', models.CharField(unique=True, max_length=30)),
                ('name', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LifeForm',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('life_form_id', models.AutoField(serialize=False, primary_key=True)),
                ('genus', models.ForeignKey(to='taxonomy.Genus')),
                ('kingdom', models.ForeignKey(to='taxonomy.Kingdom')),
            ],
        ),
        migrations.CreateModel(
            name='Rootstock',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('rootstock_id', models.AutoField(serialize=False, primary_key=True)),
                ('denormalized_name', models.CharField(max_length=30)),
                ('dwarfing', models.CharField(choices=[('vd', 'Very-Dwarfing'), ('d', 'Dwarf'), ('sd', 'Semi-Dwarf'), ('f', 'Full-Size')], max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('species_id', models.AutoField(serialize=False, primary_key=True)),
                ('latin_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('genus', models.ForeignKey(to='taxonomy.Genus')),
                ('origin_location', models.ForeignKey(to='geography.Location', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTaxonomySettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('use_latin_name', models.BooleanField(default=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('variety_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('history', models.TextField(blank=True, null=True)),
                ('origin_year', models.IntegerField(blank=True, null=True)),
                ('chromosome_count', models.IntegerField(blank=True, null=True)),
                ('origin_location', models.ForeignKey(to='geography.Location', blank=True, null=True)),
                ('parent_a', models.ForeignKey(related_name='first_children', to='taxonomy.Variety', blank=True, null=True)),
                ('parent_b', models.ForeignKey(related_name='second_children', to='taxonomy.Variety', blank=True, null=True)),
                ('species', models.ForeignKey(to='taxonomy.Species')),
            ],
        ),
        migrations.AddField(
            model_name='rootstock',
            name='variety',
            field=models.OneToOneField(to='taxonomy.Variety'),
        ),
        migrations.AddField(
            model_name='lifeform',
            name='rootstock',
            field=models.ForeignKey(to='taxonomy.Rootstock', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lifeform',
            name='species',
            field=models.ForeignKey(to='taxonomy.Species'),
        ),
        migrations.AddField(
            model_name='lifeform',
            name='variety',
            field=models.ForeignKey(to='taxonomy.Variety', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='graftedlifeform',
            name='rootstock',
            field=models.ForeignKey(default=taxonomy.models.get_unknown_rootstock, to='taxonomy.Rootstock'),
        ),
        migrations.AddField(
            model_name='graftedlifeform',
            name='scion',
            field=models.ForeignKey(to='taxonomy.LifeForm'),
        ),
        migrations.AddField(
            model_name='genus',
            name='kingdom',
            field=models.ForeignKey(to='taxonomy.Kingdom'),
        ),
        migrations.AlterUniqueTogether(
            name='variety',
            unique_together=set([('species', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='species',
            unique_together=set([('genus', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='lifeform',
            unique_together=set([('kingdom', 'genus', 'species', 'variety', 'rootstock')]),
        ),
        migrations.AlterUniqueTogether(
            name='graftedlifeform',
            unique_together=set([('scion', 'rootstock')]),
        ),
    ]
