# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20150206_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/avatars'), upload_to='', verbose_name='Profile Pic', null=True, blank=True),
            preserve_default=True,
        ),
    ]
