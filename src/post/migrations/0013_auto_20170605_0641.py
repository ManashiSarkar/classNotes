# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20170604_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(null=True),
        ),
    ]