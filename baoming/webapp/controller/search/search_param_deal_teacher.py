import json

from django.core.paginator import Paginator

from webapp.controller.renderUtil import render_result
from webapp.controller.search.search_common import *
from webapp.utils.date_encoder import *

report_skill_main_classes = ReportSkillMainClass.objects.\
        filter().values("id", "skill_main_class_code", "skill_main_class_name").order_by('-id')

if len(report_skill_main_classes) > 0:
    tmp_list = []
    for i in report_skill_main_classes:
        tmp_list.append(i)
            # result['data'] = serializers.serialize('json', objects)
    report_skill_main_list = json.dumps(tmp_list, ensure_ascii=False)
    

report_skill_result = ReportSkill.objects.\
        filter().values("skill_id", "skill_name", "skill_main_class", "skill_main_class_name").order_by('-skill_id')
if len(report_skill_result) > 0:
    tmp_list = []
    for i in report_skill_result:
        tmp_list.append(i)
            # result['data'] = serializers.serialize('json', objects)
    report_skill_list = json.dumps(tmp_list, ensure_ascii=False)


def search_parameter(request, search_type=None):
    teacher_tmp = None
    role_name = request.session.get('role_name', None)  # 用户名
    if role_name is not None:
        if role_name in 'teacher':
            username = request.session.get('username', None)  # 用户名
            if username:
                register_user_info = RegisterUserInfo.objects.get(username=username)
                user_info_tmp = UserInfo.objects.get(register_user_info=register_user_info)
                teacher_tmp = TeacherInfo.objects.get(user_info=user_info_tmp)
        else:
            pass
    print('role')
    print(role_name)
    print(teacher_tmp)
    title_msg = "所有学员的条件查询"
    student_search = StudentSearchForm(request.GET)
    user_search = UserInfoSearchForm(request.GET)
    page_search = PageSearchForm(request.GET)
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
    per_page = 10
    page = 1
    if page_search.is_valid():
        if page_search.cleaned_data.get('per_page', None):
            per_page = page_search.cleaned_data.get('per_page', None)
        if page_search.cleaned_data.get('page', None):
            page = page_search.cleaned_data.get('page', None)
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
            else:
                identification_level = 0
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
            else:
                teacher_info = teacher_tmp
                
            last_school_term = SchoolTerm.objects.last()
            if school_term:
                if type(school_term) == str:
                    if int(school_term) > 0:
                        kwargs['school_term'] = int(school_term)
                        student_info.school_term = SchoolTerm.objects.get(id=int(school_term))
                else:
                    kwargs['school_term'] = school_term
                    student_info.school_term = SchoolTerm.objects.get(id=school_term)
            else:
                if last_school_term:
                    last_school_term = SchoolTerm.objects.last()
                    school_term = last_school_term.id
                    kwargs['school_term'] = school_term
                    student_info.school_term = SchoolTerm.objects.get(id=school_term)
                    
            report_skill_main_tmp = student_search.cleaned_data.get('skill_main_class', None)
            if report_skill_main_tmp:
                if type(report_skill_main_tmp) == str:
                    if int(report_skill_main_tmp) > 0:
                        kwargs['skill_main_class'] = int(report_skill_main_tmp)
                        student_info.skill_main_class = report_skill_main_tmp
                else:
                    kwargs['skill_main_class'] = report_skill_main_tmp
                    student_info.report_skill_main = report_skill_main_tmp
            else:
                skill_main_class = 0
                
            report_skill_tmp = student_search.cleaned_data.get('skill_main_class', None)
            if report_skill_tmp:
                if type(report_skill_tmp) == str:
                    if int(report_skill_tmp) > 0:
                        kwargs['report_skill'] = int(report_skill_tmp)
                        student_info.report_skill = report_skill_tmp
                else:
                    kwargs['report_skill'] = report_skill_tmp
                    student_info.teacher_info = report_skill_tmp
            else:
                report_skill = 0
                
            if report_skill_main_tmp:
                report_skill_main = report_skill_main_tmp
            else:
                report_skill_main = 0
                
            if report_skill_tmp:
                report_skill = report_skill_tmp
            else:
                report_skill = 0
                
            student_info.user_info = user_info
            print('rrrrrrrrrrrrrrrrrrr')
            print(kwargs)
            print(school_term)
            print(teacher_info)
            if search_type == 'teacher_search_wait_review':
                student_infos = StudentInfo.objects.filter(teacher_info=teacher_info,
                                                           **kwargs).order_by('-id')
            else:
                student_infos = StudentInfo.objects.filter(**kwargs).order_by('-id')
            student_infos_all_term_count = StudentInfo.objects.filter(teacher_info=teacher_info).count()
            paginator = Paginator(student_infos, per_page)
            contacts = paginator.get_page(page)
            if teacher_tmp:
                teacher_info = teacher_tmp
            if len(school_terms) <= 0:
                return render_result(request, "index.html",
                                     {'title_msg': title_msg, 'need_login': False, 'no_term': False})
            else:
                param_result = {'tmp_list':tmp_list,
                'report_skill_main_list':report_skill_main_list,
                'report_skill_list':report_skill_list,
                'last_school_term':last_school_term,
                'student_info':student_info,
                'contacts':contacts,
                'teacher_infos':teacher_infos,
                'school_terms':school_terms,
                'school_term':school_term,
                'teacher_info':teacher_info,
                'identification_level':identification_level,
                'report_skill_main':report_skill_main,
                'report_skill':report_skill,
                'student_infos_all_term_count':student_infos_all_term_count,
                'current_term_student_len': len(student_infos)}
                return param_result
        else:
            print(user_search.error_class, user_search.errors)
            message = '系统提示：获取当前用户失败，请重新登陆后尝试，或联系管理员.'

    else:
        print(student_search.error_class, student_search.errors)
        message = '系统提示：参数传输错误.' + str(student_search.errors)

    return render_result(request, "page_main_controller/message.html",
                         {'title_msg': title_msg, 'message': message})