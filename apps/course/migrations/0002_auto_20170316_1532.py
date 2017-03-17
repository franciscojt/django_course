# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Courses')),
            ],
        ),
        migrations.AlterField(
            model_name='descriptions',
            name='course_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.Courses'),
        ),
    ]
