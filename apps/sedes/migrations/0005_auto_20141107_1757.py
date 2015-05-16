# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0004_alumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='asignacion_universal',
            field=models.CharField(default=b'no', max_length=2, choices=[(b'no', b'NO'), (b'si', b'SI')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='discapacidad',
            field=models.CharField(default=b'no', max_length=2, choices=[(b'no', b'NO'), (b'si', b'SI')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='edad',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='pueblos_originarios',
            field=models.CharField(default=b'no', max_length=2, choices=[(b'no', b'NO'), (b'si', b'SI')]),
            preserve_default=True,
        ),
    ]
