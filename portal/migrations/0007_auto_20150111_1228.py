# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20150110_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='article_UUID',
            field=django_extensions.db.fields.UUIDField(blank=True, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='definition',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
