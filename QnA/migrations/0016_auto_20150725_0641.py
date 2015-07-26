# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0015_specialty_hot_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='tag_profile',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
