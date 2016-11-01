# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-01 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctdata', '0022_auto_20161101_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencesession',
            name='conference',
            field=models.ForeignKey(blank=True, help_text='Leave blank if you want to add session to the parent conference.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sessions', to='ctdata.ConferencePage'),
        ),
    ]
