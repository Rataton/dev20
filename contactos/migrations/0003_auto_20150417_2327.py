# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0002_auto_20150417_0208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='person',
        ),
        migrations.AddField(
            model_name='group',
            name='person',
            field=models.ManyToManyField(to='contactos.Person'),
        ),
    ]
