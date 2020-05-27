from webapp.controller.renderUtil import render_result
from webapp.controller.search.search_common import *
from webapp.controller.search.search_param_deal_teacher import search_parameter

from webapp.utils.date_encoder import *
from django.core.paginator import Paginator
import json

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def teacher_search_wait_review(request):
    title_msg = '当前负责人名下学员'
    param_result = search_parameter(request, 'teacher_search_wait_review')
    report_skill_main_list = param_result['report_skill_main_list']
    report_skill_list = param_result['report_skill_list']
    tmp_list = param_result['tmp_list']
    last_school_term = param_result['last_school_term']
    student_info = param_result['student_info']
    contacts = param_result['contacts']
    teacher_infos = param_result['teacher_infos']
    school_terms = param_result['school_terms']
    school_term = param_result['school_term']
    teacher_info = param_result['teacher_info']
    identification_level = param_result['identification_level']
    report_skill_main = param_result['report_skill_main']
    report_skill = param_result['report_skill']
    student_infos_all_term_count = param_result['student_infos_all_term_count']
    current_term_student_len = param_result['current_term_student_len']
    print("ssss")
    print(f"{ param_result['contacts'].object_list }")
    page_result = {'title_msg': title_msg, 
                   'need_login': False,
                   'report_skill_main_list':report_skill_main_list,
                   'report_skill_list':report_skill_list,
                   'tmp_list': json.dumps(tmp_list, ensure_ascii=False),
                   'last_school_term': last_school_term, 'student_info': student_info,
                   'contacts': contacts, 'teacher_infos': teacher_infos,
                   'school_terms': school_terms, 'school_term': school_term,
                   'teacher_info': teacher_info,
                   'identification_level': identification_level,
                   'report_skill_main':report_skill_main,'report_skill':report_skill,
                   'student_infos_all_term_count':student_infos_all_term_count,
                   'current_term_student_len': current_term_student_len,'no_term': True}
    return render_result(request,
                         "page_main_controller/teacher/report_student_info_list_teacher.html",
                         page_result)
