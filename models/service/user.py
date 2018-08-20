#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18/8/5 下午7:45
# @Author  : yzt
# @Email   : 15510937782@163.com
# @File    : user.py
# @Software: PyCharm
from models.dao.user import DaoUser

class ServiceUser(object):

    @staticmethod
    def get_users(**kwargs):

        print('555555')
        return DaoUser.get_user(**kwargs)

    @staticmethod
    def edit_user(request):

        print('88888888')
        return DaoUser.edit_user(request)

#
#         print(kwargs)
#         # kwargs = {}
#         # keys = {
#         #     'name'
#         # }
#         # for (k, v) in dict(request.GET).items():
#         #
#         #     if (k in keys) and (v[0] != u'0'):
#         #         kwargs[k] = v[0]
#         #
#         # data = []
#         # if kwargs != {}:
#         print('44444')
#         data = DaoUser.get_user()
#
#         return data