#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18/7/29 下午4:45
# @Author  : yzt
# @Email   : 15510937782@163.com
# @File    : view.py
# @Software: PyCharm
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, RedirectView

from django.shortcuts import redirect

class LoginView(TemplateView):

    template_name = "index/index.html"


#
# def testdb(request):
#
#     kwarg = {'name' :'runoob'}
#     test1 = ServiceUser.get_users(**kwarg)
#
#     return HttpResponse(test1)
#
# def testedit(request):
#
#     print('111111111')
#     res = ServiceUser.edit_user(request)
#     return HttpResponse(res)

#
# def hello(request):
#     print '1111111111122222222'
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
#     return render(request, 'index/index.html', {'list_mian':canno_list,'user':tag,'tuser':taga})

# def search_form(request):
#
#     return render(request,'index/serch.html')
#
#
# # 接收请求数据
# def search(request):
#
#     keys = {"q"}
#     request.encoding = 'utf-8'
#     for (k, v) in dict(request.GET).items():
#         if (k in keys):
#             message = v
#         else:
#             message = '你提交了空表单'
#     # if 'q' in request.GET:
#     #     message = '你搜索的内容为: ' + request.GET['q']
#     # else:
#     #     message = '你提交了空表单'
#     return HttpResponse(message)
