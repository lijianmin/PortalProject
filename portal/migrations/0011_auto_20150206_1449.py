# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20150125_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(verbose_name='Profile Pic', upload_to='media/avatars/', null=True, blank=True),
            preserve_default=True,
        ),
    ]
