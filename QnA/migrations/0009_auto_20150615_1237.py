# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0008_auto_20150614_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='downvote',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='upvote',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
