# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0004_auto_20141111_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
