# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profesores', '0003_clase'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='usuario',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clase',
            name='nombre_de_clase',
            field=models.CharField(max_length=100, verbose_name=b'Nombre de la Clase'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clase',
            name='numero_de_clase',
            field=models.IntegerField(max_length=2, verbose_name=b'Numero de la Clase'),
            preserve_default=True,
        ),
    ]
