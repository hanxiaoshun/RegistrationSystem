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


def apply_chemical(student):
    """
    非化工类的申请表下载专用
    :param student:
    :return:
    """
    try:
        user_info = student.user_info
        system_type = platform.system()
        if 'indows' in system_type:
            tpl = DocxTemplate('D:/PycharmProjects/lelingzdy/baoming/webapp/utils/fujian03.docx')
        else:
            tpl = DocxTemplate('/data/python3_space/lelingzdy/baoming/webapp/utils/fujian03.docx')
        print(user_info.hukou_province.region_name)
        file_root = MEDIA_ROOT + '/' + str(user_info.two_inch_photo.picture_path)
        file_root = file_root.replace("\\", "/")
        id_number = str(user_info.id_number)
        rt_aa = RichText('')
        rt_aa.add(id_number[0], size=14)  # 字体大小
        rt_bb = RichText('')
        rt_bb.add(id_number[1], size=14)  # 字体大小
        rt_cc = RichText('')
        rt_cc.add(id_number[2], size=14)  # 字体大小
        rt_dd = RichText('')
        rt_dd.add(id_number[3], size=14)  # 字体大小
        rt_ee = RichText('')
        rt_ee.add(id_number[4], size=14)  # 字体大小
        rt_ff = RichText('')
        rt_ff.add(id_number[5], size=14)  # 字体大小
        rt_gg = RichText('')
        rt_gg.add(id_number[6], size=14)  # 字体大小
        rt_hh = RichText('')
        rt_hh.add(id_number[7], size=14)  # 字体大小
        rt_ii = RichText('')
        rt_ii.add(id_number[8], size=14)  # 字体大小
        rt_jj = RichText('')
        rt_jj.add(id_number[9], size=14)  # 字体大小
        rt_kk = RichText('')
        rt_kk.add(id_number[10], size=14)  # 字体大小
        rt_ll = RichText('')
        rt_ll.add(id_number[11], size=14)  # 字体大小
        rt_mm = RichText('')
        rt_mm.add(id_number[12], size=14)  # 字体大小
        rt_nn = RichText('')
        rt_nn.add(id_number[13], size=14)  # 字体大小
        rt_oo = RichText('')
        rt_oo.add(id_number[14], size=14)  # 字体大小
        rt_pp = RichText('')
        rt_pp.add(id_number[15], size=14)  # 字体大小
        rt_qq = RichText('')
        rt_qq.add(id_number[16], size=14)  # 字体大小
        rt_rr = RichText('')
        rt_rr.add(id_number[17], size=14)  # 字体大小

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
        if str(former_occupation).__len__() >= 4:
            rt_former_occupation.add(former_occupation, size=14)  # 字体大小
        else:
            rt_former_occupation.add(former_occupation)  # 字体大小
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

        if student.career_life:
            career_life = student.career_life
        else:
            career_life = ''
        # 文化程度
        education_degree = student.user_info.education_degree
        if education_degree:
            education_name = student.user_info.education_degree.education_name
        else:
            education_name = ''
        context = {
            'r_e': user_info.real_name,
            'sa': get_sex(user_info.sex),
            'bir': user_info.birthday,
            'edu': education_name,
            'id_number': user_info.id_number,
            'work_unit': user_info.work_unit,
            'u_n': user_info.unit_nature.unit_nature,
            's_w_d': user_info.start_working_date,
            'cl': career_life,
            'hukou': rt_hukou,
            'email': user_info.email,
            'f_p': user_info.fixed_telephone,
            'unit_address': user_info.unit_address,
            'address': user_info.address,
            'id_addr': rt_id_addr,
            'postal_c': user_info.postal_code,
            # 'p': rt_p_status,
            'nati': user_info.nation_info.nation_name,
            'f_occ': rt_former_occupation,
            'p_level': primary_level,
            'issuance_time': issuance_time,
            'issue_unit': student.issue_unit,
            'o_cer_num': original_certificate_number,
            'dec_of_occ': rt_declaration_of_occupation,
            'id_level': identification_level,
            'work_training': student.work_training,
            'inch_img': InlineImage(tpl, file_root, width=Mm(35), height=Mm(48)),
            'major': student.major,
            'a': rt_aa,
            'b': rt_bb,
            'c': rt_cc,
            'd': rt_dd,
            'e': rt_ee,
            'f': rt_ff,
            'g': rt_gg,
            'h': rt_hh,
            'i': rt_ii,
            'j': rt_jj,
            'k': rt_kk,
            'l': rt_ll,
            'm': rt_mm,
            'n': rt_nn,
            'o': rt_oo,
            'p': rt_pp,
            'q': rt_qq,
            'r': rt_rr
        }
        day_string = str(time.strftime('%Y/%m/%d', time.localtime(time.time())))
        day_files_path = 'report_files/apply_chemical/' + student.declaration_of_occupation + "/" + str(
            student.identification_level) + "/" + day_string
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
            file_manage.file_name = "化工报表-" + declaration_of_occupation
            file_manage.file_uuid = uuid_string
            file_manage.file_path = file_day_files_path
            file_manage.save()
            # 附件1 申请表获取成功，

            return str(file_manage.file_uuid)
        else:
            return None
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
