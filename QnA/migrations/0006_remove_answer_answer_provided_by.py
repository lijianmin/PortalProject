# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0005_question_qn_clinical_specialty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_provided_by',
        ),
    ]
