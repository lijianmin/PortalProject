# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20141214_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='masterCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('master_category_name', models.CharField(max_length=150)),
                ('master_category_slug', models.CharField(unique=True, max_length=150, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='master_category',
            field=models.ForeignKey(to='portal.masterCategory'),
            preserve_default=False,
        ),
    ]
