import inspect
import json
import os
import time
import datetime
from PIL import Image
from django.http import JsonResponse

from baoming.settings import MEDIA_URL, MEDIA_ROOT
from webapp.controller.common import *
from webapp.controller.renderUtil import render_result
from webapp.forms.PictureForm import PictureForm
from webapp.forms.WorkingHistoryForm import *
from webapp.models import ReportCondition, ReportSkill
from webapp.utils.form_to_obj import *
from webapp.utils.save_operation_log import save_operation_log

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def report_skill_info(request):
    """��ȡ���еļ����б�."""
    # print(ReportSkill.objects.filter())
    # query_set = ReportSkill.objects.all.order_by("skill_id")
    query_set = ReportSkill.objects.\
        filter().values("skill_id", "skill_name", "skill_main_class", "skill_main_class_name").order_by('-skill_id')

    print(query_set)
    try:
        if len(query_set) > 0:
            tmp_list = []
            for i in query_set:
                tmp_list.append(i)
            # result['data'] = serializers.serialize('json', objects)
            result['status'] = True
            result['data'] = json.dumps(tmp_list, ensure_ascii=False)
        else:
            result['status'] = False
            result['message'] = '获取数据记录 0'
            result['data'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = '获取数据记录 0,错误提示：' + str(e)
        result['data'] = ''
    return JsonResponse(result, safe=False)

def report_condition_info(request):
    """��ȡ���еļ��������б�."""
    print(request.GET)
    skill_id = request.GET.get('skill_id', None)
    condition_level = request.GET.get('condition_level', None)
    condition_id = request.GET.get('condition_id', None)
    # query_set = ReportCondition.objects.all.order_by('-id')
    # query_set = ReportCondition.objects.\
    #     filter(condition_for_skill=skill_id, condition_level=level).\
    #     values("skill_id", "skill_name").order_by('-skill_id')
    print(type(skill_id))
    print(type(condition_level))
    print(skill_id)
    print(condition_level)
    query_set = None
    if condition_id:
        print('更新的查询')
        print(condition_id)
        query_set = ReportCondition.objects.\
            filter(condition_id=condition_id).values(
            'condition_id', 'condition_name', 'condition_level', 'record_status',
            'condition_for_skill_id', 'apprentice_status',
            'work_of_this_occupation_status',
            'work_of_this_occupation_requirement', 'primary_level_status',
            'primary_level_requirement', 'original_certificate_info_status',
            'original_certificate_worker_time_status',
            'original_certificate_worker_time_requirement', 'school_info_status',
            'graduation_time_status', 'graduation_low_requirement',
            'graduation_lowest', 'graduation_is_Fresh', 'graduation_extra_two',
            'graduation_extra_three', 'certificate_photos_status',
            'diploma_certificate_photos_status', 'explain_condition', 'explain',
            'user_operator_id', 'create_time')
    else:
        query_set = ReportCondition.objects.filter(
            condition_for_skill=int(skill_id),
            condition_level=int(condition_level)).values(
                'condition_id', 'condition_name', 'condition_level',
                'record_status', 'condition_for_skill_id', 'apprentice_status',
                'work_of_this_occupation_status',
                'work_of_this_occupation_requirement', 'primary_level_status',
                'primary_level_requirement',
                'original_certificate_info_status',
                'original_certificate_worker_time_status',
                'original_certificate_worker_time_requirement',
                'school_info_status', 'graduation_time_status',
                'graduation_low_requirement', 'graduation_lowest',
                'graduation_is_Fresh', 'graduation_extra_two',
                'graduation_extra_three', 'certificate_photos_status',
                'diploma_certificate_photos_status', 'explain_condition',
                'explain', 'user_operator_id', 'create_time')
    print(len(query_set))
    print(query_set)
    print(condition_id)
    try:
        if len(query_set) > 0:
            tmp_list = []
            for i in query_set:
                print(i)
                i['create_time'] = date_encoder(i['create_time'])
                tmp_list.append(i)
            print(tmp_list)
            # result['data'] = serializers.serialize('json', objects)
            result['status'] = True
            result['data'] = json.dumps(tmp_list, ensure_ascii=False)
            result['message'] = '获取成功'
            # result['data'] = tmp_list
        else:
            result['status'] = False
            result['message'] = '没有找到本级别的申报条件选项，请重新选择或联系负责人确认'
            result['data'] = ''
    except Exception as e:
        raise e
        result['status'] = False
        result['message'] = '获取申报条件发生错误：' + str(e)
        result['data'] = ''
    print(result)
    return JsonResponse(result, safe=False)

def report_skill_introduction(request):
    query_set_skill = ReportSkill.objects.all().values("skill_id", 
                                                          "skill_name",
                                                          "skill_main_class",
                                                          "skill_main_class_name","skill_explain").order_by('-skill_id')
    print(query_set_skill)
    query_set_condition = ReportCondition.objects.all().values(
                'condition_id', 'condition_name', 'condition_level',
                'record_status', 'condition_for_skill_id', 'explain_condition')
    try:
        if len(query_set_condition) > 0:
            tmp_list_skill = []
            if len(query_set_skill) > 0:
                for j in query_set_skill:
                    tmp_list_conditon = []
                    for i in query_set_condition:
                        if i['condition_for_skill_id'] == j['skill_id']:
                            tmp_list_conditon.append(i)
                    j['list_conditon'] = tmp_list_conditon
                    tmp_list_skill.append(j)
            # result['data'] = serializers.serialize('json', objects)
            result['status'] = True
            result['data'] = json.dumps(tmp_list_skill, ensure_ascii=False)
            result['message'] = '获取成功'
            # result['data'] = tmp_list
        else:
            result['status'] = False
            result['message'] = '没有找到本级别的申报条件选项，请重新选择或联系负责人确认'
            result['data'] = ''
    except Exception as e:
        raise e
        result['status'] = False
        result['message'] = '获取申报条件发生错误：' + str(e)
        result['data'] = ''
    print(result)
    return JsonResponse(result, safe=False)


def date_encoder(obj):
    if isinstance(obj, (datetime.date)):
        return obj.strftime('%Y-%m-%d')
    if isinstance(obj, (datetime.datetime)):
        return obj.strftime('%Y-%m-%d %H:%M:%S')


# def default(self, obj):
#     if isinstance(obj, datetime):
#         return obj.strftime('%Y-%m-%d %H:%M:%S')
#     elif isinstance(obj, date):
#         return obj.strftime('%Y-%m-%d')
#     else:
#         return json.JSONEncoder.default(self, obj)
