# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postman_attachments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(upload_to='attachments/', verbose_name='attachments'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='GenericFile',
        ),
    ]
