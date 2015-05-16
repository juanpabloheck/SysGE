# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0008_auto_20141110_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='ano_de_cursado',
            field=models.IntegerField(max_length=4, null=True, verbose_name=b'A\xc3\xb1o de cursado', blank=True),
            preserve_default=True,
        ),
    ]
