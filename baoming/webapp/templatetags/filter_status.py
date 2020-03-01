from django import template

register = template.Library()


@register.filter
def get_submit_status(value):
    """
    提交状态
    :param value:
    :return:
    """
    submit_status = {'1': '已提交',
                     '2': '未提交'}
    return submit_status[str(value)]


@register.filter
def get_review_status(value):
    """
    审核状态
    :param value:
    :return:
    """
    review_status = {'1': '已审核',
                     '2': '未审核'}
    return review_status[value]


@register.filter
def get_cancel_status(value):
    """
    审核状态
    :param value:
    :return:
    """
    cancel_status = {'1': '申请注销', '2': '未申请注销'}
    return cancel_status[value]


@register.filter
def get_confirm_status(value):
    """
    报名结果状态
    :param value:
    :return:
    """
    confirm_status = {'1': '通过', '2': '未通过'}
    return confirm_status[value]


@register.filter
def get_pay_status(value):
    """
    支付完成状态
    :param value:
    :return:
    """
    pay_status = {'1': '已缴纳', '2': '未缴纳'}
    return pay_status[value]


@register.filter
def get_examination_status(value):
    """
    考核结果
    :param value:
    :return:
    """
    examination_status = {'1': '通过', '2': '未通过'}
    return examination_status[value]
