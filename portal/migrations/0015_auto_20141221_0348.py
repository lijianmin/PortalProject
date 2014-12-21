# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_auto_20141221_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.OneToOneField(to='portal.Comments', null=True),
            preserve_default=True,
        ),
    ]
