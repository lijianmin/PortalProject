# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20141215_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastercategory',
            name='master_category_slug',
            field=models.CharField(max_length=150, unique=True),
            preserve_default=True,
        ),
    ]
