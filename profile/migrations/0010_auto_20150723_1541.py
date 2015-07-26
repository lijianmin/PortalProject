# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0009_auto_20150714_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicuserprofile',
            name='alcohol_intake',
            field=models.IntegerField(default=1, choices=[(1, '<7 drinks a week'), (2, '8-14 drinks a week'), (3, '>15 drinks a week')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicuserprofile',
            name='cancer_desc',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicuserprofile',
            name='current_medical_conditions',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicuserprofile',
            name='lactose_intolerant',
            field=models.IntegerField(default=1, choices=[(1, 'Yes'), (2, 'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicuserprofile',
            name='race',
            field=models.CharField(max_length=100, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicuserprofile',
            name='relative_with_cancer',
            field=models.IntegerField(default=1, choices=[(1, 'None'), (2, 'Grandfather'), (3, 'Grandmother'), (4, 'Father'), (5, 'Mother'), (6, 'Sibling')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicuserprofile',
            name='sexual_history',
            field=models.IntegerField(default=1, choices=[(1, 'Not Sexually Active'), (2, 'Homosexual'), (3, 'Heterosexual'), (4, 'Bisexual')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicuserprofile',
            name='smoking',
            field=models.IntegerField(default=1, choices=[(1, 'Yes'), (2, 'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicuserprofile',
            name='smoking_packs',
            field=models.CharField(max_length=4, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicuserprofile',
            name='smoking_years',
            field=models.CharField(max_length=4, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicuserprofile',
            name='allergies',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
