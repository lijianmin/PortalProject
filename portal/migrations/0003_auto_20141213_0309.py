# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_category_category_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='posts',
            new_name='post',
        ),
    ]
