# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20150408_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicuserprofile',
            name='id',
        ),
        migrations.AddField(
            model_name='publicuserprofile',
            name='userprofile_ptr',
            field=models.OneToOneField(to='portal.UserProfile', auto_created=True, default=1, primary_key=True, parent_link=True, serialize=False),
            preserve_default=False,
        ),
    ]
