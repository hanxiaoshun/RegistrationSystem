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

tpl = DocxTemplate('fujian04.docx')

rt_hukou = RichText('')
rt_hukou.add('内蒙古突泉县', size=12)  # 字体大小
rt_id_number = RichText('')
rt_id_number.add('内蒙古突泉县', size=12)  # 字体大小
rt_p_status = RichText('')
rt_p_status.add('共青团员', size=12)  # 字体大小

id_number = '152224199101104567'

context_ = {
    'r_e': '韩小顺',
    'sa': '男',
    'bir': '1991-01-10',
    'edu': '本科',
    'id_number': '15222419910110651x',
    'work_unit': '青峰白羽软件技术工作室',
    'f_p': '021-09765432',
    'u_n': '私营企业',
    'profession': '计算机软件',
    's_w_d': '2015-08-20',
    'cl': '4',
    'hukou': rt_hukou,
    'address': '北京大兴区旧宫镇',
    'unit_address': '北京大兴区旧宫镇',
    'email': '北京大兴区旧宫镇',
    'id_addr': rt_id_number,
    'postal_c': '137512',
    # 'p': rt_p_status, 这里不填单位性质
    'nati': '蒙古族',
    'f_occ': '电工',
    'p_level': '初级',
    'o_cer_num': '333444556677888',
    'issuance_time': '2018-09-09',
    'issue_unit': '青峰白羽软件技术工作室',
    'dec_of_occ': '电工',
    'id_level': '中级',
    'work_training': '我从事的是计算机软件编程，及互联网网站建设。',
    'inch_img': InlineImage(tpl, 'tfz2.jpg', width=Mm(35), height=Mm(48)),
}

context = {
    'tbl_contents': [
        {'index': '1', 'r_e': '韩小顺', 'id_number': '152224199101106515', 'sa': '男', 'school': '', 'f_occ': '电工',
         's_w_d': '2018-09-01', 'id_level': '初级', 'jsll': '', 'sjcz': '', 'o_cer_num': '213131312331',
         'issuance_time': '2019-08-07'},
    ]
}

jinja_env = jinja2.Environment(autoescape=True)
tpl.render(context, jinja_env)
tpl.save('f04_04.docx')
