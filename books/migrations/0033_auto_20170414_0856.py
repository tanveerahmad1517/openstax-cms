# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0032_book_comp_copy_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='comp_copy_available',
            field=models.BooleanField(default=True),
        ),
    ]