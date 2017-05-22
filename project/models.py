# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Project(models.Model):
    project_name = models.CharField('项目名称', max_length=100)
    master_ip = models.CharField('主库IP', max_length=60)
    problem_info = models.CharField('问题描述', max_length=150)
    dba = models.CharField('负责dba', max_length=100)
    department = models.CharField('研发一级部门', max_length=60)
    remark = models.CharField('备注', max_length=200)
    create_date = models.DateTimeField('发表时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.project_name
