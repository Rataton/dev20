# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='color',
            field=models.IntegerField(choices=[(b'info', b'Blue'), (b'danger', b'Red'), (b'warning', b'Yellow'), (b'success', b'Green')]),
        ),
    ]
