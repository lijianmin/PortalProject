# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0013_auto_20150618_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
