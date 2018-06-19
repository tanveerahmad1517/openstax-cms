# Generated by Django 2.0.2 on 2018-05-15 21:03

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0014_auto_20180509_1010'),
        ('wagtailimages', '0019_delete_filter'),
        ('news', '0020_auto_20180509_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertsBios',
            fields=[
                ('experts_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news.Experts')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('news.experts', models.Model),
        ),
        migrations.CreateModel(
            name='MissionStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MissionStatements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model, modelcluster.fields.ParentalKey),
        ),
        migrations.CreateModel(
            name='NewsMention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('headline', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='expertspr',
            name='experts_pr',
        ),
        migrations.RemoveField(
            model_name='expertspr',
            name='experts_ptr',
        ),
        migrations.RenameField(
            model_name='experts',
            old_name='blurb',
            new_name='bio',
        ),
        migrations.AddField(
            model_name='experts',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='pressindex',
            name='experts_blurb',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pressindex',
            name='experts_heading',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pressindex',
            name='press_inquiry_email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pressindex',
            name='press_inquiry_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pressindex',
            name='press_inquiry_phone',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pressrelease',
            name='excerpt',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='NewsMentions',
            fields=[
                ('newsmention_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news.NewsMention')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('news_mentions', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_mentions', to='news.PressIndex')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('news.newsmention', models.Model),
        ),
        migrations.DeleteModel(
            name='ExpertsPR',
        ),
        migrations.AddField(
            model_name='newsmention',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='snippets.NewsSource'),
        ),
        migrations.AddField(
            model_name='missionstatements',
            name='mission_statements',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='mission_statements', to='news.PressIndex'),
        ),
        migrations.AddField(
            model_name='expertsbios',
            name='experts_bios',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='experts_bios', to='news.PressIndex'),
        ),
    ]