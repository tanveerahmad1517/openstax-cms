# Generated by Django 2.0.2 on 2018-07-26 18:25

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0131_remove_teampage_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='people',
            field=wagtail.core.fields.StreamField((('person', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('bio', wagtail.core.blocks.CharBlock(required=False)), ('photo', pages.models.APIImageChooserBlock(required=False))), icon='user')),)),
        ),
    ]