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

#生成一个新文件

def electronic_communication(student_infos):
    # 增加行数据，在第5行新增
    #     # for i in range(10):
    #     #     data.loc[i + 4] = [1, '韩小顺', '男', '152224199101105555', '初级', '否', 33.5, '17099887654', '1999-01-01',
    #     #                        '青峰白羽软件技术工作室',
    #     #                        '韩小顺', '电（高）, 钳（中）']
    try:
        # 生成将要保存的文件路径
        day_string = str(time.strftime('%Y/%m/%d', time.localtime(time.time())))
        file_root = MEDIA_ROOT + "/files/"
        day_files_path = file_root + 'electronic_communication' + "/files/" + day_string
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
        # create_data_user = create_data(student_infos_real_name)
        # create_data_unit = create_data(student_infos_unit)

        # 保存数据
        with pd.ExcelWriter(file_day_files_path) as writer:  # doctest: +SKIP
            create_data_worker.to_excel(writer, sheet_name='Sheet1', index=False, header=0, na_rep='')
            # create_data_user.to_excel(writer, sheet_name='按姓名统计', index=False, header=0, na_rep='')
            # create_data_unit.to_excel(writer, sheet_name='按单位统计', index=False, header=0, na_rep='')
        print("系统：：" + file_day_files_path)
        if os.path.exists(file_day_files_path):
            file_manage = FileManage()
            file_manage.file_name = "电子通信类导入模板-" + day_string
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
    # 职业(工种)	级别	身份类型		中文名	英文名	性别	
    # 出生日期	工作单位	从事职业	民族	本工种职业年限	
    # 文化程度	参加工作日期	考生来源	来源省份	来源地区	
    # 现役军人	下岗人员	失业人员	残疾人员	农民工	两劳人员	
    # 其他	在校学生	联系电话	手机	身份地址	常住地址	
    # 邮政编码	政治面貌	报名点	鉴定科目	鉴定类型	原证书号	
    # 申报条件	报名备注	补贴类型	补贴证件类型	补贴证件号码	预报考点

    if len(student_infos) > 0:
        tmp_num = 0
        data = pd.DataFrame([['职业(工种)',
                              '级别',
                              '身份类型',
                              '中文名',
                              '英文名',
                              '性别',
                              '出生日期',
                              '工作单位',
                              '从事职业',
                              '民族',
                              '本工种职业年限',
                              '文化程度',
                              '参加工作日期',
                              '考生来源',
                              '来源省份',
                              '来源地区',
                              '现役军人',
                              '下岗人员',
                              '失业人员',
                              '残疾人员',
                              '农民工',
                              '两劳人员',
                              '其他',
                              '在校学生',
                              '联系电话',
                              '手机',
                              '身份地址',
                              '常住地址',
                              '邮政编码',
                              '政治面貌',
                              '报名点',
                              '鉴定科目',
                              '鉴定类型',
                              '原证书号',
                              '申报条件',
                              '报名备注',
                              '补贴类型',
                              '补贴证件类型',
                              '补贴证件号码',
                              '预报考点']])
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
            payment_amount = student.payment_amount
            if payment_amount == "0":
                payment_amount = ""
            elif payment_amount == 0:
                payment_amount = ""
            else:
                pass
            unpaid_amount = student.unpaid_amount
            if unpaid_amount == "0":
                unpaid_amount = ""
            elif unpaid_amount == 0:
                unpaid_amount = ""
            else:
                pass
            print(payment_amount)

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
            tmp_num = tmp_num + 1
            data.loc[tmp_num + 2] = [student.declaration_of_occupation,#职业工种
                                     identification_level,#级别
                                     '',#身份类型
                                     student.user_info.real_name,#中文名
                                     '',#英文名
                                     get_sex(student.user_info.sex),#性别
                                     student.user_info.birthday,#生日
                                     student.user_info.work_unit,#工作单位
                                     '',#从事职业
                                     student.user_info.nation_info.nation_name,#民族
                                     working_year,#工作年限
                                     education_name,#文化程度
                                     student.user_info.start_working_date,#参加工作日期
                                     '',#考生来源
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
                                     rt_id_addr,#身份地址
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
                                     ]
        return data
    else:
        pass
