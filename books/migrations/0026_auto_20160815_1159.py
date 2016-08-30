# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0025_auto_20160719_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='short_description',
        ),
        migrations.AlterField(
            model_name='book',
            name='amazon_blurb',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookstore_blurb',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='license_text',
            field=models.TextField(blank=True, help_text='Text blurb that describes the license.', null=True),
        ),
        migrations.AlterField(
            model_name='bookindex',
            name='page_description',
            field=models.TextField(),
        ),
    ]