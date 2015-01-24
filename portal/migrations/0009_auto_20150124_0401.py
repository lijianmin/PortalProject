# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20150122_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to='media/', verbose_name='Profile Pic', blank=True, null=True),
            preserve_default=True,
        ),
    ]
