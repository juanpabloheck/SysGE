# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0006_auto_20141107_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinador',
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
                ('titulo', models.CharField(max_length=255, choices=[(b'1', b'Maestro de Primaria'), (b'2', b'Profesor de Secundaria de la Materia a su cargo'), (b'3', b'Profesor de Secundaria de otra materia a su cargo'), (b'4', b'Licenciado en la disciplina a su cargo'), (b'5', b'Licenciado en otra disciplina'), (b'6', b'Magister-Doctor')])),
                ('formacion_en_tics', models.CharField(default=b'no', max_length=2, choices=[(b'no', b'NO'), (b'si', b'SI')])),
                ('sede', models.ForeignKey(to='sedes.Sede')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
