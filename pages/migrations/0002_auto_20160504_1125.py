# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='classroom_text',
        ),
        migrations.AddField(
            model_name='contactus',
            name='mailing_address',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='mailing_header',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='phone_number',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='tagline',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]