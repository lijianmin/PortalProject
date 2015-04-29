# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_userprofile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinicianprofile',
            name='userprofile',
        ),
        migrations.DeleteModel(
            name='ClinicianProfile',
        ),
        migrations.RemoveField(
            model_name='publicuserprofile',
            name='userprofile',
        ),
        migrations.DeleteModel(
            name='PublicUserProfile',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
