# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20170605_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='state',
            name='message_list',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]