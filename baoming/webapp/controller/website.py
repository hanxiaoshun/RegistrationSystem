# coding:utf-8
import inspect

from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect

from webapp.controller.common import *
from webapp.controller.renderUtil import render_result
from webapp.forms.RegisterForm import *
from webapp.models import *
from webapp.utils.form_to_obj import *
from webapp.utils.password import *
from webapp.utils.save_operation_log import save_operation_log

sys_msg = '报名系统'

result = {'status': True, 'message': ''}


def introduction(request):
    query_set = ReportCondition.objects.all()
    return render_result(request, "introduction.html", {'query_set':query_set, 'title_msg': "报考说明"})


def system_guide(request):
    return render_result(request, "system_guide.html",
                         {'title_msg': "系统操作指南"})


def index(request):
    """
    欢迎页：展示功能但无法操作
    :param request:
    :return:
    """
    # return HttpResponse(u"欢迎光临 aic!")
    title_msg = sys_msg + '-首页'
    role_name = request.session.get('role_name', None)  # 尝试获取用户名
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    if role_name:
        if role_name == 'administrator':
            return HttpResponseRedirect("/report/report_info_confirm/")
        elif role_name == 'teacher':
            return HttpResponseRedirect("/report/report_info_review/")
        else:
            if school_terms.count() <= 0:
                return render_result(request, "index.html",
                                     {'title_msg': title_msg, 'need_login': False, 'no_term': False,
                                      'index_page': True})
            else:
                school_term = SchoolTerm.objects.last()
                return render_result(request, "index.html",
                                     {'title_msg': title_msg, 'need_login': False, 'school_term': school_term,
                                      'no_term': True,
                                      'index_page': True})
    else:
        if school_terms.count() <= 0:
            return render_result(request, "index.html",
                                 {'title_msg': title_msg, 'need_login': True, 'no_term': False, 'index_page': True})
        else:
            school_term = SchoolTerm.objects.last()
            return render_result(request, "index.html",
                                 {'title_msg': title_msg, 'need_login': True, 'school_term': school_term,
                                  'no_term': True,
                                  'index_page': True})


def to_login(request):
    """
    点击登录：跳转到登录页面
    :param request:
    :return:
    """
    # return HttpResponse(u"欢迎光临 aic!")
    title_msg = sys_msg + '-登陆'
    school_term = SchoolTerm.objects.last()
    return render_result(request, "login.html", {'title_msg': title_msg, 'school_term': school_term})


def sign_out(request):
    """
    清空session
    :param request:
    :return:
    """
    # return HttpResponse(u"欢迎光临 aic!")
    title_msg = '重新登陆？'
    try:
        nickname = request.session.get('nickname', None)  # 用户昵称
        username = request.session.get('username', None)  # 用户名
        role_id = request.session.get('role_id', None)  # 角色ID
        role_name = request.session.get('role_name', None)  # 角色名称
        result['message'] = "正常退出"
        result['level'] = log_level_logout
        save_operation_log(request, inspect.stack()[0][3], "", result)
        if username:
            del request.session['username']
        if nickname:
            del request.session['nickname']
        if role_id:
            del request.session['role_id']
        if role_name:
            del request.session['role_name']
    except Exception as e:
        result['status'] = False
        result['message'] = "退出系统时异常：" + str(e)
        result['data'] = ''
        result['level'] = log_level_logout
        save_operation_log(request, inspect.stack()[0][3], "", result)
    return render_result(request, "login.html", {'title_msg': title_msg})


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
    try:
        if request.method == 'POST':
            object_form = RegisterForm(request.POST)
            if object_form.is_valid():
                form_object = form_to_obj(object_form.cleaned_data, RegisterUserInfo())
                # 密码加密处理
                form_object.password = Password.encryption(form_object.password)
                role_infos = RoleInfo.objects.filter(role_name='student')
                if len(role_infos) > 0:
                    form_object.role = role_infos[0]
                    form_object.save()
                    result['message'] = "注册成功"
                    result['level'] = log_level_register
                    save_operation_log(request, inspect.stack()[0][3], form_object.__str__(True), result)
                    title_msg = sys_msg + '-登陆'
                    sign_in_msg = '注册成功，请您登陆'
                    return render_result(request, "login.html", {'title_msg': title_msg, 'sign_in_msg': sign_in_msg,
                                                                 'username': form_object.username})
                else:
                    print(type(object_form.errors), object_form.errors)  # errors类型是ErrorDict，里面是ul，li标签
                    sign_in_msg = '-注册失败,请勿登陆,初始角色信息获取失败,请稍后重试，或者联系管理员查看和管理角色信息！'
                    title_msg = sys_msg + '-注册失败！'
                    return render_result(request, "login.html", {'title_msg': title_msg, 'sign_in_msg': sign_in_msg})
                # user_role = UserRole()
                # role = RoleInfo.objects.get(role_name='student')
                # user = RegisterUserInfo.objects.get(username=form_object.username)
                # user_role.user = user
                # user_role.role_name = role
                # user_role.explain = "默认注册都是学生"
                # user_role.save()
            else:
                print(type(object_form.errors), object_form.errors)  # errors类型是ErrorDict，里面是ul，li标签
                title_msg = sys_msg + '-注册失败'
                sign_in_msg = '注册失败,请勿登陆,请重试或联系管理员！报错内容：' + object_form.errors
                return render_result(request, "login.html", {'title_msg': title_msg, 'sign_in_msg': sign_in_msg})
    except Exception as e:
        print(str(e))
        sign_in_msg = '-注册失败,请勿登陆,请重试或联系管理员！报错内容：' + str(e)
        title_msg = sys_msg + '-注册失败'
        return render_result(request, "login.html", {'title_msg': title_msg, 'sign_in_msg': sign_in_msg})


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
                    return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
                password = request.POST['password']
                if '' == password:
                    sign_in_msg = '密码不能为空'
                    return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
                if username and password:
                    register_user_info = RegisterUserInfo.objects.get(username=username)
                    # 验证密码
                    if Password.decrypt_check(password, register_user_info.password):
                        if register_user_info.status == '2':
                            sign_in_msg = '您当前状态未注销状态，无法登陆请联系负责人或系统管理员。'
                            return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
                        else:
                            school_terms = SchoolTerm.objects.filter()
                            user_role = register_user_info.role

                            if user_role.role_name is None:
                                sign_in_msg = '尚未分配角色，或角色信息被改动，请稍后重试或联系管理员。'
                                return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
                            else:
                                if user_role.role_name in 'administrator':
                                    request.session['nickname'] = register_user_info.nickname  # 用户昵称
                                    request.session['username'] = register_user_info.username  # 用户名
                                    request.session['role_id'] = str(user_role.id)  # 角色ID
                                    request.session['role_name'] = str(user_role.role_name)  # 角色名称
                                    request.session.set_expiry(7200)
                                    result['message'] = "系统管理员（学校管理员）登陆成功"
                                    result['level'] = log_level_login
                                    save_operation_log(request, inspect.stack()[0][3], "", result)
                                    return HttpResponseRedirect('/report/report_info_confirm/')
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
                                            request.session.set_expiry(7200)
                                            result['message'] = "负责人登陆成功"
                                            result['level'] = log_level_login
                                            save_operation_log(request, inspect.stack()[0][3], "", result)
                                            return HttpResponseRedirect('/report/report_info_review/')
                                        elif status == '2':
                                            sign_in_msg = '您当前处于被注销状态，请联系管理员核实再行登陆。'
                                            return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
                                        else:
                                            sign_in_msg = '您当前系统状态不明，请联系管理员核实再行登陆。'
                                            return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
                                    else:
                                        school_term = SchoolTerm.objects.last()
                                        return render_result(request, "index.html",
                                                             {'title_msg': title_msg, 'need_login': False,
                                                              'school_term': school_term,
                                                              'no_term': True})
                                elif user_role.role_name in 'student':
                                    request.session['nickname'] = register_user_info.nickname  # 用户昵称
                                    request.session['username'] = register_user_info.username  # 用户名
                                    request.session['role_id'] = str(user_role.id)  # 角色ID
                                    request.session['role_name'] = str(user_role.role_name)  # 角色名称
                                    request.session.set_expiry(7200)
                                    result['message'] = '学员登陆成功！'
                                    result['level'] = log_level_login
                                    save_operation_log(request, inspect.stack()[0][3], "", result)
                                    return HttpResponseRedirect('/report/to_index/')
                                else:
                                    sign_in_msg = '您当前系统角色不明，请联系管理员核实或重新注册新用户再行登陆。'
                                    return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
                    else:
                        sign_in_msg = '密码错误'
                        return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
                else:
                    sign_in_msg = '用户不存在'
                    return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
            else:
                sign_in_msg = '登陆异常，用户名不能为空'
                return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
        else:
            sign_in_msg = '登陆异常，请检查输入内容或联系系统管理员'
            return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
    except BaseException as e:
        sign_in_msg = '登陆异常，请检查输入内容或联系系统管理员'
        print("登录异常:", str(e))
        result['level'] = log_level_login
        save_operation_log(request, inspect.stack()[0][3],
                           "登录异常:" + str(e) + "==student",
                           result)
        return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})


def to_index(request):
    """
    返回首页
    :param request:
    :return:
    """
    is_report = False
    username = request.session.get('username', None)  # 用户名
    school_terms = SchoolTerm.objects.filter()
    title_msg = '返回首页'
    if username:
        register_user_info = RegisterUserInfo.objects.get(username=username)
        user_infos = UserInfo.objects.filter(register_user_info=register_user_info)
        if len(user_infos) == 1:
            user_info = user_infos[0]
            # 消息
            system_messages_receiver = SystemMessage.objects.filter(receiver=user_info,
                                                                    hidden_status_receiver=2).order_by(
                '-id')
            not_confirm = system_messages_receiver.filter(feedback_status=2).count()
            # 消息
            student_infos = StudentInfo.objects.filter(
                user_info=user_info)
            if len(student_infos) > 0:
                # 如果已经存在这个注册用户的学生信息，则匹配学生信息
                status = user_info.status
                if status == '1':
                    if len(school_terms) <= 0:
                        return render_result(request, "index.html",
                                             {'title_msg': title_msg,
                                              'need_login': False,
                                              'no_term': False,
                                              'is_report': False,
                                              'not_confirm': not_confirm,
                                              'index_page': True})
                    else:
                        school_term = SchoolTerm.objects.last()
                        return render_result(request, "index.html",
                                             {'title_msg': title_msg,
                                              'need_login': False,
                                              'school_term': school_term,
                                              'no_term': True,
                                              'is_report': True,
                                              'not_confirm': not_confirm,
                                              'index_page': True})
                elif status == '2':
                    # 用户信息注销，无法正常登陆
                    sign_in_msg = '您当前处于被注销状态，请联系报名负责人或系统管理员核实再行登陆。'
                    return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
                else:
                    sign_in_msg = '您当前系统状态不明，请联系管理员核实再行登陆。'
                    return render_result(request, "login.html", {'sign_in_msg': sign_in_msg})
            else:
                if len(school_terms) <= 0:
                    return render_result(request, "index.html",
                                         {'title_msg': title_msg, 'need_login': False,
                                          'no_term': False, 'is_report': False, 'not_confirm': not_confirm,
                                          'index_page': True})
                else:
                    school_term = SchoolTerm.objects.last()
                    return render_result(request, "index.html",
                                         {'title_msg': title_msg, 'need_login': False,
                                          'school_term': school_term, 'no_term': True,
                                          'is_report': False, 'not_confirm': not_confirm, 'index_page': True})
        else:
            if len(school_terms) <= 0:
                return render_result(request, "index.html",
                                     {'title_msg': title_msg, 'need_login': False,
                                      'no_term': False, 'is_report': False, 'not_confirm': 0, 'index_page': True})
            else:
                school_term = SchoolTerm.objects.last()
                return render_result(request, "index.html",
                                     {'title_msg': title_msg, 'need_login': False,
                                      'school_term': school_term, 'no_term': True,
                                      'is_report': False, 'not_confirm': 0, 'index_page': True})
    else:
        title_msg = "首页"
        if len(school_terms) <= 0:
            return render_result(request, "index.html",
                                 {'title_msg': title_msg, 'need_login': True, 'no_term': True})
        else:
            school_term = SchoolTerm.objects.last()
            return render_result(request, "index.html",
                                 {'title_msg': title_msg, 'need_login': True, 'school_term': school_term,
                                  'no_term': False, 'index_page': True})


def to_index_teacher(request):
    """
    返回学生首页
    :param request:
    :return:
    """
    return render_result(request, 'teacher.html', {'title_msg': sys_msg})


def to_index_administrator(request):
    """
    返回学生首页
    :param request:
    :return:
    """
    return render_result(request, 'administrator.html', {'title_msg': sys_msg})
