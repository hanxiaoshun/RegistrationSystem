#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/26 16:20
# @Author  : Hanxiaoshun@天谕传说
# @Site    : 
# @File    : 
# @Software: PyCharm
from django.urls import path

from . import views as v

urlpatterns = [

    path('introduction/', v.introduction, name='introduction'),
    path('system_guide/', v.system_guide, name='system_guide'),

    path('to_login/', v.to_login, name='to_login'),
    path('sign_in/', v.sign_in, name='sign_in'),
    path('sign_out/', v.sign_out, name='sign_out'),
    path('to_index/', v.to_index, name='to_index'),
    path('check_username/', v.check_username, name='check_username'),
    path('check_nickname/', v.check_nickname, name='check_nickname'),
    path('register/', v.register, name='register'),
    # start business
    path('worker/', v.worker, name='worker'),  # 工种填报页面选择

    path('to_index_teacher/', v.to_index_teacher, name='to_index_teacher'),
    path('report_info_review/', v.report_info_review, name='report_info_review'),  # 信息审核列表
    path('report_do_review/', v.report_do_review, name='report_do_review'),  # 信息审核操作
    path('report_do_review_cancel/', v.report_do_review_cancel, name='report_do_review_cancel'),  # 信息审核操作

    path('administrator_all_student_base_info/', v.administrator_all_student_base_info,
         name='administrator_all_student_base_info'),
    path('administrator_reporter_chemical_not/', v.administrator_reporter_chemical_not,
         name='administrator_reporter_chemical_not'),
    path('administrator_reporter_chemical/', v.administrator_reporter_chemical, name='administrator_reporter_chemical'),

    path('report_info_confirm/', v.report_info_confirm, name='report_info_confirm'),
    path('admin_term_picture_data/', v.admin_term_picture_data, name='admin_term_picture_data'),
    path('del_register_info/', v.del_register_info, name='del_register_info'),

    path('report_teacher_list/', v.report_teacher_list, name='report_teacher_list'),  # 信息确认
    path('report_school_term_list/', v.report_school_term_list, name='report_school_term_list'),  # 信息确认
    path('add_school_term/', v.add_school_term, name='add_school_term'),  # 信息确认
    path('to_update_term_info/', v.to_update_term_info, name='to_update_term_info'),  # 信息确认
    path('update_school_term/', v.update_school_term, name='update_school_term'),  # 信息确认
    path('del_term_info/', v.del_term_info, name='del_term_info'),  # 信息确认
    path('admin_del_term_info_data/', v.admin_del_term_info_data, name='admin_del_term_info_data'),  # 信息确认

    path('refresh_school_term_data/', v.refresh_school_term_data, name='refresh_school_term_data'),  # 信息确认
    path('report_operation_log_list/', v.report_operation_log_list, name='report_operation_log_list'),  # 信息确认
    path('report_system_info_detail/', v.report_system_info_detail, name='report_system_info_detail'),  # 信息确认
    path('report_delete_force/', v.report_delete_force, name='report_delete_force'),  # 信息确认
    path('delete_force/', v.delete_force, name='delete_force'),  # 信息确认

    path('register_teacher/', v.register_teacher, name='register_teacher'),
    path('to_update_teacher/', v.to_update_teacher, name='to_update_teacher'),
    path('update_teacher_info/', v.update_teacher_info, name='update_teacher_info'),
    path('cancel_teacher/', v.cancel_teacher, name='cancel_teacher'),
    path('start_teacher/', v.start_teacher, name='start_teacher'),
    path('teacher_search_wait_review/', v.teacher_search_wait_review, name='teacher_search_wait_review'),

    path('report_do_confirm/', v.report_do_confirm, name='report_do_confirm'),
    path('report_cancel_confirm/', v.report_cancel_confirm, name='report_cancel_confirm'),
    path('admin_del_student/', v.admin_del_student, name='admin_del_student'),

    path('add_student_info/', v.add_student_info, name='add_student_info'),
    path('report_student_info_list/', v.report_student_info_list, name='report_student_info_list'),
    path('student_info_detail/', v.student_info_detail, name='student_info_detail'),
    path('to_student_info_update/', v.to_student_info_update, name='to_student_info_update'),
    path('student_info_update/', v.student_info_update, name='student_info_update'),
    path('report_student_del/', v.report_student_del, name='report_student_del'),
    path('report_student_submit/', v.report_student_submit, name='report_student_submit'),
    path('report_student_payment/', v.report_student_payment, name='report_student_payment'),

    path('report_student_cancel/', v.report_student_cancel, name='report_student_cancel'),
    path('report_student_cancel_return/', v.report_student_cancel_return, name='report_student_cancel_return'),

    path('add_user_info/', v.add_user_info, name='add_user_info'),
    path('update_user_info/', v.update_user_info, name='update_user_info'),
    path('user_info_list/', v.user_info_list, name='user_info_list'),
    path('user_setting/', v.user_setting, name='user_setting'),

    path('reset_password/', v.reset_password, name='reset_password'),
    path('reset_password_page/', v.reset_password_page, name='reset_password_page'),
    path('user_setting/', v.user_setting, name='user_setting'),
    path('to_user_info_update/', v.to_user_info_update, name='to_user_info_update'),
    path('update_user_base_info/', v.update_user_base_info, name='update_user_base_info'),

    path('check_origin_password/', v.check_origin_password, name='check_origin_password'),
    path('final_reset_password/', v.final_reset_password, name='final_reset_password'),

    path('worker_history/', v.worker_history, name='worker_history'),
    path('add_work_history/', v.add_work_history, name='add_work_history'),
    path('delete_history/', v.delete_history, name='delete_history'),

    # tools link
    path('education_degree/', v.education_degree, name='education_degree'),  # 获取教育程度信息
    path('unit_nature/', v.unit_nature, name='unit_nature'),  # 获取教育程度信息
    path('nation_info/', v.nation_info, name='nation_info'),  # 获取教育程度信息

    path('province/', v.province, name='province'),  # 获取教育程度信息
    path('city/', v.city, name='city'),  # 获取教育程度信息
    path('county/', v.county, name='county'),  # 获取教育程度信息

    # 文件工具
    path('image_upload/', v.image_upload, name='image_upload'),
    # 下载工具
    path('download_apply/', v.download_apply, name='download_apply'),
    path('start_download/', v.start_download, name='start_download'),
    path('all_student_base_info/', v.all_student_base_info, name='all_student_base_info'),
    path('reporter_chemical_not/', v.reporter_chemical_not, name='start_download'),
    path('reporter_chemical/', v.reporter_chemical, name='reporter_chemical'),
    path('report_download_page/', v.report_download_page, name='report_download_page'),
    path('administrator_search_chemical_download/', v.administrator_search_chemical_download,
         name='administrator_search_chemical_download'),
    path('administrator_search_chemical_not_download/', v.administrator_search_chemical_not_download,
         name='administrator_search_chemical_not_download'),
    path('all_student_base_info_download/', v.all_student_base_info_download,
         name='all_student_base_info_download'),

    # search part 所有的列表查询部分
    path('administrator_search_chemical/', v.administrator_search_chemical, name='administrator_search_chemical'),
    path('administrator_search_chemical_not/', v.administrator_search_chemical_not,
         name='administrator_search_chemical_not'),
    path('administrator_search_all_student/', v.administrator_search_all_student,
         name='administrator_search_all_student'),
    path('administrator_search_wait_confirm/', v.administrator_search_wait_confirm,
         name='administrator_search_wait_confirm'),

    # system_message
    path('send/', v.send, name='send'),
    path('receive/', v.receive, name='receive'),
    path('admin_message/', v.admin_message, name='admin_message'),

    path('message_add/', v.message_add, name='message_add'),
    path('message_to_receiver/', v.message_to_receiver, name='message_to_receiver'),
    path('message_to_message/', v.message_to_message, name='message_to_message'),
    path('save_system_message/', v.save_system_message, name='save_system_message'),
    path('system_message_detail/', v.system_message_detail, name='system_message_detail'),
    path('system_message_confirm/', v.system_message_confirm, name='system_message_confirm'),
    path('system_message_hidden/', v.system_message_hidden, name='system_message_hidden'),
    path('system_message_confirm_send/', v.system_message_confirm_send, name='system_message_confirm_send'),
    path('reply_system_message/', v.reply_system_message, name='reply_system_message'),

    # system_message search
    path('get_like_user_info/', v.get_like_user_info, name='get_like_user_info'),
]