# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0021_auto_20141221_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.OneToOneField(to='portal.Comments'),
            preserve_default=True,
        ),
    ]
