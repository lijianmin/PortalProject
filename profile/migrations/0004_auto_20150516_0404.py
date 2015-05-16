# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20150516_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicianprofile',
            name='clinic_of_practice',
            field=models.ForeignKey(default=1, to='profile.Clinic'),
            preserve_default=False,
        ),
    ]
