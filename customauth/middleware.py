#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : middleware.py.py
# @Author: yuzhiteng@youle.com
# @Date  : 2018/6/26
# @Desc  :
from django.conf import settings
from django.utils.functional import SimpleLazyObject
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

def get_user(request):

    if not hasattr(request, '_cached_user'):
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
        request._cached_user = session_key
    return request._cached_user


class AuthenticationMiddleware(object):

    def process_request(self, request):
        assert hasattr(request, 'session'), "The Django authentication middleware requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."

        request.user = SimpleLazyObject(lambda: get_user(request))

        if request.path_info.startswith('/static/'):

            return None

        if (request.COOKIES.get('username') == None or request.user == None) and request.path_info not in ["/users/login/", '/emailtemplate/audithtml/']:

            print('888888')
            return redirect(reverse('users:login', args=[]))
