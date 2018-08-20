#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18/7/29 下午4:45
# @Author  : yzt
# @Email   : 15510937782@163.com
# @File    : view.py
# @Software: PyCharm
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, RedirectView



class LoginView(RedirectView):

    def get(self, request):
        print('eereewwewwewee')
        host = request.get_host()
        # callback_url = "http://%s/users/check/" % host
        # ucenter = Ucenter()
        # url = ucenter.run('Common.loginUrl', {'callback': callback_url})
        # print '-------------', url
        # return redirect(url)



# def hello(request):
#
#     tag = 'yzt'
#     taga = 'yzt'
#     canno_list = [
#         {
#             'name': 'YZT'
#         },
#         {
#             'name': 'yanmg'
#         },
#         {
#             'name': 'tiantian'
#         },
#         {
#             'name': 'liuhan'
#         },
#         {
#             'name': 'simian'
#         }
#     ]
#     return render(request, 'admin/index.html', {'list_mian':canno_list,'user':tag,'tuser':taga})