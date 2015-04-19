# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20150413_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicianprofile',
            name='registered_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
