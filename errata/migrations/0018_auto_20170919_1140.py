# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-19 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errata', '0017_auto_20170419_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errata',
            name='resolution',
            field=models.CharField(blank=True, choices=[('Duplicate', 'Duplicate'), ('Not An Error', 'Not An Error'), ('Will Not Fix', 'Will Not Fix'), ('Approved', 'Approved'), ('Major Book Revision', 'Major Book Revision'), ('Sent to Customer Support', 'Sent to Customer Support')], max_length=100, null=True),
        ),
    ]
