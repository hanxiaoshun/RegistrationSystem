import inspect
import json
import os
import time

from PIL import Image
from django.http import JsonResponse

from baoming.settings import MEDIA_URL, MEDIA_ROOT
from webapp.controller.common import *
from webapp.controller.renderUtil import render_result
from webapp.forms.PictureForm import PictureForm
from webapp.forms.IDCardPictureForm import IDCardPictureForm
from webapp.forms.WorkingHistoryForm import *
from webapp.models import *
from webapp.utils.form_to_obj import *
from webapp.utils.save_operation_log import save_operation_log

sys_msg = '报名系统'
result = {'status': True, 'message': ''}


def worker(request):
    """
    进入系统判断是否在填报的周期内，如在周期内
    :param request:
    :return:
    """
    title_msg = sys_msg + '-系统提示页面'
    try:
        school_terms = SchoolTerm.objects.filter()
        if len(school_terms) <= 0:
            message = "报名尚未开始，请您等待或联系管理员！"
            return render_result(request, "page_main_controller/message.html",
                                 {'title_msg': title_msg, 'message': message})
        else:
            pass

        school_term = SchoolTerm.objects.last()
        school_term_start = school_term.school_term_start
        school_term_end = school_term.school_term_end
        # time.mktime(time.strptime(school_term_start, '%Y-%m-%d %H:%M:%S'))
        # time.mktime(time.strptime(school_term_end, '%Y-%m-%d %H:%M:%S'))
        # starts = str(school_term_start).split('-')
        # year_start = int(starts[0])
        # month_start = int(starts[1])
        # day_start = int(starts[2])

        # ends = str(school_term_end).split('-')
        # year_end = int(ends[0])
        # month_end = int(ends[1])
        # day_end = int(ends[2])
        school_term_start.timetuple()
        # print(f"{school_term_start},--{school_term_end}")
        # print(f"{time.mktime(school_term_start.timetuple())},--{time.mktime(school_term_end.timetuple())}")
        school_term_start_timestamp = time.mktime(school_term_start.timetuple())
        school_term_end_timestamp = time.mktime(school_term_end.timetuple())

        school_term_end_timestamp = school_term_end_timestamp + 86400

        # print(type(school_term_end_timestamp))  # float
        # year = timezone.now().year
        # month = timezone.now().month
        # day = timezone.now().day
        # print(f"{year}:{month}:{day}, {time.time()}")

        # 应该用时间戳大小来比较，这样可能性和错误率就没有了

        # # 首先考虑跨年份的情况
        # if year > year_start:
        #     # 如果当前年份大于开始年份，则判断当前年份是否等于结束年份
        #     if year == year_end:
        #         # 如果当前年份等于结束年份
        #
        #
        #
        #
        #
        #
        #
        # if year != year_start and year != year_end:
        #     flag = True
        # else:
        #     if month < month_start:
        #         flag = True
        #     elif month > month_end:
        #         flag = True
        #     elif month < month_end:
        #         # 如果跨月份报名的话，不需要改动
        #         flag = False
        #     elif month == month_end:
        #         print(month+"sssss")
        #         if day < day_start:
        #             flag = True
        #         elif day > day_end:
        #             flag = True
        #         else:
        #             pass

        if school_term_end_timestamp > time.time() > school_term_start_timestamp:
            # print("在当前报名时间段内")
            flag = False
        else:
            flag = True

        if flag:
            message = "当前日期不在==《" + school_term.school_term_name + "》==报名的时间范围内，请核验首页本期报名时间信息！"
            return render_result(request, "page_main_controller/message.html",
                                 {'title_msg': title_msg, 'message': message})
        else:
            skill_main_class = request.GET.get('skill_main_class', None)
            skill_id = request.GET.get('skill_id', None)
            skill_name = request.GET.get('skill_name', None)
            if skill_name:
                username = request.session.get('username', None)  # 用户名
                title_msg = sys_msg + '-' + skill_name
                if username:
                    register_user_info = RegisterUserInfo.objects.get(username=username)
                    user_infos = UserInfo.objects.filter(register_user_info=register_user_info.id).order_by('-id')
                    if len(user_infos) > 0:
                        user_info = user_infos[0]
                        if user_info.two_inch_photo:
                            image_url = MEDIA_URL + str(user_info.two_inch_photo.picture_path)
                        else:
                            image_url = ''
                        return render_result(request, "page_main_controller/student/report_student_info.html",
                                             {'title_msg': title_msg, 'skill_name': skill_name, 'skill_id': skill_id,
                                              'need_list': True,
                                              'skill_main_class': skill_main_class,
                                              'user_info': user_info,
                                              'image_url': image_url})
                    else:
                        return render_result(request, "page_main_controller/student/report_student_info.html",
                                             {'title_msg': title_msg, 'skill_name': skill_name, 'skill_id': skill_id,
                                              'image_url': "/media/images/2019/06/other_time.jpeg"})
                else:
                    return render_result(request, "page_main_controller/report_student_info.html",
                                         {'title_msg': title_msg, 'skill_name': skill_name, 'skill_id': skill_id,
                                          'image_url': "/media/images/2019/06/other_time.jpeg"})
            else:
                message = "系统访问格式异常，请稍后尝试，或者联系管理员！"
                return render_result(request, "page_main_controller/message.html",
                                     {'title_msg': title_msg, 'message': message})
    except Exception as e:
        message = "系统异常，请稍后尝试，或者联系管理员！错误提示：" + str(e)
        return render_result(request, "page_main_controller/message.html",
                             {'title_msg': title_msg, 'message': message})


def education_degree(request):
    # EducationDegree.objects.filter().values() 按条件查询
    # objects = EducationDegree.objects.all().order_by("-id")
    query_set = EducationDegree.objects.values("id", "education_name").order_by('id')
    tmp_list = []
    try:
        if len(query_set) > 0:
            for i in query_set:
                tmp_list.append(i)
            # result['data'] = serializers.serialize('json', objects)
            result['status'] = True
            result['message'] = '文化程度基础数据获取正常'
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


def unit_nature(request):
    # EducationDegree.objects.filter().values() 按条件查询
    # objects = EducationDegree.objects.all().order_by("-id")
    query_set = UnitNature.objects.values("id", "unit_nature").order_by('-id')
    tmp_list = []
    try:
        if len(query_set) > 0:
            for i in query_set:
                tmp_list.append(i)
            # result['data'] = serializers.serialize('json', objects)
            result['status'] = True
            result['message'] = '单位性质基础数据获取正常'
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


def nation_info(request):
    query_set = NationInfo.objects.values("id", "nation_name").order_by('id')
    tmp_list = []
    try:
        if len(query_set) > 0:
            for i in query_set:
                tmp_list.append(i)
            # result['data'] = serializers.serialize('json', objects)
            result['status'] = True
            result['message'] = '民族基础数据获取正常'
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


def province(request):
    """
    获取省的信息
    :param request:
    :return:
    """
    query_set = ProvinceCityCountry.objects.filter(region_level=0).values("id", "region_name").order_by('-id')
    tmp_list = []
    try:
        if len(query_set) > 0:
            for i in query_set:
                tmp_list.append(i)
            result['status'] = True
            result['message'] = '户口所在省基础数据获取正常'
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


def city(request):
    """
    获取市的信息
    :param request:
    :return:
    """
    region = request.GET.get("province", None)
    try:
        region_city = ProvinceCityCountry.objects.get(id=region)
        query_set = ProvinceCityCountry.objects.filter(parent=region_city.id).values("id", "region_name").order_by(
            '-id')
        print(query_set)
        tmp_list = []
        if len(query_set) > 0:
            for i in query_set:
                tmp_list.append(i)
            result['status'] = True
            result['data'] = json.dumps(tmp_list, ensure_ascii=False)
            return JsonResponse(result, safe=False)
        else:
            result['status'] = False
            result['message'] = '获取数据记录 0'
            result['data'] = ''
    except ProvinceCityCountry.DoesNotExist as e:
        result['status'] = False
        result['message'] = '获取数据记录 0'
        result['data'] = ''
    return JsonResponse(result, safe=False)


def county(request):
    """
    获取县的信息
    :param request:
    :return:
    """
    region = request.GET.get("city", None)
    try:
        region_city = ProvinceCityCountry.objects.get(id=region)
        query_set = ProvinceCityCountry.objects.filter(parent=region_city).values("id", "region_name").order_by('-id')
        tmp_list = []
        if len(query_set) > 0:
            for i in query_set:
                tmp_list.append(i)
            result['status'] = True
            result['data'] = json.dumps(tmp_list, ensure_ascii=False)
        else:
            result['status'] = False
            result['message'] = '获取数据记录 0'
            result['data'] = ''
    except ProvinceCityCountry.DoesNotExist as e:
        result['status'] = False
        result['message'] = '获取数据记录 0'
        result['data'] = ''
    return JsonResponse(result, safe=False)


def image_upload(request):
    """
    文件上传
    :param request:
    :return:
    """
    operation_object = None
    school_term_name = None
    school_terms = SchoolTerm.objects.all().order_by('-id')
    if school_terms.count() > 0:
        for school_term in school_terms:
            school_term_name = school_term.school_term_name
            school_term_start = school_term.school_term_start
            school_term_end = school_term.school_term_end
            school_term_start_timestamp = time.mktime(school_term_start.timetuple())
            school_term_end_timestamp = time.mktime(school_term_end.timetuple())
            if school_term_end_timestamp > time.time() > school_term_start_timestamp:
                # print("在当前报名时间段内")
                flag = False
            else:
                flag = True
    # school_term = SchoolTerm.objects.last()
    # school_term_start = school_term.school_term_start
    # school_term_end = school_term.school_term_end
    #
    # school_term_start.timetuple()
    # school_term_start_timestamp = time.mktime(school_term_start.timetuple())
    # school_term_end_timestamp = time.mktime(school_term_end.timetuple())

    # if school_term_end_timestamp > time.time() > school_term_start_timestamp:
    #     # print("在当前报名时间段内")
    #     flag = False
    # else:
    #     flag = True

    try:
        if request.method == 'POST':
            form = PictureForm(request.POST, request.FILES)
            if form.is_valid():
                # file is saved
                print(form.cleaned_data.items())
                instance = Picture(picture_path=request.FILES['file'])
                # instance.picture_name = form.cleaned_data['picture_name']
                username = request.session.get('username', None)  # 用户名
                register_user_info = RegisterUserInfo.objects.get(username=username)
                instance.user_operator = register_user_info
                instance.save()
                # 更换图片文件的名字开始，如果不处理，将受到系统和安全两个方面各种问题
                old_path = str(instance.picture_path)
                old_paths = old_path.split('/')
                old_paths[len(old_paths) - 1] = str(instance.picture_uuid)[:16] + '.jpg'
                new_path = "/".join(old_paths)
                picture_old_os_path = MEDIA_ROOT + "\\" + str(instance.picture_path)
                picture_old_os_path = picture_old_os_path.replace("\\", "/")
                # 如果是上唇2寸照片需要判断

                picture_new_os_path = MEDIA_ROOT + "\\" + new_path
                picture_new_os_path = picture_new_os_path.replace("\\", "/")
                os.rename(picture_old_os_path, picture_new_os_path)
                instance.picture_path = new_path
                instance.save()
                operation_object = instance.id
                # 更换图片文件的名字结束
                file_type = request.POST.get('file_type', None)
                print("file_type:::" + str(file_type))
                # 将文件备份到学期的文件夹下
                term_picture_root = MEDIA_ROOT + "/term_picture/" + school_term_name + "/"
                if file_type:
                    im = Image.open(picture_new_os_path)  # 返回一个Image对象

                    resized = im.resize((64, 64))

                    resized.save("test.jpg")

                    print('宽：%d,高：%d' % (im.size[0], im.size[1]))
                    # 介于一寸照片和二寸照片
                    if 420 > im.size[0] > 280:
                        if 650 > im.size[1] > 400:
                            result['status'] = True
                            result['data'] = MEDIA_URL + str(instance.picture_path)
                            result['message'] = '图片上传状态正常！'
                            result['picture'] = instance.id
                        else:
                            im = im.convert('RGB')
                            resized = im.resize((400, 580))
                            picture_new_os_path = picture_new_os_path.replace('.jpg', '_resize.jpg')
                            resized.save(picture_new_os_path)
                            instance.picture_path = new_path.replace('.jpg', '_resize.jpg')
                            result['status'] = True
                            result['data'] = MEDIA_URL + str(instance.picture_path)
                            result['message'] = '图片上传状态正常！'
                            result['picture'] = instance.id
                            # result['status'] = False
                            # result['message'] = '照片尺寸判断异常！请重新上传尺寸为：宽：380~413* 高：590~626像素 的二寸头像图片'
                            # result['error'] = ''
                    else:
                        im = im.convert('RGB')
                        resized = im.resize((400, 580))
                        picture_new_os_path = picture_new_os_path.replace('.jpg', '_resize.jpg')
                        resized.save(picture_new_os_path)
                        instance.picture_path = new_path.replace('.jpg', '_resize.jpg')
                        result['status'] = True
                        result['data'] = MEDIA_URL + str(instance.picture_path)
                        result['message'] = '图片上传状态正常！'
                        result['picture'] = instance.id
                        # result['status'] = False
                        # result['message'] = '照片尺寸判断异常！请重新上传尺寸为：380~413*590~626像素 的二寸头像图片'
                        # result['error'] = ''
                else:
                    result['status'] = True
                    result['data'] = MEDIA_URL + str(instance.picture_path)
                    result['message'] = '图片上传状态正常！'
                    result['picture'] = instance.id
                # return HttpResponseRedirect('/success/url/')
        else:
            result['status'] = False
            result['message'] = '网络访问协议异常'
            result['error'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = '获取数据记录 0' + str(e)
        result['error'] = ''
    result["level"] = log_level_upload
    save_operation_log(request, inspect.stack()[0][3], "uid:" + str(operation_object), result)
    return JsonResponse(result, safe=False)

def image_upload_id_card(request):
    """
    文件上传
    :param request:
    :return:
    """
    operation_object = None
    school_term_name = None
    school_terms = SchoolTerm.objects.all().order_by('-id')
    if school_terms.count() > 0:
        for school_term in school_terms:
            school_term_name = school_term.school_term_name
            school_term_start = school_term.school_term_start
            school_term_end = school_term.school_term_end
            school_term_start_timestamp = time.mktime(school_term_start.timetuple())
            school_term_end_timestamp = time.mktime(school_term_end.timetuple())
            if school_term_end_timestamp > time.time() > school_term_start_timestamp:
                # print("在当前报名时间段内")
                flag = False
            else:
                flag = True
    # school_term = SchoolTerm.objects.last()
    # school_term_start = school_term.school_term_start
    # school_term_end = school_term.school_term_end
    #
    # school_term_start.timetuple()
    # school_term_start_timestamp = time.mktime(school_term_start.timetuple())
    # school_term_end_timestamp = time.mktime(school_term_end.timetuple())

    # if school_term_end_timestamp > time.time() > school_term_start_timestamp:
    #     # print("在当前报名时间段内")
    #     flag = False
    # else:
    #     flag = True

    try:
        if request.method == 'POST':
            form = IDCardPictureForm(request.POST, request.FILES)
            if form.is_valid():
                # file is saved
                print(form.cleaned_data.items())
                instance = IDCardPicture(picture_path=request.FILES['file'])
                # instance.picture_name = form.cleaned_data['picture_name']
                username = request.session.get('username', None)  # 用户名
                register_user_info = RegisterUserInfo.objects.get(username=username)
                instance.user_operator = register_user_info
                instance.save()
                # 更换图片文件的名字开始，如果不处理，将受到系统和安全两个方面各种问题
                old_path = str(instance.picture_path)
                old_paths = old_path.split('/')
                old_paths[len(old_paths) - 1] = str(instance.picture_uuid)[:16] + '.jpg'
                new_path = "/".join(old_paths)
                picture_old_os_path = MEDIA_ROOT + "\\" + str(instance.picture_path)
                picture_old_os_path = picture_old_os_path.replace("\\", "/")
                # 如果是上唇2寸照片需要判断

                picture_new_os_path = MEDIA_ROOT + "\\" + new_path
                picture_new_os_path = picture_new_os_path.replace("\\", "/")
                os.rename(picture_old_os_path, picture_new_os_path)
                instance.picture_path = new_path
                instance.save()
                operation_object = instance.id
                # 更换图片文件的名字结束
                file_type = request.POST.get('file_type', None)
                print("file_type:::" + str(file_type))
                # 将文件备份到学期的文件夹下
                term_picture_root = MEDIA_ROOT + "/term_picture/" + school_term_name + "/"
                if file_type:
                    im = Image.open(picture_new_os_path)  # 返回一个Image对象

                    resized = im.resize((64, 64))

                    resized.save("test.jpg")

                    print('宽：%d,高：%d' % (im.size[0], im.size[1]))
                    # 介于一寸照片和二寸照片
                    if 420 > im.size[0] > 280:
                        if 650 > im.size[1] > 400:
                            result['status'] = True
                            result['data'] = MEDIA_URL + str(instance.picture_path)
                            result['message'] = '图片上传状态正常！'
                            result['picture'] = instance.id
                        else:
                            im = im.convert('RGB')
                            resized = im.resize((400, 580))
                            picture_new_os_path = picture_new_os_path.replace('.jpg', '_resize.jpg')
                            resized.save(picture_new_os_path)
                            instance.picture_path = new_path.replace('.jpg', '_resize.jpg')
                            result['status'] = True
                            result['data'] = MEDIA_URL + str(instance.picture_path)
                            result['message'] = '图片上传状态正常！'
                            result['picture'] = instance.id

                            # result['status'] = False
                            # result['message'] = '照片尺寸判断异常！请重新上传尺寸为：宽：380~413* 高：590~626像素 的二寸头像图片'
                            # result['error'] = ''
                    else:
                        im = im.convert('RGB')
                        resized = im.resize((400, 580))
                        picture_new_os_path = picture_new_os_path.replace('.jpg', '_resize.jpg')
                        resized.save(picture_new_os_path)
                        instance.picture_path = new_path.replace('.jpg', '_resize.jpg')
                        result['status'] = True
                        result['data'] = MEDIA_URL + str(instance.picture_path)
                        result['message'] = '图片上传状态正常！'
                        result['picture'] = instance.id
                        # result['status'] = False
                        # result['message'] = '照片尺寸判断异常！请重新上传尺寸为：380~413*590~626像素 的二寸头像图片'
                        # result['error'] = ''
                else:
                    result['status'] = True
                    result['data'] = MEDIA_URL + str(instance.picture_path)
                    result['message'] = '图片上传状态正常！'
                    result['picture'] = instance.id
                # return HttpResponseRedirect('/success/url/')
        else:
            result['status'] = False
            result['message'] = '网络访问协议异常'
            result['error'] = ''
    except Exception as e:
        result['status'] = False
        result['message'] = '获取数据记录 0' + str(e)
        result['error'] = ''
    result["level"] = log_level_upload
    save_operation_log(request, inspect.stack()[0][3], "uid:" + str(operation_object), result)
    return JsonResponse(result, safe=False)


def worker_history(request):
    """
    跳转到工作经验证明的页面
    :param request:
    :return:
    """
    title_msg = sys_msg + '-工作履历'
    username = request.session.get('username', None)  # 用户名
    register_user_info = RegisterUserInfo.objects.get(username=username)
    user_infos = UserInfo.objects.filter(register_user_info=register_user_info.id)
    if len(user_infos) > 0:
        user_info = user_infos[len(user_infos) - 1]
        # user_Info_working_history = user_info.user_Info_working_history.all().values()
        # 获得纯值，而非对象集合
        # print("user_Info_working_history::" + str(user_Info_working_history))
        working_history_list = user_info.user_Info_working_history.all()
        print("user_Info_working_history::" + str(working_history_list))

        student_infos = StudentInfo.objects.filter(user_info=user_info)
        if len(student_infos) > 0:
            student_info = student_infos[0]
            return render_result(request, "page_main_controller/report_worker_history.html",
                                 {'title_msg': title_msg, 'student_info': student_info,
                                  'working_history_list': working_history_list, 'not_report': False})
        else:
            return render_result(request, "page_main_controller/report_worker_history.html",
                                 {'title_msg': title_msg, 'not_report': True})
    else:
        return render_result(request, "page_main_controller/report_worker_history.html",
                             {'title_msg': title_msg, 'not_report': True})


def add_work_history(request):
    """
    添加工作经验历史
    :param request:
    :return:
    """
    title_msg = sys_msg + '-工作履历'
    try:
        if request.method == 'POST':
            object_form = WorkingHistoryForm(request.POST)
            # print(object_form)
            if object_form.is_valid():
                user_info_id = object_form.cleaned_data['obj_id']
                user_info = UserInfo.objects.get(id=user_info_id)
                form_object_working_history = form_to_obj(object_form.cleaned_data, WorkingHistory())
                # 关联县
                hukou_county = object_form.cleaned_data['hukou_county_form']
                if hukou_county == -1:
                    # 关联市
                    hukou_city = object_form.cleaned_data['hukou_city_form']
                    hukou_city_obj = ProvinceCityCountry.objects.get(id=hukou_city)
                    form_object_working_history.city_or_county = hukou_city_obj
                else:
                    hukou_county_obj = ProvinceCityCountry.objects.get(id=hukou_county)
                    form_object_working_history.city_or_county = hukou_county_obj
                form_object_working_history.save()
                # 添加一条工作记录
                user_info.user_Info_working_history.add(form_object_working_history)
                # 查找出所有的工作记录
                working_history_list = user_info.user_Info_working_history.all()
                print("user_Info_working_history::" + str(working_history_list))

                student_info = StudentInfo.objects.get(user_info=user_info)
                return render_result(request, "page_main_controller/report_worker_history.html",
                                     {'title_msg': title_msg, 'student_info': student_info,
                                      'working_history_list': working_history_list, 'is_report': True})
            else:
                print(type(object_form.errors), object_form.errors)  # errors类型是ErrorDict，里面是ul，li标签
                message = '系统提示：信息填报内容未完善，请返回重新填报或完善填报信息再提交！'
                return render_result(request, "page_main_controller/message.html",
                                     {'title_msg': title_msg, 'message': message})
        else:
            message = '系统提示：请求方式出现异常，请重试或联系管理员'
            return render_result(request, "page_main_controller/message.html",
                                 {'title_msg': title_msg, 'message': message})
    except Exception as e:
        raise e


def delete_history(request):
    try:
        if request.method == 'POST':
            uid = request.POST.get("uid", None)
            WorkingHistory.objects.filter(id=int(uid)).delete()
            result['data'] = "删除成功"
            return JsonResponse(result, safe=False)
        else:
            pass
    except Exception as e:
        print(str(e))
        result['status'] = False
        result['message'] = '获取数据记录 0'
        result['error'] = str(e)
        return JsonResponse(result, safe=False)


def teacher_info(request):
    """
    获取负责人信息
    """
    query_set = TeacherInfo.objects.all.order_by('-id')
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