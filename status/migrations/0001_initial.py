# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-15 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment', models.TextField()),
                ('severity', models.IntegerField()),
                ('description', models.TextField()),
                ('outage_start', models.DateTimeField()),
                ('outage_detected', models.DateTimeField()),
                ('outage_ended', models.DateTimeField()),
                ('timezone', models.CharField(max_length=3, null=True)),
                ('what_affected', models.TextField()),
                ('who_affected', models.TextField()),
                ('it_owner', models.TextField()),
                ('rca', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
