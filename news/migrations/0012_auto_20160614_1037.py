# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20160614_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsarticle',
            old_name='image',
            new_name='featured_image',
        ),
    ]