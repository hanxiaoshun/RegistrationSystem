import os
import platform
import time

import jinja2
import pandas as pd
from docxtpl import DocxTemplate
from pandas import DataFrame
from baoming.settings import MEDIA_URL, MEDIA_ROOT, BASE_DIR
from webapp.controller.common import *
from webapp.models import *
import xlrd
import xlutils.copy
import platform
from webapp.utils.date_encoder import *


def reporter_chemical_not_list(student_infos=None):
    """
    非化学类的
    :return:
    """
    try:
        document_root = os.path.join(BASE_DIR, 'document')
        filepath = document_root + "/fujian04_excel_format.xlsx"

        # system_type = platform.system()
        # if 'indows' in system_type:
        #     filepath = "D:/PycharmProjects/lelingzdy/baoming/webapp/utils/fujian04_excel_format.xlsx"
        # else:
        #     filepath = "/opt/python3_space/lelingzdy/baoming/webapp/utils/fujian04_excel_format.xlsx"
        original_data = pd.read_excel(filepath, encoding='utf-8')
        # rb打开该excel，formatting_info=True表示打开excel时并保存原有的格式
        rb = xlrd.open_workbook(filepath, formatting_info=True)
        # 创建一个可写入的副本
        wb = xlutils.copy.copy(rb)
        if not student_infos:
            student_infos = StudentInfo.objects.filter(confirm_status=1, chemical_worker=2)
        tmp_array = []
        if len(student_infos) > 0:
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
                    original_certificate_number = ""

                    # 文化程度
                education_degree = student.user_info.education_degree
                if education_degree:
                    education_name = student.user_info.education_degree.education_name
                else:
                    education_name = ''
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
                    primary_level = ''
                if student.user_info.start_working_date:
                    start_working_date = date_encoder(student.user_info.start_working_date)
                else:
                    start_working_date = ''

                if student.issuance_time:
                    issuance_time = date_encoder(student.issuance_time)
                else:
                    issuance_time = ''

                tmp_array.append([tmp_num,
                                  student.user_info.real_name,
                                  student.user_info.id_number,
                                  get_sex(student.user_info.sex),
                                  '',
                                  education_name,
                                  student.declaration_of_occupation,
                                  start_working_date,
                                  identification_level,
                                  '',
                                  '',
                                  '',
                                  original_certificate_number,
                                  issuance_time])
            num = 0
            print('len:::' + str(len(original_data)))
            for row in range(0, len(original_data)):
                if row > 3:
                    out_sheet = wb.get_sheet(0)
                    if num < len(tmp_array):
                        set_out_cell(out_sheet, 0, row, tmp_array[num][0])
                        set_out_cell(out_sheet, 1, row, tmp_array[num][1])
                        set_out_cell(out_sheet, 2, row, tmp_array[num][2])
                        set_out_cell(out_sheet, 3, row, tmp_array[num][3])
                        set_out_cell(out_sheet, 4, row, tmp_array[num][4])
                        set_out_cell(out_sheet, 5, row, tmp_array[num][5])
                        set_out_cell(out_sheet, 6, row, tmp_array[num][6])
                        set_out_cell(out_sheet, 7, row, tmp_array[num][7])
                        set_out_cell(out_sheet, 8, row, tmp_array[num][8])
                        set_out_cell(out_sheet, 9, row, tmp_array[num][9])
                        set_out_cell(out_sheet, 10, row, tmp_array[num][10])
                        set_out_cell(out_sheet, 11, row, tmp_array[num][11])
                        set_out_cell(out_sheet, 12, row, tmp_array[num][12])
                        set_out_cell(out_sheet, 13, row, tmp_array[num][13])
                    else:
                        set_out_cell(out_sheet, 0, row, num + 1)
                    num = num + 1

            day_string = str(time.strftime('%Y/%m/%d', time.localtime(time.time())))
            file_root = MEDIA_ROOT + "/files/"
            day_files_path = file_root + 'reporter_chemical_not_list' + "/files/" + day_string
            if os.path.exists(day_files_path):
                pass
            else:
                os.makedirs(day_files_path)
            uuid_string = str(uuid.uuid4())
            file_day_files_path = day_files_path + "/" + uuid_string + ".xlsx"
            wb.save(file_day_files_path)
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


def set_out_cell(out_sheet, col, row, value):
    """ Change cell value without changing formatting. """

    def _getOutCell(out_sheet, colIndex, rowIndex):
        """ HACK: Extract the internal xlwt cell representation. """
        row = out_sheet._Worksheet__rows.get(rowIndex)
        if not row: return None

        cell = row._Row__cells.get(colIndex)
        return cell

    # HACK to retain cell style.
    previousCell = _getOutCell(out_sheet, col, row)
    # END HACK, PART I

    out_sheet.write(row, col, value)

    # HACK, PART II
    if previousCell:
        newCell = _getOutCell(out_sheet, col, row)
        if newCell:
            newCell.xf_idx = previousCell.xf_idx
