# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_student_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='balance',
        ),
    ]
