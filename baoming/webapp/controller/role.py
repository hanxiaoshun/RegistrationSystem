from django.core.paginator import Paginator
from django.shortcuts import render

from webapp.models import *


def role_info_list(request):
    """
    返回所有的角色
    :param request:
    :return:
    """
    role_infos = RoleInfo.objects.filter()
    print(str(role_infos.values()))
    paginator = Paginator(role_infos, 20)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    title_msg = '学生填报信息待确认列表'
    return render(request, "page_main_controller/administrator/role/register_list.html",
                  {'title_msg': title_msg, "contacts": contacts})
