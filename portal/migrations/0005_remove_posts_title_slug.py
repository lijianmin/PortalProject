# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='title_slug',
        ),
    ]
