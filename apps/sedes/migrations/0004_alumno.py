# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0003_auto_20141107_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.IntegerField(max_length=8)),
                ('cuil', models.CharField(max_length=13)),
                ('genero', models.CharField(max_length=15, choices=[(b'hombre', b'Hombre'), (b'mujer', b'Mujer')])),
                ('fecha_de_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('situacion', models.CharField(blank=True, max_length=20, null=True, choices=[(b'padre', b'Padre'), (b'madre', b'Madre')])),
                ('discapacidad', models.CharField(default=b'NO', max_length=2, choices=[(b'si', b'SI'), (b'no', b'NO')])),
                ('pueblos_originarios', models.BooleanField(default=False)),
                ('anio_de_ingreso', models.IntegerField(max_length=4, null=True, blank=True)),
                ('asignacion_universal', models.CharField(default=b'NO', max_length=2, choices=[(b'si', b'SI'), (b'no', b'NO')])),
                ('activo', models.BooleanField(default=True)),
                ('estado', models.CharField(default=b'Regular', max_length=15, choices=[(b'regular', b'Regular'), (b'egresado', b'Egresado'), (b'libre', b'Libre'), (b'ex-alumno', b'Ex-Alumno')])),
                ('dni_tutor', models.IntegerField(max_length=8, null=True, blank=True)),
                ('nombre_tutor', models.CharField(max_length=100, null=True, blank=True)),
                ('apellido_tutor', models.CharField(max_length=50, null=True, blank=True)),
                ('cuil_tutor', models.CharField(max_length=13, null=True, blank=True)),
                ('parentesco', models.CharField(default=b'Madre', max_length=20, choices=[(b'padre', b'Padre'), (b'madre', b'Madre'), (b'hermano', b'Hermano'), (b'tia', b'Tia'), (b'otro', b'Otro')])),
                ('sede', models.ForeignKey(to='sedes.Sede')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
