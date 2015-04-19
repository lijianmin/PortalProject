# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_squashed_0018_auto_20150411_0612'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicianProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('medical_reg_no', models.CharField(max_length=9)),
                ('registered_date', models.DateTimeField()),
                ('practice_address', models.TextField()),
                ('practice_contact_no', models.CharField(max_length=20)),
                ('practice_country', models.CharField(max_length=200)),
                ('practice_website', models.URLField()),
                ('practice_email_add', models.EmailField(max_length=75)),
                ('practice_gps_coord', models.CharField(max_length=20)),
                ('clinical_specialty', models.TextField()),
                ('medical_interests', models.TextField()),
                ('grad_school', models.CharField(max_length=200)),
                ('grad_year', models.CharField(max_length=4)),
                ('degree_type', models.CharField(max_length=7)),
                ('writeup_text', models.TextField()),
                ('userprofile', models.OneToOneField(to='portal.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicUserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('allergies', models.TextField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('userprofile', models.OneToOneField(to='portal.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
