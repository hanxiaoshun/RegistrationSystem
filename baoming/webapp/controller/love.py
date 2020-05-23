from django.http import JsonResponse
from django.shortcuts import render


def love(request):
    """
    个人信息发布
    :param request:
    :return:
    """    
    return render(request, "love.html")


def ada():
    print("asdada")