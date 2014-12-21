# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20141221_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.OneToOneField(default=0, to='portal.Comments'),
            preserve_default=False,
        ),
    ]
