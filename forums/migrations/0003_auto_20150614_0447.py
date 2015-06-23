# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20150606_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='downvote',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='upvote',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='impact_scale',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='side_effect_scale',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1),
            preserve_default=True,
        ),
    ]
