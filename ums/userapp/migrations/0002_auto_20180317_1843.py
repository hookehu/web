# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-17 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SysInterface',
        ),
        migrations.AddField(
            model_name='sys',
            name='redirect_url',
            field=models.CharField(default='', max_length=512),
        ),
    ]
