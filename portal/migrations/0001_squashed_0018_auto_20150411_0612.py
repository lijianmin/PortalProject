# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    replaces = [('portal', '0001_initial'), ('portal', '0002_post_comments_enabled'), ('portal', '0003_post_published'), ('portal', '0004_category_definition'), ('portal', '0005_auto_20150110_0347'), ('portal', '0006_auto_20150110_0350'), ('portal', '0007_auto_20150111_1228'), ('portal', '0008_auto_20150122_1537'), ('portal', '0009_auto_20150124_0401'), ('portal', '0010_auto_20150125_1539'), ('portal', '0011_auto_20150206_1449'), ('portal', '0012_auto_20150207_0626'), ('portal', '0013_auto_20150207_1700'), ('portal', '0014_auto_20150316_1430'), ('portal', '0015_auto_20150408_1543'), ('portal', '0016_auto_20150408_1552'), ('portal', '0017_auto_20150409_1342'), ('portal', '0018_auto_20150411_0612')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('category_slug', models.SlugField(unique=True, max_length=100)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='masterCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('master_category_name', models.CharField(max_length=150)),
                ('master_category_slug', models.CharField(db_index=True, max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('title_slug', models.SlugField(unique=True, max_length=200)),
                ('bodytext', models.TextField()),
                ('view_count', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(to='portal.category')),
                ('comments_enabled', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=False)),
                ('article_UUID', django_extensions.db.fields.UUIDField(blank=True, editable=False, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('country', models.CharField(max_length=150)),
                ('zip_code', models.CharField(max_length=6)),
                ('home_address', models.TextField()),
                ('mobile_no', models.CharField(max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ImageField(blank=True, verbose_name='Profile Pic', upload_to='images/', null=True)),
                ('posts', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='master_category',
            field=models.ForeignKey(to='portal.masterCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='definition',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='mastercategory',
            options={'verbose_name_plural': 'Master Categories'},
        ),
    ]
