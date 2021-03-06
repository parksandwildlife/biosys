# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 01:56
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_auto_20161219_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('species_name',
                 models.CharField(blank=True, help_text='Species Name (as imported)', max_length=500, null=True,
                                  verbose_name='Species Name')),
                ('name_id', models.IntegerField(default=-1, help_text='The unique ID from the species database',
                                                verbose_name='Name ID')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Dataset')),
                ('site',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Site')),
            ],
        ),
    ]
