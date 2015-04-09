# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_auto_20150316_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicianProfile',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='portal.UserProfile')),
                ('medical_reg_no', models.CharField(max_length=9)),
                ('registered_date', models.DateTimeField()),
                ('practice_address', models.TextField()),
                ('practice_contact_no', models.CharField(max_length=20)),
                ('practice_website', models.URLField()),
                ('practice_email_add', models.EmailField(max_length=75)),
                ('practice_gps_coord', models.CharField(max_length=20)),
                ('clinical_specialty', models.TextField()),
            ],
            options={
            },
            bases=('portal.userprofile',),
        ),
        migrations.CreateModel(
            name='PublicUserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('allergies', models.TextField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=3)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=3)),
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
