# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=100, verbose_name='\u5bc6\u7801')),
                ('email', models.CharField(max_length=100, verbose_name='\u90ae\u4ef6')),
                ('fullname', models.CharField(max_length=100, verbose_name='\u5168\u540d')),
                ('erp', models.CharField(max_length=60, verbose_name='ERP')),
                ('address', models.CharField(max_length=100, verbose_name='\u5730\u5740')),
                ('city', models.CharField(max_length=200, verbose_name='\u57ce\u5e02')),
                ('sex', models.IntegerField(default=0, verbose_name='\u6027\u522b')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ['username'],
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]
