# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0010_auto_20150723_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicuserprofile',
            name='alcohol_intake',
            field=models.IntegerField(default=1, choices=[(1, 'None'), (2, '<7 drinks a week'), (3, '8-14 drinks a week'), (4, '>15 drinks a week')]),
            preserve_default=True,
        ),
    ]
