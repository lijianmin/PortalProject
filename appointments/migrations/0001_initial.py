# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0009_auto_20150714_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('booking_datetime', models.DateTimeField()),
                ('remarks', models.TextField(default='')),
                ('email_address', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=25)),
                ('appointment_UUID', django_extensions.db.fields.UUIDField(blank=True, editable=False, null=True)),
                ('doctor', models.ForeignKey(to='profile.ClinicianProfile')),
                ('user', models.ForeignKey(to='profile.PublicUserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
