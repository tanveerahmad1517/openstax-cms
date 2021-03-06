# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-06 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_settings', '0003_auto_20160906_1348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stickynote',
            options={'verbose_name': 'Sticky Note'},
        ),
        migrations.RenameField(
            model_name='stickynote',
            old_name='give_sticky_expires',
            new_name='expires',
        ),
        migrations.RenameField(
            model_name='stickynote',
            old_name='show_sticky',
            new_name='show',
        ),
        migrations.RemoveField(
            model_name='stickynote',
            name='sticky_content',
        ),
        migrations.AddField(
            model_name='stickynote',
            name='content',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stickynote',
            name='header',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
