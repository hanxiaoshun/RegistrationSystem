import json

from django.db.models import Q
from django.http import JsonResponse

from webapp.models import *

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def get_like_user_info(request):
    """
    返回模糊匹配的查询结果
    :param request:
    :return:
    """
    record = request.POST.get('record', None)
    message_range = request.POST.get('message_range', None)
    kwargs = {}
    ids = []
    username = request.session.get('username', None)
    if username:
        register_user_info = RegisterUserInfo.objects.get(username=username)
        if register_user_info.role.role_name == 'teacher':
            teacher_info = TeacherInfo.objects.get(
                user_info=UserInfo.objects.get(register_user_info=register_user_info))
            student_infos = StudentInfo.objects.filter(teacher_info=teacher_info).order_by('-id')
            user_info_ids = student_infos.values('user_info')
            if len(user_info_ids) > 0:
                for user_id_dict in user_info_ids:
                    ids.append(user_id_dict['user_info'])
                if record:
                    kwargs['real_name__icontains'] = record
                    kwargs['register_user_info__username__icontains'] = record
                    kwargs['register_user_info__nickname__icontains'] = record
                    # 多条件与关键字同在的查询
                    # user_infos = UserInfo.objects.filter(confirm_status=1,
                    #                                      cancel_status=2,
                    #                                      chemical_worker=1,
                    #                                      **kwargs).order_by('-id')
                    user_infos = UserInfo.objects.filter(
                        Q(real_name__icontains=record) | Q(register_user_info__username__icontains=record) | Q(
                            register_user_info__nickname__icontains=record)).order_by('-id').values('id', 'real_name',
                                                                                                    'register_user_info__username',
                                                                                                    'register_user_info__nickname')
                    tmp_list = []
                    try:
                        if len(user_infos) > 0:
                            if ids.__len__() > 0:
                                for i in user_infos:
                                    print(i)
                                    if i['id'] in ids:
                                        tmp_list.append(i)
                                if tmp_list.__len__() > 0:
                                    result['status'] = True
                                    result['message'] = '用户基础信息模糊查询基础数据获取正常'
                                    result['data'] = json.dumps(tmp_list, ensure_ascii=False)
                                else:
                                    result['status'] = False
                                    result['message'] = '获取数据记录 0,系统基础数据获取异常，请联系管理员管理'
                                    result['data'] = ''
                            else:
                                result['status'] = False
                                result['message'] = '获取数据记录 0,系统基础数据获取异常，请联系管理员管理'
                                result['data'] = ''
                        else:
                            result['status'] = False
                            result['message'] = '获取数据记录 0,系统基础数据获取异常，请联系管理员管理'
                            result['data'] = ''
                    except Exception as e:
                        result['status'] = False
                        result['message'] = '系统异常，错误提示：' + str(e)
                        result['data'] = ''
        else:
            if record:
                kwargs['real_name__icontains'] = record
                kwargs['register_user_info__username__icontains'] = record
                kwargs['register_user_info__nickname__icontains'] = record
                # 多条件与关键字同在的查询
                # user_infos = UserInfo.objects.filter(confirm_status=1,
                #                                      cancel_status=2,
                #                                      chemical_worker=1,
                #                                      **kwargs).order_by('-id')

                if message_range == "4":
                    user_infos = UserInfo.objects.filter(
                        Q(real_name__icontains=record) | Q(register_user_info__username__icontains=record) | Q(
                            register_user_info__nickname__icontains=record),
                        register_user_info__role__role_name='teacher').order_by('-id').values('id', 'real_name',
                                                                                              'register_user_info__username',
                                                                                              'register_user_info__nickname')
                else:
                    user_infos = UserInfo.objects.filter(
                        Q(real_name__icontains=record) | Q(register_user_info__username__icontains=record) | Q(
                            register_user_info__nickname__icontains=record)).order_by('-id').values('id', 'real_name',
                                                                                                    'register_user_info__username',
                                                                                                    'register_user_info__nickname')
                tmp_list = []
                print(user_infos)
                try:
                    if len(user_infos) > 0:
                        for i in user_infos:
                            print(i)
                            tmp_list.append(i)
                        if tmp_list.__len__() > 0:
                            result['status'] = True
                            result['message'] = '用户基础信息模糊查询基础数据获取正常'
                            result['data'] = json.dumps(tmp_list, ensure_ascii=False)
                        else:
                            result['status'] = False
                            result['message'] = '获取数据记录 0,系统基础数据获取异常，请联系管理员管理'
                            result['data'] = ''
                except Exception as e:
                    result['status'] = False
                    result['message'] = '系统异常，错误提示：' + str(e)
                    result['data'] = ''
    return JsonResponse(result, safe=False)
