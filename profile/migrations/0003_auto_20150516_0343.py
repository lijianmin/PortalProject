# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20150502_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=254, verbose_name='Clinic Name')),
                ('address', models.TextField()),
                ('contact_no', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=200)),
                ('website', models.URLField(verbose_name='Business Website')),
                ('business_email_address', models.EmailField(max_length=254, verbose_name='Business Email Address', db_index=True)),
                ('gps_coord', models.CharField(max_length=20)),
                ('business_registered_date', models.DateTimeField(verbose_name='Date joined')),
                ('services', models.TextField(verbose_name='Provided Services')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 5, 16)),
            preserve_default=True,
        ),
    ]
