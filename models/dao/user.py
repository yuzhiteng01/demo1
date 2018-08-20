#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18/8/5 下午7:35
# @Author  : yzt
# @Email   : 15510937782@163.com
# @File    : user.py
# @Software: PyCharm
from models.model.user import User

class DaoUser(object):

    @staticmethod
    def get_user(**kwargs):
        print('3333')
        result = User.objects.get(id=2)
        return result.name

    @staticmethod
    def edit_user(request):

        print('6666666')
        # test1 = User.objects.get(id=1)
        # test1.name = 'Google'
        # test1.save()
        User.objects.filter(id=2).update(name='yuzhiteng')
        # User.objects.filter(id=1).update(name='Google123')
        return '修改成功123'
