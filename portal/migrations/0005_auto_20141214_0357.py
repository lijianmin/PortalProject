# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20141214_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title_slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
