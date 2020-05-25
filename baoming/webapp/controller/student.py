import inspect
import json

from django.core.paginator import Paginator
from django.http import JsonResponse

from baoming.settings import MEDIA_URL
from webapp.controller.common import *
from webapp.controller.renderUtil import render_result
from webapp.forms.StudentForm import *
from webapp.forms.StudentUpdateForm import *
from webapp.models import *
from webapp.utils.form_to_obj import *
from webapp.utils.save_operation_log import save_operation_log
from webapp.utils.shutilwhichUtil import term_worker_picture

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def add_student_info(request):
    """����ѧ������Ϣ.

    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            object_form = StudentForm(request.POST)
            print(object_form)
            if object_form.is_valid():
                print(object_form.cleaned_data)

                form_object_student_info = form_to_obj(object_form.cleaned_data, StudentInfo())
                # # 关联教育程度
                # education_degree = object_form.cleaned_data.get('education_degree_form', None)
                # if education_degree:
                #     education_degree_obj = EducationDegree.objects.get(id=education_degree)
                #     form_object_student_info.education_degree = education_degree_obj
                # # 关联教育程度
                # 关联职业资格证书照片
                certificate_photos = object_form.cleaned_data.get(
                    'certificate_photos_form', None)
                if certificate_photos:
                    certificate_photos_obj = Picture.objects.get(
                        id=certificate_photos)
                    form_object_student_info.certificate_photos = certificate_photos_obj
                # 关联职业资格证书照片

                # 关联院校毕业证书照片
                diploma_certificate_photos = object_form.cleaned_data.get(
                    'diploma_certificate_photos_form', None)
                if diploma_certificate_photos:
                    diploma_certificate_photos_obj = Picture.objects.get(
                        id=diploma_certificate_photos)
                    form_object_student_info.diploma_certificate_photos = diploma_certificate_photos_obj
                # 关联院校毕业证书照片
                # 关联登陆用户基础信息
                username = request.session.get('username', None)  # 用户名
                register_user_info = RegisterUserInfo.objects.get(
                    username=username)
                user_infos = UserInfo.objects.filter(
                    register_user_info=register_user_info)
                image_url = ''
                if len(user_infos) > 0:
                    user_info_old = user_infos[len(user_infos) - 1]
                    if user_info_old.two_inch_photo:
                        if user_info_old.two_inch_photo.picture_path:
                            image_url = MEDIA_URL + str(
                                user_info_old.two_inch_photo.picture_path)
                    else:
                        image_url = ''
                        # 学生附属信息
                    form_object_student_info.user_info = user_info_old
                else:
                    # 用户基础信息
                    user_info_new = UserInfo()
                    # 关联注册员信息
                    user_info_new.register_user_info = register_user_info

                    user_info_new.save()
                    form_object_student_info.user_info = user_info_new
                declaration_of_occupation = form_object_student_info.declaration_of_occupation

                if declaration_of_occupation in chemical_industry:
                    form_object_student_info.chemical_worker = '1'
                else:
                    form_object_student_info.chemical_worker = '2'

                school_term = SchoolTerm.objects.last()
                form_object_student_info.school_term = school_term
                declaration_of_occupation = form_object_student_info.declaration_of_occupation
                identification_level = form_object_student_info.identification_level
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
                    declaration_of_occupation_first = str(
                        declaration_of_occupation)[0:1]
                identification_level_dict = {
                    '5': '(初)',
                    '4': '(中)',
                    '3': '(高)'
                }
                identification_level_str = identification_level_dict[str(
                    identification_level)]
                explain = declaration_of_occupation_first + identification_level_str
                form_object_student_info.explain = explain

                print("primary_level::" +
                      form_object_student_info.primary_level)

                # if form_object_student_info.identification_level == "3":
                #     # 如果申报等级是高级那么工作年限将不设置
                #     form_object_student_info.career_life = 0
                #     form_object_student_info.original_certificate_worker_year = 0
                #     form_object_student_info.apprentice_year = 0
                #     form_object_student_info.apprentice_month = 0
                # else:
                #     pass

                form_object_student_info.save()
                if diploma_certificate_photos:
                    # 备份到对应的
                    term_worker_picture(
                        school_term.school_term_name,
                        form_object_student_info.declaration_of_occupation,
                        username, "毕业证件照", form_object_student_info.
                        diploma_certificate_photos.picture_path)
                if certificate_photos:
                    # 备份到对应的
                    term_worker_picture(
                        school_term.school_term_name,
                        form_object_student_info.declaration_of_occupation,
                        username, "资格证件照", form_object_student_info.
                        certificate_photos.picture_path)

                result['message'] = "学员信息添加成功！"
                result["level"] = log_level_add
                save_operation_log(request,
                                   inspect.stack()[0][3],
                                   form_object_student_info.__str__(True),
                                   result)
                student_id = form_object_student_info.id
                # user_info = UserInfo.objects.get(register_user_info=register_user_info.id)
                # working_history_list = user_info.user_Info_working_history.all()
                # print("user_Info_working_history::" + str(working_history_list))
                title_msg = sys_msg + '-学生信息'
                student_infos = StudentInfo.objects.filter(id=student_id)

                if len(student_infos) > 0:
                    student_info = student_infos[0]
                    user_info = student_info.user_info
                    if not user_info.real_name:
                        user_info.real_name = ""
                    if not user_info.id_number:
                        user_info.id_number = ""
                    if not user_info.id_card_address:
                        user_info.id_card_address = ""
                    if not user_info.address:
                        user_info.address = ""
                    if not user_info.work_unit:
                        user_info.work_unit = ""
                    if not user_info.fixed_telephone:
                        user_info.fixed_telephone = ""
                    if not user_info.contact_number:
                        user_info.contact_number = ""
                    if not user_info.postal_code:
                        user_info.postal_code = ""
                    if not user_info.main_occupation:
                        user_info.main_occupation = ""
                    teacher_infos = TeacherInfo.objects.all()
                    return render_result(
                        request,
                        "page_main_controller/user/report_user_info_update.html",
                        {
                            'title_msg': title_msg,
                            'user_info': student_info.user_info,
                            'student_id': student_id,
                            'image_url': image_url,
                            'teacher_infos': teacher_infos
                        })
            else:
                print(type(object_form.errors),
                      object_form.errors)  # errors类型是ErrorDict，里面是ul，li标签
                title_msg = sys_msg + '-错误信息展示页面'
                message = '添加失败：输入项不全，请返回重新确认并填写，或联系管理员'
                return render_result(request,
                                     "page_main_controller/message.html", {
                                         'title_msg': title_msg,
                                         'message': message
                                     })
                # return render_result(request, "account/form1.html", {"error": f.errors})
        else:
            title_msg = sys_msg + '-错误信息展示页面'
            message = '系统提示：请求方式有误，请重新提交或者联系管理员'
            return render_result(request, "page_main_controller/message.html",
                                 {
                                     'title_msg': title_msg,
                                     'message': message
                                 })
    except Exception as e:
        raise e
        # print(str(e))
        # title_msg = sys_msg + '-错误信息展示页面'
        # message = '系统提示，请重新提交或者联系管理员，错误提示：' + str(e)
        # return render_result(request, "page_main_controller/message.html",
        #               {'title_msg': title_msg, 'message': message})


def report_student_info_list(request):
    """��ѯѧ��������Ϣ�б�.

    :param request:
    :return:
    """
    # 关联登陆用户基础信息
    title_msg = '学生填报信息列表'
    username = request.session.get('username', None)  # 用户名
    register_user_info = RegisterUserInfo.objects.get(username=username)
    students = StudentInfo.objects.filter(
        user_info__register_user_info=register_user_info).order_by('-id')
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    if SchoolTerm.objects.count() > 0:
        school_term = SchoolTerm.objects.last()
        return render_result(
            request,
            "page_main_controller/student/report_student_info_list.html", {
                'title_msg': title_msg,
                "contacts": contacts,
                'school_term': school_term,
                'need_list': False
            })
    else:
        return render_result(
            request,
            "page_main_controller/student/report_student_info_list.html", {
                'title_msg': title_msg,
                'need_list': False
            })


def student_info_detail(request):
    """
    查看本条记录的学生信息详情
    :return:
    """
    if request.method == 'GET':
        student_id = request.GET.get('studentId', None)
        if int(student_id) > 0:
            student_infos = StudentInfo.objects.filter(id=student_id)
            if len(student_infos) == 0:
                title_msg = sys_msg + '-填报详情'
                return render_result(
                    request,
                    "page_main_controller/student/report_student_user_info_detail.html",
                    {
                        'title_msg': title_msg,
                        'not_exist': True
                    })
            else:
                student_info = student_infos[0]
                title_msg = sys_msg + '-填报详情'
                image_url = ''
                if student_info.user_info.two_inch_photo:
                    image_url = MEDIA_URL + str(
                        student_info.user_info.two_inch_photo.picture_path)
                # 全部汇总在大填报表格里面
                certificate_photos_url = ''
                if student_info.certificate_photos:
                    certificate_photos_url = MEDIA_URL + str(
                        student_info.certificate_photos.picture_path)
                condition_selected_str = ''
                if student_info.condition_selected:
                    condition_selected_str = student_info.condition_selected.condition_name
                    # condition_query_set = ReportCondition.objects.\
                    #     filter(condition_id=student_info.condition_selected).\
                    #         values('condition_id',
                    #                'condition_name',
                    #                'condition_level',
                    #                'record_status')
                    # print(condition_query_set)
                    # if len(condition_query_set) > 0:
                    #     condition_selected_str = condition_query_set[0]['condition_name']
                print(condition_selected_str)
                diploma_certificate_photos_url = ''
                if student_info.diploma_certificate_photos:
                    diploma_certificate_photos_url = MEDIA_URL + str(
                        student_info.diploma_certificate_photos.picture_path)
                return render_result(
                    request,
                    "page_main_controller/student/report_student_user_info_detail.html",
                    {
                        'title_msg': title_msg,
                        'student_info': student_info,
                        'image_url': image_url,
                        'certificate_photos_url': certificate_photos_url,
                        'diploma_certificate_photos_url':
                        diploma_certificate_photos_url,
                        'not_exist': False,
                        'condition_selected': condition_selected_str
                    })


def student_info_update(request):
    """
    修改学生的填报信息
    :return:
    """
    try:
        if request.method == 'POST':
            object_form = StudentUpdateForm(request.POST)
            # print(object_form.__str__())
            if object_form.is_valid():
                student_info_id = object_form.cleaned_data.get('obj_id', None)
                if student_info_id:
                    student_infos = StudentInfo.objects.filter(id=student_info_id).order_by('-id')
                    if len(student_infos) > 0:
                        student_info = student_infos[0]

                        student_id = student_info.id
                        # 用户基础信息
                        form_object_student_info = form_to_obj(
                            object_form.cleaned_data, student_info)
                        # 关联申报的级别信息
                        identification_level = object_form.cleaned_data.get(
                            'update_identification_level', None)
                        if identification_level:
                            form_object_student_info.identification_level = identification_level
                        # 关联职业资格证书照片
                        certificate_photos = object_form.cleaned_data.get(
                            'certificate_photos_form', None)
                        if certificate_photos:
                            certificate_photos_obj = Picture.objects.get(
                                id=certificate_photos)
                            form_object_student_info.certificate_photos = certificate_photos_obj
                        # 关联职业资格证书照片
                        # 关联院校毕业证书照片

                        diploma_certificate_photos = object_form.cleaned_data.get(
                            'diploma_certificate_photos_form', None)
                        if diploma_certificate_photos:
                            diploma_certificate_photos_obj = Picture.objects.get(
                                id=diploma_certificate_photos)
                            form_object_student_info.diploma_certificate_photos = diploma_certificate_photos_obj
                        # 关联院校毕业证书照片

                        # 关联登陆用户基础信息
                        username = request.session.get('username', None)  # 用户名
                        register_user_info = RegisterUserInfo.objects.get(
                            username=username)
                        form_object_student_info.user_operator = register_user_info
                        declaration_of_occupation = form_object_student_info.declaration_of_occupation
                        identification_level = form_object_student_info.identification_level
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
                            declaration_of_occupation_first = str(
                                declaration_of_occupation)[0:1]
                        identification_level_dict = {
                            '5': '(初)',
                            '4': '(中)',
                            '3': '(高)'
                        }
                        identification_level_str = identification_level_dict[
                            str(identification_level)]
                        explain = declaration_of_occupation_first + identification_level_str
                        form_object_student_info.explain = explain

                        print("primary_level::" +
                              form_object_student_info.primary_level)

                        # if form_object_student_info.identification_level == "3":
                        #     # 如果申报等级是高级那么工作年限将不设置
                        #     form_object_student_info.career_life = 0
                        #     form_object_student_info.original_certificate_worker_year = 0
                        #     form_object_student_info.apprentice_year = 0
                        #     form_object_student_info.apprentice_month = 0
                        # else:
                        #     pass

                        form_object_student_info.save()
                        student_username = form_object_student_info.user_info.register_user_info.username
                        if diploma_certificate_photos:
                            # 备份到对应的
                            term_worker_picture(
                                form_object_student_info.school_term.
                                school_term_name, form_object_student_info.
                                declaration_of_occupation, student_username,
                                "毕业证件照", form_object_student_info.
                                diploma_certificate_photos.picture_path)
                        if certificate_photos:
                            # 备份到对应的
                            term_worker_picture(
                                form_object_student_info.school_term.
                                school_term_name, form_object_student_info.
                                declaration_of_occupation, student_username,
                                "资格证件照", form_object_student_info.
                                certificate_photos.picture_path)
                        result['message'] = "学员信息添加成功！"
                        result["level"] = log_level_add
                        save_operation_log(
                            request,
                            inspect.stack()[0][3],
                            form_object_student_info.__str__(True), result)
                        # user_info = UserInfo.objects.get(register_user_info=register_user_info.id)
                        # working_history_list = user_info.user_Info_working_history.all()
                        # print("user_Info_working_history::" + str(working_history_list))
                        title_msg = sys_msg + '-工作用户信息'
                        teacher_infos = TeacherInfo.objects.all()
                        teacher_info_id = form_object_student_info.teacher_info
                        if form_object_student_info.user_info:
                            user_info = form_object_student_info.user_info
                            if not user_info.real_name:
                                user_info.real_name = ""
                            if not user_info.id_number:
                                user_info.id_number = ""
                            if not user_info.id_card_address:
                                user_info.id_card_address = ""
                            if not user_info.address:
                                user_info.address = ""
                            if not user_info.work_unit:
                                user_info.work_unit = ""
                            if not user_info.fixed_telephone:
                                user_info.fixed_telephone = ""
                            if not user_info.contact_number:
                                user_info.contact_number = ""
                            if not user_info.postal_code:
                                user_info.postal_code = ""
                            if not user_info.main_occupation:
                                user_info.main_occupation = ""
                            if user_info.two_inch_photo:
                                if user_info.two_inch_photo.picture_path:
                                    image_url = MEDIA_URL + str(
                                        user_info.two_inch_photo.picture_path)
                                    return render_result(
                                        request,
                                        "page_main_controller/user/report_user_info_update.html",
                                        {
                                            'title_msg': title_msg,
                                            'user_info':
                                            student_info.user_info,
                                            'student_id': student_id,
                                            'image_url': image_url,
                                            'teacher_infos': teacher_infos,
                                            'teacher_info_id': teacher_info_id
                                        })
                            else:
                                return render_result(
                                    request,
                                    "page_main_controller/user/report_user_info_update.html",
                                    {
                                        'title_msg': title_msg,
                                        'user_info': user_info,
                                        'student_id': student_id,
                                        'image_url': '',
                                        'teacher_infos': teacher_infos,
                                        'teacher_info_id': teacher_info_id
                                    })
                else:
                    print(type(object_form.errors),
                          object_form.errors)  # errors类型是ErrorDict，里面是ul，li标签
                    title_msg = sys_msg + '-错误信息展示页面'
                    message = '更新失败：系统没有此信息记录，请重试或联系管理员！'
                    return render_result(request,
                                         "page_main_controller/message.html", {
                                             'title_msg': title_msg,
                                             'message': message
                                         })
            else:
                print(type(object_form.errors),
                      object_form.errors)  # errors类型是ErrorDict，里面是ul，li标签
                title_msg = sys_msg + '-错误信息展示页面'
                message = '更新失败：输入项不全，请返回重新确认并填写'
                return render_result(request,
                                     "page_main_controller/message.html", {
                                         'title_msg': title_msg,
                                         'message': message
                                     })
        else:
            title_msg = sys_msg + '-错误信息展示页面'
            message = '系统提示：请求方式有误，请重新提交或者联系管理员'
            return render_result(request, "page_main_controller/message.html",
                                 {
                                     'title_msg': title_msg,
                                     'message': message
                                 })

    except Exception as e:
        print(str(e))
        raise e


def to_student_info_update(request):
    """
    去修改学生的填报信息
    :return:
    """
    title_msg = sys_msg + '-填报信息修改'
    message = ''
    if request.method == 'GET':
        student_id = request.GET.get('studentId', None)
        if int(student_id) > 0:
            student_infos = StudentInfo.objects.filter(id=student_id)
            if len(student_infos) == 0:
                title_msg = sys_msg + '-填报信息修改'
                return render_result(
                    request,
                    "page_main_controller/student/report_student_user_info_detail.html",
                    {
                        'title_msg': title_msg,
                        'not_exist': True
                    })
            else:
                student_info = student_infos[0]
                condition_selected_str = ''
                if student_info.condition_selected:
                    condition_query_set = ReportCondition.objects.\
                        filter(condition_id=int(student_info.condition_selected)).\
                            values('condition_id',
                                   'condition_name',
                                   'condition_level',
                                   'record_status')
                    print(condition_query_set)
                    if len(condition_query_set) > 0:
                        condition_selected_str = condition_query_set[0]['condition_name']
                print(condition_selected_str)
                
                # 判断当前操作填报学期是否已经完结

                # 学生的信息处于原始的信息保存状态，可以进行修改
                editable = False
                if student_info.school_term.status == "2":
                    title_msg = sys_msg + '-错误信息展示页面'
                    message = '系统提示：当前: ' + student_info.school_term.school_term_name + '  学期报名已完结,或由管理员关停！您您已无法修改'
                    return render_result(request,
                                         "page_main_controller/message.html", {
                                             'title_msg': title_msg,
                                             'message': message
                                         })
                else:
                    role_name = request.session.get('role_name', None)
                    if role_name == 'administrator':
                        if student_info.confirm_status == "1":
                            title_msg = sys_msg + '-错误信息展示页面'
                            message = '系统提示：您的信息已由学校管理员最终确认，您暂时无法修改，如欲修改请提交注销申请！'
                        else:
                            editable = True
                    elif role_name == 'teacher':
                        if student_info.review_status == "1":
                            title_msg = sys_msg + '-错误信息展示页面'
                            message = '系统提示：您的信息已由负责人提交学校管理员确认，您暂时无法修改，如欲修改请提交注销申请！'
                        elif student_info.confirm_status == "1":
                            title_msg = sys_msg + '-错误信息展示页面'
                            message = '系统提示：您的信息已由学校管理员最终确认，您暂时无法修改，如欲修改请提交注销申请！'
                        else:
                            editable = True
                    elif role_name == 'student':
                        # 修改之前进行状态的判断
                        if student_info.submit_status == "1":
                            title_msg = sys_msg + '-错误信息展示页面'
                            message = '系统提示：您的信息已提交管理员审核，您暂时无法修改，如欲修改请提交注销申请！'
                        elif student_info.review_status == "1":
                            title_msg = sys_msg + '-错误信息展示页面'
                            message = '系统提示：您的信息已由负责人提交学校管理员确认，您暂时无法修改，如欲修改请提交注销申请！'
                        elif student_info.confirm_status == "1":
                            title_msg = sys_msg + '-错误信息展示页面'
                            message = '系统提示：您的信息已由学校管理员最终确认，您暂时无法修改，如欲修改请提交注销申请！'

                        else:
                            editable = True
                    if editable:
                        certificate_photos_url = ''
                        if student_info.certificate_photos:
                            certificate_photos_url = MEDIA_URL + str(
                                student_info.certificate_photos.picture_path)

                        diploma_certificate_photos_url = ''
                        if student_info.diploma_certificate_photos:
                            diploma_certificate_photos_url = MEDIA_URL + \
                                                             str(student_info.diploma_certificate_photos.picture_path)
                        return render_result(
                            request,
                            "page_main_controller/student/report_student_info_update.html",
                            {
                                'title_msg': title_msg,
                                'student_info': student_info,
                                'diploma_certificate_photos_url':
                                diploma_certificate_photos_url,
                                'certificate_photos_url':
                                certificate_photos_url,
                                'not_report': False,
                                'condition_selected': condition_selected_str
                            })
                    else:
                        # 状态修改修改权限也修改了
                        return render_result(
                            request, "page_main_controller/message.html", {
                                'title_msg': title_msg,
                                'message': message
                            })
        else:
            message = '查询提示：参数异常，请重试或联系管理员。'
            return render_result(request, "page_main_controller/message.html",
                                 {
                                     'title_msg': title_msg,
                                     'message': message
                                 })
    else:
        message = '系统提示：请求方式有误，请重新提交或者联系管理员'
        return render_result(request, "page_main_controller/message.html", {
            'title_msg': title_msg,
            'message': message
        })


def report_student_del(request):
    """����id ɾ��.

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
                    if int(submit_status) == 1:
                        # 如果是已提交状态，将无法删除
                        result['status'] = False
                        result['message'] = '所要删除的记录已经提交，您无法删除，您可以申请注销。'
                        result['data'] = ''
                    else:
                        # 如果是未提交状态，可以删除
                        operation_object = student_info
                        student_info.delete()
                        student_infos_check = StudentInfo.objects.filter(
                            id=student_del_id)
                        if len(student_infos_check) == 0:
                            result['status'] = True
                            result['message'] = '删除记录成功'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                        else:
                            result['status'] = False
                            result['message'] = '未能成功删除或者有多条记录，请查询确认后继续删除!'
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
    save_operation_log(request,
                       inspect.stack()[0][3], operation_object.__str__(True),
                       result)
    return JsonResponse(result, safe=False)


def report_student_submit(request):
    """ѧԱ�ύ��Ϣ��ť.

    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            student_id = request.POST.get('record_id', None)
            if int(student_id) > 0:
                student_infos = StudentInfo.objects.filter(
                    id=student_id).order_by('-id')
                if len(student_infos) == 1:
                    student_info = student_infos[0]
                    submit_status = student_info.submit_status
                    if student_info.user_info:
                        # 学员的基础信息是否完备
                        if student_info.teacher_info:
                            # 学员的负责人信息是否完备
                            if submit_status == "2":
                                student_info.submit_status = 1
                                student_info.save()
                                operation_object = student_info.id
                                result['status'] = True
                                result['message'] = '提交记录成功'
                                result['data'] = json.dumps({},
                                                            ensure_ascii=False)
                            else:
                                result['status'] = False
                                result['message'] = '已提交，请不要重复提交!'
                                result['data'] = ''
                        else:
                            result['status'] = False
                            result['message'] = '所要提交的记录负责人信息未提交，请修改!'
                            result['data'] = ''
                    else:
                        result['status'] = False
                        result['message'] = '所要提交的记录个人基础信息未提交，请修改添加!'
                        result['data'] = ''
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
    save_operation_log(request,
                       inspect.stack()[0][3], "uid:" + str(operation_object),
                       result)
    return JsonResponse(result, safe=False)


def report_student_cancel(request):
    """ȡ���ύ��¼.

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
                    review_status = student_info.review_status
                    confirm_status = student_info.confirm_status
                    if confirm_status == "2":
                        if review_status == "2":
                            if submit_status == "1":
                                # cancel_status = student_info.cancel_status
                                student_info.submit_status = "2"
                                operation_object = student_info.id
                                student_info.save()
                                result['status'] = True
                                result['message'] = '申请注销提交操作成功'
                                result['data'] = json.dumps({},
                                                            ensure_ascii=False)

                                # if submit_status == "2":
                                #     student_info.cancel_status = "1"
                                #     operation_object = student_info.id
                                #     student_info.save()
                                #     result['status'] = True
                                #     result['message'] = '申请注销提交操作成功'
                                #     result['data'] = json.dumps({}, ensure_ascii=False)
                                # else:
                                #     result['status'] = False
                                #     result['message'] = '已在申请中，请勿重复申请!'
                                #     result['data'] = ''
                            else:
                                result['status'] = False
                                result[
                                    'message'] = '所要申请的注销记录信息尚未提交或已经取消，请不要重复操作!'
                                result['data'] = ''
                        else:
                            result['status'] = False
                            result[
                                'message'] = '所要申请的记录已经由负责人审核通过，请联系负责人取消审核再修改!'
                            result['data'] = ''
                    else:
                        result['status'] = False
                        result[
                            'message'] = '您的报名信息已经通过最终审核，请联系负责人取消审核之后才能修改信息!'
                        result['data'] = ''
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
    save_operation_log(request,
                       inspect.stack()[0][3], "uid:" + str(operation_object),
                       result)
    return JsonResponse(result, safe=False)


def report_student_cancel_return(request):
    """��������ע���ύ��¼.

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
                    if submit_status == "1":
                        cancel_status = student_info.cancel_status
                        if cancel_status == "1":
                            student_info.cancel_status = "2"
                            operation_object = student_info.id
                            student_info.save()
                            result['status'] = True
                            result['message'] = '撤销申请注销提交操作成功'
                            result['data'] = json.dumps({}, ensure_ascii=False)
                        else:
                            result['status'] = False
                            result['message'] = '本提交记录，没有注销申请，请您先注销!'
                            result['data'] = ''
                    else:
                        result['status'] = False
                        result['message'] = '已经通过负责人同意注销记录，请继续修改记录然后提交!'
                        result['data'] = ''
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
    save_operation_log(request,
                       inspect.stack()[0][3], "uid:" + str(operation_object),
                       result)
    return JsonResponse(result, safe=False)


def report_student_payment(request):
    """ѧԱ�ɷ�.

    :param request:
    :return:
    """
    operation_object = None
    try:
        if request.method == 'POST':
            student_id = request.POST.get('record_id', None)
            payment_amount = request.POST.get('payment_amount', None)
            unpaid_amount = request.POST.get('unpaid_amount', None)

            if int(student_id) > 0:
                student_infos = StudentInfo.objects.filter(id=student_id)
                if len(student_infos) == 1:
                    student_info = student_infos[0]
                    review_status = student_info.review_status
                    confirm_status = student_info.confirm_status
                    submit_status = student_info.submit_status
                    if submit_status == "1":
                        if review_status == "2":
                            if confirm_status == "2":
                                student_info.payment_amount = int(
                                    payment_amount)
                                student_info.unpaid_amount = int(unpaid_amount)
                                operation_object = student_info.id
                                student_info.save()
                                result['status'] = True
                                result['message'] = '缴费成功！已缴纳：' + str(
                                    payment_amount) + " 元。" + "未缴费：" + str(
                                        unpaid_amount) + " 元。"
                                result['data'] = json.dumps({},
                                                            ensure_ascii=False)
                            else:
                                result['status'] = False
                                result['message'] = '您已报名成功，不要继续操作，请等待考试信息通告!'
                                result['data'] = ''
                        else:
                            result['status'] = False
                            result['message'] = '您已通过负责人各项，请不要继续操作!'
                            result['data'] = ''
                    else:
                        result['status'] = False
                        result['message'] = '您尚未提交审核资料，暂时无法进行缴费!'
                        result['data'] = ''
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
    save_operation_log(request,
                       inspect.stack()[0][3], "uid:" + str(operation_object),
                       result)
    return JsonResponse(result, safe=False)
