# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
