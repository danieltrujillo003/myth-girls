# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chicas', '0004_remove_entry_reply_new_entry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='entry_reply',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='new_entry',
            name='space',
            field=models.CharField(default='', max_length=1, choices=[(b'1', b'model1'), (b'2', b'model2'), (b'3', b'model3'), (b'4', b'model4')]),
            preserve_default=False,
        ),
    ]
