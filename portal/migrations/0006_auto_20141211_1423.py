# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_remove_posts_title_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(default=datetime.datetime(2014, 12, 11, 14, 23, 28, 722775, tzinfo=utc), to='portal.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='title_slug',
            field=models.SlugField(default=datetime.datetime(2014, 12, 11, 14, 23, 51, 524090, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
            preserve_default=True,
        ),
    ]
