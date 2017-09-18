# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0002_auto_20170829_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sighting',
            name='source',
        ),
        migrations.AddField(
            model_name='pokemonzone',
            name='guild',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonzone',
            name='destination',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='sightingmessage',
            name='channel',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='sightingmessage',
            name='message',
            field=models.BigIntegerField(),
        ),
    ]