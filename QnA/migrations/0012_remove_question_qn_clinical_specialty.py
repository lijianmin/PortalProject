# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0011_auto_20150617_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='qn_clinical_specialty',
        ),
    ]
