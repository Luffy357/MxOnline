# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-31 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181031_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '\u6ce8\u518c'), ('forget', '\u627e\u56de'), ('update_email', '\u4fee\u6539\u90ae\u7bb1')], max_length=10),
        ),
    ]
