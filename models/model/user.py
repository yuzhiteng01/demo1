#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18/8/5 下午5:05
# @Author  : yzt
# @Email   : 15510937782@163.com
# @File    : user.py
# @Software: PyCharm
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    creater_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'