# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 08:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vdnapp', '0016_auto_20170411_0735'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dataset',
            unique_together=set([]),
        ),
    ]