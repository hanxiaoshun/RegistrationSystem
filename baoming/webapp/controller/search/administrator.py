import json

from django.core.paginator import Paginator

from webapp.controller.renderUtil import render_result
from webapp.controller.search.search_common import *
from webapp.utils.date_encoder import *

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def administrator_search_chemical(request):
    """
    化工类待条件查询
    :param request:
    :return:
    """
    student_search = StudentSearchForm(request.POST)
    user_search = UserInfoSearchForm(request.POST)
    teacher_infos = TeacherInfo.objects.all()
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
    if student_search.is_valid():
        if user_search.is_valid():
            # 用户信息
            kwargs = {}
            # kwargs['confirm_status'] = 1,
            # kwargs['chemical_worker'] = 1,
            user_info = UserInfo()
            real_name = user_search.cleaned_data.get('real_name', None)
            if real_name:
                user_info.real_name = real_name
                kwargs['user_info__real_name__icontains'] = real_name
            work_unit = user_search.cleaned_data.get('work_unit', None)
            if work_unit:
                user_info.work_unit = work_unit
                kwargs['user_info__work_unit__icontains'] = work_unit
            education_degree = user_search.cleaned_data.get('education_degree', None)
            if education_degree:
                user_info.education_degree = education_degree
                if type(education_degree) == str:
                    if int(education_degree) > 0:
                        kwargs['user_info__education_degree__id'] = int(education_degree)
                else:
                    kwargs['user_info__education_degree__id'] = education_degree
            # 学生信息
            student_info = StudentInfo()
            identification_level = student_search.cleaned_data.get('identification_level', None)
            declaration_of_occupation = student_search.cleaned_data.get('declaration_of_occupation', None)
            teacher_info = student_search.cleaned_data.get('teacher_info', None)
            school_term = student_search.cleaned_data.get('school_term', None)
            if identification_level:
                student_info.identification_level = identification_level
                if type(identification_level) == str:
                    if int(identification_level) > 0:
                        kwargs['identification_level'] = int(identification_level)
                else:
                    kwargs['identification_level'] = identification_level
            if declaration_of_occupation:
                student_info.declaration_of_occupation = declaration_of_occupation
                kwargs['declaration_of_occupation__icontains'] = declaration_of_occupation

            if teacher_info:
                if type(teacher_info) == str:
                    if int(teacher_info) > 0:
                        kwargs['teacher_info'] = int(teacher_info)
                        student_info.teacher_info = TeacherInfo.objects.get(id=int(teacher_info))
                else:
                    kwargs['teacher_info'] = teacher_info
                    student_info.teacher_info = TeacherInfo.objects.get(id=teacher_info)

            if school_term:
                if type(school_term) == str:
                    if int(school_term) > 0:
                        kwargs['school_term'] = int(school_term)
                        student_info.school_term = SchoolTerm.objects.get(id=int(school_term))
                else:
                    kwargs['school_term'] = school_term
                    student_info.school_term = SchoolTerm.objects.get(id=school_term)

            student_info.user_info = user_info
            print(kwargs)
            student_infos = StudentInfo.objects.filter(confirm_status=1,
                                                       cancel_status=2,
                                                       chemical_worker=1,
                                                       **kwargs).order_by('-id')
            paginator = Paginator(student_infos, 10)
            page = request.GET.get('page')
            contacts = paginator.get_page(page)
            title_msg = "学员报名资料(化工)"
            # return render_result(request, "page_main_controller/administrator/reporter_chemical.html",
            #               {'title_msg': title_msg, "contacts": contacts, 'student_info': student_info,
            #                'teacher_infos': teacher_infos, 'teacher_info': teacher_info, 'school_terms': school_terms,
            #                'school_term': school_term, 'identification_level': identification_level})
            last_school_term = SchoolTerm.objects.last()
            return render_result(request,
                                 "page_main_controller/administrator/reporter_chemical.html",
                                 {'title_msg': title_msg, 'need_login': False,
                                  'tmp_list': json.dumps(tmp_list, ensure_ascii=False),
                                  'last_school_term': last_school_term, 'student_info': student_info,
                                  'contacts': contacts, 'teacher_infos': teacher_infos,
                                  'school_terms': school_terms, 'school_term': school_term,
                                  'teacher_info': teacher_info,
                                  'identification_level': identification_level})
        else:
            print(type(user_search.errors), user_search.errors)  # errors类型是ErrorDict，里面是ul，li标签
    else:
        print(type(student_search.errors), student_search.errors)  # errors类型是ErrorDict，里面是ul，li标签


def administrator_search_chemical_not(request):
    """
    (非化工类)化工类待条件查询
    :param request:
    :return:
    """
    student_search = StudentSearchForm(request.POST)
    user_search = UserInfoSearchForm(request.POST)
    teacher_infos = TeacherInfo.objects.all()
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
    if student_search.is_valid():
        if user_search.is_valid():
            # 用户信息
            kwargs = {}
            # kwargs['confirm_status'] = 1,
            # kwargs['chemical_worker'] = 1,
            user_info = UserInfo()
            real_name = user_search.cleaned_data.get('real_name', None)
            if real_name:
                user_info.real_name = real_name
                kwargs['user_info__real_name__icontains'] = real_name
            work_unit = user_search.cleaned_data.get('work_unit', None)
            if work_unit:
                user_info.work_unit = work_unit
                kwargs['user_info__work_unit__icontains'] = work_unit
            education_degree = user_search.cleaned_data.get('education_degree', None)
            if education_degree:
                user_info.education_degree = education_degree
                if type(education_degree) == str:
                    if int(education_degree) > 0:
                        kwargs['user_info__education_degree__id'] = int(education_degree)
                else:
                    kwargs['user_info__education_degree__id'] = education_degree
            # 学生信息
            student_info = StudentInfo()
            identification_level = student_search.cleaned_data.get('identification_level', None)
            declaration_of_occupation = student_search.cleaned_data.get('declaration_of_occupation', None)
            teacher_info = student_search.cleaned_data.get('teacher_info', None)
            school_term = student_search.cleaned_data.get('school_term', None)
            if identification_level:
                student_info.identification_level = identification_level
                if type(identification_level) == str:
                    if int(identification_level) > 0:
                        kwargs['identification_level'] = int(identification_level)
                else:
                    kwargs['identification_level'] = identification_level
            if declaration_of_occupation:
                student_info.declaration_of_occupation = declaration_of_occupation
                kwargs['declaration_of_occupation__icontains'] = declaration_of_occupation

            if teacher_info:
                if type(teacher_info) == str:
                    if int(teacher_info) > 0:
                        kwargs['teacher_info'] = int(teacher_info)
                        student_info.teacher_info = TeacherInfo.objects.get(id=int(teacher_info))
                else:
                    kwargs['teacher_info'] = teacher_info
                    student_info.teacher_info = TeacherInfo.objects.get(id=teacher_info)

            if school_term:
                if type(school_term) == str:
                    if int(school_term) > 0:
                        kwargs['school_term'] = int(school_term)
                        student_info.school_term = SchoolTerm.objects.get(id=int(school_term))
                else:
                    kwargs['school_term'] = school_term
                    student_info.school_term = SchoolTerm.objects.get(id=school_term)

            student_info.user_info = user_info
            print(kwargs)
            student_infos = StudentInfo.objects.filter(confirm_status=1,
                                                       cancel_status=2,
                                                       chemical_worker=2,
                                                       **kwargs).order_by('-id')

            paginator = Paginator(student_infos, 10)
            page = request.GET.get('page')
            contacts = paginator.get_page(page)
            title_msg = "学员报名资料(非化工)"
            # return render_result(request, "page_main_controller/administrator/reporter_chemical_not.html",
            #               {'title_msg': title_msg, "contacts": contacts, 'student_info': student_info,
            #                'teacher_infos': teacher_infos, 'teacher_info': teacher_info, 'school_terms': school_terms,
            #                'school_term': school_term, 'identification_level': identification_level})
            last_school_term = SchoolTerm.objects.last()
            return render_result(request,
                                 "page_main_controller/administrator/reporter_chemical_not.html",
                                 {'title_msg': title_msg, 'need_login': False,
                                  'tmp_list': json.dumps(tmp_list, ensure_ascii=False),
                                  'last_school_term': last_school_term, 'student_info': student_info,
                                  'contacts': contacts, 'teacher_infos': teacher_infos,
                                  'school_terms': school_terms, 'school_term': school_term,
                                  'teacher_info': teacher_info,
                                  'identification_level': identification_level})


def administrator_search_all_student(request):
    """
    所有学员的条件查询
    :param request:
    :return:
    """
    student_search = StudentSearchForm(request.POST)
    user_search = UserInfoSearchForm(request.POST)
    teacher_infos = TeacherInfo.objects.all()
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
    if student_search.is_valid():
        if user_search.is_valid():
            # 用户信息
            kwargs = {}
            # kwargs['confirm_status'] = 1,
            # kwargs['chemical_worker'] = 1,
            user_info = UserInfo()
            real_name = user_search.cleaned_data.get('real_name', None)
            if real_name:
                user_info.real_name = real_name
                kwargs['user_info__real_name__icontains'] = real_name
            work_unit = user_search.cleaned_data.get('work_unit', None)
            if work_unit:
                user_info.work_unit = work_unit
                kwargs['user_info__work_unit__icontains'] = work_unit
            education_degree = user_search.cleaned_data.get('education_degree', None)
            if education_degree:
                user_info.education_degree = education_degree
                if type(education_degree) == str:
                    if int(education_degree) > 0:
                        kwargs['user_info__education_degree__id'] = int(education_degree)
                else:
                    kwargs['user_info__education_degree__id'] = education_degree
            # 学生信息
            student_info = StudentInfo()
            identification_level = student_search.cleaned_data.get('identification_level', None)
            declaration_of_occupation = student_search.cleaned_data.get('declaration_of_occupation', None)
            teacher_info = student_search.cleaned_data.get('teacher_info', None)
            school_term = student_search.cleaned_data.get('school_term', None)
            if identification_level:
                student_info.identification_level = identification_level
                if type(identification_level) == str:
                    if int(identification_level) > 0:
                        kwargs['identification_level'] = int(identification_level)
                else:
                    kwargs['identification_level'] = identification_level
            if declaration_of_occupation:
                student_info.declaration_of_occupation = declaration_of_occupation
                kwargs['declaration_of_occupation__icontains'] = declaration_of_occupation

            if teacher_info:
                if type(teacher_info) == str:
                    if int(teacher_info) > 0:
                        kwargs['teacher_info'] = int(teacher_info)
                        student_info.teacher_info = TeacherInfo.objects.get(id=int(teacher_info))
                else:
                    kwargs['teacher_info'] = teacher_info
                    student_info.teacher_info = TeacherInfo.objects.get(id=teacher_info)

            if school_term:
                if type(school_term) == str:
                    if int(school_term) > 0:
                        kwargs['school_term'] = int(school_term)
                        student_info.school_term = SchoolTerm.objects.get(id=int(school_term))
                else:
                    kwargs['school_term'] = school_term
                    student_info.school_term = SchoolTerm.objects.get(id=school_term)

            student_info.user_info = user_info
            print(kwargs)
            student_infos = StudentInfo.objects.filter(confirm_status=1,
                                                       cancel_status=2,
                                                       **kwargs).order_by('-id')

            paginator = Paginator(student_infos, 10)
            page = request.GET.get('page')
            contacts = paginator.get_page(page)
            title_msg = "学员报名资料(非化工)"
            # return render_result(request, "page_main_controller/administrator/all_student_base_info.html",
            #               {'title_msg': title_msg, "contacts": contacts, 'student_info': student_info,
            #                'teacher_infos': teacher_infos, 'teacher_info': teacher_info, 'school_terms': school_terms,
            #                'school_term': school_term, 'identification_level': identification_level})
            last_school_term = SchoolTerm.objects.last()
            return render_result(request,
                                 "page_main_controller/administrator/all_student_base_info.html",
                                 {'title_msg': title_msg, 'need_login': False,
                                  'tmp_list': json.dumps(tmp_list, ensure_ascii=False),
                                  'last_school_term': last_school_term, 'student_info': student_info,
                                  'contacts': contacts, 'teacher_infos': teacher_infos,
                                  'school_terms': school_terms, 'school_term': school_term,
                                  'teacher_info': teacher_info,
                                  'identification_level': identification_level})


def administrator_search_wait_confirm(request):
    """
    待确认学生信息列表
    :param request:
    :return:
    """
    student_search = StudentSearchForm(request.POST)
    user_search = UserInfoSearchForm(request.POST)
    teacher_infos = TeacherInfo.objects.all()
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

    if student_search.is_valid():
        if user_search.is_valid():
            # 用户信息
            kwargs = {}
            # kwargs['confirm_status'] = 1,
            # kwargs['chemical_worker'] = 1,
            user_info = UserInfo()
            real_name = user_search.cleaned_data.get('real_name', None)
            if real_name:
                user_info.real_name = real_name
                kwargs['user_info__real_name__icontains'] = real_name
            work_unit = user_search.cleaned_data.get('work_unit', None)
            if work_unit:
                user_info.work_unit = work_unit
                kwargs['user_info__work_unit__icontains'] = work_unit
            education_degree = user_search.cleaned_data.get('education_degree', None)
            if education_degree:
                user_info.education_degree = education_degree
                if type(education_degree) == str:
                    if int(education_degree) > 0:
                        kwargs['user_info__education_degree__id'] = int(education_degree)
                else:
                    kwargs['user_info__education_degree__id'] = education_degree
            # 学生信息
            student_info = StudentInfo()
            identification_level = student_search.cleaned_data.get('identification_level', None)
            declaration_of_occupation = student_search.cleaned_data.get('declaration_of_occupation', None)
            teacher_info = student_search.cleaned_data.get('teacher_info', None)
            school_term = student_search.cleaned_data.get('school_term', None)
            if identification_level:
                student_info.identification_level = identification_level
                if type(identification_level) == str:
                    if int(identification_level) > 0:
                        kwargs['identification_level'] = int(identification_level)
                else:
                    kwargs['identification_level'] = identification_level
            if declaration_of_occupation:
                student_info.declaration_of_occupation = declaration_of_occupation
                kwargs['declaration_of_occupation__icontains'] = declaration_of_occupation

            if teacher_info:
                if type(teacher_info) == str:
                    if int(teacher_info) > 0:
                        kwargs['teacher_info'] = int(teacher_info)
                        student_info.teacher_info = TeacherInfo.objects.get(id=int(teacher_info))
                else:
                    kwargs['teacher_info'] = teacher_info
                    student_info.teacher_info = TeacherInfo.objects.get(id=teacher_info)
            # 根据学期选择性操作
            if school_term:
                if type(school_term) == str:
                    if int(school_term) > 0:
                        kwargs['school_term'] = int(school_term)
                        student_info.school_term = SchoolTerm.objects.get(id=int(school_term))
                else:
                    kwargs['school_term'] = school_term
                    student_info.school_term = SchoolTerm.objects.get(id=school_term)

            student_info.user_info = user_info
            print(kwargs)
            student_infos = StudentInfo.objects.filter(review_status=1,
                                                       cancel_status=2,
                                                       **kwargs).order_by('-id')

            # student_infos = get_student_by_conditions_status(request, review_status=1, cancel_status=2)
            # if student_infos:
            #     student_infos = student_infos.filter(school_term=SchoolTerm.objects.last()).order_by('-id')
            paginator = Paginator(student_infos, 20)
            page = request.GET.get('page')
            contacts = paginator.get_page(page)
            title_msg = '学生填报信息待确认列表'
            if len(school_terms) <= 0:
                return render_result(request, "index.html",
                                     {'title_msg': title_msg, 'need_login': False, 'no_term': False})
            else:
                last_school_term = SchoolTerm.objects.last()
                return render_result(request,
                                     "page_main_controller/administrator/report_student_info_list_admin.html",
                                     {'title_msg': title_msg, 'need_login': False,
                                      'tmp_list': json.dumps(tmp_list, ensure_ascii=False),
                                      'last_school_term': last_school_term, 'student_info': student_info,
                                      'no_term': True, 'contacts': contacts, 'teacher_infos': teacher_infos,
                                      'school_terms': school_terms, 'school_term': school_term,
                                      'teacher_info': teacher_info,
                                      'identification_level': identification_level})
