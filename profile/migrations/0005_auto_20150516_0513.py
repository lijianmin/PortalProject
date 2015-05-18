# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20150516_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='initial',
            field=models.CharField(verbose_name='Initial', max_length=4, default=None, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clinicianprofile',
            name='clinic_of_practice',
            field=models.ForeignKey(default=1, to='profile.Clinic'),
            preserve_default=True,
        ),
    ]
