# coding:utf-8
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
import pandas as pd
from pandas import DataFrame


def all_student_base_info_list(student_infos):
    # 增加行数据，在第5行新增
    #     # for i in range(10):
    #     #     data.loc[i + 4] = [1, '韩小顺', '男', '152224199101105555', '初级', '否', 33.5, '17099887654', '1999-01-01',
    #     #                        '青峰白羽软件技术工作室',
    #     #                        '韩小顺', '电（高）, 钳（中）']
    try:
        # 生成将要保存的文件路径
        day_string = str(time.strftime('%Y/%m/%d', time.localtime(time.time())))
        day_files_path = 'django/all_student_base_info_list' + "/files/" + day_string
        if os.path.exists(day_files_path):
            pass
        else:
            os.makedirs(day_files_path)
        uuid_string = str(uuid.uuid4())
        file_day_files_path = day_files_path + "/" + uuid_string + ".xlsx"
        # 生成将要获取的data数据的querySet
        if student_infos:
            student_infos_declaration_of_occupation = student_infos.filter(confirm_status=1).order_by(
                'declaration_of_occupation')
            student_infos_real_name = student_infos.filter(confirm_status=1).order_by('user_info')
            student_infos_unit = student_infos.filter(confirm_status=1).order_by('teacher_info')
        else:
            student_infos_declaration_of_occupation = StudentInfo.objects.filter(confirm_status=1).order_by(
                'declaration_of_occupation')
            student_infos_real_name = StudentInfo.objects.filter(confirm_status=1).order_by('user_info')
            student_infos_unit = StudentInfo.objects.filter(confirm_status=1).order_by('teacher_info')

        # 生成data
        create_data_worker = create_data(student_infos_declaration_of_occupation)
        create_data_user = create_data(student_infos_real_name)
        create_data_unit = create_data(student_infos_unit)

        # 保存数据
        with pd.ExcelWriter(file_day_files_path) as writer:  # doctest: +SKIP
            create_data_worker.to_excel(writer, sheet_name='按工种统计', index=False, header=0, na_rep='')
            create_data_user.to_excel(writer, sheet_name='按姓名统计', index=False, header=0, na_rep='')
            create_data_unit.to_excel(writer, sheet_name='按单位统计', index=False, header=0, na_rep='')
        print("系统：：" + file_day_files_path)
        if os.path.exists(file_day_files_path):
            file_manage = FileManage()
            file_manage.file_name = "化工类学员报名表-" + day_string
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


def create_data(student_infos):
    system_type = platform.system()
    # if 'indows' in system_type:
    #     data = pd.read_excel("D:/PycharmProjects/lelingzdy/baoming/webapp/utils/all_info.xlsx",
    #                          sheet_name='按工种统计')
    # else:
    #     data = pd.read_excel("/data/python3_space/lelingzdy/baoming/webapp/utils/all_info.xlsx",
    #                          sheet_name='按工种统计')

    if len(student_infos) > 0:
        tmp_num = 0
        data = pd.DataFrame([['',
                              '',
                              '',
                              '',
                              '',
                              '报名统计表',
                              '',
                              '',
                              '',
                              '',
                              '',
                              ''
                              ], ['序号',
                                  '姓名',
                                  '身份证号码',
                                  '性别',
                                  '拟报工种',
                                  '级别',
                                  '已交费金额',
                                  '欠交费金额',
                                  '电话',
                                  '单位名称',
                                  '负责报名的负责人',
                                  '备注'
                                  ]])
        # # data.loc[0] =
        # data.loc[1] = ['序号',
        #                '姓名',
        #                '身份证号码',
        #                '性别',
        #                '拟报工种',
        #                '级别',
        #                '已交费金额',
        #                '欠交费金额',
        #                '电话',
        #                '单位名称',
        #                '负责报名的负责人',
        #                '备注'
        #                ]
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
            # data.loc[i + 4] = [1, '韩小顺', '男', '152224199101105555', '初级', '否', 33.5, '17099887654', '1999-01-01',
            #                    '青峰白羽软件技术工作室',
            #                    '韩小顺', '电（高）, 钳（中）']
            tmp_num = tmp_num + 1
            data.loc[tmp_num + 2] = [tmp_num,
                                     student.user_info.real_name,
                                     student.user_info.id_number,
                                     get_sex(student.user_info.sex),
                                     student.declaration_of_occupation,
                                     identification_level,
                                     student.payment_amount,
                                     student.unpaid_amount,
                                     student.user_info.contact_number,
                                     student.user_info.work_unit,
                                     student.teacher_info.user_info.real_name,
                                     student.explain
                                     ]
        return data
    else:
        pass


def create_data_user_(student_infos, file_day_files_path):
    system_type = platform.system()
    if 'indows' in system_type:
        data = pd.read_excel("D:/PycharmProjects/lelingzdy/baoming/webapp/utils/all_info.xlsx",
                             sheet_name='按姓名统计')

    else:
        data = pd.read_excel("/data/python3_space/lelingzdy/baoming/webapp/utils/all_info.xlsx",
                             sheet_name='按姓名统计')
    if len(student_infos) > 0:
        tmp_num = 0
        data.loc[0] = ['',
                       '',
                       '',
                       '',
                       '',
                       '报名统计表',
                       '',
                       '',
                       '',
                       '',
                       '',
                       ''
                       ]
        data.loc[1] = ['序号',
                       '姓名',
                       '身份证号码',
                       '性别',
                       '拟报工种',
                       '级别',
                       '已交费金额',
                       '欠交费金额',
                       '电话',
                       '单位名称',
                       '负责报名的负责人',
                       '备注'
                       ]
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
            # data.loc[i + 4] = [1, '韩小顺', '男', '152224199101105555', '初级', '否', 33.5, '17099887654', '1999-01-01',
            #                    '青峰白羽软件技术工作室',
            #                    '韩小顺', '电（高）, 钳（中）']

            # 缴费金额
            payment_amount = student.payment_amount
            if payment_amount == 0:
                payment_amount_str = ''
            else:
                payment_amount_str = str(payment_amount)

                # 欠缴费金额
            unpaid_amount = student.unpaid_amount
            if unpaid_amount == 0:
                unpaid_amount_str = ''
            else:
                unpaid_amount_str = str(unpaid_amount)

            tmp_num = tmp_num + 1
            data.loc[tmp_num + 2] = [tmp_num,
                                     student.user_info.real_name,
                                     get_sex(student.user_info.sex),
                                     student.user_info.id_number,
                                     student.declaration_of_occupation,
                                     identification_level,
                                     payment_amount_str,
                                     unpaid_amount_str,
                                     student.user_info.contact_number,
                                     student.user_info.work_unit,
                                     student.teacher_info.user_info.real_name,
                                     student.explain
                                     ]
        writer = pd.ExcelWriter(file_day_files_path)
        DataFrame(data).to_excel(writer, sheet_name='按姓名统计', index=False, header=0, na_rep='')
        writer.save()
        writer.close()
    else:
        pass


def create_data_unit_(student_infos, file_day_files_path):
    system_type = platform.system()
    if 'indows' in system_type:
        data = pd.read_excel("D:/PycharmProjects/lelingzdy/baoming/webapp/utils/all_info.xlsx",
                             sheet_name='按单位统计')
    else:
        data = pd.read_excel("/data/python3_space/lelingzdy/baoming/webapp/utils/all_info.xlsx",
                             sheet_name='按单位统计')
    if len(student_infos) > 0:
        tmp_num = 0
        data.loc[0] = ['',
                       '',
                       '',
                       '',
                       '',
                       '报名统计表',
                       '',
                       '',
                       '',
                       '',
                       '',
                       ''
                       ]
        data.loc[1] = ['序号',
                       '姓名',
                       '身份证号码',
                       '性别',
                       '拟报工种',
                       '级别',
                       '已交费金额',
                       '欠交费金额',
                       '电话',
                       '单位名称',
                       '负责报名的负责人',
                       '备注'
                       ]
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
            # data.loc[i + 4] = [1, '韩小顺', '男', '152224199101105555', '初级', '否', 33.5, '17099887654', '1999-01-01',
            #                    '青峰白羽软件技术工作室',
            #                    '韩小顺', '电（高）, 钳（中）']
            tmp_num = tmp_num + 1
            data.loc[tmp_num + 2] = [tmp_num,
                                     student.user_info.real_name,
                                     get_sex(student.user_info.sex),
                                     student.user_info.id_number,
                                     student.declaration_of_occupation,
                                     identification_level,
                                     student.payment_amount,
                                     student.unpaid_amount,
                                     student.user_info.contact_number,
                                     student.user_info.work_unit,
                                     student.teacher_info.user_info.real_name,
                                     student.explain
                                     ]
        writer = pd.ExcelWriter(file_day_files_path)
        DataFrame(data).to_excel(writer, sheet_name='按单位统计', index=False, header=0, na_rep='')
        writer.save()
        writer.close()
    else:
        pass
