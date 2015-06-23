# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0010_auto_20150617_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specialty',
            options={'verbose_name_plural': 'Specialties'},
        ),
        migrations.AddField(
            model_name='question',
            name='specialty',
            field=models.ForeignKey(to='QnA.Specialty', default=1),
            preserve_default=True,
        ),
    ]
