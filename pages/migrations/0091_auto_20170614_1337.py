# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-14 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('pages', '0090_resource_resourceavailability'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro_heading', models.CharField(max_length=255)),
                ('intro_description', models.TextField()),
                ('banner_cta', models.CharField(max_length=255)),
                ('select_tech_heading', models.CharField(max_length=255)),
                ('select_tech_step_1', models.CharField(max_length=255)),
                ('select_tech_step_2', models.CharField(max_length=255)),
                ('select_tech_step_3', models.CharField(max_length=255)),
                ('new_frontier_heading', models.CharField(max_length=255)),
                ('new_frontier_subheading', models.CharField(max_length=255)),
                ('new_frontier_description', models.TextField()),
                ('new_frontier_cta_1', models.CharField(max_length=255)),
                ('new_frontier_cta_2', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='resource',
            name='alternate_text',
            field=models.CharField(blank=True, help_text='If this has text, availability is ignored.', max_length=255, null=True),
        ),
    ]
