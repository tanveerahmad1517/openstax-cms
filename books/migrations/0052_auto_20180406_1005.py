# Generated by Django 2.0.2 on 2018-04-06 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0051_bookcommunityresources'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='community_resources',
            new_name='community_resource_content',
        ),
    ]