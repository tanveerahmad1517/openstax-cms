# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-12 15:37
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20160707_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('person', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(required=True)), ('position', wagtail.core.blocks.CharBlock(required=True)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('biography', wagtail.core.blocks.RichTextBlock())))))),
        ),
    ]
