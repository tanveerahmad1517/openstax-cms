# Generated by Django 2.0.2 on 2018-05-17 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0027_auto_20180517_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pressindex',
            name='mentions',
        ),
    ]