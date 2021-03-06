import json

from django.core.paginator import Paginator

from ..renderUtil import render_result
from .search_common import *
from .search_param_deal import search_return, search_parameter

from webapp.utils.date_encoder import *


sys_msg = '报名系统'
result = {'status': True, 'message': ''}

def administrator_search_chemical(request):
    """
    化工类待条件查询
    :param request:
    :return:
    """
    title_msg = '化工类学员'
    param_result = search_parameter(request)
    if 'school_term' in param_result:
            if param_result['school_term'] is None:
                message = '尚未添加->报考学期->信息，请->管理员->添加相关信息'
                return render_result(request, "page_main_controller/message.html",
                            {'title_msg': title_msg, 'message': message})
            elif 'user_search_error_class' in param_result:
                    if param_result['user_search_error_class'] is not None:
                        print(param_result['user_search_error_class'], param_result['user_search_errors'])
                        message = '系统提示：参数传输错误：' + param_result['user_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            elif 'student_search_error_class' in param_result:
                    if param_result['student_search_error_class'] is  not None:
                        print(param_result['student_search_error_class'], param_result['student_search_errors'])
                        message = '系统提示：获取当前用户信息失败：' + param_result['student_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            else:
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
                            'report_skill_main':report_skill_main,'report_skill':report_skill}
                if param_result:
                        return render_result(request,
                                            "page_main_controller/administrator/reporter_chemical.html",
                                            page_result)

def administrator_search_chemical_not(request):
    """
    (非化工类)化工类待条件查询
    :param request:
    :return:
    """
    title_msg = "学员报名资料(非化工)"
    param_result = search_parameter(request)
    if 'school_term' in param_result:
            if param_result['school_term'] is None:
                message = '尚未添加->报考学期->信息，请->管理员->添加相关信息'
                return render_result(request, "page_main_controller/message.html",
                            {'title_msg': title_msg, 'message': message})
            elif 'user_search_error_class' in param_result:
                    if param_result['user_search_error_class'] is not None:
                        print(param_result['user_search_error_class'], param_result['user_search_errors'])
                        message = '系统提示：参数传输错误：' + param_result['user_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            elif 'student_search_error_class' in param_result:
                    if param_result['student_search_error_class'] is  not None:
                        print(param_result['student_search_error_class'], param_result['student_search_errors'])
                        message = '系统提示：获取当前用户信息失败：' + param_result['student_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            else:
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
                            'report_skill_main':report_skill_main,'report_skill':report_skill}
                if param_result:
                        return render_result(request,
                                            "page_main_controller/administrator/reporter_chemical_not.html",
                                            page_result)

def administrator_search_all_student(request):
    """
    所有学员的条件查询
    :param request:
    :return:
    """
    title_msg = '查询所有学员'
    param_result = search_parameter(request, 'all_student')
    if 'school_term' in param_result:
            if param_result['school_term'] is None:
                message = '尚未添加->报考学期->信息，请->管理员->添加相关信息'
                return render_result(request, "page_main_controller/message.html",
                            {'title_msg': title_msg, 'message': message})
            elif 'user_search_error_class' in param_result:
                    if param_result['user_search_error_class'] is not None:
                        print(param_result['user_search_error_class'], param_result['user_search_errors'])
                        message = '系统提示：参数传输错误：' + param_result['user_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            elif 'student_search_error_class' in param_result:
                    if param_result['student_search_error_class'] is  not None:
                        print(param_result['student_search_error_class'], param_result['student_search_errors'])
                        message = '系统提示：获取当前用户信息失败：' + param_result['student_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            else:
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
                            'report_skill_main':report_skill_main,'report_skill':report_skill,'no_term': True}

                if param_result:
                        return render_result(request,
                                            "page_main_controller/administrator/all_student_base_info.html",
                                            page_result)


def administrator_search_wait_confirm(request):
    """
    待确认学生信息列表
    :param request:
    :return:
    """
    title_msg = '学生填报信息待确认列表'
    param_result = search_parameter(request, 'wait_confirm')
    if 'school_term' in param_result:
            if param_result['school_term'] is None:
                message = '尚未添加->报考学期->信息，请->管理员->添加相关信息'
                return render_result(request, "page_main_controller/message.html",
                            {'title_msg': title_msg, 'message': message})
            elif 'user_search_error_class' in param_result:
                    if param_result['user_search_error_class'] is not None:
                        print(param_result['user_search_error_class'], param_result['user_search_errors'])
                        message = '系统提示：参数传输错误：' + param_result['user_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            elif 'student_search_error_class' in param_result:
                    if param_result['student_search_error_class'] is  not None:
                        print(param_result['student_search_error_class'], param_result['student_search_errors'])
                        message = '系统提示：获取当前用户信息失败：' + param_result['student_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            else:
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
                            'report_skill_main':report_skill_main,
                            'report_skill':report_skill,
                            'no_term': True}
                if param_result:
                    return render_result(request,
                                        "page_main_controller/administrator/report_student_info_list_admin.html",
                                        page_result)
    

def administrator_reporter_electronic_communication(request):
    """
    电子通信类
    :param request:
    :return:
    """
    param_result = search_parameter(request, 'electronic_communication')
    if 'school_term' in param_result:
            if param_result['school_term'] is None:
                message = '尚未添加->报考学期->信息，请->管理员->添加相关信息'
                return render_result(request, "page_main_controller/message.html",
                            {'title_msg': title_msg, 'message': message})
            elif 'user_search_error_class' in param_result:
                    if param_result['user_search_error_class'] is not None:
                        print(param_result['user_search_error_class'], param_result['user_search_errors'])
                        message = '系统提示：参数传输错误：' + param_result['user_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            elif 'student_search_error_class' in param_result:
                    if param_result['student_search_error_class'] is  not None:
                        print(param_result['student_search_error_class'], param_result['student_search_errors'])
                        message = '系统提示：获取当前用户信息失败：' + param_result['student_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            else:
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
                title_msg = "电子通信类导入模板"

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
                            'report_skill_main':report_skill_main,'report_skill':report_skill}

                if param_result:
                        return render_result(request,
                                            "page_main_controller/administrator/reporter_electronic_communication.html",
                                            page_result)

def administrator_reporter_spin(request):
    """
    纺织类
    :param request:
    :return:
    """
    title_msg = '查询所有纺织大类学员'
    param_result = search_parameter(request, 'spin')
    if 'school_term' in param_result:
            if param_result['school_term'] is None:
                message = '尚未添加->报考学期->信息，请->管理员->添加相关信息'
                return render_result(request, "page_main_controller/message.html",
                            {'title_msg': title_msg, 'message': message})
            elif 'user_search_error_class' in param_result:
                    if param_result['user_search_error_class'] is not None:
                        print(param_result['user_search_error_class'], param_result['user_search_errors'])
                        message = '系统提示：参数传输错误：' + param_result['user_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            elif 'student_search_error_class' in param_result:
                    if param_result['student_search_error_class'] is  not None:
                        print(param_result['student_search_error_class'], param_result['student_search_errors'])
                        message = '系统提示：获取当前用户信息失败：' + param_result['student_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            else:
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
                            'report_skill_main':report_skill_main,'report_skill':report_skill}

                if param_result:
                        return render_result(request,
                                            "page_main_controller/administrator/reporter_spin.html",
                                            page_result)

def administrator_worker_years_6(request):
    """
    工作满6年（含）以上人员名单
    :param request:
    :return:
    """
    title_msg = '工作满6年（含）以上人员名单'
    param_result = search_parameter(request, '')
    if 'school_term' in param_result:
            if param_result['school_term'] is None:
                message = '尚未添加->报考学期->信息，请->管理员->添加相关信息'
                return render_result(request, "page_main_controller/message.html",
                            {'title_msg': title_msg, 'message': message})
            elif 'user_search_error_class' in param_result:
                    if param_result['user_search_error_class'] is not None:
                        print(param_result['user_search_error_class'], param_result['user_search_errors'])
                        message = '系统提示：参数传输错误：' + param_result['user_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            elif 'student_search_error_class' in param_result:
                    if param_result['student_search_error_class'] is  not None:
                        print(param_result['student_search_error_class'], param_result['student_search_errors'])
                        message = '系统提示：获取当前用户信息失败：' + param_result['student_search_errors']
                        return render_result(request, "page_main_controller/message.html",
                                    {'title_msg': title_msg, 'message': message})
            else:
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
                            'report_skill_main':report_skill_main,'report_skill':report_skill}

                if param_result:
                        return render_result(request,
                                            "page_main_controller/administrator/reporter_worker_years_6.html",
                                            page_result)