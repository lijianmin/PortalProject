# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_post_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='definition',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
