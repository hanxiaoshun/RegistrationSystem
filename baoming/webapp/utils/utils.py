from webapp.models import *
from django.http import JsonResponse
import json


def get_client_ip(request):
    """
    获取客户端的访问IP
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
    :存储日志反馈信息
    :param request:
    :return: save_operation_log_msg
    """
    save_operation_log_msg = None
    try:
        ip_address = get_client_ip(request)
        # print(sys._getframe().f_code.co_name) #直接打印
        # print(inspect.stack()[0][3])  #方法更灵活，从栈内信信息找出信息
        # print(len(operation_content))
        InterviewAudit.objects.create(operation=operation,
                                      username=request.session.get('username', False),
                                      ip_address=ip_address,
                                      operation_content=operation_content,
                                      operation_result=operation_result['status'],
                                      operation_error_msg=operation_result['error']
                                      )
        if operation_result['status']:
            return save_operation_log_msg
        else:
            return operation_result['error']
    except Exception as e:
        save_operation_log_msg = str(e)
    return save_operation_log_msg


#
# def obj_to_string():
def get_operation_log(request, operation, operation_content, operation_result):
    log_msg = save_operation_log(request, operation, operation_content, operation_result)
    if log_msg is None:
        operation_result['status'] = True
        operation_result['error'] = ''
        # result_01 = {'status': True, 'error': ""}
        # print(utils.save_operation_log(request, businessUsers.__str__(True), result_01['status'], result_01['error']))
    # elif log_msg == operation_result['error']:
    #     operation_result['status'] = False
    #     operation_result['error'] = "操作失败，日志记录正常"
    else:
        operation_result['status'] = False
        operation_result['error'] = log_msg
    return JsonResponse(json.dumps(operation_result), safe=False)
