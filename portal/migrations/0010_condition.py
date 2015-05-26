# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('portal', '0009_auto_20150429_0435'),
    ]

    operations = [
        migrations.CreateModel(
            name='condition',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, db_index=True, max_length=250)),
                ('name_slug', models.SlugField(max_length=200)),
                ('condition_UUID', django_extensions.db.fields.UUIDField(editable=False, null=True, blank=True)),
                ('overview', models.TextField()),
                ('transmission', models.TextField()),
                ('symptoms', models.TextField()),
                ('complications', models.TextField()),
                ('diagnosis', models.TextField()),
                ('treatment', models.TextField()),
                ('prevention', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='portal.category')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', verbose_name='Tags', help_text='A comma-separated list of tags.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
