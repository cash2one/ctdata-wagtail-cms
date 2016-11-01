# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-01 12:15
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ctdata', '0019_conferencepage_conferencesession_conferencesessionparticipants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencesession',
            name='conference',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.PROTECT, related_name='sessions', to='ctdata.ConferencePage'),
        ),
    ]
