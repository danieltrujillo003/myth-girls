# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chicas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_entry',
            name='name',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='new_entry',
            name='entry',
            field=models.TextField(max_length=128),
            preserve_default=True,
        ),
    ]
