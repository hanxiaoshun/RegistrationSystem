from webapp.models import *
from django.core.paginator import Paginator
from webapp.utils.form_to_obj import *
from webapp.forms.RegisterTeacherUpdateForm import *
from webapp.utils.save_operation_log import save_operation_log
from webapp.controller.common import *
import inspect
from django.http import JsonResponse
import json
from webapp.controller.renderUtil import render_result
from webapp.utils.date_encoder import *
import inspect
import json

from django.core.paginator import Paginator
from django.http import JsonResponse

from webapp.controller.common import *
from webapp.controller.renderUtil import render_result
from webapp.forms.RegisterTeacherUpdateForm import *
from webapp.models import *
from webapp.utils.date_encoder import *
from webapp.utils.form_to_obj import *
from webapp.utils.save_operation_log import save_operation_log

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def teacher(request):
    worker_type = request.GET['type']
    worker_switch = {
        '0': "page_main_controller/teacher/all_student_base_info.html",
        '1': "page_main_controller/teacher/reporter_chemical.html",
        '3': "page_main_controller/teacher/reporter_chemical_not.html",  # 化工
    }
    title_switch = {
        '0': "学员缴费情况",
        '1': "学员报名资料(化工)",
        '3': "技术评定花名册",
    }
    # 默认是最新一期
    student_infos = StudentInfo.objects.filter(school_term=SchoolTerm.objects.last()).order_by('-id')
    title_msg = sys_msg + '-' + title_switch[worker_type]
    paginator = Paginator(student_infos, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render_result(request, worker_switch[worker_type], {'title_msg': title_msg, "contacts": contacts})


def report_info_review(request):
    """
    管理员确认学员信息列表
    :param request:
    :return:
    """
    title_msg = '学生填报信息待审核列表'
    username = request.session.get('username', None)  # 用户名
    register_user_infos = RegisterUserInfo.objects.filter(username=username)
    school_terms = SchoolTerm.objects.filter().order_by('-id')

    school_terms_values = school_terms.values()
    tmp_list = []
    print(school_terms_values)
    if len(school_terms_values) > 0:
        for i in school_terms_values:
            tmp_json = {}
            tmp_json['id_str'] = i['id']
            tmp_json['school_term_name'] = i['school_term_name']
            tmp_json['school_term_start'] = date_encoder(i['school_term_start'])
            tmp_json['school_term_end'] = date_encoder(i['school_term_end'])
            tmp_list.append(tmp_json)
    print(tmp_list)
    if len(register_user_infos) > 0:
        register_user_info = register_user_infos[0]
        # 消息
        user_info = UserInfo.objects.get(register_user_info=register_user_info)
        system_messages_receiver = SystemMessage.objects.filter(receiver=user_info,
                                                                hidden_status_receiver=2).order_by(
            '-id')
        not_confirm = system_messages_receiver.filter(feedback_status=2).count()
        # 消息
        if register_user_info:
            user_infos = UserInfo.objects.filter(register_user_info=register_user_info)
            if len(user_infos) > 0:
                teacher_infos = TeacherInfo.objects.filter(user_info=user_infos[0])
                if len(teacher_infos) > 0:
                    student_infos = StudentInfo.objects.filter(record_status='1',
                                                               teacher_info=teacher_infos[0]).order_by('-id')
                    paginator = Paginator(student_infos, 20)
                    page = request.GET.get('page')
                    contacts = paginator.get_page(page)
                    if len(school_terms) <= 0:
                        return render_result(request, "index.html",
                                             {'title_msg': title_msg, 'need_login': False,
                                              'no_term': False})
                    else:
                        last_school_term = SchoolTerm.objects.last()
                        # return render(request,
                        #               "page_main_controller/teacher/report_student_info_list_teacher.html",
                        #               {'title_msg': title_msg, 'need_login': False,'school_terms': school_terms,
                        #                'last_school_term': last_school_term, 'no_term': True,
                        #                'contacts': contacts, 'not_confirm': not_confirm})
                        return render_result(request,
                                             "page_main_controller/teacher/report_student_info_list_teacher.html",
                                             {'title_msg': title_msg, 'need_login': False,
                                              'last_school_term': last_school_term,
                                              'no_term': True, 'contacts': contacts,
                                              'school_terms': school_terms,
                                              'tmp_list': json.dumps(tmp_list, ensure_ascii=False),
                                              'not_confirm': not_confirm, 'school_term': 0,
                                              'identification_level': 0})
                    #
                    # return render(request, "page_main_controller/teacher/report_student_info_list_teacher.html",
                    #               {'title_msg': title_msg, "contacts": contacts})
            else:
                message = '系统提示：获取当前用户基本信息失败，请重新登陆后尝试，或联系管理员'
                return render_result(request, "page_main_controller/message.html",
                                     {'title_msg': title_msg, 'message': message})
        else:
            message = '系统提示：获取当前用户失败，请重新登陆后尝试，或联系管理员.'
            return render_result(request, "page_main_controller/message.html",
                                 {'title_msg': title_msg, 'message': message})
    else:
        message = '系统提示：获取当前用户失败，请重新登陆后尝试，或联系管理员'
        return render_result(request, "page_main_controller/message.html",
                             {'title_msg': title_msg, 'message': message})


def report_do_review(request):
    """
    负责人确认审核信息
    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            student_del_id = request.POST.get('record_id', None)
            if int(student_del_id) > 0:
                student_infos = StudentInfo.objects.filter(id=student_del_id)
                if len(student_infos) == 1:
                    student_info = student_infos[0]
                    submit_status = student_info.submit_status
                    record_status = student_info.record_status
                    cancel_status = student_info.cancel_status
                    review_status = student_info.review_status
                    confirm_status = student_info.confirm_status
                    print("cancel_status:::" + cancel_status)
                    if int(record_status) == 1:
                        # 资料状态正常
                        if int(submit_status) == 1:
                            # 已提交
                            if int(cancel_status) == 2:
                                # 未申请注销
                                if review_status == "2":
                                    if confirm_status == "2":
                                        student_info.review_status = "1"
                                        operation_object = student_info.id
                                        student_info.save()
                                        result['status'] = True
                                        result['message'] = '审核记录成功'
                                        result['data'] = json.dumps({}, ensure_ascii=False)
                                    else:
                                        result['status'] = False
                                        result['message'] = '审核失败，此纪录已经由系统管理员确认，您不需要再审核！'
                                        result['data'] = json.dumps({}, ensure_ascii=False)
                                else:
                                    result['status'] = False
                                    result['message'] = '已审核，请不要重复审核！'
                                    result['data'] = json.dumps({}, ensure_ascii=False)
                            else:
                                result['status'] = False
                                result['message'] = '审核失败，此纪录正在申请注销，请处理此纪录的申请注销信息！'
                                result['data'] = json.dumps({}, ensure_ascii=False)
                        else:
                            result['status'] = False
                            result['message'] = '审核失败，此记录尚未提交！'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                    else:
                        result['status'] = False
                        result['message'] = '审核失败，此记录已是注销状态，不可操作！'
                        result['data'] = json.dumps({}, ensure_ascii=False)
                else:
                    result['status'] = False
                    result['message'] = '所要提交的记录不存在!'
                    result['data'] = ''
            else:
                result['status'] = False
                result['message'] = '所要提交的记录不存在!'
                result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_change_status
    save_operation_log(request, inspect.stack()[0][3], "uid:" + str(operation_object), result)
    return JsonResponse(result, safe=False)


def report_do_review_cancel(request):
    """
    取消确认审核
    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            student_del_id = request.POST.get('record_id', None)
            if int(student_del_id) > 0:
                student_infos = StudentInfo.objects.filter(id=student_del_id)
                if len(student_infos) == 1:
                    student_info = student_infos[0]
                    submit_status = student_info.submit_status
                    record_status = student_info.record_status
                    cancel_status = student_info.cancel_status
                    review_status = student_info.review_status
                    confirm_status = student_info.confirm_status
                    print("cancel_status:::" + cancel_status)
                    if int(record_status) == 1:
                        # 资料状态正常
                        if int(submit_status) == 1:
                            # 已提交
                            if int(cancel_status) == 2:
                                # 未申请注销
                                if review_status == "1":
                                    if confirm_status == "2":
                                        student_info.review_status = "2"
                                        operation_object = student_info.id
                                        student_info.save()
                                        result['status'] = True
                                        result['message'] = '取消审核成功'
                                        result['data'] = json.dumps({}, ensure_ascii=False)
                                    else:
                                        result['status'] = False
                                        result['message'] = '取消审核失败，此纪录处于学校管理员确认通过状态！'
                                        result['data'] = json.dumps({}, ensure_ascii=False)
                                else:
                                    result['status'] = False
                                    result['message'] = '未审核或已经取消审核，请不要重复操作！'
                                    result['data'] = json.dumps({}, ensure_ascii=False)
                            else:
                                result['status'] = False
                                result['message'] = '审核失败，此纪录正在申请注销，请处理此纪录的申请注销信息！'
                                result['data'] = json.dumps({}, ensure_ascii=False)
                        else:
                            result['status'] = False
                            result['message'] = '审核失败，此记录尚未提交！'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                    else:
                        result['status'] = False
                        result['message'] = '审核失败，此记录已是注销状态，不可操作！'
                        result['data'] = json.dumps({}, ensure_ascii=False)
                else:
                    result['status'] = False
                    result['message'] = '所要提交的记录不存在!'
                    result['data'] = ''
            else:
                result['status'] = False
                result['message'] = '所要提交的记录不存在!'
                result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_change_status
    save_operation_log(request, inspect.stack()[0][3], "uid:" + str(operation_object), result)
    return JsonResponse(result, safe=False)


def to_update_teacher(request):
    """
    跳转修改弹窗页面
    :param request:
    :return:
    """
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher_id', None)
        if teacher_id:
            teacher_info_values = TeacherInfo.objects.filter(id=teacher_id)
            if len(teacher_info_values) == 1:
                teacher_info_object = teacher_info_values[0]
                teacher_info_values = teacher_info_values.values()[0]
                teacher_info_object_user_info = teacher_info_object.user_info
                teacher_info_object_user_info_values = teacher_info_object.user_info.__dict__
                teacher_info_object_user_info_reg_values = teacher_info_object.user_info.register_user_info.__dict__
                # school_term['school_term_start'] = date_encoder(school_term['school_term_start'])
                # school_term['school_term_end'] = date_encoder(school_term['school_term_end'])
                tmp_dict = {}
                for k, v in teacher_info_object_user_info_reg_values.items():
                    tmp_dict[k] = v
                for k, v in teacher_info_object_user_info_values.items():
                    tmp_dict[k] = v
                for k, v in teacher_info_values.items():
                    tmp_dict[k] = v
                del tmp_dict['_state']
                del tmp_dict['password']
                del tmp_dict['create_time']
                del tmp_dict['modify_time']

                print(tmp_dict.__str__())

                result['status'] = True
                result['message'] = '获取成功！'
                result['data'] = json.dumps(tmp_dict, ensure_ascii=False)
                return JsonResponse(result, safe=False)
            else:
                result['status'] = False
                result['message'] = '系统异常，请稍后尝试或联系管理员!'
                result['data'] = ''
        else:
            result['status'] = False
            result['message'] = '系统异常，请稍后尝试或联系管理员!'
            result['data'] = ''
    else:
        result['status'] = False
        result['message'] = '系统异常，请稍后尝试或联系管理员!'
        result['data'] = ''
    return JsonResponse(result, safe=False)


def update_teacher_info(request):
    """
    修改负责任的基本信息
    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            object_form = RegisterTeacherUpdateForm(request.POST)
            if object_form.is_valid():
                update_id = object_form.cleaned_data.get('update_id', None)
                if update_id:
                    main_object_terms = TeacherInfo.objects.filter(id=update_id)
                    if len(main_object_terms) == 1:
                        form_object_main_object = form_to_obj(object_form.cleaned_data, main_object_terms[0])
                        form_object_main_object.save()
                        # 用户基础信息
                        form_object_user_info = form_to_obj(object_form.cleaned_data, form_object_main_object.user_info)
                        form_object_user_info.save()
                        operation_object = form_object_user_info
                        # 注册信息修改（除了密码信息）
                        form_object_register_user_info = form_to_obj(object_form.cleaned_data,
                                                                     form_object_user_info.register_user_info)
                        form_object_register_user_info.save()
                        result['status'] = True
                        result['message'] = '修改成功！'
                        result['data'] = json.dumps({}, ensure_ascii=False)
                        return JsonResponse(result, safe=False)
            else:
                print(type(object_form.errors), object_form.errors)  # errors类型是ErrorDict，里面是ul，li标签
                result['status'] = False
                result['message'] = '系统异常，请稍后尝试或联系管理员!'
                result['data'] = ''
        else:
            result['status'] = False
            result['message'] = '系统异常，请稍后尝试或联系管理员!'
            result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_edit
    save_operation_log(request, inspect.stack()[0][3], operation_object.__str__(True), result)
    return JsonResponse(result, safe=False)


def cancel_teacher(request):
    """
    注销此负责人
    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            teacher_id = request.POST.get('teacher_id', None)
            if teacher_id:
                teacher_info_values = TeacherInfo.objects.filter(id=teacher_id)
                if len(teacher_info_values) == 1:
                    teacher_info_object = teacher_info_values[0]
                    teacher_info_object.status = "2"
                    teacher_info_object.save()
                    operation_object = teacher_info_object.id
                    result['status'] = True
                    result['message'] = '注销成功！'
                    result['data'] = json.dumps({}, ensure_ascii=False)
                elif len(teacher_info_values) == 2:
                    result['status'] = False
                    result['message'] = '已经是注销状态。'
                    result['data'] = ''
                else:
                    result['status'] = False
                    result['message'] = '注销失败！系统识别错误，请联系管理员！'
                    result['data'] = ''
            else:
                result['status'] = False
                result['message'] = '注销失败！系统异常，请稍后尝试或联系管理员!'
                result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_change_status
    save_operation_log(request, inspect.stack()[0][3], "uid:" + str(operation_object), result)
    return JsonResponse(result, safe=False)


def start_teacher(request):
    """
    启用此负责人
    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            teacher_id = request.POST.get('teacher_id', None)
            if teacher_id:
                teacher_info_values = TeacherInfo.objects.filter(id=teacher_id)
                if len(teacher_info_values) == 1:
                    teacher_info_object = teacher_info_values[0]
                    if int(teacher_info_object.status) == 2:
                        teacher_info_object.status = '1'
                        teacher_info_object.save()
                        operation_object = teacher_info_object.id
                        result['status'] = True
                        result['message'] = '启用成功！'
                        result['data'] = json.dumps({}, ensure_ascii=False)
                    elif int(teacher_info_object.status) == 1:
                        result['status'] = False
                        result['message'] = '已经是启用状态。'
                        result['data'] = ''
                    else:
                        result['status'] = False
                        result['message'] = '启用失败！系统识别错误，请联系管理员！'
                        result['data'] = ''
                else:
                    result['status'] = False
                    result['message'] = '注销失败！系统暂无本负责人信息，请重试或者联系管理员。'
                    result['data'] = ''
            else:
                result['status'] = False
                result['message'] = '注销失败！系统异常，请稍后尝试或联系管理员!'
                result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_change_status
    save_operation_log(request, inspect.stack()[0][3], "uid:" + str(operation_object), result)
    return JsonResponse(result, safe=False)
