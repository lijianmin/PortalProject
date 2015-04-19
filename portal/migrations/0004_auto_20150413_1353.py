# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20150413_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicianprofile',
            name='registered_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
