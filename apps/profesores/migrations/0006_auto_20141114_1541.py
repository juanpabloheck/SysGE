# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0002_motivoinasistencia'),
        ('profesores', '0005_auto_20141111_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clase',
            name='numero_de_clase',
        ),
        migrations.AddField(
            model_name='clase',
            name='tipo_clase',
            field=models.ForeignKey(default=3, to='configuraciones.TipoClase'),
            preserve_default=False,
        ),
    ]
