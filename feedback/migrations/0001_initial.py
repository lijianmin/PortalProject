# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('submitter_name', models.CharField(max_length=120)),
                ('submit_datetime', models.DateTimeField()),
                ('submitter_email', models.CharField(max_length=120)),
                ('feedback_text', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
