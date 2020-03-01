from docxtpl import DocxTemplate, InlineImage, RichText
from docx.shared import Mm, Inches, Pt
import jinja2

tpl = DocxTemplate('fujian03.docx')

rt_hukou = RichText('')
rt_hukou.add('内蒙古突泉县', size=12)  # 字体大小
rt_id_number = RichText('')
rt_id_number.add('内蒙古突泉县', size=12)  # 字体大小
rt_p_status = RichText('')
rt_p_status.add('共青团员', size=12)  # 字体大小

id_number = '152224199101104567'

context = {
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
    'a': id_number[0],
    'b': id_number[1],
    'c': id_number[2],
    'd': id_number[3],
    'e': id_number[4],
    'f': id_number[5],
    'g': id_number[6],
    'h': id_number[7],
    'i': id_number[8],
    'j': id_number[9],
    'k': id_number[10],
    'l': id_number[11],
    'm': id_number[12],
    'n': id_number[13],
    'o': id_number[14],
    'p': id_number[15],
    'q': id_number[16],
    'r': id_number[17],
}

jinja_env = jinja2.Environment(autoescape=True)
tpl.render(context, jinja_env)
tpl.save('f03_02.docx')
