from webapp.models import *
from django.http import JsonResponse
import json


def get_client_ip(request):
    """
        :得到对应的IP地址
        :author shun
        :param request:
        :return:
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split('', '')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def save_operation_log(request, operation, operation_content, operation_result):
    """
    在程序中进行系统日志统计
    :param request:
    :param operation:
    :param operation_content:
    :param operation_result:
    :return:
    """
    ip_address = get_client_ip(request)
    username = request.session.get('username', False)
    try:
        if username:
            # print(sys._getframe().f_code.co_name) #直接打印
            # print(inspect.stack()[0][3])  #方法更灵活，从栈内信信息找出信息
            # print(len(operation_content))
            interview_audit = InterviewAudit()
            interview_audit.username = username
            interview_audit.operation = operation
            interview_audit.ip_address = ip_address
            interview_audit.operation_level = operation_result['level']
            interview_audit.operation_content = operation_content
            interview_audit.operation_result = operation_result['status']
            interview_audit.operation_message = operation_result['message']
            interview_audit.save()
        else:
            interview_audit = InterviewAudit()
            # 游客身份登陆
            interview_audit.username = "anonymous"
            interview_audit.operation = operation
            interview_audit.ip_address = ip_address
            interview_audit.operation_level = operation_result['level']
            interview_audit.operation_content = operation_content
            interview_audit.operation_result = operation_result['status']
            interview_audit.operation_message = operation_result['message']
            interview_audit.save()
    except Exception as e:
        if username:
            interview_audit = InterviewAudit()
            interview_audit.username = username
            interview_audit.operation = operation
            interview_audit.operation_level = operation_result['level']
            interview_audit.ip_address = ip_address
            interview_audit.operation_content = operation_content
            interview_audit.operation_result = operation_result['status']
            interview_audit.operation_message = operation_result['message']
            interview_audit.save()
        print(str(e))
