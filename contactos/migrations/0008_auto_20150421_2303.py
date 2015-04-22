# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0007_auto_20150421_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='person',
        ),
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
