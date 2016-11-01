# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chicas', '0003_entry_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry_reply',
            name='new_entry',
        ),
    ]
