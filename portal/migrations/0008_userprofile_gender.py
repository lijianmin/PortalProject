# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20150423_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Female'), ('F', 'Male'), ('UN', 'Unknown')], default='F', max_length=2),
            preserve_default=True,
        ),
    ]
