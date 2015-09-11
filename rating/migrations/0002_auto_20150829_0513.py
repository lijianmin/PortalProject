# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentwithrating',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
