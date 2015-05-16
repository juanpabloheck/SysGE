# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0010_auto_20141112_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conectividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_de_registro', models.DateField()),
                ('hay_conectividad', models.CharField(max_length=2, choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('velocidad_de_subida', models.FloatField(null=True, blank=True)),
                ('velocidad_de_bajada', models.FloatField(null=True, blank=True)),
                ('sede', models.ForeignKey(to='sedes.Sede')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
