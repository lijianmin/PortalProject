# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20141215_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastercategory',
            name='master_category_slug',
            field=models.CharField(db_index=True, max_length=150),
            preserve_default=True,
        ),
    ]
