# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user_id', models.CharField(max_length=15)),
                ('email_address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('home_address', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='posts',
            name='title_slug',
            field=models.SlugField(default='DEFAULT-SLUG', unique=True),
            preserve_default=False,
        ),
    ]
