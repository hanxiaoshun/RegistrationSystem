from django.shortcuts import render
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
from webapp.utils.password import *
import datetime
from django.db.models import Sum, Count, Max, Min, Avg, constants

from django.db import connection


# def user_info_list(request):
#     """
#     返回所有用户列表
#     :param request:
#     :return:
#     """
#     # cursor = connection.cursor()
#     # sql = '''select name,age from student'''
#     # cursor.execute(sql)
#     # fetchall = cursor.fetchall()
#     # students = []
#     # for object in fetchall:
#     #     students.append({'name': object[0], 'age': object[1]})
#     student_infos = StudentInfo.objects.filter()
#     paginator = Paginator(student_infos, 20)
#     page = request.GET.get('page')
#     contacts = paginator.get_page(page)
#     title_msg = '用户信息列表'
#     return render(request, "page_main_controller/user/user_info_list.html",
#                   {'title_msg': title_msg, "contacts": contacts})

