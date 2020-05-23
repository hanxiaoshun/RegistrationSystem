import inspect
import json

from django.core.paginator import Paginator
from django.http import JsonResponse

from baoming.settings import MEDIA_ROOT
from webapp.controller.common import *
from webapp.controller.renderUtil import render_result
from webapp.forms.RegisterTeacherForm import *
from webapp.forms.SchoolTermForm import SchoolTermForm
from webapp.forms.SchoolTermUpdateForm import SchoolTermUpdateForm
from webapp.models import *
from webapp.utils.date_encoder import *
from webapp.utils.form_to_obj import *
from webapp.utils.password import *
from webapp.utils.psInfo import PsInfo, DiskInfo
from webapp.utils.save_operation_log import save_operation_log
from webapp.utils.shutilwhichUtil import term_make_archive
from webapp.utils.system_info import SystemInfo, SystemPythonInfo

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def administrator_all_student_base_info(request):
    role_name = request.session.get('role_name', None)  # 用户名
    print(role_name)
    if role_name in 'teacher':
        username = request.session.get('username', None)  # 用户名
        if username:
            register_user_info = RegisterUserInfo.objects.get(username=username)
            user_info_tmp = UserInfo.objects.get(register_user_info=register_user_info)
            teacher_tmp = TeacherInfo.objects.get(user_info=user_info_tmp)
            print(teacher_tmp)
            
    else:
        pass
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    # 消息
    school_terms_values = school_terms.values()
    tmp_list = []
    if len(school_terms_values) > 0:
        for i in school_terms_values:
            tmp_json = {}
            tmp_json['id_str'] = i['id']
            tmp_json['school_term_name'] = i['school_term_name']
            tmp_json['school_term_start'] = date_encoder(i['school_term_start'])
            tmp_json['school_term_end'] = date_encoder(i['school_term_end'])
            tmp_list.append(tmp_json)
    last_school_term = SchoolTerm.objects.last()
    student_infos = StudentInfo.objects.filter(confirm_status=1, cancel_status=2, ).order_by('-id')
    paginator = Paginator(student_infos, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render_result(request, "page_main_controller/administrator/all_student_base_info.html",
                         {'title_msg': '学员报名表',
                          'last_school_term': last_school_term,
                          'no_term': False, 'contacts': contacts, 'teacher_infos': teacher_infos,
                          'school_terms': school_terms, 'tmp_list': json.dumps(tmp_list, ensure_ascii=False),
                          'school_term': 0, 'teacher_info': 0,
                          'identification_level': 0}
                         )


def administrator_reporter_chemical(request):
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    # 消息
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
    last_school_term = SchoolTerm.objects.last()
    # 化工类学生
    student_infos = StudentInfo.objects.filter(confirm_status=1, cancel_status=2, chemical_worker=1).order_by('-id')
    paginator = Paginator(student_infos, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    return render_result(request,
                         "page_main_controller/administrator/reporter_chemical.html",
                         {'title_msg': '学员报名表',
                          'last_school_term': last_school_term,
                          'no_term': False, 'contacts': contacts, 'teacher_infos': teacher_infos,
                          'school_terms': school_terms, 'tmp_list': json.dumps(tmp_list, ensure_ascii=False),
                          'school_term': 0, 'teacher_info': 0,
                          'identification_level': 0})


def administrator_reporter_chemical_not(request):
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    # 消息
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
    last_school_term = SchoolTerm.objects.last()
    # 非化工类学生
    student_infos = StudentInfo.objects.filter(confirm_status=1, cancel_status=2, chemical_worker=2).order_by('-id')
    paginator = Paginator(student_infos, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render_result(request,
                         "page_main_controller/administrator/reporter_chemical_not.html",
                         {'title_msg': '学员报名表',
                          'last_school_term': last_school_term,
                          'no_term': False, 'contacts': contacts, 'teacher_infos': teacher_infos,
                          'school_terms': school_terms, 'tmp_list': json.dumps(tmp_list, ensure_ascii=False),
                          'school_term': 0, 'teacher_info': 0,
                          'identification_level': 0})


def report_info_confirm(request):
    """
    管理员确认学员信息列表
    :param request:
    :return:
    """
    teacher_infos = TeacherInfo.objects.all()
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    # student_infos = StudentInfo.objects.filter(review_status=1, cancel_status=2,
    #                                            school_term=SchoolTerm.objects.last()).order_by('-id')
    # student_infos = StudentInfo.objects.filter(review_status=1, cancel_status=2).order_by('-id')
    # 应该是已经提交的，这样确认人需要知晓哪些被审核了那些尚未被审核
    student_infos = StudentInfo.objects.filter(submit_status=1, cancel_status=2).order_by('-id')
    paginator = Paginator(student_infos, 20)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    title_msg = '学生填报信息待确认列表'

    # 消息
    register_user_info = RegisterUserInfo.objects.get(username=request.session.get('username', None))
    user_info = UserInfo.objects.get(register_user_info=register_user_info)
    system_messages_receiver = SystemMessage.objects.filter(receiver=user_info,
                                                            hidden_status_receiver=2).order_by(
        '-id')
    not_confirm = system_messages_receiver.filter(feedback_status=2).count()
    # 消息
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
    if len(school_terms) <= 0:
        return render_result(request, "index.html",
                             {'title_msg': title_msg, 'need_login': False, 'no_term': False})
    else:
        last_school_term = SchoolTerm.objects.last()
        return render_result(request,
                             "page_main_controller/administrator/report_student_info_list_admin.html",
                             {'title_msg': title_msg, 'need_login': False,
                              'last_school_term': last_school_term,
                              'no_term': True, 'contacts': contacts, 'teacher_infos': teacher_infos,
                              'school_terms': school_terms, 'tmp_list': json.dumps(tmp_list, ensure_ascii=False),
                              'not_confirm': not_confirm, 'school_term': 0, 'teacher_info': 0,
                              'identification_level': 0})


def report_teacher_list(request):
    """
        单位负责人确认学员信息列表
        :param request:
        :return:
    """
    teacher_infos = TeacherInfo.objects.filter().order_by('-id')
    print(str(teacher_infos.values()))
    paginator = Paginator(teacher_infos, 20)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    title_msg = '学生填报信息待确认列表'
    return render_result(request, "page_main_controller/administrator/teacher_list.html",
                         {'title_msg': title_msg, "contacts": contacts})


def report_school_term_list(request):
    """
    报名周期管理
    :return:
    """
    school_terms = SchoolTerm.objects.filter().order_by('-id')
    paginator = Paginator(school_terms, 20)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    title_msg = '报名周期确认列表'
    return render_result(request, "page_main_controller/administrator/school_term_list.html",
                         {'title_msg': title_msg, "contacts": contacts})


def add_school_term(request):
    """
    添加报名周期
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            object_form = SchoolTermForm(request.POST)
            if object_form.is_valid():
                form_object_school_term = form_to_obj(object_form.cleaned_data, SchoolTerm())
                form_object_school_term.save()
                school_term_name = str(timezone.now().year) + "年第" + str(SchoolTerm.objects.count()) + "期"
                form_object_school_term.school_term_name = school_term_name
                form_object_school_term.save()
                operation_object = form_object_school_term
                result['status'] = True
                result['message'] = '新一期报名开始、截止时间添加成功！'
                result['data'] = json.dumps({}, ensure_ascii=False)

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
    result["level"] = log_level_add
    save_operation_log(request, inspect.stack()[0][3], operation_object.__str__(True), result)
    return JsonResponse(result, safe=False)


def to_update_term_info(request):
    """
    返回信息
    :param request:
    :return:
    """
    if request.method == 'POST':
        term_id = request.POST.get('term_id', None)
        if term_id:
            school_term_values = SchoolTerm.objects.filter(id=term_id).values('id', 'school_term_start',
                                                                              'school_term_end', 'explain')
            if len(school_term_values) == 1:
                school_term = school_term_values[0]
                school_term['school_term_start'] = date_encoder(school_term['school_term_start'])
                school_term['school_term_end'] = date_encoder(school_term['school_term_end'])
                result['status'] = True
                result['message'] = '新一期报名开始、截止时间添加成功！'
                result['data'] = json.dumps(school_term, ensure_ascii=False)
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


def date_encoder(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.strftime('%Y-%m-%d')


def update_school_term(request):
    """
    修改周期的开始时间和结束时间
    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            object_form = SchoolTermUpdateForm(request.POST)
            if object_form.is_valid():
                update_id = object_form.cleaned_data.get('update_id', None)
                if update_id:
                    school_terms = SchoolTerm.objects.filter(id=update_id)
                    if len(school_terms) == 1:
                        form_object_school_term = form_to_obj(object_form.cleaned_data, school_terms[0])
                        form_object_school_term.save()
                        operation_object = form_object_school_term
                        result['status'] = True
                        result['message'] = '修改成功！'
                        result['data'] = json.dumps({}, ensure_ascii=False)
                    else:
                        result['status'] = False
                        result['message'] = '系统异常，请稍后尝试或联系管理员!'
                        result['data'] = ''
            else:
                print(type(object_form.errors), object_form.errors)  # errors类型是ErrorDict，里面是ul，li标签
                result['status'] = False
                result['message'] = '系统异常，请稍后尝试或联系管理员!错误提示：' + type(object_form.errors) + "," + object_form.errors
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


def register_teacher(request):
    """
    系统管理员添加负责人信息
    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            object_form = RegisterTeacherForm(request.POST)
            if object_form.is_valid():
                form_object_register = form_to_obj(object_form.cleaned_data, RegisterUserInfo())
                # 密码加密处理
                # 保存注册信息
                form_object_register.password = Password.encryption(form_object_register.password)
                form_object_register.role = RoleInfo.objects.get(role_name='teacher')
                form_object_register.save()

                # 关联用户基本信息，注册基本信息表
                user_info = UserInfo()
                real_name = object_form.cleaned_data.get('real_name', None)
                if real_name:
                    user_info.real_name = real_name

                work_unit = object_form.cleaned_data.get('work_unit', None)
                if work_unit:
                    user_info.work_unit = work_unit

                contact_number = object_form.cleaned_data.get('contact_number', None)
                if contact_number:
                    user_info.contact_number = contact_number

                user_info.register_user_info = form_object_register
                user_info.save()

                teacher_info = TeacherInfo()
                teacher_info.user_info = user_info
                teacher_explain = object_form.cleaned_data.get('explain', None)
                if teacher_explain:
                    teacher_info.explain = teacher_explain
                teacher_info.number = "xlt" + str(form_object_register.id)
                teacher_info.save()
                operation_object = teacher_info
                result['status'] = True
                result['message'] = '负责人:' + form_object_register.username + ', 注册成功,编号为：！' + teacher_info.number
                result['data'] = json.dumps({}, ensure_ascii=False)
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
    result["level"] = log_level_register
    save_operation_log(request, inspect.stack()[0][3], operation_object.__str__(True), result)
    return JsonResponse(result, safe=False)


def report_do_confirm(request):
    """
    超级管理员进行信息最终确认
    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            record_id = request.POST.get('record_id', None)
            if int(record_id) > 0:
                student_infos = StudentInfo.objects.filter(id=record_id)
                if len(student_infos) == 1:
                    student_info = student_infos[0]
                    submit_status = student_info.submit_status
                    record_status = student_info.record_status
                    cancel_status = student_info.cancel_status
                    review_status = student_info.review_status
                    confirm_status = student_info.confirm_status
                    print("cancel_status:::" + cancel_status)
                    if record_status == '1':
                        # 资料状态正常
                        if submit_status == '1':
                            # 已提交
                            if cancel_status == '2':
                                # 未申请注销
                                print("review_status:::" + review_status)
                                if review_status == '1':
                                    # 负责人已审核
                                    if confirm_status == '2':
                                        # 信息未确认
                                        student_info.confirm_status = "1"
                                        student_info.save()
                                        operation_object = student_info.id
                                        result['status'] = True
                                        result['message'] = '确认成功'
                                        result['data'] = json.dumps({}, ensure_ascii=False)

                                        # 多工种备注的配置
                                        confirms = StudentInfo.objects.filter(confirm_status=1,
                                                                              user_info=student_info.user_info).order_by(
                                            '-id')
                                        explain_current = ''
                                        for index in range(0, len(confirms)):
                                            declaration_of_occupation = confirms[index].declaration_of_occupation
                                            identification_level = confirms[index].identification_level
                                            if '工业废水' in declaration_of_occupation:
                                                declaration_of_occupation_first = '工废'
                                            elif '工业固体' in declaration_of_occupation:
                                                declaration_of_occupation_first = '工固'
                                            elif '中式烹调师' in declaration_of_occupation:
                                                declaration_of_occupation_first = '烹'
                                            elif '中式面点师' in declaration_of_occupation:
                                                declaration_of_occupation_first = '面'
                                            elif '电梯安装维修工' in declaration_of_occupation:
                                                declaration_of_occupation_first = '电梯'
                                            else:
                                                declaration_of_occupation_first = str(declaration_of_occupation)[0:1]
                                            identification_level_dict = {'5': '(初)', '4': '(中)', '3': '(高)'}
                                            identification_level_str = identification_level_dict[
                                                str(identification_level)]
                                            explain = declaration_of_occupation_first + identification_level_str
                                            confirms[index].explain = explain
                                            if index == 0:
                                                explain_current = explain
                                            else:
                                                explain_current = explain_current + ',' + explain
                                            confirms[index].save()

                                        for student in confirms:
                                            student.explain = explain_current
                                            student.save()
                                            # explain_previous = confirms[1].explain
                                            # for index in range(0, len(confirms)):
                                            #     if index == len(confirms) - 1:
                                            #         if confirms[index].explain not in explain_current:
                                            #             explain_current = explain_current + confirms[index].explain
                                            #     else:
                                            #         explain_current = explain_current + confirms[index].explain + ','
                                    else:
                                        result['status'] = False
                                        result['message'] = '已确认，请不要重复确认！'
                                        result['data'] = json.dumps({}, ensure_ascii=False)
                                else:
                                    result['status'] = False
                                    result['message'] = '确认失败，此纪录正在审核之中，请通知负责人审核信息！'
                                    result['data'] = json.dumps({}, ensure_ascii=False)
                            else:
                                result['status'] = False
                                result['message'] = '确认失败，此纪录正在申请注销，请督促负责人处理此纪录的申请注销信息！'
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


def report_cancel_confirm(request):
    """
    超级管理员取消确认
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
                    if record_status == '1':
                        # 资料状态正常
                        if submit_status == '1':
                            # 已提交
                            if cancel_status == '2':
                                # 未申请注销
                                print("review_status:::" + review_status)
                                if review_status == '1':
                                    # 负责人已审核
                                    if confirm_status == '1':
                                        # 信息已经确认，取消确认
                                        student_info.confirm_status = "2"
                                        student_info.save()
                                        operation_object = student_info.id
                                        result['status'] = True
                                        result['message'] = '取消成功'
                                        result['data'] = json.dumps({}, ensure_ascii=False)

                                        # 取消本学员的多工种备注的配置
                                        declaration_of_occupation = student_info.declaration_of_occupation
                                        identification_level = student_info.identification_level
                                        if '工业废水' in declaration_of_occupation:
                                            declaration_of_occupation_first = '工废'
                                        elif '工业固体' in declaration_of_occupation:
                                            declaration_of_occupation_first = '工固'
                                        elif '中式烹调师' in declaration_of_occupation:
                                            declaration_of_occupation_first = '烹'
                                        elif '中式面点师' in declaration_of_occupation:
                                            declaration_of_occupation_first = '面'
                                        elif '电梯安装维修工' in declaration_of_occupation:
                                            declaration_of_occupation_first = '电梯'
                                        else:
                                            declaration_of_occupation_first = str(declaration_of_occupation)[0:1]
                                        identification_level_dict = {'5': '(初)', '4': '(中)', '3': '(高)'}
                                        identification_level_str = identification_level_dict[str(identification_level)]
                                        explain = declaration_of_occupation_first + identification_level_str
                                        student_info.explain = explain
                                        student_info.save()

                                        confirms = StudentInfo.objects.filter(confirm_status=1,
                                                                              user_info=student_info.user_info).order_by(
                                            '-id')
                                        if len(confirms) > 0:
                                            explain_cancel = student_info.explain
                                            explain_confirm = confirms[0].explain
                                            if ',' + explain_cancel in explain_confirm:
                                                print('需要取消备注内容存在，应当去除掉')
                                                explain_confirm = str(explain_confirm).replace(',' + explain_cancel, '')
                                            if explain_cancel + ',' in explain_confirm:
                                                print('需要取消备注内容存在，应当去除掉')
                                                explain_confirm = str(explain_confirm).replace(explain_cancel + ',', '')
                                            else:
                                                pass

                                            for student in confirms:
                                                student.explain = explain_confirm
                                                student.save()
                                        else:
                                            pass

                                    else:
                                        result['status'] = False
                                        result['message'] = '尚未确认，请不要执行取消操作！'
                                        result['data'] = json.dumps({}, ensure_ascii=False)
                                else:
                                    result['status'] = False
                                    result['message'] = '取消失败，此纪录正在审核之中，请通知负责人审核信息！'
                                    result['data'] = json.dumps({}, ensure_ascii=False)
                            else:
                                result['status'] = False
                                result['message'] = '取消失败，此纪录正在申请注销，请督促负责人处理此纪录的申请注销信息！'
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
                    result['message'] = '所要操作的记录不存在!'
                    result['data'] = ''
            else:
                result['status'] = False
                result['message'] = '所要操作的记录不存在!'
                result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_change_status
    save_operation_log(request, inspect.stack()[0][3], "uid:" + str(operation_object), result)
    return JsonResponse(result, safe=False)


def refresh_school_term_data(request):
    """
    刷新本期报名的相关数据信息
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            term_id = request.POST.get('term_id', None)
            if term_id:
                school_terms = SchoolTerm.objects.filter(id=term_id)
                if len(school_terms) == 1:
                    school_term = school_terms[0]
                    student_infos = StudentInfo.objects.filter(school_term=school_term)
                    if len(student_infos) > 0:
                        school_term.students = student_infos.count()
                        school_term.students_chemical = student_infos.filter(chemical_worker=1,
                                                                             confirm_status=1).count()
                        school_term.students_chemical_not = student_infos.filter(chemical_worker=2,
                                                                                 confirm_status=1).count()
                        school_term.students_submit = student_infos.filter(submit_status=1, confirm_status=1).count()
                        school_term.students_submit_not = student_infos.filter(submit_status=2,
                                                                               confirm_status=1).count()
                        school_term.students_review = student_infos.filter(review_status=1, confirm_status=1).count()
                        school_term.students_review_not = student_infos.filter(review_status=2,
                                                                               confirm_status=1).count()
                        school_term.students_confirm = student_infos.filter(confirm_status=1).count()
                        school_term.students_confirm_not = student_infos.filter(confirm_status=2).count()
                        school_term.students_pay = student_infos.filter(payment_amount__gt=0, confirm_status=1).count()
                        school_term.students_pay_not = student_infos.filter(unpaid_amount__gt=0,
                                                                            confirm_status=1).count()
                        school_term.students_status_yes = student_infos.filter(record_status=1,
                                                                               confirm_status=1).count()
                        school_term.students_status_not = student_infos.filter(record_status=2,
                                                                               confirm_status=1).count()
                        print(school_term.__str__())
                        school_term.save()
                        result['status'] = True
                        result['message'] = '信息刷新完毕！'
                        result['data'] = json.dumps({}, ensure_ascii=False)
                    else:
                        school_term.students = student_infos.count()
                        school_term.students_chemical = student_infos.filter(chemical_worker=1,
                                                                             confirm_status=1).count()
                        school_term.students_chemical_not = student_infos.filter(chemical_worker=2,
                                                                                 confirm_status=1).count()
                        school_term.students_submit = student_infos.filter(submit_status=1, confirm_status=1).count()
                        school_term.students_submit_not = student_infos.filter(submit_status=2,
                                                                               confirm_status=1).count()
                        school_term.students_review = student_infos.filter(review_status=1, confirm_status=1).count()
                        school_term.students_review_not = student_infos.filter(review_status=2,
                                                                               confirm_status=1).count()
                        school_term.students_confirm = student_infos.filter(confirm_status=1).count()
                        school_term.students_confirm_not = student_infos.filter(confirm_status=2).count()
                        school_term.students_pay = student_infos.filter(payment_amount__gt=0, confirm_status=1).count()
                        school_term.students_pay_not = student_infos.filter(unpaid_amount__gt=0,
                                                                            confirm_status=1).count()
                        school_term.students_status_yes = student_infos.filter(record_status=1,
                                                                               confirm_status=1).count()
                        school_term.students_status_not = student_infos.filter(record_status=2,
                                                                               confirm_status=1).count()
                        school_term.save()
                        result['status'] = False
                        result['message'] = '本期尚未开始报名，或报名学生数量为0，暂不刷新!'
                        result['data'] = ''

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
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    return JsonResponse(result, safe=False)


def del_term_info(request):
    """
    删除本学期数据
    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            record_id = request.POST.get('record_id', None)
            if record_id:
                school_terms = SchoolTerm.objects.filter(id=record_id)
                if len(school_terms) == 1:
                    school_term = school_terms[0]
                    student_infos = StudentInfo.objects.filter(school_term=school_term)
                    if len(student_infos) == 0:
                        operation_object = school_term
                        school_term.delete()
                        object_infos_check = SchoolTerm.objects.filter(id=record_id)
                        if len(object_infos_check) == 0:
                            result['status'] = True
                            result['message'] = '删除记录成功'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                        else:
                            result['status'] = False
                            result['message'] = '系统错误：为获取到本信息或本信息已被删除!'
                            result['data'] = ''
                    elif len(student_infos) > 0:
                        result['status'] = False
                        result['message'] = '删除失败:此学期已有报名学员信息未处理，无法删除!'
                        result['data'] = ''
                else:
                    result['status'] = False
                    result['message'] = '删除失败:系统为获取到本学期信息!'
                    result['data'] = ''
        else:
            result['status'] = False
            result['message'] = '系统异常:请稍后尝试或联系管理员!'
            result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_cancel
    save_operation_log(request, inspect.stack()[0][3], operation_object.__str__(True), result)
    return JsonResponse(result, safe=False)


def admin_del_term_info_data(request):
    """
    学校管理员删除当前学期的学生填报数据
    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            record_id = request.POST.get('record_id', None)
            if record_id:
                school_terms = SchoolTerm.objects.filter(id=record_id)
                if len(school_terms) == 1:
                    school_term = school_terms[0]
                    operation_object = school_term.school_term_name
                    if StudentInfo.objects.filter(school_term=school_term).count() > 0:
                        StudentInfo.objects.filter(school_term=school_term).delete()
                        if StudentInfo.objects.filter(school_term=school_term).count() == 0:
                            result['status'] = True
                            result['message'] = '删除填报数据成功'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                        else:
                            result['status'] = False
                            result['message'] = '删除失败:数据异常，或删除之后数据有残留!'
                            result['data'] = ''
                    else:
                        result['status'] = False
                        result['message'] = '删除失败:本期暂无填报数据，或已经清空!'
                        result['data'] = ''
                else:
                    result['status'] = False
                    result['message'] = '删除失败:此学期信息有误，无法删除!'
                    result['data'] = ''
            else:
                result['status'] = False
                result['message'] = '系统异常:请求参数异常!'
                result['data'] = ''
        else:
            result['status'] = False
            result['message'] = '系统异常:请求方式异常!'
            result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_cancel
    save_operation_log(request, inspect.stack()[0][3], operation_object, result)
    return JsonResponse(result, safe=False)


def admin_del_student(request):
    """
    管理员删除
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
                    cancel_status = student_info.cancel_status
                    cancel_result = student_info.cancel_result
                    confirm_status = student_info.confirm_status
                    if int(confirm_status) == 1:
                        # 如果是已提交状态，将无法删除
                        result['status'] = False
                        result['message'] = '所要删除的记录信息已经确认，您无法删除。'
                        result['data'] = ''
                    else:
                        # 如果是未提交状态，可以删除
                        student_info.delete()
                        student_infos_check = StudentInfo.objects.filter(id=student_del_id)
                        if len(student_infos_check) == 0:
                            operation_object = student_info
                            result['status'] = True
                            result['message'] = '删除记录成功'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                        else:
                            result['status'] = False
                            result['message'] = '未能成功删除或者有多条记录，请查询确认后继续删除!'
                            result['data'] = ''
                else:
                    result['status'] = False
                    result['message'] = '系统获取相关数据数量异常，请稍后再试，或联系管理员!'
                    result['data'] = ''
            else:
                result['status'] = False
                result['message'] = '所要删除的记录不存在!'
                result['data'] = ''
        else:
            result['status'] = False
            result['message'] = '所要删除的记录不存在!'
            result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_cancel
    save_operation_log(request, inspect.stack()[0][3], operation_object.__str__(True), result)
    return JsonResponse(result, safe=False)


def report_operation_log_list(request):
    """
    返回管理员日志列表页面
    :param request:
    :return:
    """
    interview_audits = InterviewAudit.objects.filter().order_by('-id')
    paginator = Paginator(interview_audits, 20)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    title_msg = '系统日志信息列表'
    return render_result(request, "page_main_controller/administrator/operation_log_list.html",
                         {'title_msg': title_msg, "contacts": contacts})


def report_system_info_detail(request):
    """
    系统运行信息
    :param request:
    :return:
    """
    title_msg = '系统运行信息'
    ps_info = PsInfo()
    disk_info = DiskInfo()
    system_info = SystemInfo()
    system_python_info = SystemPythonInfo()
    return render_result(request, "page_main_controller/system_info/system_info_detail.html",
                         {'title_msg': title_msg,
                          'ps_info': ps_info,
                          'disk_info': disk_info,
                          'system_info': system_info,
                          'system_python_info': system_python_info})


def report_delete_force(request):
    """
    深度删除
    :param request:
    :return:
    """
    return render_result(request, "page_main_controller/administrator/delete_force.html", {})


def delete_force(request):
    """
    删除对应的数据
    :param request:
    :return:
    """
    operation_object = None
    delete_force_type = request.POST.get('delete_force_type', None)
    if delete_force_type:
        operation_object = delete_force_type
        if delete_force_type == 'student_info':
            StudentInfo.objects.filter().delete()
            title_msg = sys_msg + '-删除成功'
            message = '系统提示:删除成功!  请查询对应数据，检测是否完全删除！'
            result['status'] = True
            result['message'] = delete_force_type + ': 删除成功！'
            result['data'] = json.dumps({}, ensure_ascii=False)
            # return render_result(request, "page_main_controller/message.html",
            #                      {'title_msg': title_msg, 'message': message})
        elif delete_force_type == 'student_user_info':
            if StudentInfo.objects.count() > 0:
                title_msg = sys_msg + '-错误信息展示页面'
                message = '系统提示:删除失败！学员填报信息尚未完全清除，请先删除所有学员填报信息'
                result['status'] = False
                result['message'] = message
                result['data'] = json.dumps({}, ensure_ascii=False)
                # return render_result(request, "page_main_controller/message.html",
                #                      {'title_msg': title_msg, 'message': message})
            else:
                UserInfo.objects.filter(register_user_info__role__role_name='student').delete()
                title_msg = sys_msg + '-删除成功'
                message = '系统提示:删除成功!  请查询对应数据，检测是否完全删除！'
                result['status'] = True
                result['message'] = delete_force_type + ': 删除成功！'
                result['data'] = json.dumps({}, ensure_ascii=False)
                # return render_result(request, "page_main_controller/message.html",
                #                      {'title_msg': title_msg, 'message': message})
        elif delete_force_type == 'student_register_info':
            if UserInfo.objects.filter(register_user_info__role__role_name='student').count() > 0:
                title_msg = sys_msg + '-错误信息展示页面'
                message = '系统提示:删除失败！学员基础信息尚未完全清除，请先删除所有学员基础信息'
                result['status'] = False
                result['message'] = message
                result['data'] = json.dumps({}, ensure_ascii=False)
                # return render_result(request, "page_main_controller/message.html",
                #                      {'title_msg': title_msg, 'message': message})
            else:
                RegisterUserInfo.objects.filter(role__role_name='student').delete()
                title_msg = sys_msg + '-删除成功'
                message = '系统提示:删除成功!  请查询对应数据，检测是否完全删除！'
                result['status'] = True
                result['message'] = delete_force_type + ': 删除成功！'
                result['data'] = json.dumps({}, ensure_ascii=False)
                # return render_result(request, "page_main_controller/message.html",
                #                      {'title_msg': title_msg, 'message': message})
        elif delete_force_type == 'student_img_file':
            picture_root = MEDIA_ROOT + '/images'
            if os.path.exists(picture_root):
                del_file(path=picture_root)
                FileManage.objects.filter().delete()
                Picture.objects.filter().delete()
                title_msg = sys_msg + '-删除成功'
                message = '系统提示:删除成功!  请查询对应数据，检测是否完全删除！'
                result['status'] = True
                result['message'] = delete_force_type + ': 删除成功！'
                result['data'] = json.dumps({}, ensure_ascii=False)
                # return render_result(request, "page_main_controller/message.html",
                #                      {'title_msg': title_msg, 'message': message})
            else:
                title_msg = sys_msg + '-错误信息展示页面'
                message = '系统提示:删除失败！图片存储目录不存在'
                result['status'] = False
                result['message'] = message
                result['data'] = json.dumps({}, ensure_ascii=False)
                # return render_result(request, "page_main_controller/message.html",
                #                      {'title_msg': title_msg, 'message': message})
        elif delete_force_type == 'action_info':
            InterviewAudit.objects.filter().delete()
            title_msg = sys_msg + '-删除成功'
            result['status'] = True
            result['message'] = delete_force_type + ': 删除成功！'
            result['data'] = json.dumps({}, ensure_ascii=False)
            message = '系统提示:删除成功!  请查询对应数据，检测是否完全删除！'
            # return render_result(request, "page_main_controller/message.html",
            #                      {'title_msg': title_msg, 'message': message})
        elif delete_force_type == 'system_message':
            SystemMessage.objects.filter().delete()
            title_msg = sys_msg + '-删除成功'
            message = '系统提示:删除成功!  请查询对应数据，检测是否完全删除！'
            result['status'] = True
            result['message'] = delete_force_type + ': 删除成功！'
            result['data'] = json.dumps({}, ensure_ascii=False)
            # return render_result(request, "page_main_controller/message.html",
            #                      {'title_msg': title_msg, 'message': message})
        elif delete_force_type == 'force_all':
            # picture_root = MEDIA_ROOT + '/images'
            # file_root = MEDIA_ROOT + "/files/"
            if os.path.exists(MEDIA_ROOT):
                StudentInfo.objects.filter().delete()
                UserInfo.objects.filter(register_user_info__role__role_name='student').delete()
                RegisterUserInfo.objects.filter(role__role_name='student').delete()
                InterviewAudit.objects.filter().delete()
                SystemMessage.objects.filter().delete()
                del_file(path=MEDIA_ROOT)
                FileManage.objects.filter().delete()
                Picture.objects.filter().delete()
                # title_msg = sys_msg + '-删除成功'
                result['status'] = True
                result['message'] = delete_force_type + ': 删除成功！'
                result['data'] = json.dumps({}, ensure_ascii=False)
                # return render_result(request, "page_main_controller/message.html",
                message = '系统提示:删除成功!  请查询对应数据，检测是否完全删除！'
                #                      {'title_msg': title_msg, 'message': message})
            else:
                title_msg = sys_msg + '-错误信息展示页面'
                message = '系统提示:删除失败！图片存储目录不存在'
                result['status'] = False
                result['message'] = message
                result['data'] = json.dumps({}, ensure_ascii=False)
                # return render_result(request, "page_main_controller/message.html",
                #                      {'title_msg': title_msg, 'message': message})
    else:
        title_msg = sys_msg + '-错误信息展示页面'
        message = '系统提示:删除失败！您尚未选择删除项目'
        result['status'] = False
        result['message'] = message
        result['data'] = json.dumps({}, ensure_ascii=False)
        # return render_result(request, "page_main_controller/message.html",
        #                      {'title_msg': title_msg, 'message': message})
    result["level"] = log_level_cancel
    if operation_object:
        save_operation_log(request, inspect.stack()[0][3], operation_object, result)
    else:
        save_operation_log(request, inspect.stack()[0][3], "", result)
    return JsonResponse(result, safe=False)


def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            # 如果文件夹为空，直接删除
            if len(os.listdir(path_file)) > 0:
                del_file(path_file)
            else:
                os.rmdir(path_file)


def admin_term_picture_data(request):
    """
    批量下载证件图片
    :param request:
    :return:
    """
    title_msg = '批量下载'
    school_term_name = request.GET.get('school_term_name', None)
    school_terms = SchoolTerm.objects.filter(school_term_name=school_term_name)
    if school_terms.count() == 1:
        school_term = school_terms[0]

        # students = StudentInfo.objects.filter(school_term=school_term).order_by('-id')
        # username = request.session.get('username', None)
        # if students.count() > 0:
        #     for student in students:
        #         declaration_of_occupation = student.declaration_of_occupation
        #         if student.diploma_certificate_photos:
        #             # 备份到对应的
        #             term_worker_picture(school_term.school_term_name,
        #                                 declaration_of_occupation,
        #                                 username,
        #                                 "毕业证件照",
        #                                 student.diploma_certificate_photos.picture_path)
        #         if student.certificate_photos:
        #             # 备份到对应的
        #             term_worker_picture(school_term.school_term_name,
        #                                 declaration_of_occupation,
        #                                 username,
        #                                 "资格证件照",
        #                                 student.diploma_certificate_photos.picture_path)
        #         if student.user_info.two_inch_photo:
        #             term_worker_picture(student.school_term.school_term_name,
        #                                 declaration_of_occupation,
        #                                 username,
        #                                 "二寸证件照",
        #                                 student.user_info.two_inch_photo.picture_path)
        if school_term.students_confirm == 0:
            message = '无数据，请先刷新查看学期的统计数据，若学员确认数量为0，请不要下载证件！'
            return render_result(request, "page_main_controller/report_download_page.html",
                                 {'title_msg': title_msg, 'not_exist': True, 'message': message})
        else:
            term_name_time = term_make_archive(school_term_name)
            if term_name_time:
                file_manage = FileManage()
                file_manage.file_name = school_term_name
                file_manage.file_path = term_name_time
                file_manage.save()
                if file_manage.file_uuid:
                    message = "文件获取成功，请点击下载查看"
                    return render_result(request, "page_main_controller/report_download_page.html",
                                         {'title_msg': title_msg, 'not_exist': False, 'message': message,
                                          'file_uuid': file_manage.file_uuid, 'chemical': True,
                                          'file_message_one': school_term_name})
                else:
                    message = '无数据，或者获取文件出现异常，请稍后重试或联系管理员'
                    return render_result(request, "page_main_controller/report_download_page.html",
                                         {'title_msg': title_msg, 'not_exist': True, 'message': message})


def del_register_info(request):
    """
    删除此账户下所有信息
    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            record_id = request.POST.get('record_id', None)
            if record_id:
                register_user_infos = RegisterUserInfo.objects.filter(id=record_id).order_by("-id")
                if register_user_infos.count() > 0:
                    register_user_info = register_user_infos[0]
                    if register_user_info.role.role_name == "student":
                        operation_object = register_user_info
                        user_infos = UserInfo.objects.filter(register_user_info=register_user_info).order_by("-id")
                        if user_infos.count() > 0:
                            user_info = user_infos[0]
                            students = StudentInfo.objects.filter(user_info=user_info)
                            senders = SystemMessage.objects.filter(sender=user_info)
                            receivers = SystemMessage.objects.filter(receiver=user_info)

                            if students.count() > 0:
                                students.delete()
                            if senders.count() > 0:
                                senders.delete()
                            if receivers.count() > 0:
                                receivers.delete()

                            user_infos.delete()
                            register_user_infos.delete()
                            result['status'] = True
                            result['message'] = '删除成功！'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                        else:
                            register_user_infos.delete()
                            result['status'] = True
                            result['message'] = '删除成功！'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                    elif register_user_info.role.role_name == "teacher":
                        user_infos = UserInfo.objects.filter(register_user_info=register_user_info).order_by("-id")
                        if user_infos.count() > 0:
                            user_info = user_infos[0]
                            teachers = TeacherInfo.objects.filter(user_info=user_info)
                            if teachers.count() > 0:
                                if StudentInfo.objects.filter(teacher_info=teachers[0]).count() > 0:
                                    result['status'] = False
                                    result['message'] = '单位负责人名下尚有报考学生，请先删除学生信息!'
                                    result['data'] = ''
                                else:
                                    teachers.delete()
                                    user_infos.delete()
                                    senders = SystemMessage.objects.filter(sender=user_info)
                                    receivers = SystemMessage.objects.filter(receiver=user_info)
                                    if senders.count() > 0:
                                        senders.delete()
                                    if receivers.count() > 0:
                                        receivers.delete()
                                    register_user_infos.delete()
                                    result['status'] = True
                                    result['message'] = '删除成功！'
                                    result['data'] = json.dumps({}, ensure_ascii=False)
                        else:
                            register_user_infos.delete()
                            result['status'] = True
                            result['message'] = '删除成功！'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                    elif register_user_info.role.role_name == "administrator":
                        result['status'] = False
                        result['message'] = '请不要删除管理员信息!'
                        result['data'] = ''
                    else:
                        result['status'] = False
                        result['message'] = '未获取角色信息，无法删除!'
                        result['data'] = ''
                else:
                    result['status'] = False
                    result['message'] = '所要删除的记录不存在!'
                    result['data'] = ''
            else:
                result['status'] = False
                result['message'] = '参数获取失败!'
                result['data'] = ''
        else:
            result['status'] = False
            result['message'] = '所要删除的记录不存在!'
            result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = "系统异常：" + str(e)
        result['data'] = ''
    result["level"] = log_level_cancel
    if operation_object:
        save_operation_log(request, inspect.stack()[0][3], operation_object.__str__(True), result)
    else:
        save_operation_log(request, inspect.stack()[0][3], "", result)
    return JsonResponse(result, safe=False)
