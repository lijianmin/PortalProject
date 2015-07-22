# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0005_auto_20150619_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='condition_desc',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
    ]
