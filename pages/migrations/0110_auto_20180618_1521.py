# Generated by Django 2.0.2 on 2018-06-18 20:21

from django.db import migrations, models
import django.db.models.deletion
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
        ('pages', '0109_printorder_featured_provider_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('who_heading', models.CharField(max_length=255)),
                ('who_paragraph', wagtail.core.fields.RichTextField()),
                ('what_heading', models.CharField(max_length=255)),
                ('what_paragraph', wagtail.core.fields.RichTextField()),
                ('what_cards', wagtail.core.fields.StreamField((('card', wagtail.core.blocks.StreamBlock((('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('paragraph', wagtail.core.blocks.TextBlock())), icon='placeholder')),))),
                ('where_heading', models.CharField(max_length=255)),
                ('where_paragraph', wagtail.core.fields.RichTextField()),
                ('where_map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'homepage'},
        ),
    ]