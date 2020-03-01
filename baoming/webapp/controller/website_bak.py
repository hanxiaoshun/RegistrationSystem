# coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse
import json
from webapp.controller import role, report, teacher, administrator, download, student, user
from webapp.forms.RegisterForm import *

from webapp.utils.form_to_obj import *
from webapp.utils.password import *
from webapp.models import *

sys_msg = '报名系统'

result = {'status': True, 'message': ''}


def index(request):
    """
    欢迎页：展示功能但无法操作
    :param request:
    :return:
    """
    # return HttpResponse(u"欢迎光临 aic!")
    title_msg = sys_msg + '-首页'
    school_terms = SchoolTerm.objects.filter()
    if len(school_terms) <= 0:
        return render(request, "index.html",
                      {'title_msg': title_msg, 'need_login': False, 'no_term': False})
    else:
        school_term = SchoolTerm.objects.last()
        return render(request, "index.html",
                      {'title_msg': title_msg, 'need_login': False, 'school_term': school_term, 'no_term': True})


def to_login(request):
    """
    点击登录：跳转到登录页面
    :param request:
    :return:
    """
    # return HttpResponse(u"欢迎光临 aic!")
    title_msg = sys_msg + '-登陆'
    school_term = SchoolTerm.objects.last()
    return render(request, "login.html", {'title_msg': title_msg, 'school_term': school_term})


def sign_out(request):
    """
    清空session
    :param request:
    :return:
    """
    # return HttpResponse(u"欢迎光临 aic!")
    nickname = request.session.get('nickname', None)  # 用户昵称
    username = request.session.get('username', None)  # 用户名
    role_id = request.session.get('role_id', None)  # 角色ID
    role_name = request.session.get('role_name', None)  # 角色名称
    title_msg = '重新登陆？'
    if nickname:
        del request.session['nickname']
    if username:
        del request.session['username']
    if role_id:
        del request.session['role_id']
    if role_name:
        del request.session['role_name']
    return render(request, "login.html", {'title_msg': title_msg})


def check_username(request):
    """
    实时检查用户名是否已被注册过
    :param request:
    :return:
    """
    result = {'status': True, 'message': ''}
    if request.method == 'POST':
        username = request.POST.get('username', None)
        if username:
            try:
                register_user_info = RegisterUserInfo.objects.get(username=username)
                if register_user_info:
                    result['status'] = False
                    result['message'] = '此用户名已被使用'
                    return JsonResponse(result, safe=False)
            except RegisterUserInfo.DoesNotExist as e:
                result['status'] = True
                result['message'] = '此用户名未被使用'
                return JsonResponse(result, safe=False)


def check_nickname(request):
    """
    实时检查用户名是否已被注册过
    :param request:
    :return:
    """
    result = {'status': True, 'message': ''}
    if request.method == 'POST':
        nickname = request.POST.get('nickname', None)
        if nickname:
            try:
                register_user_info = RegisterUserInfo.objects.get(nickname=nickname)
                if register_user_info:
                    result['status'] = False
                    result['message'] = '此昵称已被使用'
                    return JsonResponse(result, safe=False)
            except RegisterUserInfo.DoesNotExist as e:
                result['status'] = True
                result['message'] = '此昵称未被使用'
                return JsonResponse(result, safe=False)


def register(request):
    """
    注册：分为管理员和普通用户
    :param request:
    :return:
    """
    if request.method == 'POST':
        object_form = RegisterForm(request.POST)
        if object_form.is_valid():
            form_object = form_to_obj(object_form.cleaned_data, RegisterUserInfo())
            # 密码加密处理
            form_object.password = Password.encryption(form_object.password)
            form_object.role = RoleInfo.objects.filter(role_name='student')
            form_object.save()
            # user_role = UserRole()
            # role = RoleInfo.objects.get(role_name='student')
            # user = RegisterUserInfo.objects.get(username=form_object.username)
            # user_role.user = user
            # user_role.role_name = role
            # user_role.explain = "默认注册都是学生"
            # user_role.save()
            title_msg = sys_msg + '-登陆'
            return render(request, "login.html", {'title_msg': title_msg})
        else:
            pass


def sign_in(request):
    """
    登录：检测是登录用户的类别，返回不同的角色
    :param request:
    :return:
    """
    title_msg = '报名系统'
    try:
        if request.method == 'POST':
            username = request.POST.get('username', None)
            if username:
                if '' == username:
                    sign_in_msg = '用户名不能为空'
                    return render(request, "login.html", {'sign_in_msg': sign_in_msg})
                password = request.POST['password']
                if '' == password:
                    sign_in_msg = '密码不能为空'
                    return render(request, "login.html", {'sign_in_msg': sign_in_msg})
                if username and password:
                    register_user_info = RegisterUserInfo.objects.get(username=username)
                    # 验证密码
                    if Password.decrypt_check(password, register_user_info.password):
                        if register_user_info.status == '2':
                            sign_in_msg = '用户名不能为空'
                            return render(request, "login.html", {'sign_in_msg': sign_in_msg})
                        else:
                            school_terms = SchoolTerm.objects.filter()
                            user_role = register_user_info.role
                            is_report = False
                            if user_role.role_name is None:
                                sign_in_msg = '尚未分配角色，或角色信息被改动，请稍后重试或联系管理员。'
                                return render(request, "login.html", {'sign_in_msg': sign_in_msg})
                                # role_infos = RoleInfo.objects.filter(role_name='student')
                                # if len(role_infos) == 1:
                                #     role_info = role_infos[0]
                                #     request.session['nickname'] = register_user_info.nickname  # 用户昵称
                                #     request.session['username'] = register_user_info.username  # 用户名
                                #     request.session['role_id'] = role_info.id  # 角色ID
                                #     request.session['role_name'] = role_info.role_name  # 角色名称
                                #     request.session.set_expiry(2400)
                                #     user_infos = UserInfo.objects.filter(register_user_info=register_user_info.id)
                                #     if len(user_infos) == 1:
                                #         student_info = StudentInfo.objects.exists(user_info=user_infos[0])
                                #         if student_info:
                                #             is_report = True
                                #             school_terms = SchoolTerm.objects.filter()
                                #             if len(school_terms) <= 0:
                                #                 return render(request, "index.html",
                                #                               {'title_msg': title_msg, 'need_login': False,
                                #                                'is_report': is_report, 'no_term': False})
                                #             else:
                                #                 school_term = SchoolTerm.objects.last()
                                #                 return render(request, "index.html",
                                #                               {'title_msg': title_msg, 'need_login': False,
                                #                                'school_term': school_term, 'is_report': is_report,
                                #                                'no_term': True})
                                #     else:
                                #         school_terms = SchoolTerm.objects.filter()
                                #         if len(school_terms) <= 0:
                                #             return render(request, "index.html",
                                #                           {'title_msg': title_msg, 'need_login': False,
                                #                            'is_report': is_report, 'no_term': False})
                                #         else:
                                #             school_term = SchoolTerm.objects.last()
                                #             return render(request, "index.html",
                                #                           {'title_msg': title_msg, 'need_login': False,
                                #                            'school_term': school_term, 'is_report': is_report,
                                #                            'no_term': True})
                            else:
                                if user_role.role_name in 'administrator':
                                    request.session['nickname'] = register_user_info.nickname  # 用户昵称
                                    request.session['username'] = register_user_info.username  # 用户名
                                    request.session['role_id'] = str(user_role.id)  # 角色ID
                                    request.session['role_name'] = str(user_role.role_name)  # 角色名称
                                    request.session.set_expiry(2400)
                                    if len(school_terms) <= 0:
                                        return render(request, "index.html",
                                                      {'title_msg': title_msg, 'need_login': False, 'no_term': False})
                                    else:
                                        school_term = SchoolTerm.objects.last()
                                        return render(request, "index.html",
                                                      {'title_msg': title_msg, 'need_login': False,
                                                       'school_term': school_term,
                                                       'no_term': True})
                                elif user_role.role_name in 'teacher':
                                    teacher_infos = TeacherInfo.objects.filter(
                                        user_info=UserInfo.objects.filter(register_user_info=register_user_info)[0])
                                    if len(teacher_infos) == 1:
                                        status = teacher_infos[0].status
                                        if status == '1':
                                            request.session['nickname'] = register_user_info.nickname  # 用户昵称
                                            request.session['username'] = register_user_info.username  # 用户名
                                            request.session['role_id'] = str(user_role.id)  # 角色ID
                                            request.session['role_name'] = str(user_role.role_name)  # 角色名称
                                            request.session.set_expiry(2400)
                                            if len(school_terms) <= 0:
                                                return render(request, "index.html",
                                                              {'title_msg': title_msg, 'need_login': False,
                                                               'no_term': False})
                                            else:
                                                school_term = SchoolTerm.objects.last()
                                                return render(request, "index.html",
                                                              {'title_msg': title_msg, 'need_login': False,
                                                               'school_term': school_term, 'no_term': True})
                                        elif status == '2':
                                            sign_in_msg = '您当前处于被注销状态，请联系管理员核实再行登陆。'
                                            return render(request, "login.html", {'sign_in_msg': sign_in_msg})
                                        else:
                                            sign_in_msg = '您当前系统状态不明，请联系管理员核实再行登陆。'
                                            return render(request, "login.html", {'sign_in_msg': sign_in_msg})
                                    else:
                                        school_term = SchoolTerm.objects.last()
                                        return render(request, "index.html",
                                                      {'title_msg': title_msg, 'need_login': False,
                                                       'school_term': school_term,
                                                       'no_term': True})
                                elif user_role.role_name in 'student':
                                    user_infos = UserInfo.objects.filter(register_user_info=register_user_info)
                                    if len(user_infos) == 1:
                                        user_info = user_infos[0]
                                        student_infos = StudentInfo.objects.filter(
                                            user_info=user_info)
                                        if len(student_infos) > 0:
                                            # 如果已经存在这个注册用户的学生信息，则匹配学生信息
                                            status = user_info.status
                                            if status == '1':
                                                # 用户信息状态正常，登陆正常
                                                request.session['nickname'] = register_user_info.nickname  # 用户昵称
                                                request.session['username'] = register_user_info.username  # 用户名
                                                request.session['role_id'] = str(user_role.id)  # 角色ID
                                                request.session['role_name'] = str(user_role.role_name)  # 角色名称
                                                request.session.set_expiry(2400)

                                                if len(school_terms) <= 0:
                                                    return render(request, "index.html",
                                                                  {'title_msg': title_msg, 'need_login': False,
                                                                   'no_term': False, 'is_report': True})
                                                else:
                                                    school_term = SchoolTerm.objects.last()
                                                    return render(request, "index.html",
                                                                  {'title_msg': title_msg, 'need_login': False,
                                                                   'school_term': school_term, 'no_term': True,
                                                                   'is_report': True})
                                            elif status == '2':
                                                # 用户信息注销，无法正常登陆
                                                sign_in_msg = '您当前处于被注销状态，请联系报名负责人或系统管理员核实再行登陆。'
                                                return render(request, "login.html", {'sign_in_msg': sign_in_msg})
                                            else:
                                                sign_in_msg = '您当前系统状态不明，请联系管理员核实再行登陆。'
                                                return render(request, "login.html", {'sign_in_msg': sign_in_msg})
                                        else:
                                            # 状态正常，登陆正常
                                            request.session['nickname'] = register_user_info.nickname  # 用户昵称
                                            request.session['username'] = register_user_info.username  # 用户名
                                            request.session['role_id'] = str(user_role.id)  # 角色ID
                                            request.session['role_name'] = str(user_role.role_name)  # 角色名称
                                            request.session.set_expiry(2400)

                                            if len(school_terms) <= 0:
                                                return render(request, "index.html",
                                                              {'title_msg': title_msg, 'need_login': False,
                                                               'no_term': False, 'is_report': False})
                                            else:
                                                school_term = SchoolTerm.objects.last()
                                                return render(request, "index.html",
                                                              {'title_msg': title_msg, 'need_login': False,
                                                               'school_term': school_term, 'no_term': True,
                                                               'is_report': False})
                                    else:
                                        # 状态正常，登陆正常
                                        request.session['nickname'] = register_user_info.nickname  # 用户昵称
                                        request.session['username'] = register_user_info.username  # 用户名
                                        request.session['role_id'] = str(user_role.id)  # 角色ID
                                        request.session['role_name'] = str(user_role.role_name)  # 角色名称
                                        request.session.set_expiry(2400)

                                        if len(school_terms) <= 0:
                                            return render(request, "index.html",
                                                          {'title_msg': title_msg, 'need_login': False,
                                                           'no_term': False, 'is_report': False})
                                        else:
                                            school_term = SchoolTerm.objects.last()
                                            return render(request, "index.html",
                                                          {'title_msg': title_msg, 'need_login': False,
                                                           'school_term': school_term, 'no_term': True, 'is_report': False})
                                else:
                                    sign_in_msg = '您当前系统角色不明，请联系管理员核实或重新注册新用户再行登陆。'
                                    return render(request, "login.html", {'sign_in_msg': sign_in_msg})
                    else:
                        sign_in_msg = '密码错误'
                        return render(request, "login.html", {'sign_in_msg': sign_in_msg})
                else:
                    sign_in_msg = '用户不存在'
                    return render(request, "login.html", {'sign_in_msg': sign_in_msg})
            else:
                sign_in_msg = '登陆异常，用户名不能为空'
                return render(request, "login.html", {'sign_in_msg': sign_in_msg})
        else:
            sign_in_msg = '登陆异常，请检查输入内容或联系系统管理员'
            return render(request, "login.html", {'sign_in_msg': sign_in_msg})
    except BaseException as e:
        sign_in_msg = '登陆异常，请检查输入内容或联系系统管理员'
        print("登录异常:", str(e))
        return render(request, "login.html", {'sign_in_msg': sign_in_msg})


def to_index(request):
    """
    返回首页
    :param request:
    :return:
    """
    school_term = SchoolTerm.objects.last()
    is_report = False
    username = request.session.get('username', None)  # 用户名
    if username:
        register_user_info = RegisterUserInfo.objects.get(username=username)
        user_infos = UserInfo.objects.filter(register_user_info=register_user_info.id)
        if len(user_infos) == 1:
            is_report = True
        title_msg = "返回首页"
        school_terms = SchoolTerm.objects.filter()
        if len(school_terms) <= 0:
            return render(request, "index.html",
                          {'title_msg': title_msg, 'need_login': False, 'no_term': False})
        else:
            school_term = SchoolTerm.objects.last()
            return render(request, "index.html",
                          {'title_msg': title_msg, 'need_login': False, 'school_term': school_term, 'no_term': True})
    else:
        title_msg = "首页"

        school_terms = SchoolTerm.objects.filter()
        if len(school_terms) <= 0:
            return render(request, "index.html",
                          {'title_msg': title_msg, 'need_login': False, 'no_term': False})
        else:
            school_term = SchoolTerm.objects.last()
            return render(request, "index.html",
                          {'title_msg': title_msg, 'need_login': False, 'school_term': school_term, 'no_term': True})


def to_index_teacher(request):
    """
    返回学生首页
    :param request:
    :return:
    """
    return render(request, 'teacher.html', {'title_msg': sys_msg})
