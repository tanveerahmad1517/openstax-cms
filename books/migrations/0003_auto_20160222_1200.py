# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160218_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_ap',
            field=models.BooleanField(default=False),
        ),
    ]