# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 11:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=250)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('address', models.TextField()),
                ('about', models.TextField()),
                ('balance', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Course')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]