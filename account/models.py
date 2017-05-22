# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    username = models.CharField('用户名', max_length=100)
    password = models.CharField('密码', max_length=100)
    email = models.CharField('邮件', max_length=100)
    fullname = models.CharField('全名', max_length=100)
    address = models.CharField('地址', max_length=100)
    city = models.CharField('城市', max_length=200)
    sex = models.IntegerField('性别', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['username']
