# Generated by Django 2.0.8 on 2018-08-21 17:16

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('pages', '0135_auto_20180806_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro_heading', models.CharField(max_length=255)),
                ('careers_content', wagtail.core.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
