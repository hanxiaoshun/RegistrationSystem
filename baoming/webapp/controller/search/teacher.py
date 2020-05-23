from webapp.controller.renderUtil import render_result
from webapp.controller.search.search_common import *
from webapp.utils.date_encoder import *
from django.core.paginator import Paginator
import json

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def teacher_search_wait_review(request):
    student_search = StudentSearchForm(request.GET)
    user_search = UserInfoSearchForm(request.GET)
    page_search = PageSearchForm(request.GET)
    school_terms = SchoolTerm.objects.filter().order_by('-id')

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

    teacher_info = TeacherInfo.objects.get(
        user_info__register_user_info__username=request.session.get('username', None))
    last_school_term = SchoolTerm.objects.last()
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

            if school_term:
                if type(school_term) == str:
                    if int(school_term) > 0:
                        kwargs['school_term'] = int(school_term)
                        student_info.school_term = SchoolTerm.objects.get(id=int(school_term))
                else:
                    kwargs['school_term'] = school_term
                    student_info.school_term = SchoolTerm.objects.get(id=school_term)
            else:
                school_term = last_school_term.id
                kwargs['school_term'] = school_term
                student_info.school_term = SchoolTerm.objects.get(id=school_term)

            student_info.user_info = user_info
            student_infos = StudentInfo.objects.filter(teacher_info=teacher_info,
                                                       **kwargs).order_by('-id')
            # current_term_student_len = StudentInfo.objects.filter(teacher_info=teacher_info,term_).count()
            student_infos_all_term_count = StudentInfo.objects.filter(teacher_info=teacher_info).count()
            paginator = Paginator(student_infos, per_page)
            contacts = paginator.get_page(page)
            print(contacts)
            print(school_term)
            title_msg = "学员报名资料(非化工)"
            if len(school_terms) <= 0:
                return render_result(request, "index.html",
                                     {'title_msg': title_msg, 'need_login': False,
                                      'no_term': False})
            else:
                # return render(request, "page_main_controller/teacher/report_student_info_list_teacher.html",
                #               {'title_msg': title_msg, "contacts": contacts, 'student_info': student_info,
                #                'school_terms': school_terms,'no_term': True,
                #                'last_school_term': last_school_term, 'identification_level': identification_level})
                return render_result(request,
                                     "page_main_controller/teacher/report_student_info_list_teacher.html",
                                     {'title_msg': title_msg, 'need_login': False,
                                      'tmp_list': json.dumps(tmp_list, ensure_ascii=False),
                                      'last_school_term': last_school_term, 'student_info': student_info,
                                      'no_term': True, 'contacts': contacts,'student_infos_all_term_count':student_infos_all_term_count,
                                      'current_term_student_len': len(student_infos),
                                      'school_terms': school_terms, 'school_term': school_term,
                                      'identification_level': identification_level})

        else:
            print(user_search.error_class, user_search.errors)
            message = '系统提示：获取当前用户失败，请重新登陆后尝试，或联系管理员.'

    else:
        print(student_search.error_class, student_search.errors)
        message = '系统提示：参数传输错误.' + str(student_search.errors)

    return render_result(request, "page_main_controller/message.html",
                         {'title_msg': title_msg, 'message': message})
