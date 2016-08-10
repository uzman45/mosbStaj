# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=50)),
                ('soyadi', models.CharField(max_length=50)),
                ('telNo', models.CharField(max_length=50)),
            ],
        ),
    ]
