from docxtpl import DocxTemplate, InlineImage, RichText
from docx.shared import Mm, Inches, Pt
import jinja2
from webapp.models import *
from baoming.settings import MEDIA_URL, MEDIA_ROOT
import datetime
import os
import time
from webapp.controller.common import *
import platform


def reporter_chemical_not_list():
    """
    非化学类的
    :return:
    """
    try:
        system_type = platform.system()
        if 'indows' in system_type:
            tpl = DocxTemplate('D:/PycharmProjects/lelingzdy/baoming/webapp/utils/fujian04.docx')
        else:
            tpl = DocxTemplate('/data/python3_space/lelingzdy/baoming/webapp/utils/fujian04.docx')

        student_infos = StudentInfo.objects.filter(confirm_status=1, chemical_worker=2)
        if len(student_infos) > 0:
            tmp_list = []
            tmp_num = 0
            for student in student_infos:
                identification_level = str(student.identification_level)
                if len(identification_level) > 0:
                    identification_level = worker_level[str(student.identification_level)]
                else:
                    identification_level = ''
                    # 原证书编号
                original_certificate_number = student.original_certificate_number
                if original_certificate_number:
                    pass
                else:
                    original_certificate_number = "无"

                if student.issuance_time:
                    issuance_time = student.issuance_time
                else:
                    issuance_time = ''
                tmp_num = tmp_num + 1
                tmp_dict = {'index': str(tmp_num),
                            'r_e': student.user_info.real_name,
                            'id_number': student.user_info.id_number,
                            'sa': get_sex(student.user_info.sex),
                            'school': student.user_info.middle_school,
                            'f_occ': student.declaration_of_occupation,
                            's_w_d': student.user_info.start_working_date,
                            'id_level': identification_level,
                            'jsll': '',
                            'sjcz': '',
                            'o_cer_num': original_certificate_number,
                            'issuance_time': issuance_time}
                tmp_list.append(tmp_dict)

            context = {'tbl_contents': tmp_list}
        # context = {
        #     'tbl_contents': [
        #         {'index': '1', 'r_e': '韩小顺', 'id_number': '152224199101106515', 'sa': '男', 'school': '', 'f_occ': '电工',
        #          's_w_d': '2018-09-01', 'id_level': '初级', 'jsll': '', 'sjcz': '', 'o_cer_num': '213131312331',
        #          'issuance_time': '2019-08-07'},
        #     ]
        # }

            day_string = str(time.strftime('%Y/%m/%d', time.localtime(time.time())))
            day_files_path = 'django/reporter_chemical_not_list' + "/files/" + day_string
            if os.path.exists(day_files_path):
                pass
            else:
                os.makedirs(day_files_path)
            uuid_string = str(uuid.uuid4())
            file_day_files_path = day_files_path + "/" + uuid_string + ".docx"
            jinja_env = jinja2.Environment(autoescape=True)
            tpl.render(context, jinja_env)
            tpl.save(file_day_files_path)
            if os.path.exists(file_day_files_path):
                file_manage = FileManage()
                file_manage.file_name = "非化工类学员报名表-" + day_string
                file_manage.file_uuid = uuid_string
                file_manage.file_path = file_day_files_path
                file_manage.save()
                # 附件1 生成非化工类学员化名册成功，
                return str(file_manage.file_uuid)
    except Exception as e:
        print(e)
        raise e


def get_sex(value):
    """
    性别过滤器
    :param value:
    :return:
    """
    return_value = ''
    if value == 'MALE':
        return_value = '男'
    if value == 'FEMALE':
        return_value = '女'
    if value == 'OTHER':
        return_value = '未填写'
    return return_value
