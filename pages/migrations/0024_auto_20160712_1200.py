# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-12 17:00
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_auto_20160712_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('tagline', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('person', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(required=True)), ('position', wagtail.core.blocks.CharBlock(required=True)), ('photo', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('biography', wagtail.core.blocks.RichTextBlock())))), ('content_row', wagtail.core.blocks.StructBlock((('content_block', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('hidden', wagtail.core.blocks.BooleanBlock(required=False))))),))), ('list', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=True)), ('description', wagtail.core.blocks.RichTextBlock()), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))))),
        ),
    ]
