# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_list', '0004_auto_20170608_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='description',
            field=models.TextField(default=''),
        ),
    ]