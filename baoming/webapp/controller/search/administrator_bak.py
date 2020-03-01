from django.shortcuts import render, redirect
from django.core import serializers
from webapp.models import *
from django.core.paginator import Paginator
from webapp.utils.form_to_obj import *
from webapp.forms.StudentForm import *
from webapp.forms.StudentUpdateForm import *
from webapp.forms.WorkingHistoryForm import *
from webapp.forms.UserInfoForm import *
from webapp.forms.UserInfoUpdateForm import *

from baoming.settings import MEDIA_URL
from django.http import JsonResponse
import json
from webapp.forms.SchoolTermForm import SchoolTermForm
from webapp.forms.SchoolTermUpdateForm import SchoolTermUpdateForm
from webapp.forms.RegisterTeacherForm import *
from webapp.forms_search.StudentSearchForm import *
from webapp.forms_search.UserInfoSearchForm import *

from webapp.utils.password import *
import datetime

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
                kwargs['identification_level'] = identification_level
                if type(identification_level) == str:
                    kwargs['identification_level'] = int(identification_level)
                else:
                    kwargs['identification_level'] = identification_level
            if declaration_of_occupation:
                student_info.declaration_of_occupation = declaration_of_occupation
                kwargs['declaration_of_occupation__icontains'] = declaration_of_occupation

            if teacher_info:
                if type(teacher_info) == str:
                    kwargs['teacher_info'] = int(teacher_info)
                    student_info.teacher_info = TeacherInfo.objects.get(id=int(teacher_info))
                else:
                    kwargs['teacher_info'] = teacher_info
                    student_info.teacher_info = TeacherInfo.objects.get(id=teacher_info)

            if school_term:
                if type(school_term) == str:
                    kwargs['school_term'] = int(school_term)
                    student_info.school_term = SchoolTerm.objects.get(id=int(school_term))
                else:
                    kwargs['school_term'] = school_term
                    student_info.school_term = SchoolTerm.objects.get(id=school_term)

            student_info.user_info = user_info
            print(kwargs)
            student_infos = StudentInfo.objects.filter(confirm_status=1,
                                                       chemical_worker=1,
                                                       **kwargs).order_by('-id')


            # student_infos = StudentInfo.objects.filter(confirm_status=1,
            #                                            chemical_worker=1,
            #                                            user_info__education_degree__id=9).order_by('-id')
            # student_infos = StudentInfo.objects.filter(confirm_status=1,
            #                                            chemical_worker=1,
            #                                            user_info__real_name__icontains='刘').order_by('-id')
            # student_infos = StudentInfo.objects.filter(confirm_status=1,
            #                                            chemical_worker=1,
            #                                            user_info__real_name__icontains='刘',
            #                                            **kwargs).order_by('-id')
            print(student_infos.__len__())
            paginator = Paginator(student_infos, 10)
            page = request.GET.get('page')
            contacts = paginator.get_page(page)
            title_msg = "学员报名资料(化工)"
            return render(request, "page_main_controller/administrator/reporter_chemical.html",
                          {'title_msg': title_msg, "contacts": contacts, 'student_info': student_info,
                           'teacher_infos': teacher_infos, 'teacher_info': teacher_info, 'school_terms': school_terms,
                           'school_term': school_term, 'identification_level': identification_level})
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
    if student_search.is_valid():
        if user_search.is_valid():
            student_info = StudentInfo()
            student_info.identification_level = student_search.cleaned_data.get('identification_level', None)
            student_info.declaration_of_occupation = student_search.cleaned_data.get('declaration_of_occupation', None)
            student_info.teacher_info = student_search.cleaned_data.get('teacher_info', None)
            student_info.school_term = student_search.cleaned_data.get('school_term', None)

            user_info = UserInfo()
            user_info.real_name = user_search.cleaned_data.get('real_name', None)
            user_info.work_unit = user_search.cleaned_data.get('work_unit', None)
            user_info.education_degree = user_search.cleaned_data.get('education_degree', None)

            student_info.user_info = user_info
            student_infos = StudentInfo.objects.filter(confirm_status=1,
                                                       chemical_worker=1,
                                                       identification_level=student_info.identification_level,
                                                       declaration_of_occupation=student_info.declaration_of_occupation,
                                                       teacher_info=student_info.teacher_info,
                                                       user_info=user_info).order_by('-id')
            paginator = Paginator(student_infos, 10)
            page = request.GET.get('page')
            contacts = paginator.get_page(page)
            title_msg = "学员报名资料(化工)"
            return render(request, "page_main_controller/administrator/reporter_chemical_not.html",
                          {'title_msg': title_msg, "contacts": contacts, 'student_info': student_info,
                           'teacher_infos': teacher_infos, 'school_terms': school_terms})
