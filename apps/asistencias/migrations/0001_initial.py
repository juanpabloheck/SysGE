# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0010_auto_20141112_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('presente', models.CharField(max_length=1, choices=[(b'P', b'Presente'), (b'A', b'Ausente')])),
                ('alumno', models.ForeignKey(to='sedes.Alumno')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
