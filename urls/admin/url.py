#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18/8/5 上午12:11
# @Author  : yzt
# @Email   : 15510937782@163.com
# @File    : url.py
# @Software: PyCharm
from django.conf.urls import include, url

from app.admin import view

urlpatterns = [

    # url(r'index/$', view.hello),
    url(r'login/$', view.LoginView.as_view(), name="login"),
]