# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('disqus_shortname', models.CharField(max_length=200)),
                ('disqus_identifier', models.CharField(max_length=200)),
                ('disqus_title', models.CharField(max_length=200)),
                ('disqus_url', models.CharField(max_length=200)),
                ('disqus_category_id', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.OneToOneField(default=False, to='portal.Comments'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='comments_enabled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
