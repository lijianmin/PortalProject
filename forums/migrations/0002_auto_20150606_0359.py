# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='diagnosis_duration',
            field=models.IntegerField(default=1, choices=[(1, '< 1 Year'), (2, '2 - 5 Years'), (3, '> 5 Years')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='experience',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='impact_scale',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='manage_cost',
            field=models.IntegerField(default=1, choices=[(1, 'Not Costly'), (2, 'Costly'), (3, 'Very Costly')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='medication',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='side_effect_scale',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
