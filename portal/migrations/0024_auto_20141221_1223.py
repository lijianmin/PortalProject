# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0023_auto_20141221_0508'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='post',
            name='comments_enabled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
