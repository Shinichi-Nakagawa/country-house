# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseRecord',
            fields=[
                ('created', models.DateTimeField(serialize=False, primary_key=True, auto_now_add=True)),
                ('code', models.TextField()),
                ('temperature', models.FloatField()),
                ('memo', models.CharField(null=True, max_length=255)),
                ('owner', models.ForeignKey(related_name='house_records', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'house_record',
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='houserecord',
            unique_together=set([('created', 'code')]),
        ),
    ]
