# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0010_auto_20141112_2300'),
        ('configuraciones', '0002_motivoinasistencia'),
        ('asistencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsistenciaMasiva',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('sedes.alumno',),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='motivo',
            field=models.ForeignKey(default=None, blank=True, to='configuraciones.MotivoInasistencia', null=True),
            preserve_default=True,
        ),
    ]
