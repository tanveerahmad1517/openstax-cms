# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-28 19:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0099_auto_20170928_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketing',
            name='icon_1_image',
        ),
    ]