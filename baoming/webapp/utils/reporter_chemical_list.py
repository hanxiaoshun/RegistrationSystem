# coding:utf-8
from docxtpl import DocxTemplate, InlineImage, RichText
from docx.shared import Mm, Inches, Pt
import jinja2
from webapp.models import *
from baoming.settings import MEDIA_URL, MEDIA_ROOT, BASE_DIR
import datetime
import os
import time
from webapp.controller.common import *
import platform

import pandas as pd
from pandas import DataFrame


def reporter_chemical_list(student_infos=None):
    """
    非化学类的
    :return:
    """
    try:
        document_root = os.path.join(BASE_DIR, 'document')
        data = pd.read_excel(document_root + "/huagonginfo.xlsx",
                             sheet_name='Sheet1')
        # system_type = platform.system()
        # if 'indows' in system_type:
        #     data = pd.read_excel("D:/PycharmProjects/lelingzdy/baoming/webapp/utils/huagonginfo.xlsx",
        #                          sheet_name='Sheet1')
        # else:
        #     data = pd.read_excel("/opt/python3_space/lelingzdy/baoming/webapp/utils/huagonginfo.xlsx",
        #                          sheet_name='Sheet1')

        # 增加行数据，在第5行新增
        # data.loc[7] = [1, '初级', '电工', '152224199101105555', '韩小顺', '男', '青峰白羽', '1991-01-10', '1999-01-01', 2,
        #                '3333333333',
        #                '本科', '18811663456', '备注的内容']
        if not student_infos:
            # 如果 student_infos 是 None 重新获取全部的student_infos
            student_infos = StudentInfo.objects.filter(confirm_status=1, chemical_worker=1)

        if len(student_infos) > 0:
            tmp_list = {}
            tmp_num = 0
            for student in student_infos:
                # 工作年限 -- start
                career_life = student.career_life
                original_certificate_worker_year = student.original_certificate_worker_year
                apprentice_year = student.apprentice_year
                apprentice_month = student.apprentice_month

                # if not career_life:
                #     if original_certificate_worker_year:
                #         working_year = original_certificate_worker_year
                #     else:
                #         if apprentice_year:
                #             if apprentice_year > 0:
                #                 working_year = str(apprentice_year)
                #             else:
                #                 if apprentice_month:
                #                     if apprentice_month > 0:
                #                         working_year = str(apprentice_month) + "月"
                #                     else:
                #                         working_year = ''
                #         else:
                #             working_year = ''
                # else:
                #     working_year = career_life

                flag_working_time = False
                if student.identification_level == "3":
                    working_year = ''
                elif student.identification_level == "4":
                    if original_certificate_worker_year:
                        if original_certificate_worker_year > 0:
                            working_year = ''
                        else:
                            flag_working_time = True
                    else:
                        flag_working_time = True
                else:
                    flag_working_time = True

                if flag_working_time:
                    if not career_life:
                        if apprentice_year:
                            if apprentice_year > 0:
                                working_year = str(apprentice_year)
                            else:
                                if apprentice_month:
                                    if apprentice_month > 0:
                                        working_year = str(apprentice_month) + "月"
                                    else:
                                        working_year = ''
                        else:
                            working_year = ''
                    else:
                        working_year = career_life
                else:
                    pass

                # if working_year is None:
                #     working_year = ''

                # 工作年限 -- end

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
                    original_certificate_number = ""

                if student.issuance_time:
                    issuance_time = student.issuance_time
                else:
                    issuance_time = ''

                    # 文化程度
                education_degree = student.user_info.education_degree
                if education_degree:
                    education_name = student.user_info.education_degree.education_name
                else:
                    education_name = ''
                tmp_num = tmp_num + 1
                data.loc[tmp_num + 1] = [tmp_num, identification_level,
                                         student.declaration_of_occupation,
                                         student.user_info.id_number,
                                         student.user_info.real_name,
                                         get_sex(student.user_info.sex),
                                         student.user_info.work_unit,
                                         student.user_info.birthday,
                                         student.user_info.start_working_date,
                                         working_year,
                                         original_certificate_number,
                                         education_name, student.user_info.contact_number, student.explain]

            day_string = str(time.strftime('%Y/%m/%d', time.localtime(time.time())))
            file_root = MEDIA_ROOT + "/files/"
            day_files_path = file_root + 'reporter_chemical_list' + "/files/" + day_string
            if os.path.exists(day_files_path):
                pass
            else:
                os.makedirs(day_files_path)
            uuid_string = str(uuid.uuid4())
            file_day_files_path = day_files_path + "/" + uuid_string + ".xlsx"
            # 保存数据
            DataFrame(data).to_excel(file_day_files_path, sheet_name='Sheet1', index=False, header=True)
            if os.path.exists(file_day_files_path):
                file_manage = FileManage()
                file_manage.file_name = "化工类学员报名表-" + day_string
                file_manage.file_uuid = uuid_string
                file_manage.file_path = file_day_files_path
                file_manage.save()
                # 附件1 生成非化工类学员化名册成功，
                return str(file_manage.file_uuid)
            else:
                return None
        else:
            return None
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
