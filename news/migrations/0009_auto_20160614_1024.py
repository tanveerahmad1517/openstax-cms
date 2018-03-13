# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 15:24
from __future__ import unicode_literals

from django.db import migrations
import news.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_newsarticle_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='body',
            field=wagtail.core.fields.StreamField((('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock()), ('alignment', news.models.ImageFormatChoiceBlock())), icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', news.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')))),
        ),
    ]
