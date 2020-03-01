import inspect
import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect

from baoming.settings import MEDIA_URL
from webapp.controller.common import *
from webapp.controller.renderUtil import render_result
from webapp.forms.UserInfoForm import *
from webapp.forms.UserInfoUpdateForm import *
from webapp.models import *
from webapp.utils.form_to_obj import *
from webapp.utils.password import *
from webapp.utils.save_operation_log import save_operation_log
from webapp.utils.shutilwhichUtil import term_worker_picture

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def add_user_info(request):
    """
    添加学生信息（化工类）
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            object_form = UserInfoForm(request.POST)
            if object_form.is_valid():
                username = request.session.get('username', None)  # 用户名
                register_user_info = RegisterUserInfo.objects.get(username=username)
                user_infos = UserInfo.objects.filter(register_user_info=register_user_info)

                if len(user_infos) > 0:
                    user_info = user_infos[len(user_infos) - 1]
                    form_object_user_info = form_to_obj(object_form.cleaned_data, user_info)
                else:
                    # 用户基础信息
                    form_object_user_info = form_to_obj(object_form.cleaned_data, UserInfo())
                    # 关联注册员信息
                    form_object_user_info.register_user_info = register_user_info
                    # 关联注册员信息

                # 关联操作员信息
                form_object_user_info.user_operator = register_user_info
                # 关联注册员信息
                # 关联教育程度
                education_degree = object_form.cleaned_data.get('education_degree_form', None)
                if education_degree:
                    education_degree_obj = EducationDegree.objects.get(id=education_degree)
                    form_object_user_info.education_degree = education_degree_obj
                # 关联教育程度

                # 关联民族信息
                nation_info = object_form.cleaned_data.get('nation_info_form', None)
                if nation_info:
                    nation_info_obj = NationInfo.objects.get(id=nation_info)
                    form_object_user_info.nation_info = nation_info_obj
                # 关联民族信息
                # 关联单位性质
                unit_nature = object_form.cleaned_data.get('unit_nature_form', None)
                if unit_nature:
                    unit_nature_obj = UnitNature.objects.get(id=unit_nature)
                    form_object_user_info.unit_nature = unit_nature_obj
                # 关联单位性质
                # 关联省
                hukou_province = object_form.cleaned_data.get('hukou_province_form', None)
                if hukou_province:
                    hukou_province_obj = ProvinceCityCountry.objects.get(id=hukou_province)
                    form_object_user_info.hukou_province = hukou_province_obj
                # 关联省
                # 关联市
                hukou_city = object_form.cleaned_data.get('hukou_city_form', None)
                if hukou_city:
                    hukou_city_obj = ProvinceCityCountry.objects.get(id=hukou_city)
                    form_object_user_info.hukou_city = hukou_city_obj
                # 关联市
                # 关联县
                hukou_county = object_form.cleaned_data.get('hukou_county_form', None)
                if hukou_county:
                    hukou_county_obj = ProvinceCityCountry.objects.get(id=hukou_county)
                    form_object_user_info.hukou_county = hukou_county_obj
                # 关联县
                # 关联二寸照片
                two_inch_photo = object_form.cleaned_data.get('two_inch_photo_form', None)
                if two_inch_photo:
                    two_inch_photo_obj = Picture.objects.get(id=two_inch_photo)
                    form_object_user_info.two_inch_photo = two_inch_photo_obj
                # 关联二寸照片
                # # 关联毕业证书照片
                # certificate_photos = object_form.cleaned_data.get('certificate_photos_form', None)
                # if certificate_photos:
                #     certificate_photos_obj = Picture.objects.get(id=certificate_photos)
                #     form_object_user_info.certificate_photos = certificate_photos_obj
                # # 关联毕业证书照片
                #
                # # 关联院校毕业证书照片
                # diploma_certificate_photos = object_form.cleaned_data.get('diploma_certificate_photos_form', None)
                # if diploma_certificate_photos:
                #     diploma_certificate_photos_obj = Picture.objects.get(id=diploma_certificate_photos)
                #     form_object_user_info.diploma_certificate_photos = diploma_certificate_photos_obj
                # # 关联院校毕业证书照片
                id_number = form_object_user_info.id_number
                if len(id_number) > 17:
                    birthday_string = str(id_number)[6:14]
                    year = birthday_string[0:4]
                    month = birthday_string[4:6]
                    day = birthday_string[6:8]
                    birthday = year + "-" + month + "-" + day
                    form_object_user_info.birthday = birthday
                    age = timezone.now().year - int(year)
                    print()
                    form_object_user_info.age = age

                start_working_date = form_object_user_info.start_working_date

                if start_working_date:
                    year = start_working_date.year
                    # year = start_working_date[0:4]
                    working_year = timezone.now().year - year
                    form_object_user_info.working_year = working_year

                form_object_user_info.save()

                # 用户基础信息

                # 关联现有的填报信息
                student_id = object_form.cleaned_data.get("student_id", None)
                if student_id:
                    student_infos = StudentInfo.objects.filter(id=student_id)
                    if len(student_infos) > 0:
                        student_info = student_infos[0]

                        person_in_charge = object_form.cleaned_data.get("person_in_charge", None)
                        if person_in_charge:
                            student_info.person_in_charge = person_in_charge
                            student_info.save()
                        student_info.user_info = form_object_user_info
                        title_msg = sys_msg + '-填报详情'
                        image_url = MEDIA_URL + str(student_info.user_info.two_inch_photo.picture_path)
                        # 全部汇总在大填报表格里面
                        certificate_photos_url = ''
                        if student_info.certificate_photos:
                            certificate_photos_url = MEDIA_URL + str(student_info.certificate_photos.picture_path)
                        return render_result(request,
                                             "page_main_controller/student/report_student_user_info_detail.html",
                                             {'title_msg': title_msg, 'student_info': student_info,
                                              'image_url': image_url,
                                              'certificate_photos_url': certificate_photos_url, 'not_exist': False})
                    else:
                        title_msg = sys_msg + '-填报详情'
                        return render_result(request,
                                             "page_main_controller/student/report_student_user_info_detail.html",
                                             {'title_msg': title_msg, 'not_exist': True})
                else:
                    title_msg = sys_msg + '-填报详情'
                    return render_result(request, "page_main_controller/student/report_student_user_info_detail.html",
                                         {'title_msg': title_msg, 'not_exist': True})
            else:
                print(type(object_form.errors), object_form.errors)  # errors类型是ErrorDict，里面是ul，li标签
                title_msg = sys_msg + '-继续填写信息'
                message = '添加失败：输入项不全，请返回重新确认并填写，或联系管理员'
                return render_result(request, "page_main_controller/message.html",
                                     {'title_msg': title_msg, 'message': message})
                # return render(request, "account/form1.html", {"error": f.errors})
    except Exception as e:
        print(str(e))
        title_msg = sys_msg + '-系统错误'
        message = '系统提示：系统异常请稍后重试，或联系管理员'
        return render_result(request, "page_main_controller/message.html",
                             {'title_msg': title_msg, 'message': message})


def update_user_info(request):
    """
    修改用户基础信息
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            object_form = UserInfoUpdateForm(request.POST)
            student_id = request.POST.get('student_id', None)
            if object_form.is_valid():
                username = request.session.get('username', None)  # 用户名
                register_user_info = RegisterUserInfo.objects.get(username=username)
                user_info_id = object_form.cleaned_data.get('user_info_id', None)
                user_infos = UserInfo.objects.filter(id=user_info_id)
                if len(user_infos) > 0:
                    user_info = user_infos[len(user_infos) - 1]
                    form_object_user_info = form_to_obj(object_form.cleaned_data, user_info)
                else:
                    # 用户基础信息
                    form_object_user_info = form_to_obj(object_form.cleaned_data, UserInfo())
                    # 关联注册员信息
                    form_object_user_info.register_user_info = register_user_info
                    # 关联注册员信息
                # 关联操作员信息
                form_object_user_info.user_operator = register_user_info
                # 关联注册员信息
                # 关联教育程度
                education_degree = object_form.cleaned_data.get('education_degree_form', None)
                if education_degree:
                    education_degree_obj = EducationDegree.objects.get(id=education_degree)
                    form_object_user_info.education_degree = education_degree_obj
                # 关联教育程度

                # 关联民族信息
                nation_info = object_form.cleaned_data.get('nation_info_form', None)
                if nation_info:
                    nation_info_obj = NationInfo.objects.get(id=nation_info)
                    form_object_user_info.nation_info = nation_info_obj
                # 关联民族信息

                # 关联单位性质
                unit_nature = object_form.cleaned_data.get('unit_nature_form', None)
                if unit_nature:
                    unit_nature_obj = UnitNature.objects.get(id=unit_nature)
                    form_object_user_info.unit_nature = unit_nature_obj
                # 关联单位性质
                # 关联省
                hukou_province = object_form.cleaned_data.get('hukou_province_form', None)
                if hukou_province:
                    hukou_province_obj = ProvinceCityCountry.objects.get(id=hukou_province)
                    form_object_user_info.hukou_province = hukou_province_obj
                # 关联省
                # 关联市
                hukou_city = object_form.cleaned_data.get('hukou_city_form', None)
                if hukou_city:
                    hukou_city_obj = ProvinceCityCountry.objects.get(id=hukou_city)
                    form_object_user_info.hukou_city = hukou_city_obj
                # 关联市
                # 关联县
                hukou_county = object_form.cleaned_data.get('hukou_county_form', None)
                if hukou_county:
                    hukou_county_obj = ProvinceCityCountry.objects.get(id=hukou_county)
                    form_object_user_info.hukou_county = hukou_county_obj
                # 关联县
                # 关联二寸照片
                two_inch_photo = object_form.cleaned_data.get('two_inch_photo_form', None)
                if two_inch_photo:
                    two_inch_photo_obj = Picture.objects.get(id=two_inch_photo)
                    form_object_user_info.two_inch_photo = two_inch_photo_obj
                # 关联二寸照片

                id_number = form_object_user_info.id_number
                if len(id_number) > 17:
                    birthday_string = str(id_number)[6:14]
                    year = birthday_string[0:4]
                    month = birthday_string[4:6]
                    day = birthday_string[6:8]
                    birthday = year + "-" + month + "-" + day
                    form_object_user_info.birthday = birthday
                    age = timezone.now().year - int(year)
                    form_object_user_info.age = age
                start_working_date = form_object_user_info.start_working_date
                if start_working_date:
                    year = start_working_date.year
                    working_year = timezone.now().year - year
                    form_object_user_info.working_year = working_year
                form_object_user_info.save()
                result['message'] = '个人信息添加成功'
                result["level"] = log_level_edit
                save_operation_log(request, inspect.stack()[0][3], form_object_user_info.__str__(True), result)

                # 用户基础信息

                # 关联现有的填报信息
                student_id = object_form.cleaned_data.get("student_id", None)
                teacher_info_form = object_form.cleaned_data.get("teacher_info_form", None)
                if student_id:
                    student_infos = StudentInfo.objects.filter(id=student_id)
                    if len(student_infos) > 0:
                        student_info = student_infos[0]
                        if teacher_info_form:
                            teacher_infos = TeacherInfo.objects.filter(id=teacher_info_form)
                            if len(teacher_infos) > 0:
                                student_info.teacher_info = teacher_infos[0]

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
                            else:
                                declaration_of_occupation_first = str(declaration_of_occupation)[0:1]
                            identification_level_dict = {'5': '(初)', '4': '(中)', '3': '(高)'}
                            identification_level_str = identification_level_dict[str(identification_level)]
                            explain = declaration_of_occupation_first + identification_level_str
                            student_info.explain = explain
                            student_info.save()
                            student_username = form_object_user_info.register_user_info.username
                            term_worker_picture(student_info.school_term.school_term_name,
                                                student_info.declaration_of_occupation,
                                                student_username,
                                                "二寸证件照",
                                                form_object_user_info.two_inch_photo.picture_path)
                            return HttpResponseRedirect("/report/student_info_detail?studentId=" + str(student_id))
                        # title_msg = sys_msg + '-填报详情'
                        # image_url = MEDIA_URL + str(student_info.user_info.two_inch_photo.picture_path)
                        # # 全部汇总在大填报表格里面
                        # certificate_photos_url = ''
                        # if student_info.certificate_photos:
                        #     certificate_photos_url = MEDIA_URL + str(student_info.certificate_photos.picture_path)
                        # diploma_certificate_photos_url = ''
                        # if student_info.diploma_certificate_photos:
                        #     diploma_certificate_photos_url = MEDIA_URL + str(
                        #         student_info.diploma_certificate_photos.picture_path)
                        #
                        # return render_result(request,
                        #                      "page_main_controller/student/report_student_user_info_detail.html",
                        #                      {'title_msg': title_msg, 'student_info': student_info,
                        #                       'image_url': image_url,
                        #                       'certificate_photos_url': certificate_photos_url,
                        #                       'diploma_certificate_photos_url': diploma_certificate_photos_url,
                        #                       'not_exist': False})
                    else:
                        title_msg = sys_msg + '-填报详情'
                        return render_result(request,
                                             "page_main_controller/student/report_student_user_info_detail.html",
                                             {'title_msg': title_msg, 'not_exist': True})
                else:
                    title_msg = sys_msg + '-填报详情'
                    return render_result(request, "page_main_controller/student/report_student_user_info_detail.html",
                                         {'title_msg': title_msg, 'not_exist': True})
            else:
                print(type(object_form.errors), object_form.errors)  # errors类型是ErrorDict，里面是ul，li标签
                title_msg = sys_msg + '-继续填写信息'
                if student_id:
                    return render_result(request, "page_main_controller/user/report_user_info.html",
                                         {'title_msg': title_msg, 'student_id': student_id})
                # return render_result(request, "account/form1.html", {"error": f.errors})
    except Exception as e:
        print(str(e))
        title_msg = sys_msg + '-系统错误'
        message = '系统提示：系统异常请稍后重试' + str(e)
        return render_result(request, "page_main_controller/message.html",
                             {'title_msg': title_msg, 'message': message})
        # raise e


def update_user_base_info(request):
    """
    修改用户的基本信息
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            object_form = UserInfoUpdateForm(request.POST)
            if object_form.is_valid():
                username = request.session.get('username', None)  # 用户名
                register_user_info = RegisterUserInfo.objects.get(username=username)
                user_info_id = object_form.cleaned_data.get('uid', None)

                print("user_info_id:::" + str(user_info_id))
                user_infos = UserInfo.objects.filter(id=user_info_id)
                if len(user_infos) > 0:
                    user_info = user_infos[len(user_infos) - 1]
                    form_object_user_info = form_to_obj(object_form.cleaned_data, user_info)
                else:
                    # 用户基础信息
                    form_object_user_info = form_to_obj(object_form.cleaned_data, UserInfo())
                    # 关联注册员信息
                    form_object_user_info.register_user_info = register_user_info
                    # 关联注册员信息
                # 关联操作员信息
                form_object_user_info.user_operator = register_user_info
                # 关联注册员信息
                # 关联教育程度
                education_degree = object_form.cleaned_data.get('education_degree_form', None)
                if education_degree:
                    education_degree_obj = EducationDegree.objects.get(id=education_degree)
                    form_object_user_info.education_degree = education_degree_obj
                # 关联教育程度

                # 关联民族信息
                nation_info = object_form.cleaned_data.get('nation_info_form', None)
                if nation_info:
                    nation_info_obj = NationInfo.objects.get(id=nation_info)
                    form_object_user_info.nation_info = nation_info_obj
                # 关联民族信息

                # 关联单位性质
                unit_nature = object_form.cleaned_data.get('unit_nature_form', None)
                if unit_nature:
                    unit_nature_obj = UnitNature.objects.get(id=unit_nature)
                    form_object_user_info.unit_nature = unit_nature_obj
                # 关联单位性质
                # 关联省
                hukou_province = object_form.cleaned_data.get('hukou_province_form', None)
                if hukou_province:
                    hukou_province_obj = ProvinceCityCountry.objects.get(id=hukou_province)
                    form_object_user_info.hukou_province = hukou_province_obj
                # 关联省
                # 关联市
                hukou_city = object_form.cleaned_data.get('hukou_city_form', None)
                if hukou_city:
                    hukou_city_obj = ProvinceCityCountry.objects.get(id=hukou_city)
                    form_object_user_info.hukou_city = hukou_city_obj
                # 关联市
                # 关联县
                hukou_county = object_form.cleaned_data.get('hukou_county_form', None)
                if hukou_county:
                    hukou_county_obj = ProvinceCityCountry.objects.get(id=hukou_county)
                    form_object_user_info.hukou_county = hukou_county_obj
                # 关联县
                # 关联二寸照片
                two_inch_photo = object_form.cleaned_data.get('two_inch_photo_form', None)
                if two_inch_photo:
                    two_inch_photo_obj = Picture.objects.get(id=two_inch_photo)
                    form_object_user_info.two_inch_photo = two_inch_photo_obj
                # 关联二寸照片

                id_number = form_object_user_info.id_number
                if len(id_number) > 17:
                    birthday_string = str(id_number)[6:14]
                    year = birthday_string[0:4]
                    month = birthday_string[4:6]
                    day = birthday_string[6:8]
                    birthday = year + "-" + month + "-" + day
                    form_object_user_info.birthday = birthday
                    age = timezone.now().year - int(year)
                    form_object_user_info.age = age
                start_working_date = form_object_user_info.start_working_date
                if start_working_date:
                    year = start_working_date.year
                    working_year = timezone.now().year - year
                    form_object_user_info.working_year = working_year
                form_object_user_info.save()
                result['message'] = '个人信息修改成功'
                result["level"] = log_level_edit
                save_operation_log(request, inspect.stack()[0][3], form_object_user_info.__str__(True), result)
                # 用户基础信息
                return HttpResponseRedirect('/report/user_setting/')
            else:
                title_msg = sys_msg + '-系统错误'
                message = '系统提示：参数获取异常'
                return render_result(request, "page_main_controller/message.html",
                                     {'title_msg': title_msg, 'message': message})
        else:
            title_msg = sys_msg + '-系统错误'
            message = '系统提示：请求方式异常'
            return render_result(request, "page_main_controller/message.html",
                                 {'title_msg': title_msg, 'message': message})
    except Exception as e:
        print(str(e))
        title_msg = sys_msg + '-系统错误'
        message = '系统提示：系统异常请稍后重试，或联系管理员，错误提示：' + str(e)
        return render_result(request, "page_main_controller/message.html",
                             {'title_msg': title_msg, 'message': message})
        # raise e


def user_info_list(request):
    """
    返回所有用户列表
    :param request:
    :return:
    """
    # cursor = connection.cursor()
    # sql = '''select name,age from student'''
    # cursor.execute(sql)
    # fetchall = cursor.fetchall()
    # students = []
    # for object in fetchall:
    #     students.append({'name': object[0], 'age': object[1]})
    user_infos = UserInfo.objects.filter().order_by('-id')
    paginator = Paginator(user_infos, 20)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    title_msg = '用户信息列表'
    return render_result(request, "page_main_controller/user/user_info_list.html",
                         {'title_msg': title_msg, "contacts": contacts})


def user_setting(request):
    """
    用户基本信息查看
    :param request:
    :return:
    """
    username = request.session.get('username', None)
    title_msg = sys_msg + '-基本信息'
    if username:
        user_infos = UserInfo.objects.filter(register_user_info__username=username)
        print(user_infos.values())
        if user_infos.count() == 1:
            user_info = user_infos[0]
            image_url = ''
            if user_info.two_inch_photo:
                image_url = MEDIA_URL + str(user_info.two_inch_photo.picture_path)
            return render_result(request, "page_main_controller/user/user_info_detail.html",
                                 {'title_msg': title_msg, 'image_url': image_url, 'user_info': user_info})

        else:
            return render_result(request, "page_main_controller/user/user_info_update.html",
                                 {'title_msg': title_msg})
    else:
        title_msg = sys_msg + '-错误信息展示页面'
        message = '查看失败：系统没有此信息记录，请重试或联系管理员！'
        return render_result(request, "page_main_controller/message.html",
                             {'title_msg': title_msg, 'message': message})


def to_user_info_update(request):
    """
    修改或添加用户基本信息
    :param request:
    :return:
    """
    uid = request.GET.get('uid', None)
    title_msg = sys_msg + '-学生信息'
    if uid:
        user_infos = UserInfo.objects.filter(id=uid)
        if user_infos.count() == 1:
            user_info = user_infos[0]
            image_url = ''
            if user_info.two_inch_photo:
                image_url = MEDIA_URL + str(user_info.two_inch_photo.picture_path)
            return render_result(request, "page_main_controller/user/user_info_update.html",
                                 {'title_msg': title_msg, 'image_url': image_url, 'user_info': user_info})
        else:
            title_msg = sys_msg + '-错误信息展示页面'
            message = '查看失败：系统没有此信息记录，请重试或联系管理员！'
            return render_result(request, "page_main_controller/message.html",
                                 {'title_msg': title_msg, 'message': message})
    else:
        title_msg = sys_msg + '-错误信息展示页面'
        message = '系统错误：请求参数获取异常！'
        return render_result(request, "page_main_controller/message.html",
                             {'title_msg': title_msg, 'message': message})


def reset_password(request):
    username = request.GET.get('username', None)
    if username:
        return HttpResponseRedirect('/report/reset_password_page?chtjskykl=' + username)
    else:
        return HttpResponseRedirect('/report/reset_password_page/')


def reset_password_page(request):
    username = request.GET.get('chtjskykl', None)
    title_msg = "修改密码"
    if username:
        return render_result(request, "page_main_controller/user/user_password.html",
                             {'title_msg': title_msg, "username": username, 'role': "administrator"})
    else:
        return render_result(request, "page_main_controller/user/user_password.html",
                             {'title_msg': title_msg, 'role': "student"})


def check_origin_password(request):
    """
    检查原始密码是否正确
    :param request:
    :return:
    """
    new_username = request.POST.get('new_username', None)
    origin_password = request.POST.get('origin_password', None)
    if new_username:
        if origin_password:
            register_user_infos = RegisterUserInfo.objects.filter(username=new_username)
            if register_user_infos.count() == 1:
                register_user_info = register_user_infos[0]
                # 验证密码
                if Password.decrypt_check(origin_password, register_user_info.password):
                    result['status'] = True
                    result['message'] = '原始密码检测成功'
                    result['data'] = json.dumps({}, ensure_ascii=False)
                else:
                    result['status'] = False
                    result['message'] = '原始密码与登陆密码不一致！'
                    result['data'] = json.dumps({}, ensure_ascii=False)
            else:
                result['status'] = False
                result['message'] = '原始密码检测失败,未获取到用户信息！'
                result['data'] = json.dumps({}, ensure_ascii=False)
        else:
            result['status'] = False
            result['message'] = '原始密码检测失败，您未输入原始密码！'
            result['data'] = json.dumps({}, ensure_ascii=False)
    else:
        result['status'] = False
        result['message'] = '原始密码检测失败，未获取到用户名信息！'
        result['data'] = json.dumps({}, ensure_ascii=False)
    return JsonResponse(result, safe=False)


def final_reset_password(request):
    """
    最终修改密码
    :param request:
    :return:
    """
    new_username = request.POST.get('new_username', None)
    new_password = request.POST.get('new_password', None)
    register_user_info = None
    if new_username:
        if new_password:
            register_user_infos = RegisterUserInfo.objects.filter(username=new_username)
            if register_user_infos.count() == 1:
                register_user_info = register_user_infos[0]
                # 验证密码
                register_user_info.password = Password.encryption(new_password)
                register_user_info.save()
                register_user_info = register_user_info.id
                nickname = request.session.get('nickname', None)  # 用户昵称
                username = request.session.get('username', None)  # 用户名
                if username:
                    if username == new_username:
                        result['level'] = log_level_edit
                        save_operation_log(request, inspect.stack()[0][3], "uid:" + str(register_user_info), result)
                        del request.session['username']
                        if nickname:
                            del request.session['nickname']
                        result['message'] = '密码修改成功！'
                    else:
                        result['message'] = '密码修改成功,请通知用户用新密码登陆系统！'
            else:
                result['status'] = False
                result['message'] = '未获取到账户信息！'
        else:
            result['status'] = False
            result['message'] = '您未输入新密码！'
    else:
        result['status'] = False
        result['message'] = '未获取到用户名信息！'
    result['level'] = log_level_edit
    save_operation_log(request, inspect.stack()[0][3], "uid:" + str(register_user_info), result)
    return JsonResponse(result, safe=False)
    # return HttpResponseRedirect(
    #     '/report/final_reset_password_page?status=False&username=' + new_username + '&message=' + result['message'])


def final_reset_password_page(request):
    """
    返回修改密码的状态
    :param request:
    :return:
    """
    status = request.GET.get("status", None)
    message = request.GET.get("message", None)
    username = request.GET.get("username", None)
    title_msg = "修改密码结果"

    if status == 'True':
        role_name = request.session.get('role_name', None)  # 角色名称
        if role_name != "administrator":
            return render_result(request, "page_main_controller/user/user_password.html",
                                 {'title_msg': title_msg, "message": message, 'status': "true"})

        else:
            title_msg = sys_msg + '-修改密码后重新登陆首页'
            school_terms = SchoolTerm.objects.filter()
            if len(school_terms) <= 0:
                return render_result(request, "index.html",
                                     {'title_msg': title_msg, 'need_login': False, 'no_term': False,
                                      'reset_pwd_info': 'true'})
            else:
                school_term = SchoolTerm.objects.last()
                return render_result(request, "index.html",
                                     {'title_msg': title_msg, 'need_login': False, 'school_term': school_term,
                                      'no_term': True, 'reset_pwd_info': 'true'})
    else:
        return render_result(request, "page_main_controller/user/user_password.html",
                             {'title_msg': title_msg, "message": message, 'status': "false", "username": username})
