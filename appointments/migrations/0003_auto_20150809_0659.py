# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20150714_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='acknowledged',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='last_updated_datetime',
            field=models.DateTimeField(default='1999-01-01 00:00', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=model_utils.fields.StatusField(max_length=100, default='PENDING', no_check_for_status=True, choices=[(0, 'dummy')]),
            preserve_default=True,
        ),
    ]
