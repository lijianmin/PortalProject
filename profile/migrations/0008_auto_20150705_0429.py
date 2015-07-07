# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0007_auto_20150523_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicianprofile',
            name='affiliations',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinicianprofile',
            name='awards',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinicianprofile',
            name='medical_careergrade',
            field=models.IntegerField(choices=[(1, 'Medical Officer'), (2, 'Senior Medical Officer'), (3, 'Registrar'), (4, 'Associate Consultant'), (5, 'Consultant'), (6, 'Senior Consultant'), (7, 'Family Physician'), (8, 'Family Physician Associate Consultant'), (9, 'Family Physician Consultant'), (10, 'Family Physician Senior Consultant'), (11, 'Resident'), (12, 'Senior Resident'), (13, 'Principal Resident')], default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinicianprofile',
            name='medical_memberships',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinicianprofile',
            name='publications',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinicianprofile',
            name='years_of_practice',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clinicianprofile',
            name='medical_interests',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clinicianprofile',
            name='writeup_text',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
