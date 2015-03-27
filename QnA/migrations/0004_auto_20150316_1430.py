# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import model_utils.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QnA', '0003_auto_20150227_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('answer_UUID', django_extensions.db.fields.UUIDField(blank=True, editable=False, null=True)),
                ('answer', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('answer_provided_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('question', models.ForeignKey(blank=True, to='QnA.Question', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='posted_by',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='status',
            field=model_utils.fields.StatusField(no_check_for_status=True, max_length=100, choices=[(0, 'dummy')], default='PENDING'),
            preserve_default=True,
        ),
    ]
