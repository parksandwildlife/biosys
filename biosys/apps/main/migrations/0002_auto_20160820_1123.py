# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-20 03:23
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='attributes_schema',
            new_name='attributes_data_package',
        ),
        migrations.RemoveField(
            model_name='site',
            name='attributes_schema',
        ),
        migrations.RemoveField(
            model_name='site',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='site',
            name='longitude',
        ),
        migrations.AddField(
            model_name='project',
            name='site_data_package',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(help_text='Enter a name for the project (required).', max_length=300, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='site',
            name='geometry',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_code',
            field=models.CharField(help_text='Local site code must be unique to this project. e.g. LCI123 (required)', max_length=100, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_name',
            field=models.CharField(blank=True, help_text='Enter a more descriptive name for this site, if one exists.', max_length=150, verbose_name='Name'),
        ),
    ]
