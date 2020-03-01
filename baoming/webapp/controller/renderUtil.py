from django.shortcuts import render

from webapp.controller.system_message import get_message_infos


def render_result(request, render_page, render_data):
    not_confirm, message_already_sent, system_announcement = get_message_infos(request)
    render_data['message_not_confirm'] = not_confirm
    render_data['message_already_sent'] = message_already_sent
    render_data['system_announcement'] = system_announcement
    return render(request, render_page, render_data)
