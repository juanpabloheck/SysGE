# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0010_auto_20141112_2300'),
        ('profesores', '0007_auto_20141114_1547'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Intervencion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observaciones', models.TextField(max_length=250, null=True, blank=True)),
                ('creado', models.DateField(auto_now_add=True)),
                ('modificado', models.DateField(auto_now_add=True)),
                ('alumno', models.ForeignKey(to='sedes.Alumno')),
                ('clase', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'profesor', chained_field=b'profesor', auto_choose=True, to='profesores.Clase')),
                ('profesor', models.ForeignKey(to='profesores.Profesor')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrabajosAprobados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_de_entrega', models.DateField()),
                ('nota_simbolica', models.IntegerField(max_length=2)),
                ('observaciones', models.TextField(max_length=200, null=True, blank=True)),
                ('creado', models.DateField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('alumno', models.ForeignKey(to='sedes.Alumno')),
                ('clase', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'profesor', chained_field=b'profesor', auto_choose=True, to='profesores.Clase')),
                ('profesor', models.ForeignKey(to='profesores.Profesor')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
