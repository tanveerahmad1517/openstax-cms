# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-19 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('pages', '0094_auto_20170919_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketing',
            name='section_4_paragraph',
            field=wagtail.wagtailcore.fields.RichTextField(default='Thousands of students have piloted OpenStax Tutor Beta. Here are the features we’ve prioritized, and more are on the way. Have suggestions for future development? Send us an email at info@openstaxtutor.org.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marketing',
            name='section_4_resource_fine_print',
            field=models.CharField(default='*Available for OpenStax Tutor Beta for College Physics', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='available_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(help_text='Resources should be added in pairs to display properly.', max_length=255),
        ),
    ]