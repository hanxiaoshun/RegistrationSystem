import inspect
import json

from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from baoming.settings import MEDIA_URL
from webapp.controller.common import *
from webapp.controller.renderUtil import render_result
from webapp.forms.StudentForm import *
from webapp.forms.StudentUpdateForm import *
from webapp.models import *
from webapp.utils.form_to_obj import *
from webapp.utils.save_operation_log import save_operation_log
from webapp.utils.shutilwhichUtil import term_worker_picture

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def get_student_info_extra(request):
    """获取学生的一些扩展信息.

    :param request:
    :return:
    """
    try:
        placeSignUp = PlaceSignUp.objects.filter()
        placeSignUp = serializers.serialize("json", placeSignUp, ensure_ascii=False)
        subsideCertificateClass = SubsideCertificateClass.objects.filter()
        subsideCertificateClass = serializers.serialize("json", subsideCertificateClass, ensure_ascii=False)
        subsideClass = SubsideClass.objects.filter()
        subsideClass = serializers.serialize("json", subsideClass, ensure_ascii=False)
        identifyClass = IdentifyClass.objects.filter()
        identifyClass = serializers.serialize("json", identifyClass, ensure_ascii=False)
        identifySubject = IdentifySubject.objects.filter()
        identifySubject = serializers.serialize("json", identifySubject, ensure_ascii=False)
        studentSourceClass = StudentSourceClass.objects.filter()
        studentSourceClass = serializers.serialize("json", studentSourceClass, ensure_ascii=False)
        examineeIdentity = ExamineeIdentity.objects.filter()
        examineeIdentity = serializers.serialize("json", examineeIdentity, ensure_ascii=False)

        
        data = {"placeSignUp":placeSignUp,
                       "subsideCertificateClass":subsideCertificateClass,
                       "subsideClass":subsideClass,
                       "identifyClass":identifyClass,
                       "identifySubject":identifySubject,
                       "studentSourceClass":studentSourceClass,
                       "examineeIdentity":examineeIdentity,}
        result['data'] = data
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json;charset=utf-8")
                
    except Exception as e:
        raise e