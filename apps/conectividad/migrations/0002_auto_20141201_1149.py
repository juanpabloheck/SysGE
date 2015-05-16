# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conectividad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conectividad',
            name='hay_conectividad',
            field=models.CharField(default=b'SI', max_length=2, choices=[(b'SI', b'SI'), (b'NO', b'NO')]),
            preserve_default=True,
        ),
    ]
