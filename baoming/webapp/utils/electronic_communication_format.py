import os
import platform
import time
from docxtpl import DocxTemplate, InlineImage, RichText
from docx.shared import Mm, Inches, Pt
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


def electronic_communication_format(student_infos=None, skill_main_class_name=None, skill_main_class_code=None):
    """
    电子通信类
    :return:
    """
    try:
        document_root = os.path.join(BASE_DIR, 'document')
        filepath = document_root + "/electronic_communication_format.xlsx"

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
            skill_main_classies = ReportSkillMainClass.objects.filter(skill_main_class_name__icontains='电子').\
                filter(skill_main_class_name__icontains='通信').values('id')
            if len(skill_main_classies) > 0:
                print(skill_main_classies[0])
                print(skill_main_classies[0]['id'])
                student_infos = StudentInfo.objects.filter(confirm_status=1, skill_main_class=skill_main_classies[0]['id'])
                # report_skills = ReportSkill.objects.filter(skill_main_class=skill_main_classies[0]).values('skill_id') 
                # if len(report_skills) > 0:
                #     report_conditions = ReportCondition.objects.filter(condition_for_skill__in=report_skills).values('condition_id')
                #     student_infos = StudentInfo.objects.filter(confirm_status=1, condition_selected__in=report_conditions)
                    # equipments = Equipment.objects.filter(rack__in = skill_main_classies)  
                    # student_infos = StudentInfo.objects.filter(confirm_status=1, chemical_worker=2)
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
                career_life = student.career_life
                original_certificate_worker_year = student.original_certificate_worker_year
                apprentice_year = student.apprentice_year
                apprentice_month = student.apprentice_month

                flag_working_time = False
                if student.identification_level == "3":
                    working_year = ''
                elif student.identification_level == "4":
                    if original_certificate_worker_year:
                        if original_certificate_worker_year > 0:
                            working_year = ''
                            flag_working_time = True
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
                
                # 文化程度
                education_degree = student.user_info.education_degree
                if education_degree:
                    education_name = student.user_info.education_degree.education_name
                else:
                    education_name = ''
                # 身份证住址
                rt_id_addr = RichText('')
                id_card_address = student.user_info.id_card_address
                if str(id_card_address).__len__() > 8:
                    rt_id_addr.add(id_card_address, size=10)  # 字体大小
                elif str(id_card_address).__len__() > 13:
                    rt_id_addr.add(id_card_address, size=8)  # 字体大小
                elif str(id_card_address).__len__() > 16:
                    rt_id_addr.add(id_card_address, size=6)  # 字体大小
                else:
                    rt_id_addr.add(id_card_address, size=14)  # 字体大小
                tmp_array.append([student.declaration_of_occupation,#职业工种
                                     identification_level,#级别
                                     '',#身份类型
                                     '',#证件号码
                                     student.user_info.real_name,#中文名
                                     '',#英文名
                                     get_sex(student.user_info.sex),#性别
                                     student.user_info.birthday,#生日
                                     student.user_info.work_unit,#工作单位
                                     '',#从事职业
                                     student.user_info.nation_info.nation_name,#民族
                                     str(working_year)+'年',#工作年限
                                     education_name,#文化程度
                                     student.user_info.start_working_date,#参加工作日期
                                     '',#考生来源
                                     '',#来源省份
                                     '',#来源地区
                                     '',#现役军人
                                     '',#下岗人员
                                     '',#失业人员
                                     '',#残疾人员
                                     '',#农民工
                                     '',#两劳人员
                                     '',#其他
                                     '',#在校学生
                                     student.user_info.contact_number,#联系电话
                                     student.user_info.fixed_telephone,#手机
                                     student.user_info.id_card_address,#身份地址
                                     student.user_info.address,#常驻地址
                                     '',#邮政编码
                                     '',#政治面貌
                                     '',#报名点
                                     student.declaration_of_occupation,#鉴定科目
                                     '',#鉴定类型
                                     student.original_certificate_number,#原证书号
                                     '',#申报条件
                                     student.explain,#报名备注
                                     '',#补贴类型
                                     '',#补贴证件类型
                                     '',#补贴证件号码
                                     ''#预报考点
                                     ])
            num = 0
            if len(original_data) == 0:
                row_data = len(tmp_array)
            else:
                row_data = len(original_data)
            for row in range(0, row_data):
                    print(row)
                    print('第几行.....')
                    # if row > 0:
                    out_sheet = wb.get_sheet(0)
                    row = row + 1
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
                        set_out_cell(out_sheet, 14, row, tmp_array[num][14])
                        set_out_cell(out_sheet, 15, row, tmp_array[num][15])
                        set_out_cell(out_sheet, 16, row, tmp_array[num][16])
                        set_out_cell(out_sheet, 17, row, tmp_array[num][17])
                        set_out_cell(out_sheet, 18, row, tmp_array[num][18])
                        set_out_cell(out_sheet, 19, row, tmp_array[num][19])
                        set_out_cell(out_sheet, 20, row, tmp_array[num][20])
                        set_out_cell(out_sheet, 21, row, tmp_array[num][21])
                        set_out_cell(out_sheet, 22, row, tmp_array[num][22])
                        set_out_cell(out_sheet, 23, row, tmp_array[num][23])
                        set_out_cell(out_sheet, 24, row, tmp_array[num][24])
                        set_out_cell(out_sheet, 25, row, tmp_array[num][25])
                        set_out_cell(out_sheet, 26, row, tmp_array[num][26])
                        set_out_cell(out_sheet, 27, row, tmp_array[num][27])
                        set_out_cell(out_sheet, 28, row, tmp_array[num][28])
                        set_out_cell(out_sheet, 29, row, tmp_array[num][29])
                        set_out_cell(out_sheet, 30, row, tmp_array[num][30])
                        set_out_cell(out_sheet, 31, row, tmp_array[num][31])
                        set_out_cell(out_sheet, 32, row, tmp_array[num][32])
                        set_out_cell(out_sheet, 33, row, tmp_array[num][33])
                        set_out_cell(out_sheet, 34, row, tmp_array[num][34])
                        set_out_cell(out_sheet, 35, row, tmp_array[num][35])
                        set_out_cell(out_sheet, 36, row, tmp_array[num][36])
                        set_out_cell(out_sheet, 37, row, tmp_array[num][37])
                        set_out_cell(out_sheet, 38, row, tmp_array[num][38])
                        set_out_cell(out_sheet, 39, row, tmp_array[num][39])
                    else:
                        set_out_cell(out_sheet, 0, row, num + 1)
                    num = num + 1

            day_string = str(time.strftime('%Y/%m/%d', time.localtime(time.time())))
            file_root = MEDIA_ROOT + "/files/"
            day_files_path = file_root + 'electronic_communication' + "/files/" + day_string
            if os.path.exists(day_files_path):
                pass
            else:
                os.makedirs(day_files_path)
            uuid_string = str(uuid.uuid4())
            file_day_files_path = day_files_path + "/" + uuid_string + ".xlsx"
            wb.save(file_day_files_path)            # 保存数据
            print("系统：：" + file_day_files_path)

            if os.path.exists(file_day_files_path):
                file_manage = FileManage()
                file_manage.file_name = "电子通信模板-" + day_string
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
    """�Ա������.

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
    print(type(value))
    print(f'{out_sheet},{col},{row},{value}')
    """Change cell value without changing formatting."""

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
