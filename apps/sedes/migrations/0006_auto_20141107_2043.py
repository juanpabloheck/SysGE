# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0005_auto_20141107_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='anio_de_ingreso',
            field=models.IntegerField(max_length=4, null=True, verbose_name=b'A\xc3\xb1o de ingreso', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='cuil',
            field=models.CharField(max_length=13, verbose_name=b'CUIL'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='cuil_tutor',
            field=models.CharField(max_length=13, null=True, verbose_name=b'CUIL del tutor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='dni',
            field=models.IntegerField(max_length=8, verbose_name=b'DNI'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='dni_tutor',
            field=models.IntegerField(max_length=8, null=True, verbose_name=b'DNI del tutor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='fecha_de_nacimiento',
            field=models.DateField(verbose_name=b'Fecha de Nacimiento'),
            preserve_default=True,
        ),
    ]
