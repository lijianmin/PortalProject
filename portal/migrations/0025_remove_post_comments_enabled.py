# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0024_auto_20141221_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments_enabled',
        ),
    ]
