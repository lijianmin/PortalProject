# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
        ('portal', '0011_auto_20150524_0518'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('article_UUID', django_extensions.db.fields.UUIDField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=200, db_index=True)),
                ('title_slug', models.SlugField(max_length=200, unique=True)),
                ('bodytext', models.TextField()),
                ('view_count', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comments_enabled', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='portal.category')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', to='taggit.Tag')),
            ],
            options={
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]
