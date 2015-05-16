# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0006_auto_20141114_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='nombre_de_clase',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'Nombre de la Clase'),
            preserve_default=True,
        ),
    ]
