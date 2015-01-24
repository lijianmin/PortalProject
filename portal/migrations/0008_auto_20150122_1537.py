# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20150111_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, blank=True, verbose_name='Profile Pic', upload_to='images/'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='posts',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
