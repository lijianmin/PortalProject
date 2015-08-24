# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0002_update_user_email_field_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentWithRating',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, serialize=False, to='django_comments.Comment', primary_key=True, parent_link=True)),
                ('rating', models.IntegerField(default=1, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
            ],
            options={
                'abstract': False,
            },
            bases=('django_comments.comment',),
        ),
    ]
