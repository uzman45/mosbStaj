# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0002_auto_20160804_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='eMail',
            field=models.EmailField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
