# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('plan_de_estudio', models.TextField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.IntegerField(max_length=8, verbose_name=b'DNI')),
                ('cuil', models.CharField(max_length=13, verbose_name=b'CUIL')),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('localidad', models.CharField(max_length=100, null=True, blank=True)),
                ('telefono_fijo', models.IntegerField(null=True, blank=True)),
                ('telefono_cel', models.IntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('dedicacion_horaria', models.IntegerField(max_length=2, null=True, blank=True)),
                ('titulo', models.CharField(max_length=255)),
                ('formacion_en_tics', models.CharField(default=b'no', max_length=2, choices=[(b'no', b'NO'), (b'si', b'SI')])),
                ('materias', models.ManyToManyField(to='profesores.Materia', verbose_name=b'Materias a cargo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
