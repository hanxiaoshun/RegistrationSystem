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


def apply_not(student):
    """
    化工类的申请表下载专用
    :param student:
    :return:
    """
    try:
        user_info = student.user_info
        print(user_info.real_name)

        document_root = os.path.join(BASE_DIR, 'document')
        tpl = DocxTemplate(document_root + '/fujian01.docx')
        tpl2 = DocxTemplate(document_root + '/fujian02.docx')
        # system_type = platform.system()
        # if 'indows' in system_type:
        #     tpl = DocxTemplate('D:/PycharmProjects/lelingzdy/baoming/webapp/utils/fujian01.docx')
        # else:
        #     tpl = DocxTemplate('/opt/python3_space/lelingzdy/baoming/webapp/utils/fujian01.docx')
        #
        # if 'indows' in system_type:
        #     tpl2 = DocxTemplate('D:/PycharmProjects/lelingzdy/baoming/webapp/utils/fujian02.docx')
        # else:
        #     tpl2 = DocxTemplate('/opt/python3_space/lelingzdy/baoming/webapp/utils/fujian02.docx')
        #
        # print(user_info.hukou_province.region_name)
        file_root = MEDIA_ROOT + '/' + str(user_info.two_inch_photo.picture_path)
        file_root = file_root.replace("\\", "/")

        # 户口所在地
        rt_hukou = RichText('')
        hukou = user_info.hukou_province.region_name + user_info.hukou_city.region_name + user_info.hukou_county.region_name
        if str(hukou).__len__() > 8:
            rt_hukou.add(hukou, size=10)  # 字体大小
        elif str(hukou).__len__() > 13:
            rt_hukou.add(hukou, size=8)  # 字体大小
        else:
            rt_hukou.add(hukou, size=14)  # 字体大小

        # 身份证住址
        rt_id_addr = RichText('')
        id_card_address = user_info.id_card_address
        if str(id_card_address).__len__() > 8:
            rt_id_addr.add(id_card_address, size=10)  # 字体大小
        elif str(id_card_address).__len__() > 13:
            rt_id_addr.add(id_card_address, size=8)  # 字体大小
        elif str(id_card_address).__len__() > 16:
            rt_id_addr.add(id_card_address, size=6)  # 字体大小
        else:
            rt_id_addr.add(id_card_address, size=14)  # 字体大小

        # 政治面貌
        rt_p_status = RichText('')
        political_status_value = political_status[str(user_info.political_status)]
        # rt_p_status.add(political_status_value, size=12)  # 字体大小
        if str(political_status_value).__len__() >= 4:
            rt_p_status.add(political_status_value, size=14)  # 字体大小
        else:
            rt_p_status.add(political_status_value)  # 字体大小

        # 原职业工种
        rt_former_occupation = RichText('')
        former_occupation = student.former_occupation
        if former_occupation:
            if str(former_occupation).__len__() >= 4:
                rt_former_occupation.add(former_occupation, size=14)  # 字体大小
            else:
                rt_former_occupation.add(former_occupation)  # 字体大小
        else:
            rt_former_occupation.add('')
        # 申报职业
        rt_declaration_of_occupation = RichText('')
        declaration_of_occupation = student.declaration_of_occupation
        if str(declaration_of_occupation).__len__() >= 4:
            rt_declaration_of_occupation.add(declaration_of_occupation, size=14)  # 字体大小
        else:
            rt_declaration_of_occupation.add(declaration_of_occupation)  # 字体大小

        # 原级别
        primary_level = str(student.primary_level)
        if len(student.primary_level) > 0:
            primary_level = worker_level[str(student.primary_level)]
        else:
            primary_level = ''

        # 申报级别
        identification_level = str(student.identification_level)
        if len(identification_level) > 0:
            identification_level = worker_level[str(student.identification_level)]
        else:
            identification_level = ''

        # 文化程度
        education_degree = student.user_info.education_degree
        if education_degree:
            education_name = student.user_info.education_degree.education_name
        else:
            education_name = ''

        # career_life = student.career_life
        # original_certificate_worker_year = student.original_certificate_worker_year
        # print("career_life::" + str(career_life))
        # print("original_certificate_worker_year::" + str(original_certificate_worker_year))
        # 
        # working_year = None
        # if not career_life:
        #     if original_certificate_worker_year:
        #         working_year = original_certificate_worker_year
        # else:
        #     working_year = career_life
        # 
        # if working_year is None:
        #     working_year = ''
        
        # 修改的内容
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

        # if not career_life:
        #     if original_certificate_worker_year:
        #         working_year = original_certificate_worker_year
        #     else:
        #         if apprentice_year > 0:
        #             working_year = str(apprentice_year)
        #         else:
        #             if apprentice_month > 0:
        #                 working_year = str(apprentice_month) + "月"
        #             else:
        #                 working_year = ''
        # else:
        #     working_year = career_life
        #
        # if student.identification_level == "3":
        #     working_year = ''
        #
        # if student.identification_level == "4":
        #     if original_certificate_worker_year > 0:
        #         working_year = ''
        #
        # if working_year is None:
        #     working_year = ''





        # 修改的内容
        print('working_year::' + str(working_year))

        print("user_info.real_name:::" + user_info.real_name)
        context = {
            'r_e': user_info.real_name,
            'sa': get_sex(user_info.sex),
            'bir': user_info.birthday,
            'edu': education_name,
            'id_number': user_info.id_number,
            'work_unit': user_info.work_unit,
            'u_n': user_info.unit_nature.unit_nature,
            's_w_d': user_info.start_working_date,
            'cl': working_year,
            'hukou': rt_hukou,
            'email': user_info.email,
            'f_p': user_info.fixed_telephone,
            'unit_address': user_info.unit_address,
            'address': user_info.address,
            'id_addr': rt_id_addr,
            'postal_c': user_info.postal_code,
            'p': rt_p_status,
            'nation': user_info.nation_info.nation_name,
            'f_occ': rt_former_occupation,
            'p_level': primary_level,
            'o_cer_num': student.original_certificate_number,
            'main_occupation': student.user_info.main_occupation,
            'dec_of_occ': rt_declaration_of_occupation,
            'id_level': identification_level,
            'work_training': student.work_training,
            'inch_img': InlineImage(tpl, file_root, width=Mm(35), height=Mm(48))
        }
        day_string = str(time.strftime('%Y/%m/%d', time.localtime(time.time())))
        # day_files_path = 'django/apply_not_chemical' + "/files/" + day_string
        file_root = MEDIA_ROOT + "/files/"
        day_files_path = file_root + 'report_files/apply_chemical_not/' + student.declaration_of_occupation + "/" + str(
            student.identification_level) + "/" + day_string
        if os.path.exists(day_files_path):
            pass
        else:
            os.makedirs(day_files_path)

        file_manage = FileManage()
        jinja_env = jinja2.Environment(autoescape=True)
        # 将附件 1 保存到文件系统
        uuid_string = str(uuid.uuid4())
        file_day_files_path = day_files_path + "/" + uuid_string + ".docx"
        tpl.render(context, jinja_env)
        tpl.save(file_day_files_path)
        if os.path.exists(file_day_files_path):
            file_manage.file_name = "非化工类报表-" + declaration_of_occupation
            file_manage.file_uuid = uuid_string
            file_manage.file_path = file_day_files_path
            file_manage.save()
        else:
            pass

        # 将附件 2 保存到文件系统
        file_manage2 = FileManage()
        uuid_string2 = str(uuid.uuid4())
        file_day_files_path2 = day_files_path + "/" + uuid_string2 + ".docx"
        tpl2.render(context, jinja_env)
        tpl2.save(file_day_files_path2)
        if os.path.exists(file_day_files_path2):
            file_manage2.file_name = "工作年限证明-" + declaration_of_occupation
            file_manage2.file_uuid = uuid_string2
            file_manage2.file_path = file_day_files_path2
            file_manage2.save()
        else:
            pass
        return str(uuid_string), str(uuid_string2)
    except Exception as e:
        print(e)
        raise e
        # return None


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
