# Generated by Django 2.0.2 on 2018-04-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0011_delete_communityresource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedcontent',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]