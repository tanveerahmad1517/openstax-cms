# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-05 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0089_marketingvideolink_marketingvideos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('available', models.BooleanField(default=False)),
                ('alternate_text', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceAvailability',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Resource')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('marketing_video', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_availability', to='pages.Marketing')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('pages.resource', models.Model),
        ),
    ]
