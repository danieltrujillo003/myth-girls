# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chicas', '0005_auto_20160923_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_entry',
            name='space',
            field=models.CharField(max_length=1, choices=[(b'1', b'modal1'), (b'2', b'modal2'), (b'3', b'modal3'), (b'4', b'modal4')]),
            preserve_default=True,
        ),
    ]
