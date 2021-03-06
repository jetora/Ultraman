# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('master_ip', models.CharField(max_length=60, verbose_name='\u4e3b\u5e93IP')),
                ('problem_info', models.CharField(max_length=150, verbose_name='\u95ee\u9898\u63cf\u8ff0')),
                ('dba', models.CharField(max_length=100, verbose_name='\u8d1f\u8d23dba')),
                ('department', models.CharField(max_length=60, verbose_name='\u7814\u53d1\u4e00\u7ea7\u90e8\u95e8')),
                ('remark', models.CharField(max_length=200, verbose_name='\u5907\u6ce8')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
        ),
    ]
