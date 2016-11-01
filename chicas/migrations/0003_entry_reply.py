# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chicas', '0002_auto_20160721_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='entry_reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('entry', models.TextField(max_length=128)),
                ('new_entry', models.ForeignKey(to='chicas.new_entry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
