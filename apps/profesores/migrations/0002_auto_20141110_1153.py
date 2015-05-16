# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0008_auto_20141110_1153'),
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='tutor_de_sede',
            field=models.ManyToManyField(related_name='Tutor de Sede', to='sedes.Sede'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profesor',
            name='materias',
            field=models.ManyToManyField(related_name='Materias', verbose_name=b'Materias a cargo', to='profesores.Materia'),
            preserve_default=True,
        ),
    ]
