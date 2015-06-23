# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0012_remove_question_qn_clinical_specialty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='specialty',
            field=models.ForeignKey(to='QnA.Specialty'),
            preserve_default=True,
        ),
    ]
