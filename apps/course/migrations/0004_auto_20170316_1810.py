# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20170316_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descriptions',
            name='id',
        ),
        migrations.AlterField(
            model_name='descriptions',
            name='course_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='course.Courses'),
        ),
    ]
