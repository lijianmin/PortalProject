# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20150110_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_slug',
            field=models.SlugField(max_length=200, unique=True),
            preserve_default=True,
        ),
    ]
