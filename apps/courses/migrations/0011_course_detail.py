# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-05 22:12
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_bannercourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9'),
        ),
    ]
