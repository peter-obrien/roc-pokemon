# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0004_pokemonzone_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonzone',
            name='radius',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=5),
        ),
    ]
