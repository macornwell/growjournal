# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0001_initial'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivar',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('cultivar_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('name_denormalized', models.CharField(max_length=50, blank=True)),
                ('latin_name', models.CharField(max_length=50, blank=True)),
                ('history', models.TextField(null=True, blank=True)),
                ('origin_year', models.IntegerField(null=True, blank=True)),
                ('chromosome_count', models.IntegerField(null=True, blank=True)),
                ('origin_location', models.ForeignKey(null=True, to='geography.Location', blank=True)),
                ('parent_a', models.ForeignKey(related_name='first_children', null=True, to='taxonomy.Cultivar', blank=True)),
                ('parent_b', models.ForeignKey(related_name='second_children', null=True, to='taxonomy.Cultivar', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('genus_id', models.AutoField(primary_key=True, serialize=False)),
                ('latin_name', models.CharField(unique=True, max_length=30)),
                ('name', models.CharField(null=True, max_length=30, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kingdom',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('kingdom_id', models.AutoField(primary_key=True, serialize=False)),
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
                ('life_form_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('latin_name', models.CharField(max_length=50, blank=True)),
                ('cultivar', models.ForeignKey(null=True, to='taxonomy.Cultivar', blank=True)),
                ('genus', models.ForeignKey(to='taxonomy.Genus')),
                ('kingdom', models.ForeignKey(to='taxonomy.Kingdom')),
            ],
        ),
        migrations.CreateModel(
            name='Rootstock',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('rootstock_id', models.AutoField(primary_key=True, serialize=False)),
                ('denormalized_name', models.CharField(max_length=30)),
                ('dwarfing', models.CharField(choices=[('vd', 'Very-Dwarfing'), ('d', 'Dwarf'), ('sd', 'Semi-Dwarf'), ('f', 'Full-Size')], max_length=2)),
                ('cultivar', models.OneToOneField(to='taxonomy.Cultivar')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteInventory',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('site_inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.PositiveIntegerField(default=0)),
                ('life_form', models.ForeignKey(to='taxonomy.LifeForm')),
                ('site', models.ForeignKey(to='core.Site')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('species_id', models.AutoField(primary_key=True, serialize=False)),
                ('latin_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('genus', models.ForeignKey(to='taxonomy.Genus')),
                ('origin_location', models.ForeignKey(null=True, to='geography.Location', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTaxonomySettings',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('use_latin_name', models.BooleanField(default=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='lifeform',
            name='rootstock',
            field=models.ForeignKey(null=True, to='taxonomy.Rootstock', blank=True),
        ),
        migrations.AddField(
            model_name='lifeform',
            name='species',
            field=models.ForeignKey(to='taxonomy.Species'),
        ),
        migrations.AddField(
            model_name='genus',
            name='kingdom',
            field=models.ForeignKey(to='taxonomy.Kingdom'),
        ),
        migrations.AddField(
            model_name='cultivar',
            name='species',
            field=models.ForeignKey(to='taxonomy.Species'),
        ),
        migrations.AlterUniqueTogether(
            name='species',
            unique_together=set([('genus', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='siteinventory',
            unique_together=set([('site', 'life_form')]),
        ),
        migrations.AlterUniqueTogether(
            name='lifeform',
            unique_together=set([('kingdom', 'genus', 'species', 'cultivar', 'rootstock')]),
        ),
        migrations.AlterUniqueTogether(
            name='cultivar',
            unique_together=set([('species', 'name')]),
        ),
    ]
