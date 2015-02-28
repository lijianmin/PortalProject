# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0002_auto_20150227_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_txt',
            new_name='question',
        ),
    ]
