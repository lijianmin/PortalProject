# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0014_auto_20150618_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='hot_topic',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
