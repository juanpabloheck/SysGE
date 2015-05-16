# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0009_alumno_ano_de_cursado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='ano_de_cursado',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name=b'A\xc3\xb1o de cursado', choices=[(b'1', b'1\xc2\xba A\xc3\xb1o'), (b'2', b'2\xc2\xba A\xc3\xb1o'), (b'3', b'3\xc2\xba A\xc3\xb1o'), (b'4', b'4\xc2\xba A\xc3\xb1o'), (b'5', b'5\xc2\xba A\xc3\xb1o')]),
            preserve_default=True,
        ),
    ]
