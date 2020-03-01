# -*- coding: utf-8 -*-
import json

from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from webapp.models import *
from webapp.utils.date_encoder import *

sys_msg = '报名系统'
result = {'status': True, 'message': ''}
try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

allow_urls = ['/love/', '/', '/report/to_login/', '/report/sign_in/', '/report/sign_out/',
              '/report/to_index/',
              '/report/check_username/', '/report/check_nickname/', '/report/system_guide/', '/report/introduction/']

sys_msg = '报名系统'


class SimpleMiddleware(MiddlewareMixin):
    """
    用户权限验证拦截器
    """

    def process_request(self, request):
        # environ = request.environ   禁用某些客户端
        scheme_type = request.scheme
        path = request.path
        title_msg = sys_msg + '-首页'
        if 'http' in scheme_type:
            # 如果没有登陆用户，且请求路径超过以下列表中选项，则提示登陆
            if 'admin' not in path:
                # 首先判断admin
                username = request.session.get('username', None)  # 尝试获取用户名
                school_terms = SchoolTerm.objects.filter().order_by('-id')
                if username is None:
                    # 过滤掉后台管理员登陆
                    print(path)
                    if path not in '/report/register/':
                        print("go>>>>>register action>>>>>>")
                        if path not in allow_urls:
                            print("go>>>>>website index >>>>>>")

                            if school_terms.count() == 0:
                                return render(request, "index.html",
                                              {'title_msg': title_msg, 'need_login': True, 'no_term': False})
                            else:
                                school_term = SchoolTerm.objects.last()
                                return render(request, "index.html",
                                              {'title_msg': title_msg, 'need_login': True, 'school_term': school_term,
                                               'no_term': True})
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
        # return HttpResponseRedirect("拦截返回一些不需要后台处理的请求信息")


def process_response(self, request, response):
    return response
