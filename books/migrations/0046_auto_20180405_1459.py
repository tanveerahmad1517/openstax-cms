# Generated by Django 2.0.2 on 2018-04-05 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0045_auto_20180405_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='ally_content',
        ),
        migrations.RemoveField(
            model_name='book',
            name='bookstore',
        ),
        migrations.RemoveField(
            model_name='book',
            name='comp_copy_content',
        ),
        migrations.RemoveField(
            model_name='book',
            name='errata_content',
        ),
        migrations.RemoveField(
            model_name='book',
            name='free_stuff_instructor',
        ),
        migrations.RemoveField(
            model_name='book',
            name='free_stuff_student',
        ),
        migrations.RemoveField(
            model_name='book',
            name='webinar_content',
        ),
    ]