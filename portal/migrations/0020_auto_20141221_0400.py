# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_auto_20141221_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.OneToOneField(to='portal.Comments'),
            preserve_default=True,
        ),
    ]
