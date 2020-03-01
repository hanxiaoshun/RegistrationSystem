from django import template

register = template.Library()


@register.filter
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
        return_value = ''
    return return_value


@register.filter
def get_apprentice_year(value):
    if value:
        return value
    else:
        return ""


@register.filter
def get_apprentice_month(value):
    if value:
        return value
    else:
        return ""


@register.filter
def get_course_hours(value):
    if value:
        return value
    else:
        return ""


@register.filter
def get_political_status(value):
    if value == '':
        return ''
    else:
        political_status = {'0': '中共党员',
                            '1': '中共预备党员',
                            '2': '共青团员',
                            '3': '民革党员',
                            '4': '民盟盟员',
                            '5': '民建会员',
                            '6': '民进会员',
                            '7': '农工党党员',
                            '8': '致公党党员',
                            '9': '九三学社社员',
                            '10': '台盟盟员',
                            '11': '无党派人士',
                            '12': '群众(普通居民)'}
        return political_status[str(value)]


@register.filter
def get_original_certificate_worker_year(value):
    if value:
        return value
    else:
        return 0


@register.filter
def get_career_life(value):
    if value:
        return value
    else:
        return 0


@register.filter
def get_course_hours(value):
    if value:
        return value
    else:
        return 0


@register.filter
def get_primary_level(value):
    if len(value) == 0:
        return ""
    else:
        primary_level = {'1': '高级技工',
                         '2': '技工',
                         '3': '高级',
                         '4': '中级',
                         '5': '初级',
                         '99': '无级别信息'}
        return primary_level[str(value)]


@register.filter
def get_identification_level(value):
    if len(value) == 0:
        return ""
    else:
        identification_level = {'1': '高级技工',
                                '2': '技工',
                                '3': '高级',
                                '4': '中级',
                                '5': '初级',
                                '99': '无级别信息'}
        return identification_level[str(value)]


@register.filter
def get_original_certificate_number(value):
    if value == '':
        return ''
    else:
        return value


@register.filter
def get_current_certificate_number(value):
    if not value:
        return '无'
    else:
        return value


@register.filter
def get_status_pay(value):
    if value:
        return '已缴费'
    else:
        return '未缴费'


@register.filter
def get_career_life(value):
    if value:
        return value
    else:
        return 0


@register.filter
def get_contact_number(value):
    if value:
        return value
    else:
        return ""


@register.filter
def get_status(value):
    print("value:::" + value)
    identification_level = {'1': '启用',
                            '2': '停用'}
    return identification_level[str(value)]


@register.filter
def get_none(value):
    if value:
        return value
    else:
        return ""


@register.filter
def get_zero(value):
    if value:
        return value
    if value == 0:
        return ""
    else:
        return ""


@register.filter
def get_message_level(value):
    message_level = {'1': '常规', '2': '预警', '3': '紧急'}
    if value:
        return message_level[value]
    else:
        return ''


@register.filter
def get_nickname(value):
    new_value = ''
    if str(value).__len__() == 2:
        new_value = str(value)[0:1] + "   " + str(value)[1:2]
    if str(value).__len__() == 3:
        new_value = str(value)[0:1] + " " + str(value)[1:2] + " " + str(value)[2:3]
    if str(value).__len__() == 4:
        new_value = str(value)[0:1] + " " + str(value)[1:2] + " " + str(value)[2:3] + " " + str(value)[3:4]
    if str(value).__len__() > 4:
        new_value = value
    return new_value
