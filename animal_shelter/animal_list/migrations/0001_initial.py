# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('color', models.CharField(max_length=30)),
                ('species', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('age', models.SmallIntegerField()),
            ],
        ),
    ]
