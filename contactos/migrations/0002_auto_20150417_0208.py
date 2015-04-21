# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='direccion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
