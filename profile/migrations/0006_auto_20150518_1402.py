# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0005_auto_20150516_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='business_registered_date',
            field=models.DateTimeField(verbose_name='Business Registration Date', null=True),
            preserve_default=True,
        ),
    ]
