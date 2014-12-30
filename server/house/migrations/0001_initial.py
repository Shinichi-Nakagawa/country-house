# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseRecord',
            fields=[
                ('created', models.DateTimeField(serialize=False, primary_key=True, auto_now_add=True)),
                ('code', models.TextField()),
                ('temperature', models.FloatField()),
                ('memo', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('created',),
                'db_table': 'house_record',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='houserecord',
            unique_together=set([('created', 'code')]),
        ),
    ]
