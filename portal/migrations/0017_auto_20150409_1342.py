# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_auto_20150408_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicuserprofile',
            name='height',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicuserprofile',
            name='weight',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
