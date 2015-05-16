# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0002_auto_20141110_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_de_clase', models.CharField(max_length=100)),
                ('numero_de_clase', models.IntegerField(max_length=2)),
                ('profesor', models.ForeignKey(to='profesores.Profesor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
