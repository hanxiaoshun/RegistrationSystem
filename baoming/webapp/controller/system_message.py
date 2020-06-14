import inspect
import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect

from webapp.controller.common import *
from webapp.forms.SystemMessageForm import SystemMessageForm
from webapp.models import *
from webapp.utils.form_to_obj import *
from webapp.utils.save_operation_log import save_operation_log

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def admin_message(request):
    """
    系统公告
    :param request:
    :return:
    """
    system_messages_system_announcement = SystemMessage.objects.filter(message_range=1,
                                                                       hidden_status_sender=2).order_by(
        '-id')
    system_announcement = system_messages_system_announcement.count()
    message_already_sent = 0
    not_confirm = 0
    username = request.session.get('username', None)
    registers = RegisterUserInfo.objects.filter(username=username)
    if len(registers) == 1:
        user_infos = UserInfo.objects.filter(register_user_info=registers[0]).order_by('-id')
        if len(user_infos) == 1:
            system_messages = SystemMessage.objects.filter(sender=user_infos[0], hidden_status_sender=2).order_by(
                '-id')
            message_already_sent = system_messages.count()
            system_messages = SystemMessage.objects.filter(receiver=user_infos[0],
                                                           hidden_status_receiver=2).order_by('-id')
            not_confirm = system_messages.filter(feedback_status=2).count()
    paginator = Paginator(system_messages_system_announcement, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    title_msg = "系统公告列表"
    return render(request, "page_main_controller/system_message/system_message.html",
                  {'title_msg': title_msg, "contacts": contacts, 'message_type': 'announcement',
                   'system_message_type': '系统公告',
                   'system_announcement': system_announcement, 'message_already_sent': message_already_sent,
                   'message_not_confirm': not_confirm,
                   'teacher_infos': teacher_infos,
                   'school_terms': school_terms, 'school_term': 0, 'teacher_info': 0})


def send(request):
    """
    发送信息列表
    :param request:
    :return:
    """
    username = request.session.get('username', None)
    title_msg = "发送的消息列表"
    system_messages_send = None
    message_already_sent = 0
    not_confirm = 0
    system_messages = SystemMessage.objects.filter(message_range=1, hidden_status_sender=2).order_by(
        '-id')
    system_announcement = system_messages.count()
    if username:
        registers = RegisterUserInfo.objects.filter(username=username)
        if len(registers) == 1:
            user_infos = UserInfo.objects.filter(register_user_info=registers[0]).order_by('-id')
            if len(user_infos) == 1:
                system_messages_send = SystemMessage.objects.filter(sender=user_infos[0],
                                                                    hidden_status_sender=2).order_by(
                    '-id')
                message_already_sent = system_messages_send.count()
                system_messages = SystemMessage.objects.filter(receiver=user_infos[0],
                                                               hidden_status_receiver=2).order_by('-id')
                not_confirm = system_messages.filter(feedback_status=2).count()
    paginator = Paginator(system_messages_send, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    return render(request, "page_main_controller/system_message/system_message.html",
                  {'title_msg': title_msg, "contacts": contacts, 'message_type': 'send', 'system_message_type': '已发送',
                   'message_already_sent': message_already_sent, 'message_not_confirm': not_confirm,
                   'system_announcement': system_announcement,
                   'teacher_infos': teacher_infos,
                   'school_terms': school_terms, 'school_term': 0, 'teacher_info': 0})


def receive(request):
    """
    接收信息列表
    :param request:
    :return:
    """
    username = request.session.get('username', None)
    title_msg = "接收的消息列表"
    system_messages_receiver = None
    message_already_sent = 0
    not_confirm = 0
    system_messages = SystemMessage.objects.filter(message_range=1, hidden_status_sender=2).order_by(
        '-id')
    system_announcement = system_messages.count()
    if username:
        registers = RegisterUserInfo.objects.filter(username=username)
        if len(registers) == 1:
            print('ddddd')
            user_infos = UserInfo.objects.filter(register_user_info=registers[0]).order_by('-id')
            system_messages_receiver = SystemMessage.objects.filter(hidden_status_receiver=2).order_by('-id')
            if len(user_infos) == 1:
                print('kkkk')
                system_messages_receiver = SystemMessage.objects.filter(receiver=user_infos[0],
                                                                        hidden_status_receiver=2).order_by('-id')
                not_confirm = system_messages_receiver.filter(feedback_status=2).count()
                receive_status_not = system_messages_receiver.filter(receive_status=2)

                system_messages = SystemMessage.objects.filter(sender=user_infos[0], hidden_status_sender=2).order_by(
                    '-id')
                message_already_sent = system_messages.count()

                for system_message in receive_status_not:
                    # 将未查看的信息状态设置为已查看
                    system_message.receive_status = "1"
                    system_message.save()
    print(system_messages_receiver)
    print(f'system_messages_receiver--{system_messages_receiver}')
    paginator = Paginator(system_messages_receiver, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    return render(request, "page_main_controller/system_message/system_message.html",
                  {'title_msg': title_msg, "contacts": contacts, 'message_type': 'receive',
                   'message_not_confirm': not_confirm,
                   'message_already_sent': message_already_sent, 'system_announcement': system_announcement,
                   'system_message_type': '已接收', 'teacher_infos': teacher_infos,
                   'school_terms': school_terms, 'school_term': 0, 'teacher_info': 0})


def message_add(request):
    """
    添加一条信息
    :param request:
    :return:
    """
    title_msg = '添加一条信息'
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    not_confirm, message_already_sent, system_announcement = get_message_infos(request)
    return render(request, "page_main_controller/system_message/system_message_send_page.html",
                  {'title_msg': title_msg, 'has_receiver': "false", 'has_receiver_message': 'false',
                   'teacher_infos': teacher_infos, 'school_terms': school_terms, 'school_term': 0,
                   'teacher_info': 0,
                   'message_not_confirm': not_confirm,
                   'message_already_sent': message_already_sent,
                   'system_announcement': system_announcement})


def message_to_receiver(request):
    """
    指定人发送
    :param request:
    :return:
    """
    not_confirm, message_already_sent, system_announcement = get_message_infos(request)
    receiver = request.GET.get('record_id', None)
    title_msg = '发送信息编辑页面'
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')

    register_info_user = RegisterUserInfo.objects.get(username=request.session.get('username', None))
    if register_info_user.role.role_name == 'administrator':
        # 如果当前发件人是学校管理员，将意见发送给此学生对应的单位负责人
        if receiver:
            # 提前指定收信人
            receiver_students = StudentInfo.objects.filter(id=receiver).order_by('-id')
            if len(receiver_students) > 0:
                receiver_student = receiver_students[0]
                return render(request, "page_main_controller/system_message/system_message_send_page.html",
                              {'title_msg': title_msg, 'receiver': receiver_student.teacher_info.user_info,
                               'has_receiver': 'true',
                               'teacher_infos': teacher_infos,
                               'school_terms': school_terms, 'school_term': 0, 'teacher_info': 0,
                               'message_not_confirm': not_confirm,
                               'message_already_sent': message_already_sent,
                               'system_announcement': system_announcement})
            else:
                title_msg = sys_msg + '-错误信息展示页面'
                message = '系统提示：没有找到这条记录基础信息，请您重试或查证后再操作！'
                return render(request, "page_main_controller/message.html",
                              {'title_msg': title_msg, 'message': message})
        else:
            title_msg = sys_msg + '-错误信息展示页面'
            message = '系统提示：没有找到这条记录基础信息，请您重试或查证后再操作！'
            return render(request, "page_main_controller/message.html",
                          {'title_msg': title_msg, 'message': message})
    else:
        if receiver:
            # 提前指定收信人
            receiver_students = StudentInfo.objects.filter(id=receiver).order_by('-id')
            if len(receiver_students) > 0:
                receiver_student = receiver_students[0]
                return render(request, "page_main_controller/system_message/system_message_send_page.html",
                              {'title_msg': title_msg, 'receiver': receiver_student.user_info,
                               'has_receiver': 'true',
                               'teacher_infos': teacher_infos,
                               'school_terms': school_terms, 'school_term': 0, 'teacher_info': 0,
                               'message_not_confirm': not_confirm,
                               'message_already_sent': message_already_sent,
                               'system_announcement': system_announcement})
            else:
                title_msg = sys_msg + '-错误信息展示页面'
                message = '系统提示：没有找到这条记录基础信息，请您重试或查证后再操作！'
                return render(request, "page_main_controller/message.html",
                              {'title_msg': title_msg, 'message': message})
        else:
            title_msg = sys_msg + '-错误信息展示页面'
            message = '系统提示：没有找到这条记录基础信息，请您重试或查证后再操作！'
            return render(request, "page_main_controller/message.html",
                          {'title_msg': title_msg, 'message': message})


def message_to_message(request):
    """
    指定信息回复
    :param request:
    :return:
    """
    receiver_message_id = request.GET.get('record_id', None)
    title_msg = '发送信息编辑页面'
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    not_confirm, message_already_sent, system_announcement = get_message_infos(request)
    if receiver_message_id:
        # 提前指定收信人
        receiver_message_infos = SystemMessage.objects.filter(id=receiver_message_id).order_by('-id')
        if len(receiver_message_infos) > 0:
            return render(request, "page_main_controller/system_message/system_message_send_page.html",
                          {'title_msg': title_msg, 'receiver_message': receiver_message_infos[0],
                           'has_receiver_message': 'true',
                           'teacher_infos': teacher_infos,
                           'school_terms': school_terms, 'school_term': 0, 'teacher_info': 0,
                           'message_not_confirm': not_confirm,
                           'message_already_sent': message_already_sent,
                           'system_announcement': system_announcement})
        else:
            title_msg = sys_msg + '-错误信息展示页面'
            message = '系统提示：没有找到这条记录基础信息，请您重试或查证后再操作！'
            return render(request, "page_main_controller/message.html",
                          {'title_msg': title_msg, 'message': message})
    else:
        title_msg = sys_msg + '-错误信息展示页面'
        message = '系统提示：未能获取到相关信息！'
        return render(request, "page_main_controller/message.html",
                      {'title_msg': title_msg, 'message': message})


def save_system_message(request):
    """
    保存并发送一个系统信息
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            object_form = SystemMessageForm(request.POST)

            if object_form.is_valid():
                form_object_system_message = form_to_obj(object_form.cleaned_data, SystemMessage())
                form_object_system_message.sender = UserInfo.objects.get(
                    register_user_info__username=request.session.get('username', None))
                message_range = object_form.cleaned_data.get('message_range', None)
                # if message_range == message_range_system_announcement:
                #     # 系统公告级别的
                #     print()
                # elif message_range == message_range_all_teacher:
                #     # 所有负责人
                # elif message_range == message_range_teacher_student:
                #     # 负责人所辖所有的学员
                if str(message_range) not in message_range_no_person:
                    # 如果消息不是全体性的回复
                    receiver = object_form.cleaned_data.get('receiver', None)
                    feedback_message = object_form.cleaned_data.get('feedback_message', None)
                    if receiver:
                        # 初始发送的消息
                        if type(receiver) == str:
                            if "-" in receiver:
                                ids = str(receiver).split("-")
                                for id_str in ids:
                                    # 保存并发送到每个指定人
                                    system_message = form_object_system_message
                                    system_message.receiver = UserInfo.objects.get(id=int(id_str))
                                    system_message.save()
                            else:
                                if len(receiver) > 0:
                                    form_object_system_message.receiver = UserInfo.objects.get(id=int(receiver))
                                    form_object_system_message.save()
                                else:
                                    title_msg = sys_msg + '-错误信息展示页面'
                                    message = '系统提示：收信人信息获取失败！'
                                    return render(request, "page_main_controller/message.html",
                                                  {'title_msg': title_msg, 'message': message})
                        else:
                            form_object_system_message.receiver = UserInfo.objects.get(id=receiver)
                            form_object_system_message.save()
                    elif feedback_message:
                        # 是确认回复的消息
                        feedback_message_objects = SystemMessage.objects.filter(id=feedback_message).order_by('-id')
                        if feedback_message_objects.count() > 0:
                            form_object_system_message.feedback_message = feedback_message_objects[0]
                            form_object_system_message.receiver = feedback_message_objects[0].sender
                            form_object_system_message.save()
                        else:
                            title_msg = sys_msg + '-错误信息展示页面'
                            message = '系统提示：确认回复信件信息获取异常！'
                            return render(request, "page_main_controller/message.html",
                                          {'title_msg': title_msg, 'message': message})
                    else:
                        title_msg = sys_msg + '-错误信息展示页面'
                        message = '系统提示：收信人信息获取异常！'
                        return render(request, "page_main_controller/message.html",
                                      {'title_msg': title_msg, 'message': message})
                else:
                    if str(message_range) == '2':
                        administrator_user_infos = UserInfo.objects.filter(
                            register_user_info__role__role_name='administrator').order_by('-id')
                        # form_object_system_message.receiver = administrator_user_infos[0]
                        if administrator_user_infos.count() > 0:
                            for administrator_user_info in administrator_user_infos:
                                form_object_system_message_admin = form_object_system_message
                                form_object_system_message_admin.receiver = administrator_user_info
                                form_object_system_message_admin.save()
                        else:
                            title_msg = sys_msg + '-错误信息展示页面'
                            message = '系统提示：学校管理员信息获取失败！'
                            return render(request, "page_main_controller/message.html",
                                          {'title_msg': title_msg, 'message': message})
                    elif str(message_range) == '3':
                        teachers = TeacherInfo.objects.all().order_by('-id')
                        if teachers.count() > 0:
                            for teacher in teachers:
                                form_object_system_message_teacher = form_object_system_message
                                form_object_system_message_teacher.receiver = teacher.user_info
                                form_object_system_message_teacher.save()
                        else:
                            title_msg = sys_msg + '-错误信息展示页面'
                            message = '系统提示：您尚未添加负责人！'
                            return render(request, "page_main_controller/message.html",
                                          {'title_msg': title_msg, 'message': message})
                    elif str(message_range) == '6':
                        username = request.session.get('username', None)
                        register_user_info = RegisterUserInfo.objects.get(username=username)
                        teacher_info = TeacherInfo.objects.get(
                            user_info=UserInfo.objects.get(register_user_info=register_user_info))
                        student_infos = StudentInfo.objects.filter(teacher_info=teacher_info).order_by('-id')
                        if student_infos.count() > 0:
                            for student in student_infos:
                                form_object_system_message_student = form_object_system_message
                                form_object_system_message_student.receiver = student.user_info
                                form_object_system_message_student.save()
                        else:
                            title_msg = sys_msg + '-错误信息展示页面'
                            message = '系统提示：您还没有负责人的学员！'
                            return render(request, "page_main_controller/message.html",
                                          {'title_msg': title_msg, 'message': message})
                    elif str(message_range) == '8':
                        username = request.session.get('username', None)
                        register_user_info = RegisterUserInfo.objects.get(username=username)
                        student_infos = StudentInfo.objects.filter(
                            user_info=UserInfo.objects.get(register_user_info=register_user_info)).order_by('-id')
                        if student_infos.count() > 0:
                            student_info = student_infos[0]
                            if student_info.teacher_info:
                                form_object_system_message.receiver = student_info.teacher_info.user_info
                                form_object_system_message.save()
                            else:
                                title_msg = sys_msg + '-错误信息展示页面'
                                message = '系统提示：请正确选择负责人'
                                return render(request, "page_main_controller/message.html",
                                              {'title_msg': title_msg, 'message': message})
                        else:
                            title_msg = sys_msg + '-错误信息展示页面'
                            message = '系统提示：您尚未填报任何职业信息，请返回首页填报鉴定职业'
                            return render(request, "page_main_controller/message.html",
                                          {'title_msg': title_msg, 'message': message})
                    else:
                        form_object_system_message.save()
                return HttpResponseRedirect('/report/send/')
    except Exception as e:
        title_msg = sys_msg + '-错误信息展示页面'
        message = '系统提示：未能获取到相关信息！错误信息提示：' + str(e)
        return render(request, "page_main_controller/message.html",
                      {'title_msg': title_msg, 'message': message})
        # raise e
        # certificate_photos = object_form.cleaned_data.get('certificate_photos_form', None)
        # if certificate_photos:
        #     certificate_photos_obj = Picture.objects.get(id=certificate_photos)
        #     form_object_student_info.certificate_photos = certificate_photos_obj


def system_message_detail(request):
    """
    查看信息详情
    :param request:
    :return:
    """
    not_confirm, message_already_sent, system_announcement = get_message_infos(request)
    record_id = request.GET.get('record_id', None)
    message_type = request.GET.get('message_type', None)
    if record_id:
        system_messages = SystemMessage.objects.filter(id=record_id).order_by("-id")
        if len(system_messages) > 0:
            title_msg = '查看消息详情'

            if message_type:
                return render(request, "page_main_controller/system_message/system_message_detail.html",
                              {'title_msg': title_msg, 'system_message': system_messages[0],
                               'message_type': message_type,
                               'message_not_confirm': not_confirm,
                               'message_already_sent': message_already_sent,
                               'system_announcement': system_announcement})
            else:
                return render(request, "page_main_controller/system_message/system_message_detail.html",
                              {'title_msg': title_msg, 'system_message': system_messages[0],
                               'message_not_confirm': not_confirm,
                               'message_already_sent': message_already_sent,
                               'system_announcement': system_announcement})
        else:
            title_msg = sys_msg + '-错误信息展示页面'
            message = '系统提示：获取数据记录数为 0 条'
            return render(request, "page_main_controller/message.html",
                          {'title_msg': title_msg, 'message': message})
    else:
        title_msg = sys_msg + '-错误信息展示页面'
        message = '系统提示：未能获取到相关信息！'
        return render(request, "page_main_controller/message.html",
                      {'title_msg': title_msg, 'message': message})


def system_message_confirm(request):
    operation_object = None
    try:
        if request.method == 'POST':
            record_id = request.POST.get('record_id', None)
            if int(record_id) > 0:
                object_infos = SystemMessage.objects.filter(id=record_id)
                if len(object_infos) == 1:
                    object_info = object_infos[0]
                    receive_status = object_info.receive_status
                    feedback_status = object_info.feedback_status
                    hidden_status_receiver = object_info.hidden_status_receiver
                    if hidden_status_receiver == '2':
                        # 信息未隐藏
                        if receive_status == '1':
                            # 信息已查看
                            if feedback_status == '2':
                                # 信息未确认
                                object_info.feedback_status = "1"
                                # 修改信息的确认状态
                                object_info.save()
                                operation_object = object_info.id
                                result['status'] = True
                                result['message'] = '信息确认成功'
                                result['data'] = json.dumps({}, ensure_ascii=False)
                            else:
                                result['status'] = False
                                result['message'] = '已确认：请不要重复确认！'
                                result['data'] = json.dumps({}, ensure_ascii=False)
                        else:
                            result['status'] = False
                            result['message'] = '确认失败：信息未查看！'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                    else:
                        result['status'] = False
                        result['message'] = '确认失败：此记录已清理！'
                        result['data'] = json.dumps({}, ensure_ascii=False)
                else:
                    result['status'] = False
                    result['message'] = '确认失败：无此消息记录！'
                    result['data'] = json.dumps({}, ensure_ascii=False)
            else:
                result['status'] = False
                result['message'] = '确认失败：所要操作的记录不存在!'
                result['data'] = ''
        else:
            result['status'] = False
            result['message'] = '确认失败：系统操作请求方式异常!'
            result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_change_status
    save_operation_log(request, inspect.stack()[0][3], "uid:" + str(operation_object), result)
    return JsonResponse(result, safe=False)


def system_message_confirm_send(request):
    """
    确认并发送消息
    :param request:
    :return:
    """
    receiver_message_id = request.GET.get('record_id', None)
    title_msg = '发送信息编辑页面'
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    not_confirm, message_already_sent, system_announcement = get_message_infos(request)
    if receiver_message_id:
        # 提前指定收信人
        receiver_message_infos = SystemMessage.objects.filter(id=receiver_message_id).order_by('-id')
        if len(receiver_message_infos) > 0:
            return render(request, "page_main_controller/system_message/system_message_confirm_send_page.html",
                          {'title_msg': title_msg, 'receiver_message': receiver_message_infos[0],
                           'has_receiver_message': 'true',
                           'teacher_infos': teacher_infos,
                           'school_terms': school_terms, 'school_term': 0, 'teacher_info': 0,
                           'message_not_confirm': not_confirm,
                           'message_already_sent': message_already_sent,
                           'system_announcement': system_announcement})
        else:
            title_msg = sys_msg + '-错误信息展示页面'
            message = '系统提示：没有找到这条记录基础信息，请您重试或查证后再操作！'
            return render(request, "page_main_controller/message.html",
                          {'title_msg': title_msg, 'message': message})
    else:
        title_msg = sys_msg + '-错误信息展示页面'
        message = '系统提示：未能获取到相关信息！'
        return render(request, "page_main_controller/message.html",
                      {'title_msg': title_msg, 'message': message})


def reply_system_message(request):
    """
    确认并回复消息保存
    :param request:
    :return:
    """
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    not_confirm, message_already_sent, system_announcement = get_message_infos(request)
    try:
        not_confirm, message_already_sent, system_announcement = get_message_infos(request)

        if request.method == 'POST':
            object_form = SystemMessageForm(request.POST)
            print(object_form.__str__())
            if object_form.is_valid():
                form_object_system_message = form_to_obj(object_form.cleaned_data, SystemMessage())
                feedback_message = object_form.cleaned_data.get("feedback_message", None)
                form_object_system_message.sender = UserInfo.objects.get(
                    register_user_info__username=request.session.get('username', None))
                if feedback_message:
                    # 是确认回复的消息
                    feedback_message_objects = SystemMessage.objects.filter(id=feedback_message).order_by('-id')
                    if len(feedback_message_objects) > 0:
                        feedback_message_object = feedback_message_objects[0]
                        form_object_system_message.feedback_message = feedback_message_object
                        form_object_system_message.receiver = feedback_message_objects[0].sender
                        # form_object_system_message.feedback_status = "1"
                        form_object_system_message.save()
                        # 将原信息修改成已确认并恢复状态
                        feedback_status = feedback_message_object.feedback_status
                        if feedback_status == '2':
                            # 信息未确认
                            feedback_message_object.feedback_status = "1"
                        reply_status = feedback_message_object.reply_status
                        if reply_status == '2':
                            # 信息未回复
                            feedback_message_object.reply_status = "1"
                        # 保存修改之后的状态
                        feedback_message_object.save()

                        return HttpResponseRedirect('/report/send/')
                        # title_msg = "消息回复详情"
                        # return render(request,
                        #               "page_main_controller/system_message/system_message_confirm_send_page.html",
                        #               {'title_msg': title_msg, 'receiver_message': feedback_message_objects[0],
                        #                'replay_message': form_object_system_message,
                        #                'replay_status': 'true',
                        #                'teacher_infos': teacher_infos,
                        #                'school_terms': school_terms, 'school_term': 0, 'teacher_info': 0,
                        #                'message_not_confirm': not_confirm,
                        #                'message_already_sent': message_already_sent,
                        #                'system_announcement': system_announcement})
                    else:
                        title_msg = sys_msg + '-错误信息展示页面'
                        message = '系统提示：未能获取到相关信息！'
                        return render(request, "page_main_controller/message.html",
                                      {'title_msg': title_msg, 'message': message})
                else:
                    title_msg = sys_msg + '-错误信息展示页面'
                    message = '系统提示：未能获取到相关信息！'
                    return render(request, "page_main_controller/message.html",
                                  {'title_msg': title_msg, 'message': message})
            else:
                title_msg = sys_msg + '-错误信息展示页面'
                message = '操作失败：所要操作的记录不存在！'
                return render(request, "page_main_controller/message.html",
                              {'title_msg': title_msg, 'message': message})
        else:
            title_msg = sys_msg + '-错误信息展示页面'
            message = '操作失败：系统操作请求方式异常！'
            return render(request, "page_main_controller/message.html",
                          {'title_msg': title_msg, 'message': message})
    except Exception as e:
        # raise e
        title_msg = sys_msg + '-错误信息展示页面'
        message = '系统提示：未能获取到相关信息！错误信息提示：' + str(e)
        return render(request, "page_main_controller/message.html",
                      {'title_msg': title_msg, 'message': message})


def system_message_hidden(request):
    operation_object = None
    try:
        if request.method == 'POST':
            record_id = request.POST.get('record_id', None)
            hidden_user = request.POST.get('hidden_user', None)

            if int(record_id) > 0:
                object_infos = SystemMessage.objects.filter(id=record_id)
                if len(object_infos) == 1:
                    object_info = object_infos[0]
                    receive_status = object_info.receive_status
                    feedback_status = object_info.feedback_status

                    if feedback_status == '1':
                        # 信息已确认
                        if receive_status == '1':
                            # 信息已查看
                            if hidden_user == 'sender':
                                hidden_status_sender = object_info.hidden_status_sender
                                if hidden_status_sender == '2':
                                    # 发信人信息未隐藏
                                    object_info.hidden_status_sender = "1"
                                    # 发信人修改信息的隐藏状态（清理即隐藏）
                                    object_info.save()
                                    operation_object = object_info.id
                                    result['status'] = True
                                    result['message'] = '信息清理（不再查看）成功'
                                    result['data'] = json.dumps({}, ensure_ascii=False)
                                else:
                                    result['status'] = False
                                    result['message'] = '已清理：请不要重复清理！'
                                    result['data'] = json.dumps({}, ensure_ascii=False)
                            else:
                                hidden_status_receiver = object_info.hidden_status_receiver
                                if hidden_status_receiver == '2':
                                    # 收信息人信息未隐藏
                                    object_info.hidden_status_receiver = "1"
                                    # 收信人修改信息的隐藏状态（清理即隐藏）
                                    object_info.save()
                                    operation_object = object_info.id
                                    result['status'] = True
                                    result['message'] = '信息清理（不再查看）成功'
                                    result['data'] = json.dumps({}, ensure_ascii=False)
                                else:
                                    result['status'] = False
                                    result['message'] = '已清理：请不要重复清理！'
                                    result['data'] = json.dumps({}, ensure_ascii=False)
                        else:
                            result['status'] = False
                            result['message'] = '清理失败：信息未查看！'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                    else:
                        result['status'] = False
                        result['message'] = '清理失败：此记录未确认！'
                        result['data'] = json.dumps({}, ensure_ascii=False)
                else:
                    result['status'] = False
                    result['message'] = '操作失败：无此消息记录！'
                    result['data'] = json.dumps({}, ensure_ascii=False)
            else:
                result['status'] = False
                result['message'] = '操作失败：所要操作的记录不存在!'
                result['data'] = ''
        else:
            result['status'] = False
            result['message'] = '操作失败：系统操作请求方式异常!'
            result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_change_status
    save_operation_log(request, inspect.stack()[0][3], "uid:" + str(operation_object), result)
    return JsonResponse(result, safe=False)


def get_message_infos(request):
    """
    获取信息的状态数据
    :param request:
    :return:
    """
    username = request.session.get('username', None)
    system_messages = SystemMessage.objects.filter(message_range=1, hidden_status_sender=2).order_by('-id')
    system_announcement = system_messages.count()
    if username:
        registers = RegisterUserInfo.objects.filter(username=username)
        if registers.count() == 1:
            user_infos = UserInfo.objects.filter(register_user_info=registers[0]).order_by('-id')
            if user_infos.count() == 1:
                system_messages_receiver = SystemMessage.objects.filter(receiver=user_infos[0],
                                                                        hidden_status_receiver=2).order_by('-id')
                message_not_confirm = system_messages_receiver.filter(feedback_status=2).count()
                receive_status_not = system_messages_receiver.filter(receive_status=2)
                system_messages = SystemMessage.objects.filter(sender=user_infos[0], hidden_status_sender=2).order_by(
                    '-id')
                message_already_sent = system_messages.count()
                for system_message in receive_status_not:
                    # 将未查看的信息状态设置为已查看
                    system_message.receive_status = "1"
                    system_message.save()
                return message_not_confirm, message_already_sent, system_announcement
            else:
                # 如果暂时没有完善用户信息，将视为未接受消息以及发送消息为0
                return 0, 0, system_announcement
        else:
            return 0, 0, system_announcement
    else:
        return 0, 0, system_announcement
