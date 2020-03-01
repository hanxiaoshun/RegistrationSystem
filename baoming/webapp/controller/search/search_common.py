from webapp.forms_search.StudentSearchForm import *
from webapp.forms_search.UserInfoSearchForm import *
from webapp.models import *

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def get_student_by_conditions(request, chemical_worker):
    """
    按条件查询学生
    :param request:
    :param chemical_worker: 1 化工类  2 非化工类
    :return:
    """
    student_search = StudentSearchForm(request.POST)
    user_search = UserInfoSearchForm(request.POST)
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
            if chemical_worker == 0:
                student_infos = StudentInfo.objects.filter(confirm_status=1,
                                                           **kwargs).order_by('-id')
            else:
                student_infos = StudentInfo.objects.filter(confirm_status=1,
                                                           chemical_worker=chemical_worker,
                                                           **kwargs).order_by('-id')
            return student_infos
        else:
            return None
    else:
        return None


def get_student_by_conditions_status(request, submit_status=1,
                                     review_status=1,
                                     confirm_status=1,
                                     pay_status=1,
                                     cancel_status=2,
                                     cancel_result=2,
                                     teacher_cancel_status=2,
                                     teacher_cancel_result=2,
                                     examination_status=2,
                                     chemical_worker=0,
                                     record_status=1):
    """
    按条件查询学生
    :param request:
    :param submit_status: 提交
    :param review_status: 审核
    :param confirm_status: 确认
    :param pay_status: 是否缴费
    :param cancel_status: 是否申请注销
    :param cancel_result: 申请注销结果
    :param teacher_cancel_status: 负责人申请注销
    :param teacher_cancel_result: 负责人申请注销结果
    :param examination_status: 考核通过 默认未通过
    :param chemical_worker: 是否为化工类学员，默认0 不区分化工和非化工
    :param record_status: 学生的状态
    :return:
    """
    student_search = StudentSearchForm(request.POST)
    user_search = UserInfoSearchForm(request.POST)
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
            if chemical_worker == 0:
                student_infos = StudentInfo.objects.filter(submit_status=submit_status, review_status=review_status,
                                                           confirm_status=confirm_status, pay_status=pay_status,
                                                           cancel_status=cancel_status,
                                                           cancel_result=cancel_result,
                                                           teacher_cancel_status=teacher_cancel_status,
                                                           teacher_cancel_result=teacher_cancel_result,
                                                           examination_status=examination_status,
                                                           record_status=record_status,
                                                           **kwargs).order_by('-id')
            else:
                student_infos = StudentInfo.objects.filter(submit_status=submit_status, review_status=review_status,
                                                           confirm_status=confirm_status, pay_status=pay_status,
                                                           cancel_status=cancel_status,
                                                           cancel_result=cancel_result,
                                                           teacher_cancel_status=teacher_cancel_status,
                                                           teacher_cancel_result=teacher_cancel_result,
                                                           examination_status=examination_status,
                                                           chemical_worker=chemical_worker,
                                                           record_status=record_status,
                                                           **kwargs).order_by('-id')
            return student_infos
        else:
            return None
    else:
        return None
