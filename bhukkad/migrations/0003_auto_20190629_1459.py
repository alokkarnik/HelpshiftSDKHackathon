# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-29 09:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bhukkad', '0002_auto_20190629_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderhistory',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderhistory',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrderHistory',
        ),
    ]
