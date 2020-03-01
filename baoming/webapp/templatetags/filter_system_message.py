from django import template

register = template.Library()


@register.filter
def get_message_level(value):
    message_level = {'1': '常规', '2': '预警', '3': '紧急'}
    if value:
        return message_level[str(value)]
    elif value == '0':
        return ''
    else:
        return ''


@register.filter
def get_message_range(value):
    message_range = {'1': '系统公告',
                     '2': '系统管理员',
                     '3': '全体负责人',
                     '4': '负责人',
                     '5': '全体学员',
                     '6': '负责人管辖全体学员',
                     '7': '学员',
                     '8': '单位报名负责人'}
    if value:
        return message_range[str(value)]
    else:
        return ''


@register.filter
def get_send_status(value):
    send_status = {'1': '成功',
                   '2': '失败'}
    if value:
        return send_status[str(value)]
    else:
        return ''


@register.filter
def get_receive_status(value):
    receive_status = {'1': '已查看',
                      '2': '未查看'}
    if value:
        return receive_status[str(value)]
    else:
        return ''


@register.filter
def get_feedback_status(value):
    feedback_status = {'1': '已确认',
                       '2': '未确认'}
    if value:
        return feedback_status[str(value)]
    else:
        return ''


@register.filter
def get_hidden_status(value):
    hidden_status = {'1': '已隐藏',
                     '2': '未隐藏'}
    if value:
        return hidden_status[str(value)]
    else:
        return ''
