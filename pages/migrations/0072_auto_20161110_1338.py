# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 19:38
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0071_auto_20161109_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='questions',
            field=wagtail.wagtailcore.fields.StreamField((('question', wagtail.wagtailcore.blocks.StructBlock((('question', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('slug', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('answer', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))))),)),
        ),
    ]
