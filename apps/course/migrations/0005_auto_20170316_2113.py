# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20170316_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='descriptions',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
