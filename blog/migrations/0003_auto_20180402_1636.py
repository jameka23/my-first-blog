# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 21:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180402_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 2, 21, 36, 43, 357661, tzinfo=utc)),
        ),
    ]
