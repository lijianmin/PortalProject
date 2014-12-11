# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('category_name', models.CharField(max_length=100)),
                ('created_datetime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('title_slug', models.SlugField()),
                ('bodytext', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('category', models.ForeignKey(to='portal.category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
