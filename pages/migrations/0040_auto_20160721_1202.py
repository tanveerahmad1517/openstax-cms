# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 17:02
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0039_auto_20160721_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='row_1',
            field=wagtail.core.fields.StreamField((('multicolumn', wagtail.core.blocks.StreamBlock((('column', wagtail.core.blocks.StructBlock((('column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('cta', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock()), ('quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('author', wagtail.core.blocks.CharBlock()))))), icon='placeholder', label='Column content')),))),))),)),
        ),
    ]
