import os
import platform
import time

import jinja2
import pandas as pd
from docxtpl import DocxTemplate
from pandas import DataFrame

from webapp.controller.common import *
from webapp.models import *


def reporter_chemical_not_list():
    """
    非化学类的
    :return:
    """
    try:
        system_type = platform.system()
        if 'indows' in system_type:
            data = pd.read_excel("D:/PycharmProjects/lelingzdy/baoming/webapp/utils/fujian04_excel.xlsx",
                                 sheet_name='培训人员花名册')
        else:
            data = pd.read_excel("/data/python3_space/lelingzdy/baoming/webapp/utils/fujian04_excel.xlsx",
                                 sheet_name='培训人员花名册')

        # 增加行数据，在第5行新增
        # data.loc[7] = [1, '初级', '电工', '152224199101105555', '韩小顺', '男', '青峰白羽', '1991-01-10', '1999-01-01', 2,
        #                '3333333333',
        #                '本科', '18811663456', '备注的内容']

        student_infos = StudentInfo.objects.filter(confirm_status=1, chemical_worker=2)
        if len(student_infos) > 0:
            tmp_list = {}
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

                    # 文化程度
                education_degree = student.user_info.education_degree
                if education_degree:
                    education_name = student.user_info.education_degree.education_name
                else:
                    education_name = '无'
                tmp_num = tmp_num + 1
                # tmp_dict = {'index': str(tmp_num),
                #             'r_e': student.user_info.real_name,
                #             'id_number': student.user_info.id_number,
                #             'sa': get_sex(student.user_info.sex),
                #             'school': student.user_info.middle_school,
                #             'f_occ': student.declaration_of_occupation,
                #             's_w_d': student.user_info.start_working_date,
                #             'id_level': identification_level,
                #             'jsll': '',
                #             'sjcz': '',
                #             'o_cer_num': original_certificate_number,
                #             'issuance_time': issuance_time}
                # tmp_list.append(tmp_dict)
                # 原级别
                primary_level = str(student.primary_level)
                if len(student.primary_level) > 0:
                    primary_level = worker_level[str(student.primary_level)]
                else:
                    primary_level = '无'
                cols = data.loc[tmp_num]
                print("cols:::" + cols)
                data.loc[tmp_num + 4] = [tmp_num,
                                         student.user_info.real_name,
                                         student.user_info.id_number,
                                         get_sex(student.user_info.sex),
                                         '',
                                         education_name,
                                         student.declaration_of_occupation,
                                         student.user_info.start_working_date,
                                         identification_level,
                                         '',
                                         '',
                                         '',
                                         original_certificate_number,
                                         issuance_time]

            day_string = str(time.strftime('%Y/%m/%d', time.localtime(time.time())))
            day_files_path = 'django/reporter_chemical_not_list' + "/files/" + day_string
            if os.path.exists(day_files_path):
                pass
            else:
                os.makedirs(day_files_path)
            uuid_string = str(uuid.uuid4())
            file_day_files_path = day_files_path + "/" + uuid_string + ".xlsx"
            # 保存数据
            # df1 = pd.DataFrame([['a', 'b'], ['c', 'd']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
            DataFrame(data).to_excel(file_day_files_path, sheet_name='培训人员花名册', index=False, na_rep='', header=0)
            # data.loc[0] = ['德州市申请职业技能鉴定（技术等级鉴定）颁发职业资格证书花名册',
            #                          '',
            #                          '',
            #                          '',
            #                          '',
            #                          '',
            #                          '',
            #                          '',
            #                          '',
            #                          '',
            #                          '',
            #                          '',
            #                          '',
            #                          '']
            # DataFrame(data).to_excel(file_day_files_path, sheet_name='培训人员花名册', index=False, na_rep='')
            # DataFrame(data).to_excel(file_day_files_path, sheet_name='培训人员花名册', index=False, na_rep='')
            # DataFrame(data).to_excel(file_day_files_path, sheet_name='培训人员花名册', index=False, na_rep='')
            if os.path.exists(file_day_files_path):
                file_manage = FileManage()
                file_manage.file_name = "非化工类学员报名表-" + day_string
                file_manage.file_uuid = uuid_string
                file_manage.file_path = file_day_files_path
                file_manage.save()
                # 附件1 生成非化工类学员化名册成功，
                return str(file_manage.file_uuid)
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
