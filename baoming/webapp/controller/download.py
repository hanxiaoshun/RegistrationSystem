import inspect
import json
from django.http import FileResponse
from django.shortcuts import HttpResponseRedirect

from webapp.controller.renderUtil import render_result
from webapp.controller.search.search_common import *
from webapp.utils.all_student_base_info_list import *
from webapp.utils.apply_chemical import *
from webapp.utils.apply_not import *
from webapp.utils.reporter_chemical_list import *
from webapp.utils.reporter_chemical_not_list_format import *
from webapp.utils.save_operation_log import save_operation_log

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def download_apply(request):
    """
    下载对应的汇总表
    :param request:
    :return:
    """
    title_msg = '下载山东省职业技能考核表格'
    student_id = request.GET.get('studentId', None)
    try:
        if student_id:
            student = StudentInfo.objects.get(id=student_id)
            if student:
                print(student.declaration_of_occupation)
                if student.declaration_of_occupation not in chemical_industry:
                    # 非化工类的
                    file_uuid, file_uuid2 = apply_not(student)
                    print(str(file_uuid))
                    if file_uuid:
                        message = "文件获取成功，请点击下载查看"
                        file_message_one = '《山东省职业技能鉴定考评表》'
                        file_message_two = '《工作年限证明》'
                        return render_result(request, "page_main_controller/student/report_download_page.html",
                                             {'title_msg': title_msg, 'not_exist': False, 'message': message,
                                              'file_uuid': file_uuid, 'file_uuid2': file_uuid2, 'chemical': False,
                                              'file_message_one': file_message_one,
                                              'file_message_two': file_message_two})
                    else:
                        message = '获取申请表出现系统异常，请稍后重新下载或者联系管理员'
                        return render_result(request, "page_main_controller/student/report_download_page.html",
                                             {'title_msg': title_msg, 'not_exist': True, 'message': message})
                elif student.declaration_of_occupation in chemical_industry:
                    file_uuid = apply_chemical(student)
                    print(str(file_uuid))
                    if file_uuid:
                        file_message_one = '&file_message_one=《化工行业特有工种职业技能鉴定申请表》'
                        return HttpResponseRedirect(
                            '/report/report_download_page?file_uuid=' + file_uuid + file_message_one)
                    else:
                        return HttpResponseRedirect('/report/report_download_page/')
                    # if file_uuid:
                    #     message = "文件获取成功，请点击下载查看"
                    #     return render_result(request, "page_main_controller/student/report_download_page.html",
                    #                   {'title_msg': title_msg, 'not_exist': False, 'message': message,
                    #                    'file_uuid': file_uuid, 'chemical': True})
                    # else:
                    #     message = '获取申请表出现系统异常，请稍后重新下载或者联系管理员'
                    #     return render_result(request, "page_main_controller/student/report_download_page.html",
                    #                   {'title_msg': title_msg, 'not_exist': True, 'message': message})
                else:
                    message = '未获取到您的填报申报行业信息与申请表不匹配，请稍后重新下载或者联系管理员'
                    return render_result(request, "page_main_controller/student/report_download_page.html",
                                         {'title_msg': title_msg, 'not_exist': True, 'message': message})
            else:
                message = '未正确获取到您的填报信息，或者系统异常，请稍后重新下载或者联系管理员'
                return render_result(request, "page_main_controller/student/report_download_page.html",
                                     {'title_msg': title_msg, 'not_exist': True, 'message': message})
        else:
            message = '未正确获取到您的填报信息，或者系统异常，请稍后重新下载或者联系管理员'
            return render_result(request, "page_main_controller/student/report_download_page.html",
                                 {'title_msg': title_msg, 'not_exist': True, 'message': message})
    except Exception as e:
        raise e


def all_student_base_info(request):
    """
    生成所有已确认的学生信息
    :param request:
    :return:
    """
    title_msg = "已确认的所有学生信息"
    student_infos = None
    file_uuid = all_student_base_info_list(student_infos)
    file_message_one = '&file_message_one=学员报名表'
    if file_uuid:
        return HttpResponseRedirect('/report/report_download_page?file_uuid=' + file_uuid + file_message_one)
    else:
        return HttpResponseRedirect('/report/report_download_page/')
    # if file_uuid:
    #     message = "文件获取成功，请点击下载查看"
    #     return render_result(request, "page_main_controller/report_download_page.html",
    #                   {'title_msg': title_msg, 'not_exist': False, 'message': message,
    #                    'file_uuid': file_uuid, 'chemical': True})
    # else:
    #     message = '无数据，或者获取文件出现系统异常，请明确查询结果稍后重新下载或者联系管理员'
    #     return render_result(request, "page_main_controller/report_download_page.html",
    #                   {'title_msg': title_msg, 'not_exist': True, 'message': message})


def reporter_chemical_not(request):
    """
    生成所有非化学类的已确认学生信息
    :param request:
    :return:
    """
    try:
        file_uuid = reporter_chemical_not_list()
        file_message_one = '&file_message_one=《德州市申请职业技能鉴定（技术等级鉴定）颁发职业资格证书花名册》'
        if file_uuid:
            return HttpResponseRedirect(
                '/report/report_download_page?file_uuid=' + file_uuid + '&file_message_one=' + file_message_one)
        else:
            return HttpResponseRedirect('/report/report_download_page/')
        # if file_uuid:
        #     message = "文件获取成功，请点击下载查看"
        #     return render_result(request, "page_main_controller/report_download_page.html",
        #                   {'title_msg': title_msg, 'not_exist': False, 'message': message,
        #                    'file_uuid': file_uuid, 'chemical': True})
        # else:
        #     message = '无数据，或者获取文件出现系统异常，请明确查询结果稍后重新下载或者联系管理员'
        #     return render_result(request, "page_main_controller/report_download_page.html",
        #                   {'title_msg': title_msg, 'not_exist': True, 'message': message})
    except Exception as e:
        raise e


def reporter_chemical(request):
    """
    生成化学类的已确认学生信息
    :param request:
    :return:
    """
    file_uuid = reporter_chemical_list()
    if file_uuid:
        file_message_one = '&file_message_one=《报名资料汇总表（化工类）》'
        return HttpResponseRedirect(
            '/report/report_download_page?file_uuid=' + file_uuid + file_message_one)
    else:
        return HttpResponseRedirect('/report/report_download_page/')

    # if file_uuid:
    #     message = "文件获取成功，请点击下载查看"
    #     return render_result(request, "page_main_controller/report_download_page.html",
    #                   {'title_msg': title_msg, 'not_exist': False, 'message': message,
    #                    'file_uuid': file_uuid, 'chemical': True})
    # else:
    #     message = '无数据，或者获取文件出现系统异常，请明确查询结果稍后重新下载或者联系管理员'
    #     return render_result(request, "page_main_controller/report_download_page.html",
    #                   {'title_msg': title_msg, 'not_exist': True, 'message': message})


def administrator_search_chemical_download(request):
    """
        化工类待条件查询
        :param request:
        :return:
        """
    student_infos = get_student_by_conditions(request, 1)
    if student_infos:
        file_uuid = reporter_chemical_list(student_infos=student_infos)
        if file_uuid:
            file_message_one = '&file_message_one=《报名资料汇总表（化工类）》'
            return HttpResponseRedirect(
                '/report/report_download_page?file_uuid=' + file_uuid + file_message_one)
        else:
            return HttpResponseRedirect('/report/report_download_page/')
    else:
        return HttpResponseRedirect('/report/report_download_page/')


def administrator_search_chemical_not_download(request):
    """
        化工类待条件查询
        :param request:
        :return:
        """
    student_infos = get_student_by_conditions(request, 2)
    if student_infos:
        file_uuid = reporter_chemical_not_list(student_infos=student_infos)
        if file_uuid:
            file_message_one = '&file_message_one=《德州市申请职业技能鉴定（技术等级鉴定）颁发职业资格证书花名册》'
            return HttpResponseRedirect(
                '/report/report_download_page?file_uuid=' + file_uuid + file_message_one)
        else:
            return HttpResponseRedirect('/report/report_download_page/')
    else:
        return HttpResponseRedirect('/report/report_download_page/')


def all_student_base_info_download(request):
    """
        化工类待条件查询
        :param request:
        :return:
        """
    student_infos = get_student_by_conditions(request, 0)
    if student_infos:
        file_uuid = all_student_base_info_list(student_infos)
        if file_uuid:
            file_message_one = '&file_message_one=学员报名表'
            return HttpResponseRedirect(
                '/report/report_download_page?file_uuid=' + file_uuid + file_message_one)
        else:
            return HttpResponseRedirect('/report/report_download_page/')
    else:
        return HttpResponseRedirect('/report/report_download_page/')


def report_download_page(request):
    """
    跳转至下载窗口
    :param request:
    :return:
    """
    file_uuid = request.GET.get('file_uuid', None)
    file_message_one = request.GET.get('file_message_one', None)
    title_msg = "学生信息下载"
    if file_uuid:
        if file_message_one:
            message = "文件获取成功，请点击下载查看"
            return render_result(request, "page_main_controller/report_download_page.html",
                                 {'title_msg': title_msg, 'not_exist': False, 'message': message,
                                  'file_uuid': file_uuid, 'chemical': True, 'file_message_one': file_message_one})
    else:
        message = '无数据，或者获取文件出现异常，请稍后重新下载或者联系管理员'
        return render_result(request, "page_main_controller/report_download_page.html",
                             {'title_msg': title_msg, 'not_exist': True, 'message': message})


def start_download(request):
    """
    开始下载
    :param request:
    :return:
    """
    try:
        file_uuid = request.GET.get('file_uuid', None)
        if file_uuid:
            files = FileManage.objects.filter(file_uuid=file_uuid)
            print(files.__len__())
            if len(files) > 0:
                file = files[len(files) - 1]
                operation_object = file.id
                file_names = str(file.file_path).split("/")
                file_name = file_names[len(file_names) - 1]
                print("file_name::" + file_name)
                ready_file = open(file.file_path, 'rb')
                response = FileResponse(ready_file)
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment;filename=' + file_name
                result['status'] = True
                result['message'] = '下载成功！'
                result['data'] = json.dumps({}, ensure_ascii=False)
                result["level"] = log_level_download
                save_operation_log(request, inspect.stack()[0][3], str(operation_object), result)
                return response
            else:
                title_msg = '下载文件异常'
                message = '未正确获取到您的填报信息，或者系统异常，请稍后重新下载或者联系管理员'
                return render_result(request, "page_main_controller/report_download_page.html",
                                     {'title_msg': title_msg, 'not_exist': True, 'message': message})
        else:
            title_msg = '下载文件异常'
            message = '未正确获取到您的填报信息，或者系统异常，请稍后重新下载或者联系管理员'
            return render_result(request, "page_main_controller/student/report_download_page.html",
                                 {'title_msg': title_msg, 'not_exist': True, 'message': message})
    except Exception as e:
        result['status'] = False
        result['message'] = '下载异常！错误提示：' + str(e)
        result['data'] = json.dumps({}, ensure_ascii=False)
        result["level"] = log_level_download
        save_operation_log(request, inspect.stack()[0][3], "", result)
        title_msg = '下载文件异常'
        message = '未正确获取到您的填报信息，或者系统异常，请稍后重新下载或者联系管理员。错误提示：' + str(e)
        return render_result(request, "page_main_controller/student/report_download_page.html",
                             {'title_msg': title_msg, 'not_exist': True, 'message': message})
